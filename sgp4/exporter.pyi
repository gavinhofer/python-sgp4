from sgp4.api import Satrec
from sgp4.types import OMMDict

def export_tle(satrec: Satrec) -> tuple[str, str]:
    """Generate the TLE for a given `Satrec` object; returns two strings."""
    ...

def export_omm(satrec: Satrec, object_name: str) -> OMMDict:
    """Export a `Satrec` object to an Orbit Mean-Elements Message (OMM) dictionary."""
    ...

def _abbreviate_rate(value: float, zero_exponent_string: str) -> str: ...
