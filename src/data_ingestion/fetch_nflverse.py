"""
fetch_nflverse.py

Pulls historical NFL stats via nfl_data_py (Python port of the R nflverse
ecosystem). This is v1's secondary/validation data source, and becomes the
primary input for the v2 custom projection model.

Why this file exists:
    We want real historical performance (weekly stats, snap counts, target
    share, red zone usage) to sanity-check FantasyPros projections in v1,
    and to eventually train our own model in v2.

TODO(intern):
    1. Implement `fetch_weekly_stats(seasons)` — pull weekly player stats
       for the given seasons using nfl_data_py.import_weekly_data().
    2. Implement `fetch_seasonal_stats(seasons)` — pull season-total stats
       using nfl_data_py.import_seasonal_data().
    3. Consider also pulling `import_ids()` (player ID crosswalk) — you'll
       need this to join nflverse data against FantasyPros names cleanly
       (name matching across sources is annoying; an ID crosswalk helps).
    4. Save raw pulls to data/raw/nflverse_<type>_<seasons>.csv

Suggested seasons for v1 baseline: last 3 completed seasons (2023-2025).
"""

import os
import pandas as pd

RAW_DATA_DIR = "data/raw"

DEFAULT_SEASONS = [2023, 2024, 2025]


def fetch_weekly_stats(seasons: list[int] = DEFAULT_SEASONS) -> pd.DataFrame:
    """
    Fetch weekly player-level stats for the given seasons.

    Returns:
        DataFrame with per-player, per-week stat lines (passing, rushing,
        receiving, fumbles, etc.) — column set comes from nfl_data_py.
    """
    raise NotImplementedError("TODO: implement via nfl_data_py.import_weekly_data")


def fetch_seasonal_stats(seasons: list[int] = DEFAULT_SEASONS) -> pd.DataFrame:
    """Fetch season-total player-level stats for the given seasons."""
    raise NotImplementedError("TODO: implement via nfl_data_py.import_seasonal_data")


def fetch_player_id_crosswalk() -> pd.DataFrame:
    """
    Fetch the player ID crosswalk (nflverse IDs <-> other sources) to make
    joining nflverse data against FantasyPros names more reliable.
    """
    raise NotImplementedError("TODO: implement via nfl_data_py.import_ids")


def save_raw(df: pd.DataFrame, filename: str) -> None:
    """Persist a raw pull to data/raw/ untouched."""
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    df.to_csv(os.path.join(RAW_DATA_DIR, filename), index=False)


if __name__ == "__main__":
    # TODO: wire up a simple CLI run once fetch functions are implemented.
    pass
