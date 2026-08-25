"""
vbd.py

Value-Based Drafting (VBD) calculation — the analytical core of the v1
cheat sheet.

Recap of the concept (see chat for the "candy" explanation):
    A player's raw projected points don't tell you how valuable they are
    relative to what you could get for free off waivers. VBD = a player's
    projected points MINUS the "replacement level" baseline for their
    position. That baseline is the projected points of the last starter-
    quality player at that position, given our league's actual roster math.

Replacement level rank, step by step:
    1. Every position needs (num_teams * required_starters) players just to
       fill the starting lineups league-wide.
       e.g. RB: 10 teams * 2 RB starters = 20 "guaranteed" RB starters.
    2. FLEX slots (RB/WR/TE eligible) add extra demand on top of that, but
       we don't know in advance which position each team will slot there.
       We approximate by splitting the flex slots across eligible positions
       using a weight (see FLEX_ALLOCATION_WEIGHTS below — tune this once
       you see how draft boards actually shake out; it's a modeling
       assumption, not a fixed truth).
    3. Replacement rank for position P = starters_from_step_1[P] +
       (flex_slots * num_teams * FLEX_ALLOCATION_WEIGHTS[P])
    4. Replacement level = the projected points of the player ranked
       exactly at that rank within position P (sort position P by
       projected points, descending, pick that row).
    5. VBD score for every player at position P = player's projected
       points - replacement level for P.

TODO(intern):
    1. Load config/league_settings.yaml (use pyyaml) to get num_teams,
       roster starters, and flex_eligible_positions — don't hardcode them
       here, so this stays in sync if league settings change.
    2. Implement `compute_replacement_ranks(league_config)` using the math
       above.
    3. Implement `compute_replacement_levels(projections_by_position,
       replacement_ranks)` — look up the projected points at each
       replacement rank.
    4. Implement `compute_vbd(projections_by_position, replacement_levels)`
       — add a `vbd_score` column to each position's DataFrame.
    5. Write a couple of unit tests / sanity prints: does RB replacement
       rank land somewhere reasonable (~20-30)? Does QB (~10-12)?
"""

from typing import Dict
import pandas as pd
import yaml

# Starting point weights for flex allocation — adjust based on how draft
# boards/ADP actually treat flex (TEs rarely get flexed in shallow leagues,
# RBs/WRs split most of it).
FLEX_ALLOCATION_WEIGHTS = {
    "RB": 0.45,
    "WR": 0.45,
    "TE": 0.10,
}


def load_league_config(path: str = "config/league_settings.yaml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def compute_replacement_ranks(league_config: dict) -> Dict[str, int]:
    """
    Returns a dict like {"QB": 10, "RB": 25, "WR": 25, "TE": 12, ...}
    representing the draft rank at which a position's players become
    "replacement level" (freely available) in our league.
    """
    raise NotImplementedError("TODO: implement replacement rank math (see docstring above)")


def compute_replacement_levels(
    projections_by_position: Dict[str, pd.DataFrame],
    replacement_ranks: Dict[str, int],
    points_col: str = "projected_points",
) -> Dict[str, float]:
    """
    For each position, find the projected points value at the replacement
    rank (after sorting descending by points_col).
    """
    raise NotImplementedError("TODO: implement replacement level lookup")


def compute_vbd(
    projections_by_position: Dict[str, pd.DataFrame],
    replacement_levels: Dict[str, float],
    points_col: str = "projected_points",
) -> pd.DataFrame:
    """
    Adds a `vbd_score` column to each position's DataFrame, then
    concatenates everything into one big board sorted by vbd_score desc.
    """
    raise NotImplementedError("TODO: implement VBD score calculation + combine into one board")


if __name__ == "__main__":
    # TODO: once implemented, wire up an end-to-end sanity check:
    # load config -> compute ranks -> print them out.
    pass
