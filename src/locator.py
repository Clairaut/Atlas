from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def locator(city):
	geolocator = Nominatim(user_agent="AtlasWizard", timeout=500)
	location = geolocator.geocode(city)
	return location

def utc(t, location):
	tz = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
	local = pytz.timezone(tz)
	t = local.localize(t, is_dst=None)
	t_utc = t.astimezone(pytz.utc)
	t_utc = t_utc.replace(tzinfo=None)
	return t_utc


