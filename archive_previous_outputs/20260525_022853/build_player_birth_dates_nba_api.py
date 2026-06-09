#!/usr/bin/env python3
"""
Build a standalone birth-date / draft-age layer for the NBA Draft ML project.

Purpose:
- Add an important prospect-age feature without storing technical NBA IDs in the final dataset.
- Use NBA Stats API as the first source for birth dates.
- Do NOT modify or merge into the final project dataset yet.

Input:
    data/nba_draft_full_clean_project_final_2000_2026.csv

Outputs:
    data/player_birth_dates_nba_api_2000_2026.csv
    data/player_birth_dates_nba_api_report.md
    data/cache/player_birth_dates_nba_api_cache.csv

Install:
    pip install pandas numpy nba_api requests beautifulsoup4 lxml tabulate

Run:
    python build_player_birth_dates_nba_api.py \
        --base data/nba_draft_full_clean_project_final_2000_2026.csv \
        --out data/player_birth_dates_nba_api_2000_2026.csv \
        --report data/player_birth_dates_nba_api_report.md
"""

from __future__ import annotations

import argparse
import re
import time
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from nba_api.stats.endpoints import (
    commonplayerinfo,
    drafthistory,
    draftcombineplayeranthro,
    draftcombinedrillresults,
)

REQUEST_SLEEP_SECONDS = 1.2
COMMON_PLAYER_SLEEP_SECONDS = 0.8
NBA_TIMEOUT_SECONDS = 60

FINAL_COLUMNS = [
    "name",
    "draft_year",
    "overall_pick",
    "birth_date",
    "draft_date",
    "draft_age",
    "birth_date_source",
    "id_source",
]

# Fallbacks are only used if scraping Basketball-Reference date text fails.
# For 2026, the first round is scheduled for 2026-06-23.
DRAFT_DATE_FALLBACKS = {
    2026: "2026-06-23",
}


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


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def first_df(endpoint_obj: Any) -> pd.DataFrame:
    frames = endpoint_obj.get_data_frames()
    if not frames:
        return pd.DataFrame()
    return frames[0].copy()


def parse_birth_date(value: Any) -> pd.Timestamp | pd.NaT:
    if pd.isna(value):
        return pd.NaT
    s = str(value).strip()
    if not s:
        return pd.NaT
    return pd.to_datetime(s, errors="coerce").normalize()


def compute_age_years(birth_date: Any, draft_date: Any) -> float | pd.NA:
    birth = pd.to_datetime(birth_date, errors="coerce")
    draft = pd.to_datetime(draft_date, errors="coerce")
    if pd.isna(birth) or pd.isna(draft):
        return pd.NA
    return round((draft - birth).days / 365.25, 3)


def fetch_draft_date_from_basketball_reference(year: int) -> tuple[str | None, str]:
    url = f"https://www.basketball-reference.com/draft/NBA_{year}.html"
    try:
        response = requests.get(
            url,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0 (educational data science project)"},
        )
        if response.status_code != 200:
            return None, f"basketball_reference_http_{response.status_code}"
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ", strip=True)
        # Examples usually look like: Date: Thursday, June 25, 2009
        match = re.search(r"Date:\s*([A-Za-z]+,\s+[A-Za-z]+\s+\d{1,2},\s+\d{4})", text)
        if not match:
            match = re.search(r"Date:\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})", text)
        if not match:
            return None, "basketball_reference_date_not_found"
        parsed = pd.to_datetime(match.group(1), errors="coerce")
        if pd.isna(parsed):
            return None, "basketball_reference_date_parse_failed"
        return parsed.strftime("%Y-%m-%d"), "basketball_reference"
    except Exception as exc:
        return None, f"basketball_reference_error:{type(exc).__name__}"


def build_draft_dates(start_year: int, end_year: int) -> tuple[dict[int, str], pd.DataFrame]:
    dates: dict[int, str] = {}
    audit_rows = []
    for year in range(start_year, end_year + 1):
        if year <= 2025:
            date_str, source = fetch_draft_date_from_basketball_reference(year)
            time.sleep(0.4)
            if date_str is not None:
                dates[year] = date_str
                audit_rows.append({"draft_year": year, "draft_date": date_str, "draft_date_source": source})
                continue

        fallback = DRAFT_DATE_FALLBACKS.get(year)
        if fallback is not None:
            dates[year] = fallback
            audit_rows.append({"draft_year": year, "draft_date": fallback, "draft_date_source": "fallback_manual"})
        else:
            # Last-resort approximation, but mark it clearly in the report.
            approx = f"{year}-06-25"
            dates[year] = approx
            audit_rows.append({"draft_year": year, "draft_date": approx, "draft_date_source": "approximate_june_25"})

    return dates, pd.DataFrame(audit_rows)


def fetch_draft_history_ids(start_year: int, end_year: int) -> pd.DataFrame:
    print("Fetching NBA Draft History IDs...")
    raw = first_df(drafthistory.DraftHistory(league_id="00", timeout=NBA_TIMEOUT_SECONDS))
    if raw.empty:
        return pd.DataFrame(columns=["name", "draft_year", "overall_pick", "person_id", "id_source"])

    df = raw.rename(
        columns={
            "PLAYER_NAME": "raw_name",
            "SEASON": "draft_year",
            "OVERALL_PICK": "overall_pick",
            "PERSON_ID": "person_id",
        }
    )
    df["name"] = df["raw_name"].map(clean_name)
    df["draft_year"] = to_numeric(df["draft_year"]).astype("Int64")
    df["overall_pick"] = to_numeric(df["overall_pick"])
    df["person_id"] = to_numeric(df["person_id"])
    df["id_source"] = "draft_history_person_id"
    df = df[df["draft_year"].between(start_year, end_year)]
    return df[["name", "draft_year", "overall_pick", "person_id", "id_source"]].dropna(subset=["person_id"])


def add_combine_keys(df: pd.DataFrame, year: int) -> pd.DataFrame:
    out = df.copy()
    if "PLAYER_ID" not in out.columns:
        out["PLAYER_ID"] = pd.NA
    if "PLAYER_NAME" not in out.columns:
        out["PLAYER_NAME"] = ""
    out["name"] = out["PLAYER_NAME"].map(clean_name)
    out["draft_year"] = year
    out["person_id"] = to_numeric(out["PLAYER_ID"])
    return out[["name", "draft_year", "person_id"]].dropna(subset=["person_id"])


def fetch_combine_ids(start_year: int, end_year: int) -> pd.DataFrame:
    frames = []
    for year in range(start_year, end_year + 1):
        print(f"Fetching combine IDs for {year}...")
        year_frames = []
        try:
            anthro = first_df(
                draftcombineplayeranthro.DraftCombinePlayerAnthro(
                    season_year=str(year), league_id="00", timeout=NBA_TIMEOUT_SECONDS
                )
            )
            if not anthro.empty:
                year_frames.append(add_combine_keys(anthro, year))
            time.sleep(REQUEST_SLEEP_SECONDS)
        except Exception as exc:
            print(f"WARNING: combine anthro failed for {year}: {exc}")

        try:
            drills = first_df(
                draftcombinedrillresults.DraftCombineDrillResults(
                    season_year=str(year), league_id="00", timeout=NBA_TIMEOUT_SECONDS
                )
            )
            if not drills.empty:
                year_frames.append(add_combine_keys(drills, year))
            time.sleep(REQUEST_SLEEP_SECONDS)
        except Exception as exc:
            print(f"WARNING: combine drills failed for {year}: {exc}")

        if year_frames:
            year_df = pd.concat(year_frames, ignore_index=True).drop_duplicates(subset=["name", "draft_year", "person_id"])
            frames.append(year_df)

    if not frames:
        return pd.DataFrame(columns=["name", "draft_year", "person_id", "id_source"])

    combine = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["name", "draft_year", "person_id"])
    combine["id_source"] = "combine_player_id"
    return combine[["name", "draft_year", "person_id", "id_source"]]


def load_cache(cache_path: Path) -> pd.DataFrame:
    if cache_path.exists():
        cache = pd.read_csv(cache_path)
        if "person_id" in cache.columns:
            cache["person_id"] = to_numeric(cache["person_id"])
        return cache
    return pd.DataFrame(columns=["person_id", "birth_date", "birth_date_source", "raw_display_first_last"])


def save_cache(cache: pd.DataFrame, cache_path: Path) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache.drop_duplicates(subset=["person_id"], keep="last").to_csv(cache_path, index=False)


def fetch_common_player_birth_date(person_id: int) -> dict[str, Any]:
    try:
        info = first_df(commonplayerinfo.CommonPlayerInfo(player_id=int(person_id), timeout=NBA_TIMEOUT_SECONDS))
        time.sleep(COMMON_PLAYER_SLEEP_SECONDS)
        if info.empty:
            return {
                "person_id": person_id,
                "birth_date": pd.NA,
                "birth_date_source": "common_player_info_empty",
                "raw_display_first_last": pd.NA,
            }

        row = info.iloc[0]
        birth = parse_birth_date(row.get("BIRTHDATE", pd.NA))
        return {
            "person_id": person_id,
            "birth_date": birth.strftime("%Y-%m-%d") if not pd.isna(birth) else pd.NA,
            "birth_date_source": "nba_api_commonplayerinfo" if not pd.isna(birth) else "nba_api_commonplayerinfo_missing_birthdate",
            "raw_display_first_last": row.get("DISPLAY_FIRST_LAST", pd.NA),
        }
    except Exception as exc:
        time.sleep(COMMON_PLAYER_SLEEP_SECONDS)
        return {
            "person_id": person_id,
            "birth_date": pd.NA,
            "birth_date_source": f"common_player_info_error:{type(exc).__name__}",
            "raw_display_first_last": pd.NA,
        }


def build_id_candidates(base: pd.DataFrame, draft_ids: pd.DataFrame, combine_ids: pd.DataFrame) -> pd.DataFrame:
    base_keys = base[["name", "draft_year", "overall_pick"]].copy()
    base_keys["row_id"] = np.arange(len(base_keys))

    # 1. Drafted rows: exact name + year + real pick.
    drafted_candidates = base_keys.merge(
        draft_ids,
        on=["name", "draft_year", "overall_pick"],
        how="left",
    )
    drafted_candidates = drafted_candidates[["row_id", "person_id", "id_source"]].dropna(subset=["person_id"])

    # 2. Combine rows: exact name + year.
    combine_candidates = base_keys.merge(
        combine_ids,
        on=["name", "draft_year"],
        how="left",
    )
    combine_candidates = combine_candidates[["row_id", "person_id", "id_source"]].dropna(subset=["person_id"])

    candidates = pd.concat([drafted_candidates, combine_candidates], ignore_index=True)
    if candidates.empty:
        return candidates

    source_priority = {"draft_history_person_id": 1, "combine_player_id": 2}
    candidates["_priority"] = candidates["id_source"].map(source_priority).fillna(99)
    candidates = candidates.sort_values(["row_id", "_priority"]).drop_duplicates(subset=["row_id"], keep="first")
    return candidates.drop(columns=["_priority"]).reset_index(drop=True)


def build_birth_date_layer(args: argparse.Namespace) -> tuple[pd.DataFrame, dict[str, Any], pd.DataFrame]:
    base = pd.read_csv(args.base)
    required = {"name", "draft_year", "overall_pick"}
    missing = required - set(base.columns)
    if missing:
        raise ValueError(f"Base CSV missing columns: {sorted(missing)}")

    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = to_numeric(base["draft_year"]).astype("Int64")
    base["overall_pick"] = to_numeric(base["overall_pick"])
    base["row_id"] = np.arange(len(base))

    draft_dates, draft_date_audit = build_draft_dates(args.start_year, args.end_year)

    draft_ids = fetch_draft_history_ids(args.start_year, min(args.end_year, 2025))
    combine_ids = fetch_combine_ids(args.start_year, args.end_year)
    candidates = build_id_candidates(base, draft_ids, combine_ids)

    person_ids = sorted(candidates["person_id"].dropna().astype(int).unique().tolist()) if not candidates.empty else []

    cache_path = Path(args.cache)
    cache = load_cache(cache_path)
    cached_ids = set(cache["person_id"].dropna().astype(int).tolist()) if not cache.empty else set()
    needed_ids = [pid for pid in person_ids if pid not in cached_ids]

    print(f"Base rows: {len(base)}")
    print(f"Rows with candidate person_id: {candidates['row_id'].nunique() if not candidates.empty else 0}")
    print(f"Unique person_ids: {len(person_ids)}")
    print(f"Need to fetch CommonPlayerInfo for: {len(needed_ids)}")

    fetched_rows = []
    for i, pid in enumerate(needed_ids, start=1):
        print(f"[{i}/{len(needed_ids)}] CommonPlayerInfo {pid}")
        fetched_rows.append(fetch_common_player_birth_date(pid))
        # Save progressively every 50 requests.
        if i % 50 == 0:
            cache = pd.concat([cache, pd.DataFrame(fetched_rows)], ignore_index=True)
            save_cache(cache, cache_path)
            fetched_rows = []

    if fetched_rows:
        cache = pd.concat([cache, pd.DataFrame(fetched_rows)], ignore_index=True)
        save_cache(cache, cache_path)

    cache = load_cache(cache_path)
    cache["person_id"] = to_numeric(cache["person_id"])
    candidates = candidates.merge(cache, on="person_id", how="left") if not candidates.empty else candidates

    out = base[["row_id", "name", "draft_year", "overall_pick"]].merge(candidates, on="row_id", how="left")
    out["draft_date"] = out["draft_year"].map(lambda y: draft_dates.get(int(y), pd.NA) if not pd.isna(y) else pd.NA)
    out["draft_age"] = [compute_age_years(b, d) for b, d in zip(out["birth_date"], out["draft_date"])]

    out["birth_date_source"] = out["birth_date_source"].fillna("no_person_id_match")
    out["id_source"] = out["id_source"].fillna("no_person_id_match")

    final = out[FINAL_COLUMNS].copy()

    stats = {
        "base_rows": len(base),
        "birth_date_rows": int(final["birth_date"].notna().sum()),
        "draft_age_rows": int(final["draft_age"].notna().sum()),
        "candidate_person_id_rows": int(candidates["row_id"].nunique()) if not candidates.empty else 0,
        "unique_person_ids": len(person_ids),
    }
    return final, stats, draft_date_audit


def write_report(layer: pd.DataFrame, stats: dict[str, Any], draft_date_audit: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    coverage = round(stats["birth_date_rows"] / stats["base_rows"] * 100, 1) if stats["base_rows"] else 0.0
    age_coverage = round(stats["draft_age_rows"] / stats["base_rows"] * 100, 1) if stats["base_rows"] else 0.0

    summary = pd.DataFrame(
        [
            ["base_rows", stats["base_rows"]],
            ["candidate_person_id_rows", stats["candidate_person_id_rows"]],
            ["unique_person_ids", stats["unique_person_ids"]],
            ["birth_date_rows", stats["birth_date_rows"]],
            ["birth_date_coverage_pct", coverage],
            ["draft_age_rows", stats["draft_age_rows"]],
            ["draft_age_coverage_pct", age_coverage],
        ],
        columns=["metric", "value"],
    )

    by_year = (
        layer.groupby("draft_year")
        .agg(rows=("name", "size"), birth_dates=("birth_date", lambda s: int(s.notna().sum())))
        .reset_index()
    )
    by_year["missing_birth_dates"] = by_year["rows"] - by_year["birth_dates"]
    by_year["birth_date_coverage_pct"] = (by_year["birth_dates"] / by_year["rows"] * 100).round(1)

    by_id_source = layer.groupby("id_source", dropna=False).size().rename("rows").reset_index()
    by_birth_source = layer.groupby("birth_date_source", dropna=False).size().rename("rows").reset_index()

    age_desc = layer["draft_age"].dropna().describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]).to_frame("draft_age").reset_index()

    missing_examples = layer[layer["birth_date"].isna()][["name", "draft_year", "overall_pick", "birth_date_source", "id_source"]].head(80)
    young_examples = layer[layer["draft_age"].notna()].sort_values("draft_age").head(30)
    old_examples = layer[layer["draft_age"].notna()].sort_values("draft_age", ascending=False).head(30)

    lines = []
    lines.append("# NBA API Birth Date / Draft Age Layer Report")
    lines.append("")
    lines.append("This is a standalone layer. The final project dataset was not modified.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## Draft Date Audit")
    lines.append("")
    lines.append(draft_date_audit.to_markdown(index=False))
    lines.append("")
    lines.append("## Birth Date Coverage By draft_year")
    lines.append("")
    lines.append(by_year.to_markdown(index=False))
    lines.append("")
    lines.append("## Rows By ID Source")
    lines.append("")
    lines.append(by_id_source.to_markdown(index=False))
    lines.append("")
    lines.append("## Rows By Birth Date Source")
    lines.append("")
    lines.append(by_birth_source.to_markdown(index=False))
    lines.append("")
    lines.append("## Draft Age Distribution")
    lines.append("")
    lines.append(age_desc.to_markdown(index=False))
    lines.append("")
    lines.append("## Youngest 30 Players With Draft Age")
    lines.append("")
    lines.append(young_examples.to_markdown(index=False))
    lines.append("")
    lines.append("## Oldest 30 Players With Draft Age")
    lines.append("")
    lines.append(old_examples.to_markdown(index=False))
    lines.append("")
    lines.append("## First 80 Missing Birth Date Examples")
    lines.append("")
    lines.append(missing_examples.to_markdown(index=False) if not missing_examples.empty else "_None_")
    lines.append("")
    lines.append("## Output Columns")
    lines.append("")
    for col in FINAL_COLUMNS:
        lines.append(f"- {col}")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_final_2000_2026.csv")
    parser.add_argument("--start-year", type=int, default=2000)
    parser.add_argument("--end-year", type=int, default=2026)
    parser.add_argument("--out", default="data/player_birth_dates_nba_api_2000_2026.csv")
    parser.add_argument("--report", default="data/player_birth_dates_nba_api_report.md")
    parser.add_argument("--cache", default="data/cache/player_birth_dates_nba_api_cache.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    layer, stats, draft_date_audit = build_birth_date_layer(args)
    layer.to_csv(out_path, index=False)
    write_report(layer, stats, draft_date_audit, report_path)

    print(f"Saved birth-date layer: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(layer)}")
    print(f"Birth dates found: {int(layer['birth_date'].notna().sum())}")
    print(f"Draft ages found: {int(layer['draft_age'].notna().sum())}")


if __name__ == "__main__":
    main()
