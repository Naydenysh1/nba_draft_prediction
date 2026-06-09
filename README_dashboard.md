# 2026 NBA Draft Dashboard

This repository includes a lightweight static dashboard in `docs/`. It uses the
saved project outputs and does not retrain the model or rewrite the notebook.

## Build locally

Install the dashboard dependencies, then build the JSON payload:

```bash
pip install -r requirements.txt
python scripts/build_dashboard.py
```

The script writes:

```text
docs/data/dashboard.json
```

If `data/final/actual_draft_2026.csv` does not exist, the dashboard stays in
pre-draft agreement mode and compares the model prediction groups with ESPN mock
draft groups. ESPN is not treated as ground truth.

## Preview locally

Because the page fetches JSON, preview it through a tiny local static server:

```bash
python -m http.server 8000 -d docs
```

Then open:

```text
http://localhost:8000/
```

## Enable GitHub Pages

In the GitHub repository settings:

1. Open **Settings**.
2. Open **Pages**.
3. Set the source to **Deploy from a branch**.
4. Choose the main branch and the `/docs` folder.
5. Save.

GitHub Pages will serve `docs/index.html`.

## Generate a QR code

After GitHub Pages is enabled, run:

```bash
python scripts/make_qr.py "https://USERNAME.github.io/REPOSITORY_NAME/"
```

This saves:

```text
docs/assets/qr_dashboard.png
```

## Update after the real 2026 draft

Create or fetch:

```text
data/final/actual_draft_2026.csv
```

Required columns:

```text
name,overall_pick
```

Then run:

```bash
python scripts/build_dashboard.py
```

The builder maps picks to the same draft groups, merges actual results by
normalized player name, and switches the page to post-draft evaluation mode with
model-vs-actual, ESPN-vs-actual, and model-vs-ESPN metrics.

The GitHub Actions workflow `.github/workflows/update-dashboard.yml` can also be
launched manually from the Actions tab. It rebuilds `docs/data/dashboard.json`
and commits it only when the JSON changed.
