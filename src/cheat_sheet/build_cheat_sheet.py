"""
build_cheat_sheet.py

Assembles the final draft-day cheat sheet from the outputs of
data_ingestion + analysis:
    1. Startable-value board: top ~15-20 per position, ranked by VBD score,
       grouped into tiers. This is your primary pick guide.
    2. Sleepers/handcuffs board: later-round / bench-building targets —
       players outside the top-N startable range worth stashing (e.g.
       handcuff RBs behind our other draftees, breakout candidates with
       favorable ADP gaps between market rank and VBD rank).

TODO(intern):
    1. Pull it all together:
        - fetch_fantasypros.fetch_adp() / fetch_projections() (or read
          from data/raw/ if already saved)
        - vbd.compute_replacement_ranks/levels/vbd (per position)
        - tiers.assign_tiers_gap_analysis (or kmeans)
    2. Build `build_startable_board(vbd_df, top_n_per_position=20)` —
       filter + sort + format for readability (rank, tier, name, pos,
       team, vbd_score, adp, "value" = adp_rank - vbd_rank as a bonus
       column showing reaches vs. steals).
    3. Build `build_sleepers_board(vbd_df, adp_df, top_n_per_position=20)`
       — candidates who rank BETTER in our VBD board than their ADP
       suggests (i.e. vbd_rank meaningfully better than adp_rank), outside
       the startable cutoff. Also consider flagging known handcuff
       relationships (RB2 behind a workhorse RB1) — this may need a manual
       mapping since it's not purely stat-driven.
    4. Export both boards to output/ as CSV (and maybe a simple formatted
       Excel/markdown version for draft-day readability).
"""

import pandas as pd

OUTPUT_DIR = "output"


def build_startable_board(vbd_df: pd.DataFrame, top_n_per_position: int = 20) -> pd.DataFrame:
    """Top N per position by vbd_score, with tier + value-vs-ADP columns."""
    raise NotImplementedError("TODO: implement startable board assembly")


def build_sleepers_board(
    vbd_df: pd.DataFrame,
    adp_df: pd.DataFrame,
    top_n_per_position: int = 20,
) -> pd.DataFrame:
    """Later-round value/handcuff targets outside the startable cutoff."""
    raise NotImplementedError("TODO: implement sleepers/handcuffs board assembly")


def export_cheat_sheet(startable_df: pd.DataFrame, sleepers_df: pd.DataFrame) -> None:
    """Write both boards to output/ as CSV."""
    raise NotImplementedError("TODO: implement export")


if __name__ == "__main__":
    # TODO: wire up the full pipeline end-to-end once the pieces above
    # are implemented:
    #   ingest -> vbd -> tiers -> startable/sleepers boards -> export
    pass
