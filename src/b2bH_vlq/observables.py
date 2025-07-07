from anaheptools.variables import Var

leading_photon_vars = [
    Var(
        name="leading_photon_pt",
        description="Leading photon transverse momentum",
        label=r"$p_{T, \gamma_1}$",
        x_title=r"$p_{T, \gamma_1}$",
        binning=(50, 0, 500),
        unit="GeV/c",
    ),
    Var(
        name="leading_photon_phi",
        description="Leading photon azimuthal angle",
        label=r"$\phi_{\gamma_1}$",
        x_title=r"$\phi_{\gamma_1}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="leading_photon_y",
        description="Leading photon rapidity",
        label=r"$y_{\gamma_!}$",
        x_title=r"$y_{\gamma_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="leading_photon_eta",
        description="Leading photon pseudorapidity",
        label=r"$\eta_{\gamma_1}$",
        x_title=r"$\eta_{\gamma_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
]

subleading_photon_vars = [
    Var(
        name="subleading_photon_pt",
        description="Subleading photon transverse momentum",
        label=r"$p_{T, \gamma_2}$",
        x_title=r"$p_{T, \gamma_2}$",
        binning=(50, 0, 500),
        unit="GeV/c",
    ),
    Var(
        name="subleading_photon_phi",
        description="Subleading photon azimuthal angle",
        label=r"$\phi_{\gamma_2}$",
        x_title=r"$\phi_{\gamma_2}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="subleading_photon_y",
        description="Subleading photon rapidity",
        label=r"$y_{\gamma_2}$",
        x_title=r"$y_{\gamma_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="subleading_photon_eta",
        description="Subleading photon pseudorapidity",
        label=r"$\eta_{\gamma_2}$",
        x_title=r"$\eta_{\gamma_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
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
    ),
    Var(
        name="diphoton_phi",
        description="Diphoton azimuthal angle",
        label=r"$\phi_{\gamma\gamma}$",
        x_title=r"$\phi_{\gamma\gamma}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="diphoton_y",
        description="Diphoton rapidity",
        label=r"$y_{\gamma\gamma}$",
        x_title=r"$y_{\gamma\gamma}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="diphoton_eta",
        description="Diphoton pseudorapidity",
        label=r"$\eta_{\gamma\gamma}$",
        x_title=r"$\eta_{\gamma\gamma}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="diphoton_mass",
        description="Diphoton invariant mass",
        label=r"$m_{\gamma\gamma}$",
        x_title=r"$m_{\gamma\gamma}$",
        binning=(50, 50, 150),
        unit="GeV/c²",
    ),
]

leading_bjet_vars = [
    Var(
        name="leading_bjet_pt",
        description="Leading b-jet transverse momentum",
        label=r"$p_{T, b_1}$",
        binning=(50, 0, 500),
        x_title=r"$p_{T, b_1}$",
        unit="GeV/c",
    ),
    Var(
        name="leading_bjet_phi",
        description="Leading b-jet azimuthal angle",
        label=r"$\phi_{b_1}$",
        x_title=r"$\phi_{b_1}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="leading_bjet_y",
        description="Leading b-jet rapidity",
        label=r"$y_{b_1}$",
        x_title=r"$y_{b_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="leading_bjet_eta",
        description="Leading b-jet pseudorapidity",
        label=r"$\eta_{b_1}$",
        x_title=r"$\eta_{b_1}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
]

subleading_bjet_vars = [
    Var(
        name="subleading_bjet_pt",
        description="Subleading b-jet transverse momentum",
        label=r"$p_{T, b_2}$",
        x_title=r"$p_{T, b_2}$",
        binning=(50, 0, 500),
        unit="GeV/c",
    ),
    Var(
        name="subleading_bjet_phi",
        description="Subleading b-jet azimuthal angle",
        label=r"$\phi_{b_2}$",
        x_title=r"$\phi_{b_2}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="subleading_bjet_y",
        description="Subleading b-jet rapidity",
        label=r"$y_{b_2}$",
        x_title=r"$y_{b_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="subleading_bjet_eta",
        description="Subleading b-jet pseudorapidity",
        label=r"$\eta_{b_2}$",
        x_title=r"$\eta_{b_2}$",
        binning=(50, -2.5, 2.5),
        unit="",
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
    ),
    Var(
        name="forward_jet_phi",
        description="Forward jet azimuthal angle",
        label=r"$\phi_{j_f}$",
        x_title=r"$\phi_{j_f}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
    Var(
        name="forward_jet_y",
        description="Forward jet rapidity",
        label=r"$y_{j_f}$",
        x_title=r"$y_{j_f}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="forward_jet_eta",
        description="Forward jet pseudorapidity",
        label=r"$\eta_{j_f}$",
        x_title=r"$\eta_{j_f}$",
        binning=(50, -2.5, 2.5),
        unit="",
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
    ),
    Var(
        name="bjet_multiplicity",
        description="Number of b-jets in the event",
        label=r"$n_{b-jets}$",
        x_title=r"$n_{b-jets}$",
        unit="",
        binning=(10, 0, 10),
        x_discrete=True,
    ),
    Var(
        name="jet_multiplicity",
        description="Number of jets in the event",
        label=r"$n_{jets}$",
        x_title=r"$n_{jets}$",
        binning=(10, 0, 10),
        unit="",
        x_discrete=True,
    ),
    Var(
        name="forwardjet_multiplicity",
        description="Number of forward jets in the event",
        label=r"$n_{forward-jets}$",
        x_title=r"$n_{forward-jets}$",
        binning=(10, 0, 10),
        unit="",
        x_discrete=True,
    ),
]

vlq_vars = [
    Var(
        name="VLQ_mass",
        description="Vector-like quark invariant mass",
        label=r"$m_{VLQ}$",
        x_title=r"$m_{VLQ}$",
        binning=(50, 500, 1500),
        unit="GeV/c²",
    ),
    Var(
        name="VLQ_pt",
        description="Vector-like quark transverse momentum",
        label=r"$p_{T, VLQ}$",
        x_title=r"$p_{T, VLQ}$",
        binning=(50, 0, 500),
        unit="GeV/c",
    ),
    Var(
        name="VLQ_y",
        description="Vector-like quark rapidity",
        label=r"$y_{VLQ}$",
        x_title=r"$y_{VLQ}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="VLQ_eta",
        description="Vector-like quark pseudorapidity",
        label=r"$\eta_{VLQ}$",
        x_title=r"$\eta_{VLQ}$",
        binning=(50, -2.5, 2.5),
        unit="",
    ),
    Var(
        name="VLQ_phi",
        description="Vector-like quark azimuthal angle",
        label=r"$\phi_{VLQ}$",
        x_title=r"$\phi_{VLQ}$",
        binning=(32, -3.2, 3.2),
        unit="rad",
    ),
]

ALL_VARIABLES = (
    leading_photon_vars
    + subleading_photon_vars
    + diphoton_vars
    + leading_bjet_vars
    + subleading_bjet_vars
    + forward_jet_vars
    + event_vars
    + vlq_vars
)

PHYSICS_GROUPS = {
    "vlq": vlq_vars,
    "photons": leading_photon_vars + subleading_photon_vars,
    "diphoton": diphoton_vars,
    "b-jets": leading_bjet_vars + subleading_bjet_vars,
    "jets": forward_jet_vars,
    "event": event_vars,
}

def get_variable_group_names() -> list[str]:
    """
    Get the names of all variable groups.

    Returns:
        list[str]: List of group names.
    """
    return list(PHYSICS_GROUPS.keys())

def get_variables_by_group(group_name: str) -> dict:
    """
    Get variables by group name.

    Args:
        group_name (str): Name of the group.

    Returns:
        dict[str, Var]: Dictionary of variable names to Var objects in the specified group.
    """
    return {v.name: v for v in PHYSICS_GROUPS.get(group_name, [])}