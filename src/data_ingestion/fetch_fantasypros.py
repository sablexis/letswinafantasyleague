"""
fetch_fantasypros.py

Loads ADP and positional rankings/projections that were manually exported
from FantasyPros (PRO tier).

Why this file exists / why it's a MANUAL workflow (updated 2026-08-24):
    We're on the FantasyPros PRO subscription tier ($5.99/mo x 6-month plan),
    not MVP or HOF. PRO gives us everything we actually need for VBD (Premium
    ECR, Custom Scoring Settings matched to our league, Custom Cheat Sheets,
    Trade Analyzer, Waiver Assistant) but does NOT include automated access:
    bulk CSV export / API Access is HOF-only ($11.99/mo). Paying 2x more just
    to automate a ~30-second weekly download isn't worth it for this project.

    So instead of scraping/API-pulling FantasyPros programmatically (which
    would also violate their ToS without API Access), the workflow is:
        1. Log into fantasypros.com (PRO account).
        2. Go to the rankings/cheat sheet page for the position/list you
           need, with OUR league's Half-PPR + custom roster scoring applied
           (FantasyPros supports Custom Scoring Settings on PRO — use it so
           the numbers already match our league, not generic half-PPR).
        3. Use the on-page "Export to CSV" / download button (available in
           the UI itself, separate from the paid bulk API) and save the file
           into data/raw/ using the naming convention below.
        4. Re-run this script (or call load_*() functions from a notebook)
           to load + lightly validate those manually-downloaded files.

    This file's job is now LOADING and validating manually-downloaded CSVs,
    not fetching them over HTTP. Keep the original function names
    (fetch_adp / fetch_projections) so downstream code (vbd.py, cheat_sheet)
    doesn't need to change — only the docstrings/implementation approach
    changed.

Expected manual download file naming (place these in data/raw/):
    fantasypros_adp_overall.csv                 (ADP fetch_adp())
    fantasypros_projections_qb.csv              (fetch_projections("QB"))
    fantasypros_projections_rb.csv              (fetch_projections("RB"))
    fantasypros_projections_wr.csv              (fetch_projections("WR"))
    fantasypros_projections_te.csv              (fetch_projections("TE"))
    fantasypros_projections_dst.csv             (fetch_projections("DST"))
    fantasypros_projections_k.csv               (fetch_projections("K"))

TODO(intern):
    1. Implement `fetch_adp()` — load data/raw/fantasypros_adp_overall.csv
       (manually downloaded per the workflow above), validate it has at
       least player_name, position, team, adp columns, and return it as a
       DataFrame. Raise a clear error telling the user which file to
       download + where to put it if the file is missing (this file won't
       auto-fetch it for you anymore).
    2. Implement `fetch_projections(position)` — same pattern, loading
       data/raw/fantasypros_projections_<position>.csv.
    3. Add a lightweight "freshness check" — e.g. print a warning if the
       file's modified date is more than ~7 days old, so stale rankings
       don't silently sneak into a waiver/trade decision mid-season.
    4. `save_raw()` stays as a passthrough helper (e.g. for saving a
       re-validated/cleaned copy) but is no longer the primary write path —
       the primary "write" is you manually saving the browser download into
       data/raw/.
    5. No credentials/API keys needed anymore — remove any assumption of
       FANTASYPROS_API_KEY env vars from downstream code/docs.

Suggested libraries: pandas (for CSV parsing + validation), pathlib/os
(file existence + mtime checks). `requests` is no longer needed here.
"""

import os
from pathlib import Path
import pandas as pd

FANTASYPROS_POSITIONS = ["QB", "RB", "WR", "TE", "DST", "K"]

RAW_DATA_DIR = "data/raw"

# How old a manually-downloaded file can be before we warn the user to
# re-export a fresh copy from FantasyPros.
STALE_FILE_WARNING_DAYS = 7


def fetch_adp(scoring_format: str = "half-ppr") -> pd.DataFrame:
    """
    Load manually-downloaded ADP data from data/raw/fantasypros_adp_overall.csv.

    This does NOT hit the network. Export the CSV from fantasypros.com
    yourself (PRO tier, Custom Scoring Settings set to our league's
    Half-PPR + roster) and save it to the path above first.

    Returns:
        DataFrame with at minimum: player_name, position, team, adp
    """

    Overalldf = pd.read_csv('fantasypros_adp_overall.csv')
    QBdf = pd.read_csv('fantasypros_projections_qb.csv')
    RBdf = pd.read_csv('fantasypros_projections_rb.csv')
    WRdf = pd.read_csv('fantasypros_projections_wr.csv')
    TEdf = pd.read_csv('fantasypros_projections_te.csv')
    DSTdf = pd.read_csv('fantasypros_projections_dst.csv')
    Kdf = pd.read_csv('fantasypros_projections_k.csv')

    raise NotImplementedError(
        "TODO: implement manual-CSV load for ADP. See module docstring for "
        "the expected file path and validation steps."
    )


def fetch_projections(position: str) -> pd.DataFrame:
    """
    Load manually-downloaded season projections for a single position from
    data/raw/fantasypros_projections_<position>.csv.

    Args:
        position: one of FANTASYPROS_POSITIONS

    Returns:
        DataFrame with at minimum: player_name, team, position,
        and the relevant projected stat columns (varies by position).
    """

    

    if position not in FANTASYPROS_POSITIONS:
        raise ValueError(f"Unknown position: {position}")
    raise NotImplementedError(
        "TODO: implement manual-CSV load for projections. See module "
        "docstring for the expected file path and validation steps."
    )


def check_file_freshness(filepath: str, warn_after_days: int = STALE_FILE_WARNING_DAYS) -> None:
    """
    Print a warning if the given manually-downloaded file is older than
    warn_after_days. Call this at the top of fetch_adp()/fetch_projections()
    once a file is found, before returning it.
    """
    raise NotImplementedError("TODO: implement mtime-based staleness check")


def save_raw(df: pd.DataFrame, filename: str) -> None:
    """
    Persist a (re-validated/cleaned) copy to data/raw/. Not the primary
    write path anymore — the primary write is your manual browser download
    from fantasypros.com landing directly in data/raw/.
    """
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    df.to_csv(os.path.join(RAW_DATA_DIR, filename), index=False)


if __name__ == "__main__":
    # TODO: wire up a simple CLI run once load functions are implemented,
    # e.g. load ADP + projections for all positions from data/raw/ and
    # print a summary (row counts, freshness) as a sanity check.
    pass
