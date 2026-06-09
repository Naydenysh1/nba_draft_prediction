# NBA Draft ML Dataset

This project builds a clean data collection layer for a classical machine
learning project about NBA Draft prospects.

The final dataset is:

```text
data/final/nba_draft_full_clean_project_FINAL_2000_2026.csv
```

The final validation report is:

```text
data/final/nba_draft_full_clean_project_FINAL_report.md
```

## Reproduce The Final Dataset

The final build does not scrape live websites. It rebuilds the final table from
saved milestone CSVs:

```bash
python scripts/build_final_dataset.py
```

## Dataset Design

The dataset covers NBA Draft years 2000-2026. Historical years 2000-2025 include
drafted players plus undrafted combine players. The 2026 rows are the prediction
pool, so `overall_pick` is intentionally missing for those rows.

Historical undrafted combine players use:

```text
overall_pick = 999
```

This keeps them distinct from drafted players while preserving them for a later
classification target.

## Milestones

Milestone files are stored in `data/milestones/`:

- `nba_draft_combine_clean_2000_2026.csv`: clean NBA Draft History and Combine base.
- `pre_draft_ncaa_torvik_2008_2026_v2.csv`: Torvik NCAA player-season stats.
- `pre_draft_ncaa_sportsref_2000_2007.csv`: early Sports-Reference NCAA stats for drafted college players.
- `pre_draft_ncaa_sportsref_undrafted_2000_2007.csv`: early Sports-Reference NCAA stats for undrafted combine players.
- `pre_draft_ncaa_unified_2000_2026.csv`: unified NCAA stats layer.
- `player_birth_dates_2000_2026_v2.csv`: validated NBA API / fallback birth-date layer.
- `player_birth_dates_2026_realgm_overrides.csv`: RealGM-audited 2026 birth-date overrides.
- `player_birth_dates_2026_realgm_unmatched.csv`: remaining unmatched 2026 birth-date audit rows.

## Modeling Notes

`draft_tier` is intentionally not created in the data collection scripts. It
should be created in the ML notebook so target definitions remain explicit and
easy to change.

Missing values are intentionally preserved. Imputation, scaling, z-scores,
percentiles, and other preprocessing belong in the modeling notebook, not in the
raw project dataset.
