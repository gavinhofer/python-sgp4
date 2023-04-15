"""Read the TLE earth satellite file format.

This is a minimally-edited copy of "sgp4io.cpp".

"""
import re
from typing import Optional, Tuple, Union, overload

import sgp4.model
import sgp4.wrapper
from sgp4.earth_gravity import EarthGravity

_SatTypes = Union[sgp4.model.Satellite, sgp4.model.Satrec, sgp4.wrapper.Satrec]

INT_RE: re.Pattern
FLOAT_RE: re.Pattern

LINE1: str
LINE2: str

error_message: str

@overload
def twoline2rv(
    longstr1: str,
    longstr2: str,
    whichconst: Union[
        EarthGravity,
        Tuple[float, float, float, float, float, float, float, float],
    ],
    opsmode: str,
    satrec: None,
) -> sgp4.model.Satellite: ...
@overload
def twoline2rv(
    longstr1: str,
    longstr2: str,
    whichconst: Union[
        EarthGravity,
        Tuple[float, float, float, float, float, float, float, float],
    ],
    opsmode: str,
    satrec: sgp4.model.Satellite,
) -> sgp4.model.Satellite: ...
@overload
def twoline2rv(
    longstr1: str,
    longstr2: str,
    whichconst: Union[
        EarthGravity,
        Tuple[float, float, float, float, float, float, float, float],
    ],
    opsmode: str,
    satrec: sgp4.model.Satrec,
) -> sgp4.model.Satrec: ...
@overload
def twoline2rv(
    longstr1: str,
    longstr2: str,
    whichconst: Union[
        EarthGravity,
        Tuple[float, float, float, float, float, float, float, float],
    ],
    opsmode: str,
    satrec: sgp4.wrapper.Satrec,
) -> sgp4.wrapper.Satrec: ...
def twoline2rv(
    longstr1: str,
    longstr2: str,
    whichconst: Union[
        EarthGravity,
        Tuple[float, float, float, float, float, float, float, float],
    ],
    opsmode: str,
    satrec: Optional[_SatTypes],
) -> _SatTypes: ...
def verify_checksum(*lines: str) -> None: ...
def fix_checksum(line: str) -> str: ...
def compute_checksum(line: str) -> int: ...
