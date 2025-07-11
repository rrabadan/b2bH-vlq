import re

from hepkit.variables import Var

leading_photon_vars = [
    Var(
        name="photon1_pt",
        description="Leading photon transverse momentum",
        label=r"$p_{T, \gamma_1}$",
        x_title=r"$p_{T, \gamma_1}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["lp_pt"],
    ),
    Var(
        name="photon1_phi",
        description="Leading photon azimuthal angle",
        label=r"$\phi_{\gamma_1}$",
        x_title=r"$\phi_{\gamma_1}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["lp_phi"],
    ),
    Var(
        name="photon1_y",
        description="Leading photon rapidity",
        label=r"$y_{\gamma_!}$",
        x_title=r"$y_{\gamma_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["lp_y"],
    ),
    Var(
        name="photon1_eta",
        description="Leading photon pseudorapidity",
        label=r"$\eta_{\gamma_1}$",
        x_title=r"$\eta_{\gamma_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["lp_eta"],
    ),
]

subleading_photon_vars = [
    Var(
        name="photon2_pt",
        description="Subleading photon transverse momentum",
        label=r"$p_{T, \gamma_2}$",
        x_title=r"$p_{T, \gamma_2}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["slp_pt"],
    ),
    Var(
        name="photon2_phi",
        description="Subleading photon azimuthal angle",
        label=r"$\phi_{\gamma_2}$",
        x_title=r"$\phi_{\gamma_2}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["slp_phi"],
    ),
    Var(
        name="photon2_y",
        description="Subleading photon rapidity",
        label=r"$y_{\gamma_2}$",
        x_title=r"$y_{\gamma_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["slp_y"],
    ),
    Var(
        name="photon2_eta",
        description="Subleading photon pseudorapidity",
        label=r"$\eta_{\gamma_2}$",
        x_title=r"$\eta_{\gamma_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["slp_eta"],
    ),
]

diphoton_vars = [
    Var(
        name="diphoton_pt",
        description="Diphoton transverse momentum",
        label=r"$p_{T, \gamma\gamma}$",
        x_title=r"$p_{T, \gamma\gamma}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["Dipho_Pt"],
    ),
    Var(
        name="diphoton_phi",
        description="Diphoton azimuthal angle",
        label=r"$\phi_{\gamma\gamma}$",
        x_title=r"$\phi_{\gamma\gamma}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["Dipho_Phi"],
    ),
    Var(
        name="diphoton_y",
        description="Diphoton rapidity",
        label=r"$y_{\gamma\gamma}$",
        x_title=r"$y_{\gamma\gamma}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["Dipho_y"],
    ),
    Var(
        name="diphoton_eta",
        description="Diphoton pseudorapidity",
        label=r"$\eta_{\gamma\gamma}$",
        x_title=r"$\eta_{\gamma\gamma}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["Dipho_Eta"],
    ),
]

bjet_vars = [
    Var(
        name="bjet_pt",
        description="Leading b-jet transverse momentum",
        label=r"$p_{T, b_1}$",
        binning=(50, 0, 500),
        x_title=r"$p_{T, b_1}$",
        unit="GeV/c",
        input_branches=["bjet_pt"],
    ),
    Var(
        name="bjet_phi",
        description="Leading b-jet azimuthal angle",
        label=r"$\phi_{b_1}$",
        x_title=r"$\phi_{b_1}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["bjet_phi"],
    ),
    Var(
        name="bjet_y",
        description="Leading b-jet rapidity",
        label=r"$y_{b_1}$",
        x_title=r"$y_{b_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["bjet_y"],
    ),
    Var(
        name="bjet_eta",
        description="Leading b-jet pseudorapidity",
        label=r"$\eta_{b_1}$",
        x_title=r"$\eta_{b_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["bjet_eta"],
    ),
]

subleading_bjet_vars = [
    Var(
        name="bjet2_pt",
        description="Subleading b-jet transverse momentum",
        label=r"$p_{T, b_2}$",
        x_title=r"$p_{T, b_2}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["bjet2_pt"],
    ),
    Var(
        name="bjet2_phi",
        description="Subleading b-jet azimuthal angle",
        label=r"$\phi_{b_2}$",
        x_title=r"$\phi_{b_2}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["bjet2_phi"],
    ),
    Var(
        name="bjet2_y",
        description="Subleading b-jet rapidity",
        label=r"$y_{b_2}$",
        x_title=r"$y_{b_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["bjet2_y"],
    ),
    Var(
        name="bjet2_eta",
        description="Subleading b-jet pseudorapidity",
        label=r"$\eta_{b_2}$",
        x_title=r"$\eta_{b_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["bjet2_eta"],
    ),
]

forward_jet_vars = [
    Var(
        name="forward_jet_pt",
        description="Forward jet transverse momentum",
        label=r"$p_{T, j_f}$",
        x_title=r"$p_{T, j_f}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["fjet_pt"],
    ),
    Var(
        name="forward_jet_phi",
        description="Forward jet azimuthal angle",
        label=r"$\phi_{j_f}$",
        x_title=r"$\phi_{j_f}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["fjet_phi"],
    ),
    Var(
        name="forward_jet_y",
        description="Forward jet rapidity",
        label=r"$y_{j_f}$",
        x_title=r"$y_{j_f}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["fjet_y"],
    ),
    Var(
        name="forward_jet_eta",
        description="Forward jet pseudorapidity",
        label=r"$\eta_{j_f}$",
        x_title=r"$\eta_{j_f}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["fjet_eta"],
    ),
]

event_vars = [
    Var(
        name="HT",
        description="Scalar sum of transverse momenta of all jets",
        label=r"$H_T$",
        x_title=r"$H_T$",
        binning=(50, 0, 2000),
        unit="GeV",
        input_branches=["HT"],
    ),
    Var(
        name="bjet_multiplicity",
        description="Number of b-jets in the event",
        label=r"$n_{b-jets}$",
        x_title=r"$n_{b-jets}$",
        unit="",
        binning=(10, 0, 10),
        x_discrete=True,
        input_branches=["n_bjet"],
    ),
    Var(
        name="jet_multiplicity",
        description="Number of jets in the event",
        label=r"$n_{jets}$",
        x_title=r"$n_{jets}$",
        binning=(10, 0, 10),
        unit="",
        x_discrete=True,
        input_branches=["n_jets"],
    ),
    Var(
        name="forwardjet_multiplicity",
        description="Number of forward jets in the event",
        label=r"$n_{forward-jets}$",
        x_title=r"$n_{forward-jets}$",
        binning=(10, 0, 10),
        unit="",
        x_discrete=True,
        input_branches=["n_fjet"],
    ),
]

vlq_vars = [
    Var(
        name="VLQ_pt",
        description="Vector-like quark transverse momentum",
        label=r"$p_{T, VLQ}$",
        x_title=r"$p_{T, VLQ}$",
        binning=(50, 0, 500),
        unit="GeV/c",
        input_branches=["B_pt"],
    ),
    Var(
        name="VLQ_eta",
        description="Vector-like quark pseudorapidity",
        label=r"$\eta_{VLQ}$",
        x_title=r"$\eta_{VLQ}$",
        binning=(50, -2.5, 2.5),
        unit="",
        input_branches=["B_eta"],
    ),
    Var(
        name="VLQ_phi",
        description="Vector-like quark azimuthal angle",
        label=r"$\phi_{VLQ}$",
        x_title=r"$\phi_{VLQ}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
        input_branches=["B_phi"],
    ),
]

delta_r_vars = [
    #    Var(
    #        name="deltaR_leading_photon_bjet",
    #        description="Delta R between leading photon and leading b-jet",
    #        label=r"$\Delta R(\gamma_1, b_1)$",
    #        x_title=r"$\Delta R(\gamma_1, b_1)$",
    #        binning=(50, 0, 5),
    #        unit="",
    #        input_branches=["B_eta"],
    #    ),
    #    Var(
    #        name="deltaR_subleading_photon_bjet",
    #        description="Delta R between subleading photon and leading b-jet",
    #        label=r"$\Delta R(\gamma_2, b_1)$",
    #        x_title=r"$\Delta R(\gamma_2, b_1)$",
    #        binning=(50, 0, 5),
    #        unit="",
    #    ),
    Var(
        name="deltaR_bjet_Higgs",
        description="Delta R between b-jet and Higgs candidate",
        label=r"$\Delta R(b, H)$",
        x_title=r"$\Delta R(b, H)$",
        binning=(50, 0, 5),
        unit="",
        input_branches=["dR_bdec_higgs"],
    ),
]

mass_vars = [
    Var(
        name="VLQ_mass",
        description="Vector-like quark invariant mass",
        label=r"$m_{VLQ}$",
        x_title=r"$m_{VLQ}$",
        binning=(50, 500, 1500),
        unit="GeV/c²",
        input_branches=["B_mass"],
    ),
    Var(
        name="diphoton_mass",
        description="Diphoton invariant mass",
        label=r"$m_{\gamma\gamma}$",
        x_title=r"$m_{\gamma\gamma}$",
        binning=(50, 50, 150),
        unit="GeV/c²",
        input_branches=["Dipho_Mass"],
    ),
]

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
