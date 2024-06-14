from timezonefinder import TimezoneFinder
import pytz

def utc(t, location):
    tz = TimezoneFinder().timezone_at(lat=location.latitude, lng=location.longitude)
    local = pytz.timezone(tz)
    t = local.localize(t, is_dst=None)
    t_utc = t.astimezone(pytz.utc)
    t_utc = t_utc.replace(tzinfo=None)
    return t_utc
