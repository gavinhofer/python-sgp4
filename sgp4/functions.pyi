def jday(
    year: int, mon: int, day: int, hr: int, minute: int, sec: float
) -> tuple[float, float]: ...
def days2mdhms(
    year: int, days: float, round_to_microsecond: int = 6
) -> tuple[int, int, int, int, float]: ...
def _day_of_year_to_month_day(
    day_of_year: int, is_leap: bool
) -> tuple[int, int]: ...
