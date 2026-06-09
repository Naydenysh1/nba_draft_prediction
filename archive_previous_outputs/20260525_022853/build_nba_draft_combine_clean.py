#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import time
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from nba_api.stats.endpoints import (
    draftcombinedrillresults,
    draftcombineplayeranthro,
    drafthistory,
)


REQUEST_SLEEP_SECONDS = 1.2
NBA_TIMEOUT_SECONDS = 60

FINAL_COLUMNS = [
    "name",
    "draft_year",
    "overall_pick",
    "position",
    "organization",
    "organization_type",
    "draft_team_abbreviation",
    "height_wo_shoes_in",
    "height_w_shoes_in",
    "weight_lbs",
    "wingspan_in",
    "standing_reach_in",
    "body_fat_pct",
    "hand_length_in",
    "hand_width_in",
    "standing_vertical_leap_in",
    "max_vertical_leap_in",
    "lane_agility_time_sec",
    "modified_lane_agility_time_sec",
    "three_quarter_sprint_sec",
    "bench_press_reps",
]

COMBINE_COLUMNS = [
    "height_wo_shoes_in",
    "height_w_shoes_in",
    "weight_lbs",
    "wingspan_in",
    "standing_reach_in",
    "body_fat_pct",
    "hand_length_in",
    "hand_width_in",
    "standing_vertical_leap_in",
    "max_vertical_leap_in",
    "lane_agility_time_sec",
    "modified_lane_agility_time_sec",
    "three_quarter_sprint_sec",
    "bench_press_reps",
]


def clean_name(name: object) -> str:
    if pd.isna(name):
        return ""
    value = str(name).strip().lower()
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^a-z0-9 ]+", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = re.sub(r"\s+(jr|sr|ii|iii|iv|v)$", "", value).strip()
    return value


def safe_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.replace("%", "", regex=False), errors="coerce")


def first_df(endpoint_obj) -> pd.DataFrame:
    frames = endpoint_obj.get_data_frames()
    if not frames:
        return pd.DataFrame()
    return frames[0].copy()


def fetch_draft_history(start_year: int, end_year: int) -> pd.DataFrame:
    print("Fetching NBA Draft History...")
    raw = first_df(drafthistory.DraftHistory(league_id="00", timeout=NBA_TIMEOUT_SECONDS))
    if raw.empty:
        raise RuntimeError("DraftHistory returned no rows.")

    df = raw.rename(
        columns={
            "PERSON_ID": "nba_person_id",
            "PLAYER_NAME": "raw_name",
            "SEASON": "draft_year",
            "ROUND_NUMBER": "round_number",
            "ROUND_PICK": "round_pick",
            "OVERALL_PICK": "overall_pick",
            "TEAM_ABBREVIATION": "draft_team_abbreviation",
            "ORGANIZATION": "organization",
            "ORGANIZATION_TYPE": "organization_type",
        }
    )
    df["draft_year"] = safe_numeric(df["draft_year"]).astype("Int64")
    df["overall_pick"] = safe_numeric(df["overall_pick"]).astype("Int64")
    df["nba_person_id"] = safe_numeric(df["nba_person_id"]).astype("Int64")
    df["name"] = df["raw_name"].map(clean_name)
    df["nba_person_id_str"] = df["nba_person_id"].astype(str).replace("<NA>", "")

    keep = [
        "nba_person_id",
        "nba_person_id_str",
        "raw_name",
        "name",
        "draft_year",
        "overall_pick",
        "organization",
        "organization_type",
        "draft_team_abbreviation",
    ]
    df = df[[col for col in keep if col in df.columns]]
    df = df[df["draft_year"].between(start_year, end_year)].reset_index(drop=True)
    return df


def add_combine_key(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "PLAYER_ID" not in out.columns:
        out["PLAYER_ID"] = np.nan
    if "PLAYER_NAME" not in out.columns:
        out["PLAYER_NAME"] = ""
    out["combine_player_id"] = safe_numeric(out["PLAYER_ID"]).astype("Int64")
    out["combine_player_id_str"] = out["combine_player_id"].astype(str).replace("<NA>", "")
    out["name"] = out["PLAYER_NAME"].map(clean_name)
    out["combine_uid"] = np.arange(len(out), dtype=np.int64)
    return out


def fetch_combine_for_year(year: int) -> pd.DataFrame:
    print(f"Fetching NBA Combine data for {year}...")
    anthro = first_df(
        draftcombineplayeranthro.DraftCombinePlayerAnthro(
            season_year=str(year), league_id="00", timeout=NBA_TIMEOUT_SECONDS
        )
    )
    time.sleep(REQUEST_SLEEP_SECONDS)
    drills = first_df(
        draftcombinedrillresults.DraftCombineDrillResults(
            season_year=str(year), league_id="00", timeout=NBA_TIMEOUT_SECONDS
        )
    )
    time.sleep(REQUEST_SLEEP_SECONDS)

    if anthro.empty and drills.empty:
        return pd.DataFrame()

    tables = []
    for raw in [anthro, drills]:
        if raw.empty:
            continue
        keyed = add_combine_key(raw)
        keyed["draft_year"] = year
        tables.append(keyed)

    df = tables[0]
    for other in tables[1:]:
        duplicate_cols = [
            col
            for col in other.columns
            if col in df.columns and col not in {"draft_year", "combine_player_id_str", "name"}
        ]
        other = other.drop(columns=duplicate_cols, errors="ignore")
        df = df.merge(other, on=["draft_year", "combine_player_id_str", "name"], how="outer")

    rename_map = {
        "PLAYER_NAME": "raw_combine_name",
        "POSITION": "position",
        "HEIGHT_WO_SHOES": "height_wo_shoes_in",
        "HEIGHT_W_SHOES": "height_w_shoes_in",
        "WEIGHT": "weight_lbs",
        "WINGSPAN": "wingspan_in",
        "STANDING_REACH": "standing_reach_in",
        "BODY_FAT_PCT": "body_fat_pct",
        "HAND_LENGTH": "hand_length_in",
        "HAND_WIDTH": "hand_width_in",
        "STANDING_VERTICAL_LEAP": "standing_vertical_leap_in",
        "MAX_VERTICAL_LEAP": "max_vertical_leap_in",
        "LANE_AGILITY_TIME": "lane_agility_time_sec",
        "MODIFIED_LANE_AGILITY_TIME": "modified_lane_agility_time_sec",
        "THREE_QUARTER_SPRINT": "three_quarter_sprint_sec",
        "BENCH_PRESS": "bench_press_reps",
    }
    df = df.rename(columns={old: new for old, new in rename_map.items() if old in df.columns})

    for col in COMBINE_COLUMNS:
        if col in df.columns:
            df[col] = safe_numeric(df[col])
        else:
            df[col] = np.nan

    if "position" not in df.columns:
        df["position"] = pd.NA
    if "combine_uid" not in df.columns:
        df["combine_uid"] = np.arange(len(df), dtype=np.int64)

    keep = ["combine_uid", "combine_player_id_str", "name", "draft_year", "position", *COMBINE_COLUMNS]
    return df[[col for col in keep if col in df.columns]].reset_index(drop=True)


def fetch_combine_all_years(start_year: int, end_year: int) -> pd.DataFrame:
    frames = []
    uid_offset = 0
    for year in range(start_year, end_year + 1):
        year_df = fetch_combine_for_year(year)
        if year_df.empty:
            continue
        year_df["combine_uid"] = np.arange(uid_offset, uid_offset + len(year_df), dtype=np.int64)
        uid_offset += len(year_df)
        frames.append(year_df)
    if not frames:
        raise RuntimeError("No combine data fetched.")
    return pd.concat(frames, ignore_index=True, sort=False)


def merge_combine_into_drafted(draft: pd.DataFrame, combine: pd.DataFrame) -> tuple[pd.DataFrame, set[int]]:
    combine_for_id = combine[combine["combine_player_id_str"].astype(str).str.len() > 0].copy()
    drafted = draft.merge(
        combine_for_id,
        left_on=["draft_year", "nba_person_id_str"],
        right_on=["draft_year", "combine_player_id_str"],
        how="left",
        suffixes=("", "_combine"),
    )

    matched = set(
        pd.to_numeric(drafted["combine_uid"], errors="coerce").dropna().astype(int).tolist()
    )

    missing_combine = drafted["combine_uid"].isna()
    if missing_combine.any():
        fallback = (
            combine[~combine["combine_uid"].isin(matched)]
            .drop_duplicates(["draft_year", "name"], keep="first")
            .copy()
        )
        patch = draft.loc[missing_combine, ["draft_year", "name"]].merge(
            fallback,
            on=["draft_year", "name"],
            how="left",
        )
        target_idx = drafted.index[missing_combine]
        for col in ["combine_uid", "combine_player_id_str", "position", *COMBINE_COLUMNS]:
            if col not in patch.columns:
                continue
            values = pd.Series(patch[col].to_numpy(), index=target_idx)
            drafted.loc[target_idx, col] = drafted.loc[target_idx, col].combine_first(values)

    matched = set(
        pd.to_numeric(drafted["combine_uid"], errors="coerce").dropna().astype(int).tolist()
    )
    drafted["data_source"] = np.where(
        drafted["combine_uid"].notna(), "combine_and_draft_history", "draft_history_only"
    )
    return drafted, matched


def build_dataset(args: argparse.Namespace) -> tuple[pd.DataFrame, pd.DataFrame]:
    draft = fetch_draft_history(args.historical_start_year, args.historical_end_year)
    combine = fetch_combine_all_years(args.historical_start_year, args.prediction_year)

    drafted, matched_combine_uids = merge_combine_into_drafted(
        draft, combine[combine["draft_year"].between(args.historical_start_year, args.historical_end_year)]
    )

    historical_combine = combine[
        combine["draft_year"].between(args.historical_start_year, args.historical_end_year)
    ].copy()
    undrafted = historical_combine[~historical_combine["combine_uid"].isin(matched_combine_uids)].copy()
    undrafted["overall_pick"] = args.undrafted_overall_pick
    undrafted["organization"] = pd.NA
    undrafted["organization_type"] = pd.NA
    undrafted["draft_team_abbreviation"] = pd.NA
    undrafted["data_source"] = "combine_undrafted"

    prediction = combine[combine["draft_year"] == args.prediction_year].copy()
    prediction["overall_pick"] = pd.NA
    prediction["organization"] = pd.NA
    prediction["organization_type"] = pd.NA
    prediction["draft_team_abbreviation"] = pd.NA
    prediction["data_source"] = "prediction_combine"

    union = pd.concat([drafted, undrafted, prediction], ignore_index=True, sort=False)
    union["draft_year"] = safe_numeric(union["draft_year"]).astype("Int64")
    union["overall_pick"] = safe_numeric(union["overall_pick"]).astype("Int64")
    for col in COMBINE_COLUMNS:
        union[col] = safe_numeric(union[col])

    final = union[FINAL_COLUMNS].copy()
    final = final.sort_values(["draft_year", "overall_pick", "name"], na_position="last").reset_index(drop=True)

    report_frame = union.copy()
    report_frame = report_frame.sort_values(["draft_year", "overall_pick", "name"], na_position="last").reset_index(drop=True)
    return final, report_frame


def markdown_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "_None_"
    safe = df.copy().astype(object).where(pd.notna(df), "")
    columns = [str(col) for col in safe.columns]
    rows = safe.astype(str).values.tolist()
    header = "| " + " | ".join(col.replace("|", "\\|") for col in columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| " + " | ".join(value.replace("|", "\\|").replace("\n", " ") for value in row) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def series_table(series: pd.Series, index_name: str, value_name: str) -> str:
    return markdown_table(series.rename_axis(index_name).reset_index(name=value_name))


def build_report(final: pd.DataFrame, report_frame: pd.DataFrame, args: argparse.Namespace) -> str:
    expected_columns_ok = list(final.columns) == FINAL_COLUMNS
    rows_by_year = (
        final["draft_year"].value_counts().sort_index().rename_axis("draft_year").reset_index(name="rows")
    )
    known_pick_counts = (
        final[final["overall_pick"].notna()]
        .groupby("draft_year")
        .size()
        .reindex(range(args.historical_start_year, args.prediction_year + 1), fill_value=0)
        .rename_axis("draft_year")
        .reset_index(name="known_non_missing_overall_pick_rows")
    )
    historical = final[
        final["draft_year"].between(args.historical_start_year, args.historical_end_year)
    ]
    prediction = final[final["draft_year"] == args.prediction_year]
    undrafted_count = int((historical["overall_pick"] == args.undrafted_overall_pick).sum())
    prediction_pick_na = bool(prediction["overall_pick"].isna().all())
    historical_pick_na = int(historical["overall_pick"].isna().sum())
    duplicate_rows = final[
        final.duplicated(["name", "draft_year", "overall_pick"], keep=False)
    ].sort_values(["draft_year", "name", "overall_pick"])

    numeric_checks = []
    for col in COMBINE_COLUMNS:
        numeric = pd.to_numeric(final[col], errors="coerce")
        unparseable = int(final[col].notna().sum() - numeric.notna().sum())
        numeric_checks.append(
            {
                "column": col,
                "dtype": str(final[col].dtype),
                "non_null": int(final[col].notna().sum()),
                "unparseable_non_null": unparseable,
                "numeric_ok": unparseable == 0,
            }
        )
    numeric_checks_df = pd.DataFrame(numeric_checks)

    combine_missing = (
        (final[COMBINE_COLUMNS].isna().mean() * 100)
        .round(1)
        .rename_axis("column")
        .reset_index(name="missing_pct")
    )
    data_source_counts = report_frame["data_source"].value_counts(dropna=False)

    validation = pd.DataFrame(
        [
            {"check": "final_columns_exact", "passed": expected_columns_ok},
            {"check": "prediction_year_rows_have_overall_pick_na", "passed": prediction_pick_na},
            {"check": "historical_rows_with_overall_pick_na", "passed": historical_pick_na == 0},
            {"check": "duplicate_name_draft_year_overall_pick_rows", "passed": len(duplicate_rows) == 0},
            {"check": "all_combine_columns_numeric", "passed": bool(numeric_checks_df["numeric_ok"].all())},
        ]
    )

    lines = [
        "# NBA Draft Combine Clean Dataset Report",
        "",
        "## Summary",
        "",
        markdown_table(
            pd.DataFrame(
                [
                    {"metric": "rows", "value": len(final)},
                    {"metric": "columns", "value": len(final.columns)},
                    {"metric": "historical_start_year", "value": args.historical_start_year},
                    {"metric": "historical_end_year", "value": args.historical_end_year},
                    {"metric": "prediction_year", "value": args.prediction_year},
                    {"metric": "historical_undrafted_overall_pick_value", "value": args.undrafted_overall_pick},
                    {"metric": "historical_undrafted_rows_overall_pick_999", "value": undrafted_count},
                    {"metric": "prediction_year_rows", "value": len(prediction)},
                    {"metric": "historical_rows_with_overall_pick_na", "value": historical_pick_na},
                    {"metric": "duplicate_name_draft_year_overall_pick_rows", "value": len(duplicate_rows)},
                ]
            )
        ),
        "",
        "## Validation Checks",
        "",
        markdown_table(validation),
        "",
        "## Rows By draft_year",
        "",
        markdown_table(rows_by_year),
        "",
        "## Known overall_pick Counts By Year",
        "",
        markdown_table(known_pick_counts),
        "",
        "## Data Source Counts Before Final Column Drop",
        "",
        series_table(data_source_counts, "data_source", "count"),
        "",
        "## Final Columns",
        "",
        "\n".join(f"- {col}" for col in final.columns),
        "",
        "## Combine Numeric Conversion Checks",
        "",
        markdown_table(numeric_checks_df),
        "",
        "## Combine Missing-Value Percentage",
        "",
        markdown_table(combine_missing),
        "",
        "## Duplicate name + draft_year + overall_pick Rows",
        "",
        markdown_table(duplicate_rows.head(50)),
        "",
        "## First 30 Rows",
        "",
        markdown_table(final.head(30)),
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--historical-start-year", type=int, default=2000)
    parser.add_argument("--historical-end-year", type=int, default=2025)
    parser.add_argument("--prediction-year", type=int, default=2026)
    parser.add_argument("--undrafted-overall-pick", type=int, default=999)
    parser.add_argument("--out", type=Path, default=Path("data/nba_draft_combine_clean_2000_2026.csv"))
    parser.add_argument("--report", type=Path, default=Path("data/nba_draft_combine_clean_report.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    final, report_frame = build_dataset(args)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    final.to_csv(args.out, index=False)
    args.report.write_text(build_report(final, report_frame, args), encoding="utf-8")

    print("Saved:", args.out)
    print("Report:", args.report)
    print("Rows:", len(final))
    print("Columns:", len(final.columns))


if __name__ == "__main__":
    main()
