from geopy.geocoders import Nominatim
from atlas.eph import Ephemeris

class AtlasBody:
    ZODIACS = [
        (0, 30, 'Aries', '♈'),
        (30, 60, 'Taurus', '♉'),
        (60, 90, 'Gemini', '♊'),
        (90, 120, 'Cancer', '♋'),
        (120, 150, 'Leo', '♌'),
        (150, 180, 'Virgo', '♍'),
        (180, 210, 'Libra', '♎'),
        (210, 240, 'Scorpio', '♏'),
        (240, 270, 'Sagittarius', '♐'),
        (270, 300, 'Capricorn', '♑'),
        (300, 330, 'Aquarius', '♒'),
        (330, 360, 'Pisces', '♓')
    ]

    def __init__(self, name, symbol, time, observer):
        self.eph = Ephemeris()

        self.name = name
        self.symbol = symbol
        self.time = time
        self.observer = observer

        self.longitude = None
        self.zodiac = None
        self.zodiac_symbol = None
        self.zodiac_orb = None

    def to_dict(self):
        return {
            'name': self.name,
            'symbol': self.symbol,
            'longitude': self.longitude,
            'zodiac': self.zodiac,
            'zodiac_symbol': self.zodiac_symbol,
            'zodiac_orb': self.zodiac_orb
        }
    
    def get_zodiac(self):
        if not 0 <= self.longitude < 360:
            raise ValueError("Longitude must be between 0 and 360 degrees")

        for start, end, sign, symbol in self.ZODIACS:
            if start <= self.longitude < end:
                self.zodiac = sign
                self.zodiac_symbol = symbol
                self.zodiac_orb = round(self.longitude - start, 2)
     
class CelestialBody(AtlasBody):
    def __init__(self, name, symbol, time, observer):
        super().__init__(name, symbol, time, observer)
        self.distance = None
        self.latitude = None
        self.longitude_speed = None
        self.latitude_speed = None
        self.retrograde = None
        
        self.phase = None
        self.phase_symbol = None
        self.phase_angle = None
        self.elongation = None
        self.diameter = None
        self.magnitude = None

        self.PHASES = [
            (0, 22.5, f'New {self.name}', '🌑︎'),
            (22.5, 67.5, 'Waxing Crescent', '🌒︎'),
            (67.5, 112.5, 'First Quarter', '🌓︎'),
            (112.5, 157.5, 'Waxing Gibbous', '🌔︎'),
            (157.5, 202.5, f'Full {self.name}', '🌕︎'),
            (202.5, 247.5, 'Waning Gibbous', '🌖︎'),
            (247.5, 292.5, 'Last Quarter', '🌗︎'),
            (292.5, 337.5, 'Waning Crescent', '🌘︎'),
            (337.5, 360, f'New {self.name}', '🌑︎')
        ]

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'distance': self.distance,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'retrograde': self.retrograde,
            'zodiac': self.zodiac,
            'zodiac_symbol': self.zodiac_symbol,
            'zodiac_orb': self.zodiac_orb,
            'elongation': self.elongation,
            'phase': self.phase,
            'phase_symbol': self.phase_symbol,
        })
        return data
    
    def get_position(self):
        self.longitude, self.latitude, self.distance, self.longitude_speed, self.latitude_speed, self.distance_speed = self.eph.observe_celestial_pos(self.time, self.target, self.location)

    def get_phenomena(self):
        self.phase_angle, _, self.elongation, self.diameter, self.magnitude = self.eph.observe_celestial_phenomena(self.time, self.target, self.location)
        
    def get_retrograde(self):
        self.retrograde = True if self.longitude_speed <= 0 else False
    
    def get_phase(self):
        if self.phase_angle is None or not -180 <= self.phase_angle < 180:
            raise ValueError("Phase Angle must be between -180 and 180 degrees")

        for start, end, phase, symbol in self.PHASES:
            if start <= self.phase_angle < end:
                self.phase = phase
                self.phase_symbol = symbol
            else:
                self.phase = None
                self.phase_symbol = None
    
class Eclipse:
    def __init__(self, celestial):
        self.t_max = None
        self.celestial = celestial
        self.type = None
        self.magnitude = None
        self.obscuration = None
        self.gamma = None

        self.FLAGS = [
            (0x0004, 'Total Eclipse'),
            (0x0040,  'Penumbral Eclipse'),
            (0x0010,  'Partial Eclipse')
        ]

    def to_dict(self):
        return {
            't_max': self.t_max,
            'type': self.type,
            'magnitude': self.magnitude,
            'obscuration': self.obscuration
        }

    def get_type(self, retflag):
        for flag, name in self.FLAGS:
            if retflag & flag:
                self.type = name

class SolarEclipse(Eclipse):
    def __init__(self):
        super().__init__('Solar')
        self.t_c1 = None
        self.t_c2 = None
        self.t_c3 = None
        self.t_c4 = None

    def to_dict(self):
        data = super().to_dict()
        data.update({
            't_c1': self.t_c1,
            't_c2': self.t_c2,
            't_c3': self.t_c3,
            't_c4': self.t_c4,
        })
        return data
    
class LunarEclipse(Eclipse):
    def __init__(self):
        super().__init__('Lunar')
        # Phases
        self.t_p1 = None
        self.t_u1 = None
        self.t_u2 = None
        self.t_u3 = None
        self.t_u4 = None
        self.t_p2 = None

    def to_dict(self):
        data = super().to_dict()
        data.update({
            't_p1': self.t_p1,
            't_u1': self.t_u1,
            't_u2': self.t_u2,
            't_u3': self.t_u3,
            't_u4': self.t_u4,
            't_p2': self.t_p2,
        })
        return data

class Aspect():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.body_one = None
        self.body_two = None
        self.orb = None

    def to_dict(self):
        return {
            'name': self.name,
            'symbol': self.symbol,
            'body_one': self.body_one,
            'body_two': self.body_two,
            'orb': self.diff
        }

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
    
