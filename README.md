# Fantasy Football Data Science

A data science project to build a competitive edge for our 10-team, Half-PPR
fantasy football league. Built incrementally, module by module.

## Roadmap (priority order)

1. **Draft Strategy** (v1 — target: Aug 28 draft)
   - Value-Based Drafting (VBD) cheat sheet using FantasyPros PRO rankings/projections
   - Positional tiers (startable value) + sleepers/handcuffs list
2. **In-season lineup optimization** — start/sit recommendations by matchup
3. **Trade analysis** — value calculators using our VBD framework
4. **Waiver wire / FAAB strategy** — bid recommendations

v2+ will layer in a custom projection model built on nflverse historical
play-by-play data (regression/GBM), backtested against 2023-2025 outcomes,
and eventually a dashboard.

## Project structure

```
config/
  league_settings.yaml   # single source of truth: roster, scoring, payouts, etc.
data/
  raw/                   # FantasyPros manual CSV exports + nflverse pulls
  processed/             # cleaned, joined, ready-for-analysis tables
src/
  data_ingestion/
    fetch_fantasypros.py # LOADS manually-exported FantasyPros CSVs (PRO tier has no API/bulk export)
    fetch_nflverse.py    # pulls historical stats via nfl_data_py
  analysis/
    vbd.py               # replacement-level + VBD score calculation
    tiers.py             # tiering logic (gap analysis / clustering)
  cheat_sheet/
    build_cheat_sheet.py # assembles final startable + sleepers/handcuffs sheets
notebooks/                # exploratory work
output/                    # final cheat sheet CSVs/exports
```

## Setup

This project is developed on macOS (bash/zsh) — commands below assume that.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

We're on FantasyPros **PRO** (not MVP/HOF) — cheaper, and it includes everything
this project needs (Premium ECR, Custom Scoring Settings, Custom Cheat Sheets,
Trade Analyzer, Waiver Assistant). PRO does **not** include bulk CSV export or
API Access (those are HOF-only) — no credentials/env vars needed here.

Instead, `fetch_fantasypros.py` loads **manually downloaded** CSVs:
1. Log into fantasypros.com, set Custom Scoring Settings to match our
   league (Half-PPR + roster from `config/league_settings.yaml`).
2. Use the page's own "Export to CSV" button for rankings/projections/ADP.
3. Save the file into `data/raw/` using the naming convention documented
   at the top of `fetch_fantasypros.py`.
4. Re-run the loader to pull it into the pipeline.

See `fetch_fantasypros.py`'s module docstring for exact filenames and a
staleness-check TODO (warn if a downloaded file is >7 days old).

## League settings

All league rules (roster slots, scoring, payouts, playoff format, tiebreakers)
live in `config/league_settings.yaml`. Update that file, not code, when
settings change.
