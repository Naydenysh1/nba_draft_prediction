#!/usr/bin/env python3
"""
Rebuild the final NBA Draft ML project dataset from milestone CSVs.

This script intentionally does not scrape external websites. It starts from the
clean NBA Draft/Combine base and applies the validated NCAA and age layers that
were saved as project milestones.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


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
    "birth_date",
    "draft_age",
]

NCAA_COLUMNS = [
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

NCAA_TEXT_COLS = [
    "ncaa_conf",
    "ncaa_pos",
    "ncaa_exp",
    "ncaa_height",
]

NCAA_NUMERIC_COLS = [
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

TECHNICAL_COLUMNS = [
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

MANUAL_NCAA_ALIASES = {
    ("wesley johnson", 2010): "wes johnson",
    ("enes freedom", 2011): "enes kanter",
    ("maurice harkless", 2012): "moe harkless",
    ("devyn marble", 2014): "roy devyn marble",
    ("bam adebayo", 2017): "edrice adebayo",
    ("t j leaf", 2017): "tj leaf",
    ("wes iwundu", 2017): "wesley iwundu",
    ("mo bamba", 2018): "amidou bamba",
    ("svi mykhailiuk", 2018): "sviatoslav mykhailiuk",
    ("nic claxton", 2019): "nicolas claxton",
    ("vj edgecombe", 2025): "j edgecombe",
}

NCAA_2026_ALIASES = {
    ("anicet dybantsa", 2026): "aj dybantsa",
    ("christopher brown", 2026): "mikel brown",
    ("christopher cenac", 2026): "chris cenac",
    ("nathaniel ament", 2026): "nate ament",
    ("matthew able", 2026): "matt able",
    ("nicholas boyd", 2026): "nick boyd",
}

NON_NCAA_2026_ORG_FIXES = {
    ("jack kayil", 2026): ("Alba Berlin", "Other Team/Club"),
    ("karim lopez", 2026): ("New Zealand Breakers", "Other Team/Club"),
    ("luigi suigo", 2026): ("Mega Basket (Serbia)", "Other Team/Club"),
    ("sergio de larrea", 2026): ("Valencia Basket", "Other Team/Club"),
}

AGE_NAME_ALIASES = {
    ("smith", 2004, 18.0): "smith",
}

SPORTSREF_UNDRAFTED_MAP = {
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


def clean_name(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip().lower()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


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


def ensure_numeric(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def prepare_ncaa_lookup(ncaa: pd.DataFrame) -> pd.DataFrame:
    ncaa = ncaa.copy()
    ncaa["draft_year"] = pd.to_numeric(ncaa["draft_year"], errors="coerce").astype("Int64")
    ncaa["_name_clean"] = ncaa["name"].map(clean_name)
    ncaa["_name_compact"] = ncaa["_name_clean"].map(compact_initials)
    ncaa["_name_spaced"] = ncaa["_name_clean"].map(spaced_initials)
    ncaa["_sort_mpg"] = pd.to_numeric(ncaa.get("ncaa_mpg"), errors="coerce")
    ncaa["_sort_games"] = pd.to_numeric(ncaa.get("ncaa_games"), errors="coerce")
    ncaa = ncaa.sort_values(["_sort_mpg", "_sort_games"], ascending=[False, False])
    return ncaa


def take_ncaa_columns(ncaa_row: pd.Series) -> dict[str, Any]:
    out = {col: ncaa_row.get(col, pd.NA) for col in NCAA_COLUMNS}
    out["organization_from_ncaa"] = ncaa_row.get("ncaa_team", pd.NA)
    return out


def make_lookup(ncaa: pd.DataFrame, key_col: str) -> dict[tuple[str, int], pd.Series]:
    deduped = ncaa.drop_duplicates(subset=[key_col, "draft_year"], keep="first")
    return {
        (str(row[key_col]), int(row["draft_year"])): row
        for _, row in deduped.iterrows()
        if pd.notna(row[key_col]) and pd.notna(row["draft_year"]) and str(row[key_col])
    }


def merge_ncaa(base: pd.DataFrame, ncaa: pd.DataFrame) -> pd.DataFrame:
    out = base.copy()
    for col in NCAA_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA

    ncaa = prepare_ncaa_lookup(ncaa)
    lookups = {
        "exact": make_lookup(ncaa, "_name_clean"),
        "compact": make_lookup(ncaa, "_name_compact"),
        "spaced": make_lookup(ncaa, "_name_spaced"),
    }

    org_from_ncaa = pd.Series(pd.NA, index=out.index, dtype="object")
    for idx, row in out.iterrows():
        year = int(row["draft_year"])
        name = clean_name(row["name"])
        keys = [
            ("exact", name),
            ("compact", compact_initials(name)),
            ("spaced", spaced_initials(name)),
        ]
        alias = MANUAL_NCAA_ALIASES.get((name, year)) or NCAA_2026_ALIASES.get((name, year))
        if alias:
            keys.append(("exact", clean_name(alias)))

        ncaa_row = None
        for method, key_name in keys:
            ncaa_row = lookups[method].get((key_name, year))
            if ncaa_row is not None:
                break
        if ncaa_row is None:
            continue

        values = take_ncaa_columns(ncaa_row)
        for col in NCAA_COLUMNS:
            out.at[idx, col] = values[col]
        org_from_ncaa.at[idx] = values["organization_from_ncaa"]

    missing_org = out["organization"].isna() | out["organization"].astype(str).str.strip().eq("")
    fill_org = missing_org & org_from_ncaa.notna()
    out.loc[fill_org, "organization"] = org_from_ncaa.loc[fill_org]
    out.loc[fill_org, "organization_type"] = "College/University"
    return out


def apply_sportsref_undrafted(out: pd.DataFrame, sportsref_path: Path) -> pd.DataFrame:
    if not sportsref_path.exists():
        return out
    sr = pd.read_csv(sportsref_path)
    sr["draft_year"] = pd.to_numeric(sr["draft_year"], errors="coerce").astype("Int64")
    sr = sr.drop_duplicates(subset=["name", "draft_year"], keep="first")
    sr_lookup = {(clean_name(r["name"]), int(r["draft_year"])): r for _, r in sr.iterrows()}

    target = (
        out["draft_year"].between(2000, 2007)
        & pd.to_numeric(out["overall_pick"], errors="coerce").eq(999)
        & (out["organization"].isna() | out["organization"].astype(str).str.strip().eq(""))
    )
    for idx, row in out[target].iterrows():
        sr_row = sr_lookup.get((clean_name(row["name"]), int(row["draft_year"])))
        if sr_row is None:
            continue
        for source_col, target_col in SPORTSREF_UNDRAFTED_MAP.items():
            if source_col in sr_row.index:
                out.at[idx, target_col] = sr_row[source_col]
        out.at[idx, "organization_type"] = "College/University"
    return out


def apply_2026_org_fixes(out: pd.DataFrame) -> pd.DataFrame:
    for (name, year), (org, org_type) in NON_NCAA_2026_ORG_FIXES.items():
        mask = out["draft_year"].eq(year) & out["name"].map(clean_name).eq(name)
        out.loc[mask, "organization"] = org
        out.loc[mask, "organization_type"] = org_type
    return out


def integrate_age(out: pd.DataFrame, age_path: Path, realgm_path: Path) -> pd.DataFrame:
    out = out.copy()
    out["birth_date"] = pd.NA
    out["draft_age"] = pd.NA

    age = pd.read_csv(age_path)
    if "age_validation_status" in age.columns:
        age = age[age["age_validation_status"].astype(str).str.startswith("valid_")].copy()
    age["overall_pick_key"] = pd.to_numeric(age["overall_pick"], errors="coerce").fillna(-1)
    out["overall_pick_key"] = pd.to_numeric(out["overall_pick"], errors="coerce").fillna(-1)
    age = age.drop_duplicates(subset=["name", "draft_year", "overall_pick_key"], keep="first")
    joined = out.reset_index().merge(
        age[["name", "draft_year", "overall_pick_key", "birth_date", "draft_age"]],
        on=["name", "draft_year", "overall_pick_key"],
        how="left",
        suffixes=("", "_age"),
    ).set_index("index")
    out["birth_date"] = joined["birth_date_age"]
    out["draft_age"] = pd.to_numeric(joined["draft_age_age"], errors="coerce")
    out = out.drop(columns=["overall_pick_key"])

    age_alias_lookup = {
        (clean_name(r["name"]), int(r["draft_year"]), float(pd.to_numeric(r["overall_pick"], errors="coerce"))): r
        for _, r in age.iterrows()
        if pd.notna(pd.to_numeric(r["overall_pick"], errors="coerce"))
    }
    for (base_name, year, pick), age_name in AGE_NAME_ALIASES.items():
        mask = (
            out["draft_year"].eq(year)
            & out["name"].map(clean_name).eq(base_name)
            & pd.to_numeric(out["overall_pick"], errors="coerce").eq(pick)
            & out["draft_age"].isna()
        )
        age_row = age_alias_lookup.get((clean_name(age_name), year, pick))
        if age_row is not None:
            out.loc[mask, "birth_date"] = age_row["birth_date"]
            out.loc[mask, "draft_age"] = pd.to_numeric(age_row["draft_age"], errors="coerce")

    if realgm_path.exists():
        rg = pd.read_csv(realgm_path)
        rg = rg.drop_duplicates(subset=["name", "draft_year"], keep="first")
        rg_lookup = {(clean_name(r["name"]), int(r["draft_year"])): r for _, r in rg.iterrows()}
        missing_2026 = out["draft_year"].eq(2026) & out["draft_age"].isna()
        for idx, row in out[missing_2026].iterrows():
            rg_row = rg_lookup.get((clean_name(row["name"]), int(row["draft_year"])))
            if rg_row is None:
                continue
            out.at[idx, "birth_date"] = rg_row["birth_date"]
            out.at[idx, "draft_age"] = pd.to_numeric(rg_row["draft_age"], errors="coerce")

    jaden_mask = out["draft_year"].eq(2026) & out["name"].map(clean_name).eq("jaden harris")
    out.loc[jaden_mask, "birth_date"] = "2005-07-22"
    draft_date = pd.Timestamp("2026-06-23")
    jaden_birth = pd.Timestamp("2005-07-22")
    out.loc[jaden_mask, "draft_age"] = round((draft_date - jaden_birth).days / 365.25, 3)
    return out


def draft_group(row: pd.Series) -> str:
    year = int(row["draft_year"])
    pick = pd.to_numeric(row["overall_pick"], errors="coerce")
    if year == 2026 and pd.isna(pick):
        return "prediction_2026_unknown"
    if pick == 999:
        return "undrafted_999"
    if pd.isna(pick):
        return "unknown"
    if pick <= 5:
        return "top_5"
    if pick <= 14:
        return "picks_6_14"
    if pick <= 30:
        return "picks_15_30"
    return "second_round"


def missing_summary(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    present = [c for c in columns if c in df.columns]
    return pd.DataFrame(
        {
            "column": present,
            "missing_pct": [round(df[c].isna().mean() * 100, 2) for c in present],
            "non_missing": [int(df[c].notna().sum()) for c in present],
        }
    )


def validate(df: pd.DataFrame) -> dict[str, Any]:
    year_2026 = df[df["draft_year"].eq(2026)]
    groups = df.apply(draft_group, axis=1)
    return {
        "final_rows": len(df),
        "final_columns": len(df.columns),
        "duplicate_name_draft_year_pick_rows": int(df.duplicated(["name", "draft_year", "overall_pick"]).sum()),
        "2026_rows": len(year_2026),
        "2026_missing_organization": int(year_2026["organization"].isna().sum()),
        "2026_draft_age_rows": int(year_2026["draft_age"].notna().sum()),
        "2026_missing_draft_age": int(year_2026["draft_age"].isna().sum()),
        "technical_columns_present": [c for c in TECHNICAL_COLUMNS if c in df.columns],
        "overall_draft_age_coverage_pct": round(df["draft_age"].notna().mean() * 100, 2),
        "top_5_draft_age_coverage_pct": round(df.loc[groups.eq("top_5"), "draft_age"].notna().mean() * 100, 2),
        "2026_draft_age_coverage_pct": round(year_2026["draft_age"].notna().mean() * 100, 2),
        "ncaa_conf_non_missing": int(df["ncaa_conf"].notna().sum()),
        "ncaa_exp_non_missing": int(df["ncaa_exp"].notna().sum()),
        "columns_exact": df.columns.tolist() == FINAL_COLUMNS,
    }


def write_report(df: pd.DataFrame, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    checks = validate(df)
    summary = pd.DataFrame([{"metric": k, "value": v} for k, v in checks.items()])
    groups = df.apply(draft_group, axis=1)
    coverage_year = (
        df.assign(has_draft_age=df["draft_age"].notna())
        .groupby("draft_year", dropna=False)
        .agg(rows=("name", "size"), draft_age_rows=("has_draft_age", "sum"))
        .reset_index()
    )
    coverage_year["draft_age_coverage_pct"] = (coverage_year["draft_age_rows"] / coverage_year["rows"] * 100).round(2)
    coverage_group = (
        df.assign(draft_group_preview=groups, has_draft_age=df["draft_age"].notna())
        .groupby("draft_group_preview", dropna=False)
        .agg(rows=("name", "size"), draft_age_rows=("has_draft_age", "sum"))
        .reset_index()
    )
    coverage_group["draft_age_coverage_pct"] = (coverage_group["draft_age_rows"] / coverage_group["rows"] * 100).round(2)
    youngest = df[df["draft_age"].notna()].sort_values("draft_age").head(30)
    oldest = df[df["draft_age"].notna()].sort_values("draft_age", ascending=False).head(30)
    summary_2026 = df[df["draft_year"].eq(2026)][
        ["name", "overall_pick", "organization", "organization_type", "birth_date", "draft_age", "ncaa_ppg"]
    ]
    absence = pd.DataFrame({"column": TECHNICAL_COLUMNS, "absent": [c not in df.columns for c in TECHNICAL_COLUMNS]})

    lines = [
        "# Final NBA Draft Project Dataset Report",
        "",
        "## Validation Summary",
        "",
        summary.to_markdown(index=False),
        "",
        "## Final Column List",
        "",
        pd.DataFrame({"column": df.columns}).to_markdown(index=False),
        "",
        "## Organization Missingness",
        "",
        missing_summary(df, ["organization", "organization_type"]).to_markdown(index=False),
        "",
        "## Combine Missingness",
        "",
        missing_summary(df, COMBINE_COLUMNS).to_markdown(index=False),
        "",
        "## NCAA Missingness",
        "",
        missing_summary(df, NCAA_NUMERIC_COLS).to_markdown(index=False),
        "",
        "## NCAA Text Column Missingness",
        "",
        missing_summary(df, NCAA_TEXT_COLS).to_markdown(index=False),
        "",
        "## Birth Date / Draft Age Missingness",
        "",
        missing_summary(df, ["birth_date", "draft_age"]).to_markdown(index=False),
        "",
        "## Coverage By Draft Year",
        "",
        coverage_year.to_markdown(index=False),
        "",
        "## Coverage By Draft Outcome Preview",
        "",
        coverage_group.to_markdown(index=False),
        "",
        "## Youngest 30 Players",
        "",
        youngest[["name", "draft_year", "overall_pick", "organization", "birth_date", "draft_age"]].to_markdown(index=False),
        "",
        "## Oldest 30 Players",
        "",
        oldest[["name", "draft_year", "overall_pick", "organization", "birth_date", "draft_age"]].to_markdown(index=False),
        "",
        "## 2026 Summary",
        "",
        summary_2026.to_markdown(index=False),
        "",
        "## Technical Column Absence Checks",
        "",
        absence.to_markdown(index=False),
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")


def build(args: argparse.Namespace) -> pd.DataFrame:
    base = pd.read_csv(args.base)
    ncaa = pd.read_csv(args.ncaa, low_memory=False)
    out = merge_ncaa(base, ncaa)
    out = apply_sportsref_undrafted(out, Path(args.sportsref_undrafted))
    out = apply_2026_org_fixes(out)
    out = integrate_age(out, Path(args.age), Path(args.realgm_overrides))
    out = ensure_numeric(out, COMBINE_COLUMNS + NCAA_NUMERIC_COLS + ["draft_age", "overall_pick"])
    out["draft_year"] = pd.to_numeric(out["draft_year"], errors="coerce").astype("Int64")
    out = out.drop(columns=[c for c in TECHNICAL_COLUMNS if c in out.columns])
    for col in FINAL_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA
    out = out[FINAL_COLUMNS]
    if out["ncaa_conf"].notna().sum() == 0 or out["ncaa_exp"].notna().sum() == 0:
        raise ValueError("NCAA text columns were lost during final build.")
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="data/milestones/nba_draft_combine_clean_2000_2026.csv")
    parser.add_argument("--ncaa", default="data/milestones/pre_draft_ncaa_unified_2000_2026.csv")
    parser.add_argument("--age", default="data/milestones/player_birth_dates_2000_2026_v2.csv")
    parser.add_argument("--realgm-overrides", default="data/milestones/player_birth_dates_2026_realgm_overrides.csv")
    parser.add_argument("--sportsref-undrafted", default="data/milestones/pre_draft_ncaa_sportsref_undrafted_2000_2007.csv")
    parser.add_argument("--out", default="data/final/nba_draft_full_clean_project_FINAL_2000_2026.csv")
    parser.add_argument("--report", default="data/final/nba_draft_full_clean_project_FINAL_report.md")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out = build(args)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    write_report(out, Path(args.report))
    checks = validate(out)
    required = {
        "final_rows": 2347,
        "final_columns": 51,
        "duplicate_name_draft_year_pick_rows": 0,
        "2026_rows": 78,
        "2026_missing_organization": 0,
        "2026_draft_age_rows": 78,
        "2026_missing_draft_age": 0,
    }
    failures = [f"{k}: expected {v}, got {checks[k]}" for k, v in required.items() if checks[k] != v]
    if checks["technical_columns_present"]:
        failures.append(f"technical columns present: {checks['technical_columns_present']}")
    if not checks["columns_exact"]:
        failures.append("final columns do not match requested column order")
    if failures:
        raise SystemExit("Validation failed:\n" + "\n".join(failures))

    print(f"Saved final dataset: {args.out}")
    print(f"Saved final report: {args.report}")
    print(f"Rows: {checks['final_rows']}")
    print(f"Columns: {checks['final_columns']}")
    print(f"Duplicate keys: {checks['duplicate_name_draft_year_pick_rows']}")
    print(f"Overall draft_age coverage: {checks['overall_draft_age_coverage_pct']}%")
    print(f"2026 draft_age coverage: {checks['2026_draft_age_coverage_pct']}%")


if __name__ == "__main__":
    main()
