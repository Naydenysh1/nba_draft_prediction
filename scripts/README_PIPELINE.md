# Data Assembly Pipeline

The current reproducible entry point is:

```bash
python scripts/build_final_dataset.py
```

It rebuilds the final project dataset from milestone CSVs and does not perform
live scraping.

## Historical Builders

`build_nba_draft_combine_clean.py` was the original source builder for NBA Draft
History and NBA Draft Combine measurements. Its output is preserved as the
milestone:

```text
data/milestones/nba_draft_combine_clean_2000_2026.csv
```

`build_ncaa_torvik_stats.R` builds the large Torvik NCAA source for draft years
2008-2026. It remains in `scripts/` because it is the main upstream NCAA source
builder.

Sports-Reference was used for early NCAA years 2000-2007 and for early
undrafted combine players whose college organization was missing from the NBA
base.

Player ages were added from the NBA API first, then patched with RealGM fallback
overrides for 2026 prediction-pool rows.

## Why Milestone-Based Rebuilds

The final reproducible script uses milestone CSVs to avoid repeatedly scraping
external websites. This keeps the project stable and fast for notebook-stage ML
work while preserving the important source layers for auditing.

The final script does not create `draft_tier`, z-score features, percentile
features, imputations, or model-ready encodings. Those belong in the modeling
notebook.
