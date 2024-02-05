from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

class Location:
	def __init__(self, longitude, latitude):
		self.longitude = longitude
		self.latitude = latitude

def locator(city):
	geolocator = Nominatim(user_agent="Atlas", timeout=500)
	location = geolocator.geocode(city)
	return location

def create_location(longitude, latitude):
	location = Location(longitude, latitude)
	return location

def utc(t, location):
	tz = TimezoneFinder().timezone_at(lng=location.longitude, lat=location.latitude)
	local = pytz.timezone(tz)
	t = local.localize(t, is_dst=None)
	t_utc = t.astimezone(pytz.utc)
	t_utc = t_utc.replace(tzinfo=None)
	return t_utc


