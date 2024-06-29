class Node:
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
        (330, 360, 'Pisces', '♓'),
    ]

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
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
            'zodiac_orb': self.zodiac_orb,
        }
    
    def get_zodiac(self, ayanamsa=None):
        if not 0 <= self.longitude < 360:
            raise ValueError("Longitude must be between 0 and 360 degrees")
        
        if ayanamsa:
            self.longitude = (self.longitude - ayanamsa) % 360
        else:
            self.longitude = self.longitude

        for start, end, sign, symbol in self.ZODIACS:
            if start <= self.longitude < end:
                self.zodiac = sign
                self.zodiac_symbol = symbol
                self.zodiac_orb = round(self.longitude - start, 2)

class Celestial(Node):
        def __init__(self, name, symbol):
            super().__init__(name, symbol)
            self.ra = None
            self.dec = None
            self.distance = None
            self.latitude = None
            self.longitude_speed = None
            self.latitude_speed = None
            self.retrograde = None

            self.phase = None
            self.phase_symbol = None
            self.phase_angle = None

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
                'ra': self.ra,
                'dec': self.dec,
                'distance': self.distance,
                'latitude': self.latitude,
                'longitude_speed': self.longitude_speed,
                'latitude_speed': self.latitude_speed,
                'retrograde': self.retrograde,
                'phase': self.phase,
                'phase_symbol': self.phase_symbol,
                'phase_angle': self.phase_angle,
            })
            return data
        
        def get_retrograde(self):
            self.retrograde = True if self.longitude_speed <= 0 else False

        def get_phase(self, sun_longitude):
            self.phase_angle = round((self.longitude - sun_longitude) % 360, 2)

            for start, end, phase, symbol in self.PHASES:
                if start <= self.phase_angle < end:
                    self.phase = phase
                    self.phase_symbol = symbol
                    break

class Aspect():
    def __init__(self, name, symbol, body_one, body_two, orb):
        self.name = name
        self.symbol = symbol
        self.body_one = body_one
        self.body_two = body_two
        self.orb = orb

    def to_dict(self):
        return {
            'name': self.name,
            'symbol': self.symbol,
            'body_one': self.body_one.to_dict(),
            'body_two': self.body_two.to_dict(),
            'orb': self.orb
        }
    
    
