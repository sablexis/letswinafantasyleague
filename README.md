# Fantasy Football Data Science

A data science project to build a competitive edge for our 10-team, Half-PPR
fantasy football league. Built incrementally, module by module.

## Roadmap (priority order)

1. **Draft Strategy** (v1 — target: Aug 28 draft)
   - Value-Based Drafting (VBD) cheat sheet using FantasyPros MVP rankings/projections
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
  raw/                   # untouched pulls from FantasyPros / nflverse
  processed/             # cleaned, joined, ready-for-analysis tables
src/
  data_ingestion/
    fetch_fantasypros.py # pulls ADP + projections/rankings
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

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

FantasyPros MVP tier requires an authenticated session/API — set credentials
via environment variables (see `fetch_fantasypros.py` TODO) rather than
hardcoding them in source:

```bash
export FANTASYPROS_API_KEY="..."   # add to ~/.zshrc to persist
```

## League settings

All league rules (roster slots, scoring, payouts, playoff format, tiebreakers)
live in `config/league_settings.yaml`. Update that file, not code, when
settings change.
