#!/usr/bin/env python3
"""
Build v2 standalone birth-date / draft-age layer.

This script does not modify or merge into the final project dataset.
"""

from __future__ import annotations

import argparse
import re
import time
import unicodedata
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from nba_api.stats.endpoints import (
    commonplayerinfo,
    drafthistory,
    draftcombineplayeranthro,
    draftcombinedrillresults,
)

REQUEST_SLEEP_SECONDS = 1.1
COMMON_PLAYER_SLEEP_SECONDS = 0.8
WIKIDATA_SLEEP_SECONDS = 0.25
NBA_TIMEOUT_SECONDS = 60

FINAL_COLUMNS = [
    "name",
    "draft_year",
    "overall_pick",
    "birth_date",
    "draft_date",
    "draft_age",
    "birth_date_source",
    "birth_date_confidence",
    "age_validation_status",
]

COMBINE_ID_SOURCE = "combine_player_id"
DRAFT_ID_SOURCE = "draft_history_person_id"

# Verified draft event dates. For two-day drafts, this uses the first draft date.
DRAFT_DATES = {
    2000: "2000-06-28",
    2001: "2001-06-27",
    2002: "2002-06-26",
    2003: "2003-06-26",
    2004: "2004-06-24",
    2005: "2005-06-28",
    2006: "2006-06-28",
    2007: "2007-06-28",
    2008: "2008-06-26",
    2009: "2009-06-25",
    2010: "2010-06-24",
    2011: "2011-06-23",
    2012: "2012-06-28",
    2013: "2013-06-27",
    2014: "2014-06-26",
    2015: "2015-06-25",
    2016: "2016-06-23",
    2017: "2017-06-22",
    2018: "2018-06-21",
    2019: "2019-06-20",
    2020: "2020-11-18",
    2021: "2021-07-29",
    2022: "2022-06-23",
    2023: "2023-06-22",
    2024: "2024-06-26",
    2025: "2025-06-25",
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
    parsed = pd.to_datetime(str(value).strip(), errors="coerce")
    if pd.isna(parsed):
        return pd.NaT
    return parsed.normalize()


def compute_age_years(birth_date: Any, draft_date: Any) -> float | pd.NA:
    birth = pd.to_datetime(birth_date, errors="coerce")
    draft = pd.to_datetime(draft_date, errors="coerce")
    if pd.isna(birth) or pd.isna(draft):
        return pd.NA
    return round((draft - birth).days / 365.25, 3)


def name_matches(project_name: str, display_name: object) -> bool:
    left = clean_name(project_name)
    right = clean_name(display_name)
    if left == right:
        return True
    # Handles initial and apostrophe variants such as cj vs c j and o shae vs oshae.
    return left.replace(" ", "") == right.replace(" ", "")


def normalized_draft_year(value: Any) -> int | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    if not text or text.lower() in {"undrafted", "na", "none"}:
        return None
    match = re.search(r"\d{4}", text)
    return int(match.group(0)) if match else None


def build_draft_dates(start_year: int, end_year: int) -> tuple[dict[int, str], pd.DataFrame]:
    rows = []
    dates = {}
    for year in range(start_year, end_year + 1):
        if year in DRAFT_DATES:
            dates[year] = DRAFT_DATES[year]
            source = "verified_hardcoded"
        else:
            dates[year] = f"{year}-06-25"
            source = "approximate_june_25"
        rows.append({"draft_year": year, "draft_date": dates[year], "draft_date_source": source})
    return dates, pd.DataFrame(rows)


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
    df["id_source"] = DRAFT_ID_SOURCE
    df = df[df["draft_year"].between(start_year, min(end_year, 2025))]
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
            frames.append(
                pd.concat(year_frames, ignore_index=True).drop_duplicates(
                    subset=["name", "draft_year", "person_id"]
                )
            )

    if not frames:
        return pd.DataFrame(columns=["name", "draft_year", "person_id", "id_source"])
    combine = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["name", "draft_year", "person_id"])
    combine["id_source"] = COMBINE_ID_SOURCE
    return combine[["name", "draft_year", "person_id", "id_source"]]


def load_cache(cache_path: Path) -> pd.DataFrame:
    cols = [
        "person_id",
        "birth_date",
        "birth_date_source",
        "display_first_last",
        "draft_year_api",
        "draft_number_api",
        "school_api",
        "country_api",
    ]
    if cache_path.exists():
        cache = pd.read_csv(cache_path)
        rename = {"raw_display_first_last": "display_first_last"}
        cache = cache.rename(columns=rename)
        for col in cols:
            if col not in cache.columns:
                cache[col] = pd.NA
        cache["person_id"] = to_numeric(cache["person_id"])
        return cache[cols]
    return pd.DataFrame(columns=cols)


def save_cache(cache: pd.DataFrame, cache_path: Path) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache.drop_duplicates(subset=["person_id"], keep="last").to_csv(cache_path, index=False)


def fetch_common_player_info_row(person_id: int) -> dict[str, Any]:
    try:
        info = first_df(commonplayerinfo.CommonPlayerInfo(player_id=int(person_id), timeout=NBA_TIMEOUT_SECONDS))
        time.sleep(COMMON_PLAYER_SLEEP_SECONDS)
        if info.empty:
            return {
                "person_id": person_id,
                "birth_date": pd.NA,
                "birth_date_source": "common_player_info_empty",
                "display_first_last": pd.NA,
                "draft_year_api": pd.NA,
                "draft_number_api": pd.NA,
                "school_api": pd.NA,
                "country_api": pd.NA,
            }

        row = info.iloc[0]
        birth = parse_birth_date(row.get("BIRTHDATE", pd.NA))
        return {
            "person_id": person_id,
            "birth_date": birth.strftime("%Y-%m-%d") if not pd.isna(birth) else pd.NA,
            "birth_date_source": "nba_api_commonplayerinfo"
            if not pd.isna(birth)
            else "nba_api_commonplayerinfo_missing_birthdate",
            "display_first_last": row.get("DISPLAY_FIRST_LAST", pd.NA),
            "draft_year_api": row.get("DRAFT_YEAR", pd.NA),
            "draft_number_api": row.get("DRAFT_NUMBER", pd.NA),
            "school_api": row.get("SCHOOL", pd.NA),
            "country_api": row.get("COUNTRY", pd.NA),
        }
    except Exception as exc:
        time.sleep(COMMON_PLAYER_SLEEP_SECONDS)
        return {
            "person_id": person_id,
            "birth_date": pd.NA,
            "birth_date_source": f"common_player_info_error:{type(exc).__name__}",
            "display_first_last": pd.NA,
            "draft_year_api": pd.NA,
            "draft_number_api": pd.NA,
            "school_api": pd.NA,
            "country_api": pd.NA,
        }


def build_id_candidates(base: pd.DataFrame, draft_ids: pd.DataFrame, combine_ids: pd.DataFrame) -> pd.DataFrame:
    base_keys = base[["name", "draft_year", "overall_pick"]].copy()
    base_keys["row_id"] = np.arange(len(base_keys))

    drafted_candidates = base_keys.merge(draft_ids, on=["name", "draft_year", "overall_pick"], how="left")
    drafted_candidates = drafted_candidates[["row_id", "person_id", "id_source"]].dropna(subset=["person_id"])

    combine_candidates = base_keys.merge(combine_ids, on=["name", "draft_year"], how="left")
    combine_candidates = combine_candidates[["row_id", "person_id", "id_source"]].dropna(subset=["person_id"])

    candidates = pd.concat([drafted_candidates, combine_candidates], ignore_index=True)
    if candidates.empty:
        return candidates

    source_priority = {DRAFT_ID_SOURCE: 1, COMBINE_ID_SOURCE: 2}
    candidates["_priority"] = candidates["id_source"].map(source_priority).fillna(99)
    return (
        candidates.sort_values(["row_id", "_priority"])
        .drop_duplicates(subset=["row_id"], keep="first")
        .drop(columns=["_priority"])
        .reset_index(drop=True)
    )


def wikidata_search_birth_date(name: str, draft_year: int, draft_date: str) -> dict[str, Any] | None:
    try:
        params = {
            "action": "wbsearchentities",
            "search": name,
            "language": "en",
            "format": "json",
            "limit": 5,
        }
        response = requests.get(
            "https://www.wikidata.org/w/api.php",
            params=params,
            headers={"User-Agent": "nba-draft-ml-project/1.0"},
            timeout=20,
        )
        time.sleep(WIKIDATA_SLEEP_SECONDS)
        if response.status_code != 200:
            return None
        results = response.json().get("search", [])
        exact = []
        for item in results:
            label = clean_name(item.get("label", ""))
            aliases = [clean_name(a) for a in item.get("aliases", [])]
            if clean_name(name) == label or clean_name(name) in aliases:
                exact.append(item)
        if not exact:
            return None

        qid = exact[0].get("id")
        entity_response = requests.get(
            f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json",
            headers={"User-Agent": "nba-draft-ml-project/1.0"},
            timeout=20,
        )
        time.sleep(WIKIDATA_SLEEP_SECONDS)
        if entity_response.status_code != 200:
            return None
        entity = entity_response.json().get("entities", {}).get(qid, {})
        claims = entity.get("claims", {})
        birth_claims = claims.get("P569", [])
        if not birth_claims:
            return None
        value = birth_claims[0].get("mainsnak", {}).get("datavalue", {}).get("value", {})
        date_raw = value.get("time")
        if not date_raw:
            return None
        birth = parse_birth_date(str(date_raw).replace("+", ""))
        if pd.isna(birth):
            return None
        age = compute_age_years(birth.strftime("%Y-%m-%d"), draft_date)
        if pd.isna(age) or age < 16 or age > 30:
            return None
        description = entity.get("descriptions", {}).get("en", {}).get("value", "")
        return {
            "birth_date": birth.strftime("%Y-%m-%d"),
            "birth_date_source": "wikidata_fallback",
            "birth_date_confidence": "medium",
            "wikidata_id": qid,
            "wikidata_description": description,
        }
    except Exception:
        return None


def validate_nba_api_birth(row: pd.Series) -> tuple[bool, str, str]:
    if pd.isna(row.get("birth_date")):
        return False, "missing_birth_date", "none"

    api_name = row.get("display_first_last")
    if not name_matches(row["name"], api_name):
        return False, "rejected_name_mismatch", "none"

    age = row.get("draft_age")
    if pd.isna(age):
        return False, "missing_draft_age", "none"
    if float(age) < 16 or float(age) > 30:
        return False, "rejected_suspicious_age", "none"

    project_pick = row.get("overall_pick")
    is_drafted = not pd.isna(project_pick) and float(project_pick) != 999
    if is_drafted:
        api_year = normalized_draft_year(row.get("draft_year_api"))
        if api_year is not None and int(api_year) != int(row["draft_year"]):
            return False, "rejected_draft_year_mismatch", "none"

    return True, "valid_nba_api", "high"


def draft_group(row: pd.Series) -> str:
    pick = row.get("overall_pick")
    year = row.get("draft_year")
    if pd.isna(pick):
        if int(year) == 2026:
            return "prediction_2026_unknown"
        return "missing_pick"
    pick = float(pick)
    if pick == 999:
        return "undrafted_999"
    if 1 <= pick <= 5:
        return "top_5"
    if 6 <= pick <= 14:
        return "picks_6_14"
    if 15 <= pick <= 30:
        return "picks_15_30"
    if pick >= 31:
        return "second_round"
    return "missing_pick"


def build_birth_date_layer(args: argparse.Namespace) -> tuple[pd.DataFrame, dict[str, Any], pd.DataFrame, pd.DataFrame]:
    base = pd.read_csv(args.base)
    required = {"name", "draft_year", "overall_pick"}
    missing = required - set(base.columns)
    if missing:
        raise ValueError(f"Base CSV missing columns: {sorted(missing)}")

    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = to_numeric(base["draft_year"]).astype("Int64")
    base["overall_pick"] = to_numeric(base["overall_pick"])
    base["row_id"] = np.arange(len(base))

    start_year = int(base["draft_year"].min())
    end_year = int(base["draft_year"].max())
    draft_dates, draft_date_audit = build_draft_dates(start_year, end_year)

    draft_ids = fetch_draft_history_ids(start_year, end_year)
    combine_ids = fetch_combine_ids(start_year, end_year)
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
        fetched_rows.append(fetch_common_player_info_row(pid))
        if i % 50 == 0:
            cache = pd.concat([cache, pd.DataFrame(fetched_rows)], ignore_index=True)
            save_cache(cache, cache_path)
            fetched_rows = []
    if fetched_rows:
        cache = pd.concat([cache, pd.DataFrame(fetched_rows)], ignore_index=True)
        save_cache(cache, cache_path)

    cache = load_cache(cache_path)
    candidates = candidates.merge(cache, on="person_id", how="left") if not candidates.empty else candidates

    out = base[["row_id", "name", "draft_year", "overall_pick"]].merge(candidates, on="row_id", how="left")
    out["draft_date"] = out["draft_year"].map(lambda y: draft_dates.get(int(y), pd.NA) if not pd.isna(y) else pd.NA)
    out["draft_age"] = [compute_age_years(b, d) for b, d in zip(out["birth_date"], out["draft_date"])]

    out["birth_date_confidence"] = "none"
    validation = out.apply(validate_nba_api_birth, axis=1, result_type="expand")
    out["_accepted"] = validation[0]
    out["age_validation_status"] = validation[1]
    out["birth_date_confidence"] = validation[2]

    suspicious_examples = out[(out["birth_date"].notna()) & (~out["_accepted"])].copy()

    reject_mask = ~out["_accepted"]
    out.loc[reject_mask, "birth_date"] = pd.NA
    out.loc[reject_mask, "draft_age"] = pd.NA
    out.loc[out["birth_date"].isna() & out["age_validation_status"].eq("missing_birth_date"), "birth_date_source"] = (
        out.loc[out["birth_date"].isna() & out["age_validation_status"].eq("missing_birth_date"), "birth_date_source"]
        .fillna("no_birth_date_from_nba_api")
    )
    out["birth_date_source"] = out["birth_date_source"].fillna("no_person_id_match")

    missing_rows = out[out["birth_date"].isna()].copy()
    print(f"Wikidata fallback attempts for missing rows: {len(missing_rows)}")
    for idx, row in missing_rows.iterrows():
        result = wikidata_search_birth_date(row["name"], int(row["draft_year"]), row["draft_date"])
        if result is None:
            continue
        out.loc[idx, "birth_date"] = result["birth_date"]
        out.loc[idx, "birth_date_source"] = result["birth_date_source"]
        out.loc[idx, "birth_date_confidence"] = result["birth_date_confidence"]
        out.loc[idx, "draft_age"] = compute_age_years(result["birth_date"], row["draft_date"])
        out.loc[idx, "age_validation_status"] = "valid_wikidata_fallback"

    out.loc[out["birth_date"].isna(), "birth_date_confidence"] = "none"
    out.loc[out["birth_date"].isna() & out["age_validation_status"].isna(), "age_validation_status"] = "missing_birth_date"

    final = out[FINAL_COLUMNS].copy()

    stats = {
        "base_rows": len(base),
        "birth_date_rows": int(final["birth_date"].notna().sum()),
        "draft_age_rows": int(final["draft_age"].notna().sum()),
        "candidate_person_id_rows": int(candidates["row_id"].nunique()) if not candidates.empty else 0,
        "unique_person_ids": len(person_ids),
        "suspicious_ages_rejected": int((suspicious_examples["age_validation_status"] == "rejected_suspicious_age").sum()),
        "rejected_rows_total": int(len(suspicious_examples)),
    }
    return final, stats, draft_date_audit, suspicious_examples


def write_report(
    layer: pd.DataFrame,
    stats: dict[str, Any],
    draft_date_audit: pd.DataFrame,
    suspicious_examples: pd.DataFrame,
    report_path: Path,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    coverage = round(stats["birth_date_rows"] / stats["base_rows"] * 100, 1) if stats["base_rows"] else 0.0
    age_coverage = round(stats["draft_age_rows"] / stats["base_rows"] * 100, 1) if stats["base_rows"] else 0.0

    report_df = layer.copy()
    report_df["draft_group"] = report_df.apply(draft_group, axis=1)

    summary = pd.DataFrame(
        [
            ["base_rows", stats["base_rows"]],
            ["candidate_person_id_rows", stats["candidate_person_id_rows"]],
            ["unique_person_ids", stats["unique_person_ids"]],
            ["birth_date_rows", stats["birth_date_rows"]],
            ["birth_date_coverage_pct", coverage],
            ["draft_age_rows", stats["draft_age_rows"]],
            ["draft_age_coverage_pct", age_coverage],
            ["suspicious_ages_rejected", stats["suspicious_ages_rejected"]],
            ["rejected_rows_total", stats["rejected_rows_total"]],
        ],
        columns=["metric", "value"],
    )

    by_year = (
        report_df.groupby("draft_year")
        .agg(rows=("name", "size"), birth_dates=("birth_date", lambda s: int(s.notna().sum())))
        .reset_index()
    )
    by_year["missing_birth_dates"] = by_year["rows"] - by_year["birth_dates"]
    by_year["birth_date_coverage_pct"] = (by_year["birth_dates"] / by_year["rows"] * 100).round(1)

    by_group = (
        report_df.groupby("draft_group")
        .agg(rows=("name", "size"), birth_dates=("birth_date", lambda s: int(s.notna().sum())))
        .reset_index()
    )
    by_group["birth_date_coverage_pct"] = (by_group["birth_dates"] / by_group["rows"] * 100).round(1)

    source_counts = report_df.groupby("birth_date_source", dropna=False).size().rename("rows").reset_index()
    status_counts = report_df.groupby("age_validation_status", dropna=False).size().rename("rows").reset_index()
    age_desc = report_df["draft_age"].dropna().describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]).to_frame("draft_age").reset_index()
    youngest = report_df[report_df["draft_age"].notna()].sort_values("draft_age").head(30)
    oldest = report_df[report_df["draft_age"].notna()].sort_values("draft_age", ascending=False).head(30)
    missing_examples = report_df[report_df["birth_date"].isna()].head(80)
    coverage_2026 = by_year[by_year["draft_year"].eq(2026)]

    suspicious_cols = [
        "name",
        "draft_year",
        "overall_pick",
        "person_id",
        "birth_date",
        "draft_date",
        "draft_age",
        "birth_date_source",
        "display_first_last",
        "draft_year_api",
        "draft_number_api",
        "age_validation_status",
    ]
    suspicious_report = suspicious_examples[[c for c in suspicious_cols if c in suspicious_examples.columns]].head(80)

    lines = [
        "# Birth Date / Draft Age Layer v2 Report",
        "",
        "This is a standalone layer. The final project dataset was not modified.",
        "",
        "## Summary",
        "",
        summary.to_markdown(index=False),
        "",
        "## Draft Date Audit",
        "",
        draft_date_audit.to_markdown(index=False),
        "",
        "## Coverage By draft_year",
        "",
        by_year.to_markdown(index=False),
        "",
        "## 2026 Coverage",
        "",
        coverage_2026.to_markdown(index=False) if not coverage_2026.empty else "_No 2026 rows_",
        "",
        "## Coverage By overall_pick Group",
        "",
        by_group.to_markdown(index=False),
        "",
        "## Suspicious / Rejected Examples",
        "",
        suspicious_report.to_markdown(index=False) if not suspicious_report.empty else "_None_",
        "",
        "## Rows By Birth Date Source",
        "",
        source_counts.to_markdown(index=False),
        "",
        "## Rows By Age Validation Status",
        "",
        status_counts.to_markdown(index=False),
        "",
        "## Draft Age Distribution",
        "",
        age_desc.to_markdown(index=False),
        "",
        "## Youngest 30 Valid Players",
        "",
        youngest.to_markdown(index=False),
        "",
        "## Oldest 30 Valid Players",
        "",
        oldest.to_markdown(index=False),
        "",
        "## First 80 Missing Birth Date Examples",
        "",
        missing_examples.to_markdown(index=False) if not missing_examples.empty else "_None_",
        "",
        "## Output Columns",
        "",
    ]
    lines.extend(f"- {col}" for col in FINAL_COLUMNS)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_final_2000_2026.csv")
    parser.add_argument("--out", default="data/player_birth_dates_2000_2026_v2.csv")
    parser.add_argument("--report", default="data/player_birth_dates_2000_2026_v2_report.md")
    parser.add_argument("--cache", default="data/cache/player_birth_dates_nba_api_cache.csv")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    layer, stats, draft_date_audit, suspicious_examples = build_birth_date_layer(args)
    layer.to_csv(out_path, index=False)
    write_report(layer, stats, draft_date_audit, suspicious_examples, report_path)

    print(f"Saved birth-date layer v2: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(layer)}")
    print(f"Birth dates found: {int(layer['birth_date'].notna().sum())}")
    print(f"Draft ages found: {int(layer['draft_age'].notna().sum())}")
    print(f"Suspicious ages rejected: {stats['suspicious_ages_rejected']}")


if __name__ == "__main__":
    main()
