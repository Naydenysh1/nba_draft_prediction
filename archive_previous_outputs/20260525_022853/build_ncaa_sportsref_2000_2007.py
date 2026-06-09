#!/usr/bin/env python3
"""
Targeted Sports-Reference NCAA stats collector for early NBA Draft years.

Purpose:
- Fill the 2000-2007 NCAA gap that Torvik does not cover well.
- Do NOT build a full NCAA universe.
- Only query players from the existing clean NBA Draft/Combine base dataset.

Input:
    data/nba_draft_combine_clean_2000_2026.csv

Output:
    data/pre_draft_ncaa_sportsref_2000_2007.csv
    data/pre_draft_ncaa_sportsref_2000_2007_unmatched.csv
    data/pre_draft_ncaa_sportsref_report.md

Install:
    pip install pandas numpy requests beautifulsoup4 lxml unidecode rapidfuzz

Example:
    python build_ncaa_sportsref_2000_2007.py \
        --base data/nba_draft_combine_clean_2000_2026.csv \
        --out data/pre_draft_ncaa_sportsref_2000_2007.csv \
        --unmatched-out data/pre_draft_ncaa_sportsref_2000_2007_unmatched.csv \
        --report data/pre_draft_ncaa_sportsref_report.md
"""

from __future__ import annotations

import argparse
from io import StringIO
import re
import time
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
from rapidfuzz import fuzz

BASE_URL = "https://www.sports-reference.com/cbb/players/{slug}.html"
REQUEST_SLEEP_SECONDS = 4.0
REQUEST_TIMEOUT_SECONDS = 30
MAX_SUFFIX = 12
MAX_SEASON_GAP_YEARS = 2

MANUAL_NAME_VARIANTS = {
    "mamadou n diaye": ["mamadou ndiaye"],
    "michael sweetney": ["mike sweetney"],
    "patrick o bryant": ["patrick obryant"],
    "pinnock": ["jr pinnock", "j r pinnock"],
}

OUTPUT_COLUMNS = [
    "name",
    "draft_year",
    "sportsref_player_raw",
    "sportsref_url",
    "sportsref_match_method",
    "sportsref_match_score",
    "sportsref_school",
    "sportsref_conf",
    "sportsref_season",
    "sportsref_games",
    "sportsref_games_started",
    "sportsref_mpg",
    "sportsref_ppg",
    "sportsref_rpg",
    "sportsref_apg",
    "sportsref_spg",
    "sportsref_bpg",
    "sportsref_tpg",
    "sportsref_fg_pct",
    "sportsref_two_pct",
    "sportsref_three_pct",
    "sportsref_ft_pct",
]


def clean_name(name: object) -> str:
    if pd.isna(name):
        return ""
    s = str(name).strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def slug_base_from_name(cleaned_name: str) -> str:
    parts = cleaned_name.split()
    if len(parts) == 0:
        return ""
    if len(parts) == 1:
        return parts[0]
    return "-".join(parts)


def slug_candidates(cleaned_name: str) -> list[str]:
    candidates = []
    for variant in name_variants(cleaned_name):
        candidates.extend(slug_candidates_for_variant(variant))

    # De-duplicate while preserving order.
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            unique.append(c)
            seen.add(c)
    return unique


def name_variants(cleaned_name: str) -> list[str]:
    variants = []
    variants.extend(MANUAL_NAME_VARIANTS.get(cleaned_name, []))
    variants.append(cleaned_name)
    seen = set()
    unique = []
    for variant in variants:
        if variant and variant not in seen:
            unique.append(variant)
            seen.add(variant)
    return unique


def slug_candidates_for_variant(cleaned_name: str) -> list[str]:
    parts = cleaned_name.split()
    if not parts:
        return []

    candidates = []
    base = slug_base_from_name(cleaned_name)
    candidates.extend([f"{base}-{i}" for i in range(1, MAX_SUFFIX + 1)])

    # Some Sports-Reference pages may omit middle particles or initials in the slug.
    if len(parts) >= 3:
        first_last = f"{parts[0]}-{parts[-1]}"
        candidates.extend([f"{first_last}-{i}" for i in range(1, MAX_SUFFIX + 1)])

    # Compact initials variant: r j barrett -> rj-barrett-1, a j abrams -> aj-abrams-1.
    if len(parts) >= 3 and all(len(p) == 1 for p in parts[:-1]):
        compact = f"{''.join(parts[:-1])}-{parts[-1]}"
        candidates.extend([f"{compact}-{i}" for i in range(1, MAX_SUFFIX + 1)])

    # De-duplicate while preserving order.
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            unique.append(c)
            seen.add(c)
    return unique


def season_label_for_draft_year(draft_year: int) -> str:
    return f"{draft_year - 1}-{str(draft_year)[-2:]}"


def to_numeric(value: Any) -> float | pd.NA:
    if pd.isna(value):
        return pd.NA
    s = str(value).strip()
    if s == "" or s.lower() in {"nan", "none"}:
        return pd.NA
    return pd.to_numeric(s.replace("%", ""), errors="coerce")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if isinstance(out.columns, pd.MultiIndex):
        out.columns = ["_".join([str(x) for x in tup if str(x) != "nan"]).strip() for tup in out.columns]
    out.columns = [str(c).strip() for c in out.columns]
    return out


def get_col(df: pd.DataFrame, candidates: list[str]) -> str | None:
    lower_to_original = {str(c).strip().lower(): c for c in df.columns}
    for candidate in candidates:
        key = candidate.strip().lower()
        if key in lower_to_original:
            return lower_to_original[key]
    return None


def extract_tables_from_html(html: str) -> list[pd.DataFrame]:
    """Sports-Reference often stores tables inside HTML comments; expose them before read_html."""
    soup = BeautifulSoup(html, "html.parser")
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        if "<table" in comment:
            comment_soup = BeautifulSoup(comment, "html.parser")
            comment.replace_with(comment_soup)

    try:
        return [normalize_columns(t) for t in pd.read_html(StringIO(str(soup)))]
    except ValueError:
        return []


def fetch_html(session: requests.Session, url: str) -> str | None:
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT_SECONDS)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.text
    finally:
        time.sleep(REQUEST_SLEEP_SECONDS)


def page_player_name(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1:
        return clean_name(h1.get_text(" ", strip=True))
    title = soup.find("title")
    if title:
        return clean_name(title.get_text(" ", strip=True).split(" Stats")[0])
    return ""


def find_per_game_table(tables: list[pd.DataFrame]) -> pd.DataFrame | None:
    for table in tables:
        cols_lower = {str(c).lower() for c in table.columns}
        has_season = "season" in cols_lower
        has_school = "school" in cols_lower or "team" in cols_lower
        has_points = "pts" in cols_lower or "points" in cols_lower
        has_games = "g" in cols_lower or "games" in cols_lower
        if has_season and has_school and has_points and has_games:
            return table.copy()
    return None


def extract_target_season_row(table: pd.DataFrame, draft_year: int) -> pd.Series | None:
    season_col = get_col(table, ["Season"])
    if season_col is None:
        return None

    table = table.copy()
    table[season_col] = table[season_col].astype(str)

    target = season_label_for_draft_year(draft_year)
    exact = table[table[season_col].eq(target)]
    if not exact.empty:
        return exact.iloc[0]

    # Fallback: latest available season ending no later than draft_year.
    def end_year_from_label(label: str) -> int | None:
        if pd.isna(label):
            return None
        m = re.match(r"^(\d{4})-(\d{2})$", str(label).strip())
        if not m:
            return None
        start = int(m.group(1))
        end_2 = int(m.group(2))
        century = start // 100 * 100
        end_year = century + end_2
        if end_year < start:
            end_year += 100
        return end_year

    tmp = table.copy()
    tmp["_end_year"] = tmp[season_col].map(end_year_from_label)
    tmp = tmp[tmp["_end_year"].notna() & (tmp["_end_year"] <= draft_year)]
    if tmp.empty:
        return None
    tmp = tmp.sort_values("_end_year", ascending=False)
    if int(tmp.iloc[0]["_end_year"]) < draft_year - MAX_SEASON_GAP_YEARS:
        return None
    return tmp.iloc[0]


def row_to_output(
    row: pd.Series,
    query_name: str,
    draft_year: int,
    url: str,
    raw_page_name: str,
    match_method: str,
    match_score: float,
) -> dict[str, Any]:
    def val(candidates: list[str]) -> Any:
        col = get_col(pd.DataFrame(columns=row.index), candidates)
        if col is None:
            return pd.NA
        return row.get(col, pd.NA)

    school = val(["School", "Team"])
    conf = val(["Conf", "Conference"])
    season = val(["Season"])

    games = val(["G", "Games"])
    games_started = val(["GS", "Games Started"])
    minutes = val(["MP", "MPG", "Minutes"])
    points = val(["PTS", "Points"])
    rebounds = val(["TRB", "RPG", "Total Rebounds"])
    assists = val(["AST", "APG", "Assists"])
    steals = val(["STL", "SPG", "Steals"])
    blocks = val(["BLK", "BPG", "Blocks"])
    turnovers = val(["TOV", "TPG", "Turnovers"])
    fg_pct = val(["FG%", "FG_pct", "FG Pct"])
    two_pct = val(["2P%", "2P_pct", "2P Pct"])
    three_pct = val(["3P%", "3P_pct", "3P Pct"])
    ft_pct = val(["FT%", "FT_pct", "FT Pct"])

    return {
        "name": query_name,
        "draft_year": draft_year,
        "sportsref_player_raw": raw_page_name,
        "sportsref_url": url,
        "sportsref_match_method": match_method,
        "sportsref_match_score": match_score,
        "sportsref_school": school,
        "sportsref_conf": conf,
        "sportsref_season": season,
        "sportsref_games": to_numeric(games),
        "sportsref_games_started": to_numeric(games_started),
        "sportsref_mpg": to_numeric(minutes),
        "sportsref_ppg": to_numeric(points),
        "sportsref_rpg": to_numeric(rebounds),
        "sportsref_apg": to_numeric(assists),
        "sportsref_spg": to_numeric(steals),
        "sportsref_bpg": to_numeric(blocks),
        "sportsref_tpg": to_numeric(turnovers),
        "sportsref_fg_pct": to_numeric(fg_pct),
        "sportsref_two_pct": to_numeric(two_pct),
        "sportsref_three_pct": to_numeric(three_pct),
        "sportsref_ft_pct": to_numeric(ft_pct),
    }


@dataclass
class MatchResult:
    output: dict[str, Any] | None
    reason: str
    attempted_urls: list[str]


def find_player_stats(session: requests.Session, player_name: str, draft_year: int) -> MatchResult:
    cleaned = clean_name(player_name)
    attempted = []

    for slug in slug_candidates(cleaned):
        url = BASE_URL.format(slug=slug)
        attempted.append(url)
        try:
            html = fetch_html(session, url)
        except requests.HTTPError as exc:
            status = getattr(exc.response, "status_code", None)
            if status in {403, 429}:
                return MatchResult(None, f"blocked_or_rate_limited_http_{status}", attempted)
            continue
        except Exception:
            continue

        if html is None:
            continue

        raw_page_clean = page_player_name(html)
        name_score = max(
            (fuzz.ratio(variant, raw_page_clean) for variant in name_variants(cleaned)),
            default=0,
        ) if raw_page_clean else 0
        if name_score < 82:
            # Avoid false positive pages with same slug pattern but different player.
            continue

        tables = extract_tables_from_html(html)
        per_game = find_per_game_table(tables)
        if per_game is None:
            continue

        season_row = extract_target_season_row(per_game, draft_year)
        if season_row is None:
            continue

        output = row_to_output(
            season_row,
            cleaned,
            draft_year,
            url,
            raw_page_clean,
            "slug_search",
            float(name_score),
        )
        return MatchResult(output, "matched", attempted)

    return MatchResult(None, "not_found", attempted)


def build_targets(base_csv: Path, start_year: int, end_year: int) -> pd.DataFrame:
    base = pd.read_csv(base_csv)
    required = {"name", "draft_year", "organization_type", "organization", "overall_pick"}
    missing = required - set(base.columns)
    if missing:
        raise ValueError(f"Base CSV missing required columns: {sorted(missing)}")

    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = pd.to_numeric(base["draft_year"], errors="coerce").astype("Int64")

    # Targeted approach: only rows with a known college/university organization.
    targets = base[
        base["draft_year"].between(start_year, end_year)
        & base["organization_type"].eq("College/University")
        & base["organization"].notna()
    ].copy()

    targets = targets[["name", "draft_year", "overall_pick", "organization", "organization_type"]]
    targets = targets.drop_duplicates(subset=["name", "draft_year"])
    return targets.sort_values(["draft_year", "overall_pick", "name"], na_position="last").reset_index(drop=True)


def write_report(
    targets: pd.DataFrame,
    matched: pd.DataFrame,
    unmatched: pd.DataFrame,
    report_path: Path,
    start_year: int,
    end_year: int,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    match_rate = 0 if len(targets) == 0 else len(matched) / len(targets) * 100
    rows_by_year = targets.groupby("draft_year").size().rename("targets").reset_index()
    matched_by_year = matched.groupby("draft_year").size().rename("matched").reset_index() if not matched.empty else pd.DataFrame(columns=["draft_year", "matched"])
    by_year = rows_by_year.merge(matched_by_year, on="draft_year", how="left")
    by_year["matched"] = by_year["matched"].fillna(0).astype(int)
    by_year["match_rate_pct"] = (by_year["matched"] / by_year["targets"] * 100).round(1)

    missing_pct = pd.DataFrame()
    if not matched.empty:
        numeric_cols = [c for c in matched.columns if c.startswith("sportsref_") and c not in {
            "sportsref_player_raw", "sportsref_url", "sportsref_match_method", "sportsref_school", "sportsref_conf", "sportsref_season"
        }]
        missing_pct = (matched[numeric_cols].isna().mean() * 100).round(1).sort_values(ascending=False).reset_index()
        missing_pct.columns = ["column", "missing_pct"]

    duplicate_count = matched.duplicated(subset=["name", "draft_year"]).sum() if not matched.empty else 0

    lines = []
    lines.append("# Sports-Reference NCAA 2000-2007 Targeted Dataset Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- start_year: {start_year}")
    lines.append(f"- end_year: {end_year}")
    lines.append(f"- target_players: {len(targets)}")
    lines.append(f"- matched_players: {len(matched)}")
    lines.append(f"- unmatched_players: {len(unmatched)}")
    lines.append(f"- match_rate_pct: {match_rate:.1f}")
    lines.append(f"- duplicate_name_draft_year_rows_after_resolution: {duplicate_count}")
    lines.append("")

    lines.append("## Match Rate By draft_year")
    lines.append("")
    lines.append(by_year.to_markdown(index=False))
    lines.append("")

    if not missing_pct.empty:
        lines.append("## Missing-Value Percentage For Matched Numeric Columns")
        lines.append("")
        lines.append(missing_pct.to_markdown(index=False))
        lines.append("")

    lines.append("## First 30 Matched Rows")
    lines.append("")
    lines.append(matched.head(30).to_markdown(index=False) if not matched.empty else "_None_")
    lines.append("")

    lines.append("## First 50 Unmatched Rows")
    lines.append("")
    lines.append(unmatched.head(50).to_markdown(index=False) if not unmatched.empty else "_None_")
    lines.append("")

    lines.append("## Output Columns")
    lines.append("")
    for col in OUTPUT_COLUMNS:
        lines.append(f"- {col}")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=str, default="data/nba_draft_combine_clean_2000_2026.csv")
    parser.add_argument("--start-year", type=int, default=2000)
    parser.add_argument("--end-year", type=int, default=2007)
    parser.add_argument("--out", type=str, default="data/pre_draft_ncaa_sportsref_2000_2007.csv")
    parser.add_argument("--unmatched-out", type=str, default="data/pre_draft_ncaa_sportsref_2000_2007_unmatched.csv")
    parser.add_argument("--report", type=str, default="data/pre_draft_ncaa_sportsref_report.md")
    parser.add_argument("--limit", type=int, default=None, help="Debug limit on target players.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_path = Path(args.base)
    out_path = Path(args.out)
    unmatched_path = Path(args.unmatched_out)
    report_path = Path(args.report)

    targets = build_targets(base_path, args.start_year, args.end_year)
    if args.limit is not None:
        targets = targets.head(args.limit).copy()

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; university-data-science-project/1.0; educational use)"
    })

    matched_rows = []
    unmatched_rows = []

    print(f"Target players: {len(targets)}")
    for i, row in targets.iterrows():
        player = row["name"]
        draft_year = int(row["draft_year"])
        print(f"[{i + 1}/{len(targets)}] {player} ({draft_year})")

        try:
            result = find_player_stats(session, player, draft_year)
        except Exception as exc:
            result = MatchResult(None, f"parser_error_{type(exc).__name__}: {exc}", [])
        if result.output is not None:
            matched_rows.append(result.output)
        else:
            unmatched_rows.append({
                "name": player,
                "draft_year": draft_year,
                "overall_pick": row.get("overall_pick", pd.NA),
                "organization": row.get("organization", pd.NA),
                "reason": result.reason,
                "attempted_urls_count": len(result.attempted_urls),
            })

    matched = pd.DataFrame(matched_rows)
    for col in OUTPUT_COLUMNS:
        if col not in matched.columns:
            matched[col] = pd.NA
    matched = matched[OUTPUT_COLUMNS]
    matched = matched.drop_duplicates(subset=["name", "draft_year"])
    matched = matched.sort_values(["draft_year", "name"]).reset_index(drop=True)

    unmatched = pd.DataFrame(unmatched_rows)
    unmatched = unmatched.sort_values(["draft_year", "overall_pick", "name"], na_position="last").reset_index(drop=True) if not unmatched.empty else unmatched

    out_path.parent.mkdir(parents=True, exist_ok=True)
    matched.to_csv(out_path, index=False)
    unmatched.to_csv(unmatched_path, index=False)
    write_report(targets, matched, unmatched, report_path, args.start_year, args.end_year)

    print(f"Saved matched CSV: {out_path}")
    print(f"Saved unmatched CSV: {unmatched_path}")
    print(f"Saved report: {report_path}")
    print(f"Matched: {len(matched)} / {len(targets)}")


if __name__ == "__main__":
    main()
