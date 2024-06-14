from geopy.geocoders import Nominatim

class Location:
    def __init__(self, longitude=None, latitude=None, altitude=None):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

    def to_dict(self):
        return {
            'longitude': self.longitude,
            'latitude': self.latitude,
            'altitude': self.altitude
        }

    def locator(self, city):
        geolocator = Nominatim(user_agent="Atlas", timeout=500)
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError(f"Unknown location: {city}")
        self.longitude = location.longitude
        self.latitude = location.latitude
        self.altitude = location.altitude
    
    def set_location(self, longitude, latitude, altitude):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
