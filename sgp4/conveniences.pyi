"""Various conveniences.

Higher-level libraries like Skyfield that use this one usually have
their own date and time handling.  But for folks using this library by
itself, native Python datetime handling could be convenient.

"""
import datetime as dt
from typing import Optional, Union

from sgp4.api import Satrec
from sgp4.model import Satellite

class _UTC(dt.tzinfo):
    def __repr__(self) -> str: ...
    def dst(self, datetime: Optional[dt.datetime]) -> dt.timedelta: ...
    def tzname(self, datetim: Optional[dt.datetime]) -> str: ...
    def utcoffset(self, datetime: Optional[dt.datetime]) -> dt.timedelta: ...

def jday_datetime(datetime: dt.datetime) -> tuple[float, float]: ...
def sat_epoch_datetime(sat: Union[Satellite, Satrec]) -> dt.datetime: ...
def dump_satrec(
    sat: Union[Satellite, Satrec],
    sat2: Optional[Union[Satellite, Satrec]] = ...,
): ...
