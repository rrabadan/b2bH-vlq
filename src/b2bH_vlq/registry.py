import re

from .observables import (
    Var,
    deltaR,
    diphoton,
    event_vars,
    forward_jet,
    leading_bjet,
    leading_photon,
    masses,
    subleading_bjet,
    subleading_photon,
    vlq,
)

ALL_VARIABLES = (
    leading_photon
    + subleading_photon
    + diphoton
    + leading_bjet
    + subleading_bjet
    + forward_jet
    + event_vars
    + vlq
    + deltaR
    + masses
)

PHYSICS_GROUPS = {
    "vlq": vlq,
    "photon1": leading_photon,
    "photon2": subleading_photon,
    "diphoton": diphoton,
    "bjet1": leading_bjet,
    "bjet2": subleading_bjet,
    "fwdjet": forward_jet,
    "event": event_vars,
    "deltaR": deltaR,
    "masses": masses,
}


def get_variable_group_names() -> list[str]:
    """
    Get the names of all variable groups.

    Returns:
        list[str]: List of group names.
    """
    return list(PHYSICS_GROUPS.keys())


def get_variables_by_group(group_name: str, exclude_pattern: str | None = None) -> dict:
    """
    Get variables by group name.

    Args:
        group_name (str): Name of the group.
        exclude_pattern (str, optional): Regex pattern to exclude variables by name.

    Returns:
        dict[str, Var]: Dictionary of variable names to Var objects in the specified group.
    """

    variables = PHYSICS_GROUPS.get(group_name, [])

    if exclude_pattern:
        pattern = re.compile(exclude_pattern)
        variables = [v for v in variables if not pattern.search(v.name)]

    return {v.name: v for v in variables}


def set_kinematic_branches(variables: list[Var], candidate: str, mapping: dict[str, str]) -> None:
    vardic = {var.name: var for var in variables}
    for prop, branch in mapping.items():
        varname = f"{candidate}_{prop}"
        if varname in vardic:
            vardic[varname].input_branches = [branch] if isinstance(branch, str) else list(branch)
