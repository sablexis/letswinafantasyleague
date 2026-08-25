"""
tiers.py

Groups ranked players (by VBD score) into draft tiers — clusters of players
who are roughly interchangeable in value, with meaningful drop-offs between
tiers. This is what makes the cheat sheet actionable in real time: "there
are 3 RBs left in Tier 2, grab one now before the tier breaks."

Two approaches worth trying (start simple, compare):
    1. Gap analysis (simple, explainable): sort by vbd_score descending
       within a position, compute the point-drop between consecutive
       players, and start a new tier whenever the drop exceeds some
       threshold (e.g. a z-score of the gaps, or a fixed % of the
       position's score range).
    2. K-means clustering (from scikit-learn) on vbd_score (1D) per
       position — lets the data pick natural breakpoints, but you must
       choose k (number of tiers) per position, which is a little
       arbitrary. Try k=5-7 for RB/WR (deep positions), k=3-4 for
       QB/TE/DEF/K (shallow positions).

    Recommendation: implement gap analysis first (it's more explainable to
    league mates when you're defending a pick), then try k-means as a
    comparison/sanity-check.

TODO(intern):
    1. Implement `assign_tiers_gap_analysis(df, position_col, score_col)`.
    2. Implement `assign_tiers_kmeans(df, position_col, score_col, k_by_position)`.
    3. Add a `tier` column (int, 1 = best tier) to the DataFrame, computed
       independently per position.
    4. Pick whichever approach "looks right" when you eyeball it against
       known positional tiers from FantasyPros analysts — this is a good
       spot for a gut-check, not just a formula.
"""

from typing import Dict
import pandas as pd


def assign_tiers_gap_analysis(
    df: pd.DataFrame,
    position_col: str = "position",
    score_col: str = "vbd_score",
    gap_threshold_std: float = 1.0,
) -> pd.DataFrame:
    """
    Assigns a `tier` column per position based on gaps between consecutive
    players' scores exceeding gap_threshold_std standard deviations of the
    within-position gap distribution.
    """
    raise NotImplementedError("TODO: implement gap-analysis tiering")


def assign_tiers_kmeans(
    df: pd.DataFrame,
    k_by_position: Dict[str, int],
    position_col: str = "position",
    score_col: str = "vbd_score",
) -> pd.DataFrame:
    """
    Assigns a `tier` column per position using k-means clustering on
    score_col, with position-specific k values from k_by_position.
    """
    raise NotImplementedError("TODO: implement k-means tiering")


if __name__ == "__main__":
    pass
