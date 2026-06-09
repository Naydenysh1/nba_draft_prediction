#!/usr/bin/env python3
"""
Repair 2026 NCAA alias matches and remaining 2026 organizations in the final NBA Draft project dataset.

Purpose:
- Work from the latest corrected dataset with organization restored from ncaa_team.
- Fill 2026 NCAA stats for players whose prospect names differ from NCAA source names.
- Fill organization for clearly non-NCAA / international 2026 prospects.
- Do NOT create draft_tier.
- Do NOT impute missing values.
- Do NOT add technical/provenance columns to the final CSV.

Inputs:
    data/nba_draft_full_clean_project_final_with_age_orgfix_2000_2026.csv
    plus one available NCAA source, preferably:
        data/pre_draft_ncaa_unified_2000_2026.csv
    or:
        data/pre_draft_ncaa_torvik_2008_2026_v2.csv

Outputs:
    data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_2000_2026.csv
    data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_report.md
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Any

import pandas as pd

TECHNICAL_COLUMNS_TO_REMOVE = [
    "ncaa_team",
    "ncaa_source",
    "ncaa_player_raw",
    "ncaa_match_method",
    "sportsref_url",
    "sportsref_match_method",
    "sportsref_match_score",
    "sportsref_player_raw",
    "birth_date_source",
    "birth_date_confidence",
    "age_validation_status",
    "id_source",
    "draft_date",
]

# Dataset name -> NCAA-layer name.
# These are 2026 prospect naming mismatches, not fuzzy matches.
NCAA_ALIAS_MAP = {
    ("anicet dybantsa", 2026): "aj dybantsa",
    ("christopher brown", 2026): "mikel brown",
    ("christopher cenac", 2026): "chris cenac",
    ("nathaniel ament", 2026): "nate ament",
    ("matthew able", 2026): "matt able",
    ("nicholas boyd", 2026): "nick boyd",
}

# Organization-only fixes for 2026 players who are not NCAA players in the current season.
# These should not receive NCAA stats from the NCAA layer.
NON_NCAA_ORG_MAP = {
    ("jack kayil", 2026): ("Alba Berlin", "Other Team/Club"),
    ("karim lopez", 2026): ("New Zealand Breakers", "Other Team/Club"),
    ("luigi suigo", 2026): ("Mega Basket (Serbia)", "Other Team/Club"),
    ("sergio de larrea", 2026): ("Valencia Basket", "Other Team/Club"),
}

NCAA_COLS_TO_COPY = [
    "ncaa_conf",
    "ncaa_pos",
    "ncaa_exp",
    "ncaa_height",
    "ncaa_games",
    "ncaa_mpg",
    "ncaa_ppg",
    "ncaa_fg_pct",
    "ncaa_two_pct",
    "ncaa_three_pct",
    "ncaa_ft_pct",
    "ncaa_oreb",
    "ncaa_dreb",
    "ncaa_rpg",
    "ncaa_apg",
    "ncaa_ast_to",
    "ncaa_spg",
    "ncaa_bpg",
    "ncaa_tpg",
    "ncaa_ortg",
    "ncaa_adj_oe",
    "ncaa_drtg",
    "ncaa_porpag",
    "ncaa_dporpag",
    "ncaa_bpm",
    "ncaa_obpm",
    "ncaa_dbpm",
    "ncaa_usage",
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


def normalize_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in cols:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    return out


def read_dataset(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["name"] = df["name"].map(clean_name)
    df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce").astype("Int64")
    if "overall_pick" in df.columns:
        df["overall_pick"] = pd.to_numeric(df["overall_pick"], errors="coerce")
    return df


def find_ncaa_source(paths: list[str]) -> Path:
    for p in paths:
        path = Path(p)
        if path.exists():
            return path
    raise FileNotFoundError(
        "No NCAA source file found. Expected one of: " + ", ".join(paths)
    )


def prepare_ncaa_lookup(ncaa_path: Path) -> pd.DataFrame:
    ncaa = pd.read_csv(ncaa_path)
    if "name" not in ncaa.columns or "draft_year" not in ncaa.columns:
        raise ValueError("NCAA source must contain name and draft_year")

    ncaa["name"] = ncaa["name"].map(clean_name)
    ncaa["draft_year"] = pd.to_numeric(ncaa["draft_year"], errors="coerce").astype("Int64")

    # Some source-specific files may not include ncaa_two_pct; keep missing if absent.
    for col in ["ncaa_team", *NCAA_COLS_TO_COPY]:
        if col not in ncaa.columns:
            ncaa[col] = pd.NA

    # Defensive duplicate resolution: prefer rows with more core stats present and more minutes/games.
    ncaa["_nonnull_core"] = ncaa[["ncaa_team", "ncaa_ppg", "ncaa_rpg", "ncaa_apg", "ncaa_bpm", "ncaa_usage"]].notna().sum(axis=1)
    ncaa = ncaa.sort_values(
        ["name", "draft_year", "_nonnull_core", "ncaa_mpg", "ncaa_games"],
        ascending=[True, True, False, False, False],
        na_position="last",
    )
    ncaa = ncaa.drop_duplicates(subset=["name", "draft_year"], keep="first")
    return ncaa.drop(columns=["_nonnull_core"])


def apply_ncaa_alias_repairs(df: pd.DataFrame, ncaa: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    out = df.copy()
    audit = []

    ncaa_index = {
        (row["name"], int(row["draft_year"])): row
        for _, row in ncaa[ncaa["draft_year"].eq(2026)].iterrows()
    }

    for (base_name, year), alias_name in NCAA_ALIAS_MAP.items():
        mask = out["name"].eq(base_name) & out["draft_year"].eq(year)
        if not mask.any():
            audit.append({
                "name": base_name,
                "draft_year": year,
                "alias_name": alias_name,
                "status": "base_row_not_found",
            })
            continue

        key = (clean_name(alias_name), year)
        if key not in ncaa_index:
            audit.append({
                "name": base_name,
                "draft_year": year,
                "alias_name": alias_name,
                "status": "alias_not_found_in_ncaa_source",
            })
            continue

        row = ncaa_index[key]
        changed_cols = []

        if pd.notna(row.get("ncaa_team", pd.NA)):
            out.loc[mask, "organization"] = row["ncaa_team"]
            out.loc[mask, "organization_type"] = "College/University"
            changed_cols.extend(["organization", "organization_type"])

        for col in NCAA_COLS_TO_COPY:
            if col in out.columns and col in row.index and pd.notna(row[col]):
                out.loc[mask, col] = row[col]
                changed_cols.append(col)

        audit.append({
            "name": base_name,
            "draft_year": year,
            "alias_name": alias_name,
            "status": "filled_from_ncaa_alias",
            "ncaa_team": row.get("ncaa_team", pd.NA),
            "ncaa_ppg": row.get("ncaa_ppg", pd.NA),
            "ncaa_bpm": row.get("ncaa_bpm", pd.NA),
            "changed_cols_count": len(set(changed_cols)),
        })

    return out, audit


def apply_non_ncaa_org_repairs(df: pd.DataFrame) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    out = df.copy()
    audit = []
    for (name, year), (org, org_type) in NON_NCAA_ORG_MAP.items():
        mask = out["name"].eq(name) & out["draft_year"].eq(year)
        if not mask.any():
            audit.append({
                "name": name,
                "draft_year": year,
                "organization": org,
                "organization_type": org_type,
                "status": "base_row_not_found",
            })
            continue

        out.loc[mask, "organization"] = org
        out.loc[mask, "organization_type"] = org_type
        audit.append({
            "name": name,
            "draft_year": year,
            "organization": org,
            "organization_type": org_type,
            "status": "filled_non_ncaa_organization_only",
        })
    return out, audit


def write_report(
    before: pd.DataFrame,
    after: pd.DataFrame,
    ncaa_path: Path,
    ncaa_audit: list[dict[str, Any]],
    org_audit: list[dict[str, Any]],
    report_path: Path,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    before_2026 = before[before["draft_year"].eq(2026)].copy()
    after_2026 = after[after["draft_year"].eq(2026)].copy()

    summary_rows = [
        ["rows_before", len(before)],
        ["rows_after", len(after)],
        ["row_count_unchanged", len(before) == len(after)],
        ["columns_after", len(after.columns)],
        ["duplicate_name_draft_year_pick_rows", int(after.duplicated(subset=["name", "draft_year", "overall_pick"]).sum())],
        ["ncaa_source_file", str(ncaa_path)],
        ["2026_rows", len(after_2026)],
        ["2026_missing_organization_before", int(before_2026["organization"].isna().sum())],
        ["2026_missing_organization_after", int(after_2026["organization"].isna().sum())],
        ["2026_missing_ncaa_ppg_before", int(before_2026["ncaa_ppg"].isna().sum())],
        ["2026_missing_ncaa_ppg_after", int(after_2026["ncaa_ppg"].isna().sum())],
        ["2026_has_ncaa_ppg_after", int(after_2026["ncaa_ppg"].notna().sum())],
    ]
    summary_rows.extend([[f"technical_{col}_absent", col not in after.columns] for col in TECHNICAL_COLUMNS_TO_REMOVE])
    summary = pd.DataFrame(summary_rows, columns=["metric", "value"])

    after_missing_2026 = after_2026[after_2026["ncaa_ppg"].isna()][[
        "name", "draft_year", "overall_pick", "position", "organization", "organization_type",
        "ncaa_conf", "ncaa_ppg", "ncaa_bpm", "draft_age"
    ]]

    repaired_2026 = after_2026[after_2026["name"].isin([k[0] for k in NCAA_ALIAS_MAP.keys()] + [k[0] for k in NON_NCAA_ORG_MAP.keys()])][[
        "name", "draft_year", "overall_pick", "position", "organization", "organization_type",
        "ncaa_conf", "ncaa_pos", "ncaa_exp", "ncaa_games", "ncaa_ppg", "ncaa_rpg", "ncaa_apg", "ncaa_bpm", "draft_age"
    ]]

    lines = []
    lines.append("# 2026 NCAA Alias / Organization Repair Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## NCAA Alias Repair Audit")
    lines.append("")
    lines.append(pd.DataFrame(ncaa_audit).to_markdown(index=False) if ncaa_audit else "_None_")
    lines.append("")
    lines.append("## Non-NCAA Organization Repair Audit")
    lines.append("")
    lines.append(pd.DataFrame(org_audit).to_markdown(index=False) if org_audit else "_None_")
    lines.append("")
    lines.append("## Repaired / Reviewed 2026 Rows")
    lines.append("")
    lines.append(repaired_2026.to_markdown(index=False) if not repaired_2026.empty else "_None_")
    lines.append("")
    lines.append("## 2026 Rows Still Missing NCAA PPG")
    lines.append("")
    lines.append(after_missing_2026.to_markdown(index=False) if not after_missing_2026.empty else "_None_")
    lines.append("")
    lines.append("## Final Columns")
    lines.append("")
    for col in after.columns:
        lines.append(f"- {col}")
    lines.append("")
    lines.append("## Technical Column Absence Checks")
    lines.append("")
    absence_checks = pd.DataFrame(
        [{"column": col, "absent": col not in after.columns} for col in TECHNICAL_COLUMNS_TO_REMOVE]
    )
    lines.append(absence_checks.to_markdown(index=False))

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2000_2026.csv")
    parser.add_argument(
        "--ncaa-source",
        default=None,
        help="Optional explicit NCAA source CSV. If omitted, common final/intermediate NCAA files are tried.",
    )
    parser.add_argument("--out", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_2000_2026.csv")
    parser.add_argument("--report", default="data/nba_draft_full_clean_project_final_with_age_orgfix_2026repair_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_path = Path(args.base)
    before = read_dataset(base_path)

    candidate_ncaa_paths = []
    if args.ncaa_source:
        candidate_ncaa_paths.append(args.ncaa_source)
    candidate_ncaa_paths.extend([
        "data/pre_draft_ncaa_unified_2000_2026.csv",
        "data/pre_draft_ncaa_torvik_2008_2026_v2.csv",
        "data/pre_draft_ncaa_torvik_2008_2026.csv",
    ])
    ncaa_path = find_ncaa_source(candidate_ncaa_paths)
    ncaa = prepare_ncaa_lookup(ncaa_path)

    after, ncaa_audit = apply_ncaa_alias_repairs(before, ncaa)
    after, org_audit = apply_non_ncaa_org_repairs(after)

    # Remove any technical columns if they accidentally exist.
    after = after.drop(columns=[c for c in TECHNICAL_COLUMNS_TO_REMOVE if c in after.columns])

    assert len(after) == len(before), "Row count changed."
    assert after.duplicated(subset=["name", "draft_year", "overall_pick"]).sum() == 0, "Duplicates introduced."

    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    after.to_csv(out_path, index=False)
    write_report(before, after, ncaa_path, ncaa_audit, org_audit, report_path)

    print(f"Saved repaired dataset: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(after)}")
    print(f"Columns: {len(after.columns)}")
    print(f"2026 missing organization: {after[after['draft_year'].eq(2026)]['organization'].isna().sum()}")
    print(f"2026 missing ncaa_ppg: {after[after['draft_year'].eq(2026)]['ncaa_ppg'].isna().sum()}")


if __name__ == "__main__":
    main()
