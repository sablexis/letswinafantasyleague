"""
fetch_fantasypros.py

Pulls ADP and positional rankings/projections from FantasyPros (MVP tier).

Why this file exists:
    FantasyPros MVP gives us consensus rankings + projections that already
    bake in beat-reporter/injury/depth-chart intel we can't easily model
    ourselves. This is our "market-based value" input for VBD.

TODO(intern):
    1. Store FantasyPros credentials/API key as environment variables
       (e.g. FANTASYPROS_API_KEY) — never hardcode secrets in source.
    2. Implement `fetch_adp()` — pull half-PPR ADP data for all draftable
       positions (QB, RB, WR, TE, DEF/DST, K).
    3. Implement `fetch_projections(position)` — pull season projections
       per position. FantasyPros exposes CSV export endpoints for MVP
       subscribers; confirm the exact URL pattern once logged in.
    4. Save raw pulls to data/raw/fantasypros_{adp,projections}_<position>.csv
       untouched (no cleaning here — that belongs in analysis/).
    5. Add basic retry/backoff — don't hammer their servers.

Suggested libraries: requests, pandas (for CSV parsing), os (for env vars).
"""

import os
import pandas as pd

FANTASYPROS_POSITIONS = ["QB", "RB", "WR", "TE", "DST", "K"]

RAW_DATA_DIR = "data/raw"


def fetch_adp(scoring_format: str = "half-ppr") -> pd.DataFrame:
    """
    Fetch Average Draft Position (ADP) data for the given scoring format.

    Returns:
        DataFrame with at minimum: player_name, position, team, adp
    """
    raise NotImplementedError("TODO: implement FantasyPros ADP fetch")


def fetch_projections(position: str) -> pd.DataFrame:
    """
    Fetch season-long projections for a single position.

    Args:
        position: one of FANTASYPROS_POSITIONS

    Returns:
        DataFrame with at minimum: player_name, team, position,
        and the relevant projected stat columns (varies by position).
    """
    if position not in FANTASYPROS_POSITIONS:
        raise ValueError(f"Unknown position: {position}")
    raise NotImplementedError("TODO: implement FantasyPros projections fetch")


def save_raw(df: pd.DataFrame, filename: str) -> None:
    """Persist a raw pull to data/raw/ untouched."""
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    df.to_csv(os.path.join(RAW_DATA_DIR, filename), index=False)


if __name__ == "__main__":
    # TODO: wire up a simple CLI run once fetch functions are implemented,
    # e.g. pull ADP + projections for all positions and save to data/raw/.
    pass
