import re

from .observables import (
    Var,
    bjet_vars,
    delta_r_vars,
    diphoton_vars,
    event_vars,
    forward_jet_vars,
    leading_photon_vars,
    mass_vars,
    subleading_bjet_vars,
    subleading_photon_vars,
    vlq_vars,
)

ALL_VARIABLES = (
    leading_photon_vars
    + subleading_photon_vars
    + diphoton_vars
    + bjet_vars
    + subleading_bjet_vars
    + forward_jet_vars
    + event_vars
    + vlq_vars
    + delta_r_vars
    + mass_vars
)

PHYSICS_GROUPS = {
    "vlq": vlq_vars,
    "photon-1": leading_photon_vars,
    "photon-2": subleading_photon_vars,
    "diphoton": diphoton_vars,
    "b-jet-1": bjet_vars,
    "b-jet-2": subleading_bjet_vars,
    "fwd-jet": forward_jet_vars,
    "event": event_vars,
    "deltaR": delta_r_vars,
    "masses": mass_vars,
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
