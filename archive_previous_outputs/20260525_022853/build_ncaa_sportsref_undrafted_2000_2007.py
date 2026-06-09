#!/usr/bin/env python3
"""
Targeted Sports-Reference NCAA stats collector for early undrafted combine players.

Purpose:
- Try to fill NCAA stats / organization for undrafted combine players from draft years 2000-2007.
- This is an experimental standalone layer.
- It does NOT modify the final NBA Draft dataset.
- It does NOT merge results into the final dataset.

Recommended input:
    data/nba_draft_full_clean_project_na_2000_2026.csv

Target rows:
    draft_year between 2000 and 2007
    overall_pick == 999
    organization is missing

Outputs:
    data/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv
    data/pre_draft_ncaa_sportsref_undrafted_2000_2007_unmatched.csv
    data/pre_draft_ncaa_sportsref_undrafted_report.md

Install:
    pip install pandas numpy requests beautifulsoup4 lxml rapidfuzz tabulate

Example:
    python build_ncaa_sportsref_undrafted_2000_2007.py \
        --base data/nba_draft_full_clean_project_na_2000_2026.csv \
        --out data/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv \
        --unmatched-out data/pre_draft_ncaa_sportsref_undrafted_2000_2007_unmatched.csv \
        --report data/pre_draft_ncaa_sportsref_undrafted_report.md
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

import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
from rapidfuzz import fuzz

BASE_URL = "https://www.sports-reference.com/cbb/players/{slug}.html"
REQUEST_SLEEP_SECONDS = 5.5
REQUEST_TIMEOUT_SECONDS = 30
MAX_SUFFIX = 14
MIN_PAGE_NAME_SCORE = 92

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


def compact_initials(name: str) -> str:
    parts = name.split()
    if len(parts) >= 3 and len(parts[0]) == 1 and len(parts[1]) == 1:
        return " ".join([parts[0] + parts[1], *parts[2:]])
    return name


def spaced_initials(name: str) -> str:
    parts = name.split()
    if len(parts) >= 2 and len(parts[0]) == 2 and parts[0].isalpha():
        return " ".join([parts[0][0], parts[0][1], *parts[1:]])
    return name


def slug_candidates(cleaned_name: str) -> list[str]:
    names = [cleaned_name, compact_initials(cleaned_name), spaced_initials(cleaned_name)]
    names = [n for n in dict.fromkeys(names) if n]

    candidates: list[str] = []
    for name in names:
        parts = name.split()
        if not parts:
            continue
        base = "-".join(parts)
        candidates.extend([f"{base}-{i}" for i in range(1, MAX_SUFFIX + 1)])

        if len(parts) >= 3:
            first_last = f"{parts[0]}-{parts[-1]}"
            candidates.extend([f"{first_last}-{i}" for i in range(1, MAX_SUFFIX + 1)])

        if len(parts) >= 3 and all(len(p) == 1 for p in parts[:-1]):
            compact = f"{''.join(parts[:-1])}-{parts[-1]}"
            candidates.extend([f"{compact}-{i}" for i in range(1, MAX_SUFFIX + 1)])

    seen = set()
    unique = []
    for c in candidates:
        if c not in seen:
            unique.append(c)
            seen.add(c)
    return unique


def season_label_for_draft_year(draft_year: int) -> str:
    return f"{draft_year - 1}-{str(draft_year)[-2:]}"


def to_numeric(value: Any) -> Any:
    if pd.isna(value):
        return pd.NA
    s = str(value).strip()
    if s == "" or s.lower() in {"nan", "none", "<na>"}:
        return pd.NA
    return pd.to_numeric(s.replace("%", ""), errors="coerce")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if isinstance(out.columns, pd.MultiIndex):
        out.columns = ["_".join([str(x) for x in tup if str(x) != "nan"]).strip() for tup in out.columns]
    out.columns = [str(c).strip() for c in out.columns]
    return out


def get_col(df_or_index: Any, candidates: list[str]) -> str | None:
    cols = df_or_index.columns if hasattr(df_or_index, "columns") else df_or_index
    lower_to_original = {str(c).strip().lower(): c for c in cols}
    for candidate in candidates:
        key = candidate.strip().lower()
        if key in lower_to_original:
            return lower_to_original[key]
    return None


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


def extract_tables_from_html(html: str) -> list[pd.DataFrame]:
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


def extract_exact_target_season_row(table: pd.DataFrame, draft_year: int) -> pd.Series | None:
    season_col = get_col(table, ["Season"])
    if season_col is None:
        return None
    target = season_label_for_draft_year(draft_year)
    tmp = table.copy()
    tmp[season_col] = tmp[season_col].astype(str)
    exact = tmp[tmp[season_col].eq(target)]
    if exact.empty:
        return None
    return exact.iloc[0]


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
        col = get_col(row.index, candidates)
        if col is None:
            return pd.NA
        return row.get(col, pd.NA)

    return {
        "name": query_name,
        "draft_year": draft_year,
        "sportsref_player_raw": raw_page_name,
        "sportsref_url": url,
        "sportsref_match_method": match_method,
        "sportsref_match_score": match_score,
        "sportsref_school": val(["School", "Team"]),
        "sportsref_conf": val(["Conf", "Conference"]),
        "sportsref_season": val(["Season"]),
        "sportsref_games": to_numeric(val(["G", "Games"])),
        "sportsref_games_started": to_numeric(val(["GS", "Games Started"])),
        "sportsref_mpg": to_numeric(val(["MP", "MPG", "Minutes"])),
        "sportsref_ppg": to_numeric(val(["PTS", "Points"])),
        "sportsref_rpg": to_numeric(val(["TRB", "RPG", "Total Rebounds"])),
        "sportsref_apg": to_numeric(val(["AST", "APG", "Assists"])),
        "sportsref_spg": to_numeric(val(["STL", "SPG", "Steals"])),
        "sportsref_bpg": to_numeric(val(["BLK", "BPG", "Blocks"])),
        "sportsref_tpg": to_numeric(val(["TOV", "TPG", "Turnovers"])),
        "sportsref_fg_pct": to_numeric(val(["FG%", "FG_pct", "FG Pct"])),
        "sportsref_two_pct": to_numeric(val(["2P%", "2P_pct", "2P Pct"])),
        "sportsref_three_pct": to_numeric(val(["3P%", "3P_pct", "3P Pct"])),
        "sportsref_ft_pct": to_numeric(val(["FT%", "FT_pct", "FT Pct"])),
    }


@dataclass
class MatchResult:
    output: dict[str, Any] | None
    reason: str
    attempted_urls: list[str]
    page_name_score: float | None = None


def find_player_stats(session: requests.Session, player_name: str, draft_year: int) -> MatchResult:
    cleaned = clean_name(player_name)
    attempted: list[str] = []

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
        name_variants = [cleaned, compact_initials(cleaned), spaced_initials(cleaned)]
        name_score = max(fuzz.ratio(v, raw_page_clean) for v in set(name_variants)) if raw_page_clean else 0
        if name_score < MIN_PAGE_NAME_SCORE:
            continue

        tables = extract_tables_from_html(html)
        per_game = find_per_game_table(tables)
        if per_game is None:
            continue

        # For undrafted players without organization validation, require exact pre-draft season.
        season_row = extract_exact_target_season_row(per_game, draft_year)
        if season_row is None:
            continue

        output = row_to_output(
            season_row,
            cleaned,
            draft_year,
            url,
            raw_page_clean,
            "strict_slug_exact_season",
            float(name_score),
        )
        return MatchResult(output, "matched", attempted, float(name_score))

    return MatchResult(None, "not_found_or_not_confident", attempted)


def build_targets(base_csv: Path, start_year: int, end_year: int) -> pd.DataFrame:
    if not base_csv.exists() and base_csv.name == "nba_draft_full_clean_project_na_2000_2026.csv":
        fallback = base_csv.with_name("nba_draft_full_clean_2000_2026.csv")
        if fallback.exists():
            print(f"Base file not found: {base_csv}; using fallback: {fallback}")
            base_csv = fallback
    base = pd.read_csv(base_csv)
    required = {"name", "draft_year", "overall_pick", "organization"}
    missing = required - set(base.columns)
    if missing:
        raise ValueError(f"Base CSV missing required columns: {sorted(missing)}")

    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = pd.to_numeric(base["draft_year"], errors="coerce").astype("Int64")
    base["overall_pick"] = pd.to_numeric(base["overall_pick"], errors="coerce")

    targets = base[
        base["draft_year"].between(start_year, end_year)
        & base["overall_pick"].eq(999)
        & base["organization"].isna()
    ].copy()

    keep = [c for c in ["name", "draft_year", "overall_pick", "position", "organization", "organization_type"] if c in targets.columns]
    targets = targets[keep]
    targets = targets.drop_duplicates(subset=["name", "draft_year"])
    return targets.sort_values(["draft_year", "name"]).reset_index(drop=True)


def write_report(targets: pd.DataFrame, matched: pd.DataFrame, unmatched: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    match_rate = round(len(matched) / len(targets) * 100, 1) if len(targets) else 0.0

    rows_by_year = targets.groupby("draft_year").size().rename("targets").reset_index()
    matched_by_year = matched.groupby("draft_year").size().rename("matched").reset_index() if not matched.empty else pd.DataFrame(columns=["draft_year", "matched"])
    by_year = rows_by_year.merge(matched_by_year, on="draft_year", how="left")
    by_year["matched"] = by_year["matched"].fillna(0).astype(int)
    by_year["unmatched"] = by_year["targets"] - by_year["matched"]
    by_year["match_rate_pct"] = (by_year["matched"] / by_year["targets"] * 100).round(1)

    duplicate_count = int(matched.duplicated(subset=["name", "draft_year"]).sum()) if not matched.empty else 0

    missing_pct = pd.DataFrame()
    if not matched.empty:
        numeric_cols = [
            c for c in matched.columns
            if c.startswith("sportsref_")
            and c not in {
                "sportsref_player_raw", "sportsref_url", "sportsref_match_method",
                "sportsref_school", "sportsref_conf", "sportsref_season"
            }
        ]
        missing_pct = (
            matched[numeric_cols]
            .isna()
            .mean()
            .mul(100)
            .round(1)
            .sort_values(ascending=False)
            .rename("missing_pct")
            .reset_index()
            .rename(columns={"index": "column"})
        )

    summary = pd.DataFrame(
        [
            ["target_undrafted_players", len(targets)],
            ["matched_players", len(matched)],
            ["unmatched_players", len(unmatched)],
            ["match_rate_pct", match_rate],
            ["duplicate_name_draft_year_rows_after_resolution", duplicate_count],
            ["min_page_name_score", MIN_PAGE_NAME_SCORE],
            ["season_rule", "exact pre-draft season required"],
        ],
        columns=["metric", "value"],
    )

    lines = []
    lines.append("# Sports-Reference Early Undrafted NCAA Layer Report")
    lines.append("")
    lines.append("This is an experimental standalone layer. No final NBA Draft dataset was modified.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## Match Rate By draft_year")
    lines.append("")
    lines.append(by_year.to_markdown(index=False))
    lines.append("")
    lines.append("## Missing-Value Percentage For Matched Numeric Columns")
    lines.append("")
    lines.append(missing_pct.to_markdown(index=False) if not missing_pct.empty else "_None_")
    lines.append("")
    lines.append("## First 50 Matched Rows")
    lines.append("")
    lines.append(matched.head(50).to_markdown(index=False) if not matched.empty else "_None_")
    lines.append("")
    lines.append("## First 80 Unmatched Rows")
    lines.append("")
    lines.append(unmatched.head(80).to_markdown(index=False) if not unmatched.empty else "_None_")
    lines.append("")
    lines.append("## Output Columns")
    lines.append("")
    for col in OUTPUT_COLUMNS:
        lines.append(f"- {col}")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_na_2000_2026.csv")
    parser.add_argument("--start-year", type=int, default=2000)
    parser.add_argument("--end-year", type=int, default=2007)
    parser.add_argument("--out", default="data/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv")
    parser.add_argument("--unmatched-out", default="data/pre_draft_ncaa_sportsref_undrafted_2000_2007_unmatched.csv")
    parser.add_argument("--report", default="data/pre_draft_ncaa_sportsref_undrafted_report.md")
    parser.add_argument("--limit", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    targets = build_targets(Path(args.base), args.start_year, args.end_year)
    if args.limit is not None:
        targets = targets.head(args.limit).copy()

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; university-data-science-project/1.0; educational use)"
    })

    matched_rows: list[dict[str, Any]] = []
    unmatched_rows: list[dict[str, Any]] = []

    print(f"Target undrafted players: {len(targets)}")
    for i, row in targets.iterrows():
        player = row["name"]
        draft_year = int(row["draft_year"])
        print(f"[{i + 1}/{len(targets)}] {player} ({draft_year})")

        result = find_player_stats(session, player, draft_year)
        if result.output is not None:
            matched_rows.append(result.output)
        else:
            unmatched_rows.append({
                "name": player,
                "draft_year": draft_year,
                "overall_pick": row.get("overall_pick", pd.NA),
                "position": row.get("position", pd.NA),
                "reason": result.reason,
                "attempted_urls_count": len(result.attempted_urls),
            })

    matched = pd.DataFrame(matched_rows)
    for col in OUTPUT_COLUMNS:
        if col not in matched.columns:
            matched[col] = pd.NA
    matched = matched[OUTPUT_COLUMNS].drop_duplicates(subset=["name", "draft_year"]).sort_values(["draft_year", "name"]).reset_index(drop=True)

    unmatched = pd.DataFrame(unmatched_rows)
    if not unmatched.empty:
        unmatched = unmatched.sort_values(["draft_year", "name"]).reset_index(drop=True)

    out_path = Path(args.out)
    unmatched_path = Path(args.unmatched_out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    matched.to_csv(out_path, index=False)
    unmatched.to_csv(unmatched_path, index=False)
    write_report(targets, matched, unmatched, report_path)

    print(f"Saved matched CSV: {out_path}")
    print(f"Saved unmatched CSV: {unmatched_path}")
    print(f"Saved report: {report_path}")
    print(f"Matched: {len(matched)} / {len(targets)}")


if __name__ == "__main__":
    main()
