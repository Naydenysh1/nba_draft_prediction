#!/usr/bin/env python3
"""
Integrate the experimental Sports-Reference early-undrafted NCAA layer into the
project-facing NBA Draft dataset.

Inputs:
    data/nba_draft_full_clean_project_na_2000_2026.csv
    data/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv

Outputs:
    data/nba_draft_full_clean_project_na_plus_undrafted_2000_2026.csv
    data/nba_draft_full_clean_project_na_plus_undrafted_report.md

Important:
- This script does NOT create draft_tier.
- This script does NOT create z-scores or percentiles.
- This script does NOT impute missing values globally.
- It only fills confirmed NCAA Sports-Reference stats for matched undrafted 2000-2007 rows.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

SPORTSREF_TO_PROJECT = {
    "sportsref_school": "organization",
    "sportsref_conf": "ncaa_conf",
    "sportsref_games": "ncaa_games",
    "sportsref_mpg": "ncaa_mpg",
    "sportsref_ppg": "ncaa_ppg",
    "sportsref_rpg": "ncaa_rpg",
    "sportsref_apg": "ncaa_apg",
    "sportsref_spg": "ncaa_spg",
    "sportsref_bpg": "ncaa_bpg",
    "sportsref_tpg": "ncaa_tpg",
    "sportsref_fg_pct": "ncaa_fg_pct",
    "sportsref_two_pct": "ncaa_two_pct",
    "sportsref_three_pct": "ncaa_three_pct",
    "sportsref_ft_pct": "ncaa_ft_pct",
}

TECHNICAL_COLUMNS_TO_DROP = [
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


def to_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.replace("%", "", regex=False), errors="coerce")


def load_inputs(base_path: Path, undrafted_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not base_path.exists() and base_path.name == "nba_draft_full_clean_project_na_2000_2026.csv":
        fallback = base_path.with_name("nba_draft_full_clean_2000_2026.csv")
        if fallback.exists():
            print(f"Base file not found: {base_path}; using fallback: {fallback}")
            base_path = fallback
    base = pd.read_csv(base_path)
    undrafted = pd.read_csv(undrafted_path)

    for df in [base, undrafted]:
        if "name" not in df.columns or "draft_year" not in df.columns:
            raise ValueError("Both inputs must contain name and draft_year columns.")
        df["name"] = df["name"].map(clean_name)
        df["draft_year"] = pd.to_numeric(df["draft_year"], errors="coerce").astype("Int64")

    if "overall_pick" not in base.columns:
        raise ValueError("Base dataset must contain overall_pick.")
    base["overall_pick"] = pd.to_numeric(base["overall_pick"], errors="coerce")

    return base, undrafted


def prepare_undrafted_layer(undrafted: pd.DataFrame) -> pd.DataFrame:
    layer = undrafted.copy()

    # One row per player-year. The standalone scraper already resolved duplicates,
    # but keep this defensive check.
    layer = layer.drop_duplicates(subset=["name", "draft_year"], keep="first")

    for src, dst in SPORTSREF_TO_PROJECT.items():
        if src not in layer.columns:
            layer[src] = pd.NA
        layer[dst] = layer[src]

    layer["organization_type"] = np.where(layer["organization"].notna(), "College/University", pd.NA)

    keep_cols = ["name", "draft_year", "organization_type"] + list(SPORTSREF_TO_PROJECT.values())
    keep_cols = list(dict.fromkeys(keep_cols))
    layer = layer[keep_cols]

    numeric_cols = [c for c in layer.columns if c.startswith("ncaa_") and c not in {"ncaa_conf"}]
    for col in numeric_cols:
        layer[col] = to_numeric(layer[col])

    return layer


def integrate(base: pd.DataFrame, layer: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    out = base.copy()

    # Ensure all destination columns exist.
    for col in ["organization", "organization_type", *[c for c in SPORTSREF_TO_PROJECT.values() if c != "organization"]]:
        if col not in out.columns:
            out[col] = pd.NA

    # We only allow filling the intended target rows.
    target_mask = (
        out["draft_year"].between(2000, 2007)
        & out["overall_pick"].eq(999)
        & out["organization"].isna()
    )

    before_target_rows = int(target_mask.sum())

    joined = out.reset_index().merge(
        layer,
        on=["name", "draft_year"],
        how="left",
        suffixes=("", "_undrafted_sr"),
    ).set_index("index")

    matched_mask = target_mask & joined["organization_undrafted_sr"].notna()

    fill_cols = ["organization", "organization_type", *[c for c in SPORTSREF_TO_PROJECT.values() if c != "organization"]]
    for col in fill_cols:
        src_col = f"{col}_undrafted_sr"
        if src_col in joined.columns:
            out.loc[matched_mask, col] = joined.loc[matched_mask, src_col]

    # Defensive cleanup: remove any accidental technical columns.
    out = out.drop(columns=[c for c in TECHNICAL_COLUMNS_TO_DROP if c in out.columns])

    audit = joined.loc[target_mask, ["name", "draft_year", "overall_pick", "organization_undrafted_sr"]].copy()
    audit["filled_from_undrafted_sportsref"] = audit["organization_undrafted_sr"].notna()
    audit = audit.rename(columns={"organization_undrafted_sr": "sportsref_school"})

    out["organization"] = out["organization"].replace("Unknown", pd.NA)
    out["organization_type"] = out["organization_type"].replace("Unknown", pd.NA)

    assert len(out) == len(base), "Row count changed during integration."
    assert out.duplicated(subset=["name", "draft_year", "overall_pick"]).sum() == 0, "Duplicates introduced."

    return out.reset_index(drop=True), audit.reset_index(drop=True)


def write_report(base: pd.DataFrame, final: pd.DataFrame, audit: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)

    filled = int(audit["filled_from_undrafted_sportsref"].sum())
    target = len(audit)

    summary = pd.DataFrame(
        [
            ["base_rows", len(base)],
            ["final_rows", len(final)],
            ["row_count_equals_base", len(base) == len(final)],
            ["base_columns", len(base.columns)],
            ["final_columns", len(final.columns)],
            ["target_early_undrafted_missing_org_rows", target],
            ["filled_from_undrafted_sportsref", filled],
            ["still_missing_after_fill", target - filled],
            ["duplicate_name_draft_year_pick_rows", int(final.duplicated(subset=["name", "draft_year", "overall_pick"]).sum())],
            ["missing_organization_before", int(base["organization"].isna().sum())],
            ["missing_organization_after", int(final["organization"].isna().sum())],
            ["missing_organization_type_before", int(base["organization_type"].isna().sum()) if "organization_type" in base.columns else pd.NA],
            ["missing_organization_type_after", int(final["organization_type"].isna().sum()) if "organization_type" in final.columns else pd.NA],
            ["ncaa_team_absent", "ncaa_team" not in final.columns],
            ["ncaa_match_method_absent", "ncaa_match_method" not in final.columns],
            ["ncaa_source_absent", "ncaa_source" not in final.columns],
            ["ncaa_player_raw_absent", "ncaa_player_raw" not in final.columns],
            ["sportsref_url_absent", "sportsref_url" not in final.columns],
            ["sportsref_match_method_absent", "sportsref_match_method" not in final.columns],
            ["sportsref_match_score_absent", "sportsref_match_score" not in final.columns],
            ["sportsref_player_raw_absent", "sportsref_player_raw" not in final.columns],
        ],
        columns=["metric", "value"],
    )

    by_year = audit.groupby("draft_year").agg(
        targets=("name", "size"),
        filled=("filled_from_undrafted_sportsref", "sum"),
    ).reset_index()
    by_year["filled"] = by_year["filled"].astype(int)
    by_year["still_missing"] = by_year["targets"] - by_year["filled"]
    by_year["fill_rate_pct"] = (by_year["filled"] / by_year["targets"] * 100).round(1)

    still_missing_examples = final[
        final["draft_year"].between(2000, 2007)
        & final["overall_pick"].eq(999)
        & final["organization"].isna()
    ][["name", "draft_year", "overall_pick", "position", "organization", "organization_type"]].head(80)

    filled_examples = final[
        final["draft_year"].between(2000, 2007)
        & final["overall_pick"].eq(999)
        & final["organization"].notna()
    ][[
        "name", "draft_year", "overall_pick", "position", "organization", "organization_type",
        "ncaa_conf", "ncaa_games", "ncaa_ppg", "ncaa_rpg", "ncaa_apg",
        "ncaa_fg_pct", "ncaa_two_pct", "ncaa_three_pct", "ncaa_ft_pct",
    ]].head(80)

    lines = []
    lines.append("# Final Project Dataset + Early Undrafted NCAA Fill Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(summary.to_markdown(index=False))
    lines.append("")
    lines.append("## Fill Rate By draft_year")
    lines.append("")
    lines.append(by_year.to_markdown(index=False))
    lines.append("")
    lines.append("## First 80 Filled Early Undrafted Examples")
    lines.append("")
    lines.append(filled_examples.to_markdown(index=False) if not filled_examples.empty else "_None_")
    lines.append("")
    lines.append("## First 80 Still-Missing Early Undrafted Examples")
    lines.append("")
    lines.append(still_missing_examples.to_markdown(index=False) if not still_missing_examples.empty else "_None_")
    lines.append("")
    lines.append("## Final Columns")
    lines.append("")
    for col in final.columns:
        lines.append(f"- {col}")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/nba_draft_full_clean_project_na_2000_2026.csv")
    parser.add_argument("--undrafted-sportsref", default="data/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv")
    parser.add_argument("--out", default="data/nba_draft_full_clean_project_final_2000_2026.csv")
    parser.add_argument("--report", default="data/nba_draft_full_clean_project_final_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base, undrafted = load_inputs(Path(args.base), Path(args.undrafted_sportsref))
    layer = prepare_undrafted_layer(undrafted)
    final, audit = integrate(base, layer)

    out_path = Path(args.out)
    report_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    final.to_csv(out_path, index=False)
    write_report(base, final, audit, report_path)

    print(f"Saved final project CSV: {out_path}")
    print(f"Saved report: {report_path}")
    print(f"Rows: {len(final)}")
    print(f"Columns: {len(final.columns)}")
    print(f"Filled early undrafted rows: {int(audit['filled_from_undrafted_sportsref'].sum())} / {len(audit)}")


if __name__ == "__main__":
    main()
