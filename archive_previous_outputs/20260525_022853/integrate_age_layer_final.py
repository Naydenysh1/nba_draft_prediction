#!/usr/bin/env python3
"""
Integrate the validated birth-date / draft-age v2 layer into the final project dataset.

Inputs:
    data/nba_draft_full_clean_project_final_2000_2026.csv
    data/player_birth_dates_2000_2026_v2.csv

Outputs:
    data/nba_draft_full_clean_project_final_with_age_2000_2026.csv
    data/nba_draft_full_clean_project_final_with_age_report.md

Important:
- Do NOT create draft_tier.
- Do NOT create z-scores or percentiles.
- Do NOT impute missing ages.
- Do NOT keep technical age-source columns in the final project CSV.
- Add only project-facing columns: birth_date and draft_age.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import pandas as pd

FINAL_ADD_COLUMNS = ["birth_date", "draft_age"]
TECHNICAL_AGE_COLUMNS = [
    "birth_date_source",
    "birth_date_confidence",
    "age_validation_status",
    "id_source",
    "draft_date",
]
TECHNICAL_DATASET_COLUMNS = [
    "ncaa_team",
    "ncaa_match_method",
    "ncaa_source",
    "ncaa_player_raw",
    "sportsref_url",
    "sportsref_match_method",
    "sportsref_match_score",
    "sportsref_player_raw",
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


def make_draft_group(row: pd.Series) -> str:
    pick = row.get("overall_pick")
    year = row.get("draft_year")
    if pd.isna(pick):
        if year == 2026:
            return "prediction_2026_unknown"
        return "missing_pick"
    if pick == 999:
        return "undrafted_999"
    if 1 <= pick <= 5:
        return "top_5"
    if 6 <= pick <= 14:
        return "picks_6_14"
    if 15 <= pick <= 30:
        return "picks_15_30"
    if 31 <= pick < 999:
        return "second_round"
    return "unknown"


def load_base(path: Path) -> pd.DataFrame:
    base = pd.read_csv(path)
    required = {"name", "draft_year", "overall_pick"}
    missing = required - set(base.columns)
    if missing:
        raise ValueError(f"Base dataset missing required columns: {sorted(missing)}")
    base["name"] = base["name"].map(clean_name)
    base["draft_year"] = pd.to_numeric(base["draft_year"], errors="coerce").astype("Int64")
    base["overall_pick"] = pd.to_numeric(base["overall_pick"], errors="coerce")
    return base


def load_age_layer(path: Path) -> pd.DataFrame:
    age = pd.read_csv(path)
    required = {"name", "draft_year", "overall_pick", "birth_date", "draft_age"}
    missing = required - set(age.columns)
    if missing:
        raise ValueError(f"Age layer missing required columns: {sorted(missing)}")
    age["name"] = age["name"].map(clean_name)
    age["draft_year"] = pd.to_numeric(age["draft_year"], errors="coerce").astype("Int64")
    age["overall_pick"] = pd.to_numeric(age["overall_pick"], errors="coerce")
    age["birth_date"] = pd.to_datetime(age["birth_date"], errors="coerce").dt.strftime("%Y-%m-%d")
    age["draft_age"] = pd.to_numeric(age["draft_age"], errors="coerce")

    # Keep only valid / accepted rows if validation status exists.
    if "age_validation_status" in age.columns:
        valid_mask = age["age_validation_status"].astype(str).str.startswith("valid_")
        missing_mask = age["age_validation_status"].eq("missing_birth_date")
        age.loc[~valid_mask & ~missing_mask, ["birth_date", "draft_age"]] = pd.NA

    age = age[["name", "draft_year", "overall_pick", "birth_date", "draft_age"]]
    age = age.drop_duplicates(subset=["name", "draft_year", "overall_pick"], keep="first")
    return age


def integrate(base: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    before_rows = len(base)

    # Remove pre-existing age columns to avoid suffix confusion, then add from v2 layer.
    base_no_age = base.drop(columns=[c for c in FINAL_ADD_COLUMNS if c in base.columns])
    merged = base_no_age.merge(age, on=["name", "draft_year", "overall_pick"], how="left")

    # Keep project-facing dataset clean.
    merged = merged.drop(columns=[c for c in TECHNICAL_AGE_COLUMNS + TECHNICAL_DATASET_COLUMNS if c in merged.columns])

    assert len(merged) == before_rows, "Row count changed during age integration."
    assert merged.duplicated(subset=["name", "draft_year", "overall_pick"]).sum() == 0, "Duplicates introduced."
    return merged


def write_report(base: pd.DataFrame, final: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    final_tmp = final.copy()
    final_tmp["draft_group_preview"] = final_tmp.apply(make_draft_group, axis=1)

    technical_absence_rows = [[f"{col}_absent", col not in final.columns] for col in TECHNICAL_DATASET_COLUMNS + TECHNICAL_AGE_COLUMNS]

    summary_rows = [
            ["base_rows", len(base)],
            ["final_rows", len(final)],
            ["row_count_equals_base", len(base) == len(final)],
            ["base_columns", len(base.columns)],
            ["final_columns", len(final.columns)],
            ["duplicate_name_draft_year_pick_rows", int(final.duplicated(subset=["name", "draft_year", "overall_pick"]).sum())],
            ["birth_date_rows", int(final["birth_date"].notna().sum())],
            ["birth_date_coverage_pct", round(final["birth_date"].notna().mean() * 100, 1)],
            ["draft_age_rows", int(final["draft_age"].notna().sum())],
            ["draft_age_coverage_pct", round(final["draft_age"].notna().mean() * 100, 1)],
            ["min_draft_age", round(final["draft_age"].min(skipna=True), 3)],
            ["max_draft_age", round(final["draft_age"].max(skipna=True), 3)],
    ]
    summary = pd.DataFrame(summary_rows + technical_absence_rows, columns=["metric", "value"])

    by_year = (
        final.groupby("draft_year")
        .agg(rows=("name", "size"), draft_age_rows=("draft_age", lambda s: int(s.notna().sum())))
        .reset_index()
    )
    by_year["missing_draft_age"] = by_year["rows"] - by_year["draft_age_rows"]
    by_year["draft_age_coverage_pct"] = (by_year["draft_age_rows"] / by_year["rows"] * 100).round(1)

    by_group = (
        final_tmp.groupby("draft_group_preview")
        .agg(rows=("name", "size"), draft_age_rows=("draft_age", lambda s: int(s.notna().sum())))
        .reset_index()
    )
    by_group["missing_draft_age"] = by_group["rows"] - by_group["draft_age_rows"]
    by_group["draft_age_coverage_pct"] = (by_group["draft_age_rows"] / by_group["rows"] * 100).round(1)

    youngest = final[final["draft_age"].notna()].sort_values("draft_age").head(30)
    oldest = final[final["draft_age"].notna()].sort_values("draft_age", ascending=False).head(30)
    missing_2026 = final[final["draft_year"].eq(2026) & final["draft_age"].isna()][
        ["name", "draft_year", "overall_pick", "position", "organization", "organization_type"]
    ].head(100)

    lines = []
    lines.append("# Final Project Dataset With Draft Age Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## Base Columns")
    lines.append("")
    for col in base.columns:
        lines.append(f"- {col}")
    lines.append("")
    lines.append("## Final Columns")
    lines.append("")
    for col in final.columns:
        lines.append(f"- {col}")
    lines.append("")
    lines.append("## Draft Age Coverage By draft_year")
    lines.append("")
    lines.append(by_year.to_markdown(index=False))
    lines.append("")
    lines.append("## Draft Age Coverage By draft_group_preview")
    lines.append("")
    lines.append(by_group.to_markdown(index=False))
    lines.append("")
    lines.append("## Youngest 30 Players")
    lines.append("")
    lines.append(youngest[["name", "draft_year", "overall_pick", "birth_date", "draft_age", "position", "organization"]].to_markdown(index=False))
    lines.append("")
    lines.append("## Oldest 30 Players")
    lines.append("")
    lines.append(oldest[["name", "draft_year", "overall_pick", "birth_date", "draft_age", "position", "organization"]].to_markdown(index=False))
    lines.append("")
    lines.append("## 2026 Rows Still Missing Draft Age")
    lines.append("")
    lines.append(missing_2026.to_markdown(index=False) if not missing_2026.empty else "_None_")
    lines.append("")
    lines.append("## Technical Column Absence Checks")
    lines.append("")
    absence_checks = pd.DataFrame(
        [{"column": col, "absent": col not in final.columns} for col in TECHNICAL_DATASET_COLUMNS + TECHNICAL_AGE_COLUMNS]
    )
    lines.append(absence_checks.to_markdown(index=False))

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_final_2000_2026.csv")
    parser.add_argument("--age", default="data/player_birth_dates_2000_2026_v2.csv")
    parser.add_argument("--out", default="data/nba_draft_full_clean_project_final_with_age_2000_2026.csv")
    parser.add_argument("--report", default="data/nba_draft_full_clean_project_final_with_age_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = load_base(Path(args.base))
    age = load_age_layer(Path(args.age))
    final = integrate(base, age)

    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    final.to_csv(out_path, index=False)
    write_report(base, final, report_path)

    print(f"Saved final dataset with age: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(final)}")
    print(f"Columns: {len(final.columns)}")
    print(f"Draft age coverage: {final['draft_age'].notna().mean() * 100:.1f}%")


if __name__ == "__main__":
    main()
