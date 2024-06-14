from datetime import datetime

from atlas.eph import Ephemeris
from atlas.node import Node, Celestial
from atlas.eclipse import SolarEclipse, LunarEclipse

class Atlas:
    def __init__(self):
        self.eph = Ephemeris()
        self.celestial_symbols = {
        'sun': ['Sun', '☉'], 'moon': ['Moon', '☽'], 'mercury': ['Mercury', '☿'], # Main Celestials
        'venus': ['Venus', '♀'], 'mars': ['Mars', '♂'], 'jupiter': ['Jupiter', '♃'], 
        'saturn': ['Saturn', '♄'], 'uranus': ['Uranus', '♅'], 'neptune': ['Neptune', '♆'], 
        'pluto': ['Pluto', '⯓'],

        'lilith': ['Lilith', '⚸'], 'selena': ['Selena', '⯝'], 'rahu': ['Lunar ASC', '☊'], # Lunar
        
        'ceres': ['Ceres', '⚳'], 'pallas': ['Pallas', '⚴'], 'juno': ['Juno', '⚵'], # Asteroid Belt
        'vesta': ['Vesta', '⚶'], 'astraea': ['Astraea', '⯙'], 'hygiea': ['Hygiea', '⯚'], 
        'psyche': ['Psyche', 'Ψ'], 'proserpina': ['Proserpina', '⯘'], 'eros': ['Eros', '➳'], 
        'icarus': ['Icarus', '⯞'],

        'chiron': ['Chiron', '⚷'], 'pholus': ['Pholus', '⯛'], 'nessus': ['Nessus', '⯜'], # Centaurs
        'quaoar': ['Quaoar', '🝾'], 'logos': ['Logos & Zoe', '†'], 'sedna': ['Sedna', '⯲'], # Neptunians
        'orcus': ['Orcus', '🝿'], 'salacia': ['Salacia', '∿'], 'eris': ['Eris', '⯱'],
        'haumea': ['Haumea', '🝻'], 'makemake': ['Makemake', '🝼'], 'gonggong': ['Gonggong', '🝽']
        }

    def get_ayanamsa(self, t, tropical):
        if not tropical:
            return self.eph.get_ayanamsa(t)
        else:
            return None

    def create_placidus(self, t, location, tropical):
        cusps, ascmc = self.eph.observe_placidus(t, location)
        placidus = dict()

        ayanamsa = self.get_ayanamsa(t, tropical)

        for i in range (1, 13):
            house_name = f"House {i}"
            house_symbol = '🜨' if i in [1, 4, 7, 10] else '⌂'
            house = Node(house_name, house_symbol)
            house.longitude = cusps[i-1]
            house.get_zodiac(ayanamsa)
            placidus[house_name] = house

        return placidus
    
    def create_celestials(self, t, location, targets, tropical=True):
        celestials = dict()

        for target in targets:
            target = target.lower().replace(' ', '_')
            name, symbol = self.celestial_symbols.get(target, (None, None))
            if name is None:
                raise ValueError(f"Invalid celestial target: {target}")
            
            celestial = Celestial(name, symbol)

            # Computing Ayanamsa
            ayanamsa = self.get_ayanamsa(t, tropical)

            # Computing Celestial Ecliptic Coordinates
            celestial.longitude, celestial.latitude, celestial.distance, celestial.longitude_speed, _, _ = self.eph.observe_celestial_ecliptic(t, location, target)

            # Computing Celestial Equatorial Coordinates
            celestial.ra, celestial.dec = self.eph.observe_celestial_equatorial(t, location, target)

            # Getting Retrograde Status
            celestial.get_retrograde()
            
            # Getting Celestial Zodiac
            celestial.get_zodiac(ayanamsa)

            # Getting Celestial Phase
            sun_longitude, _, _, _, _, _ = self.eph.observe_celestial_ecliptic(t, location, 'sun')
            celestial.get_phase(sun_longitude)

            celestials[name] = celestial

        return celestials
    
    def create_solar_eclipse(self, t, location):
        retflag, tret, attr = self.eph.observe_solar_eclipse(t, location)

        ecltimes = []
        for i in range(len(tret)):
            year, month, day, hour = tret[i]
            if year < 0:
                ecltimes.append(None)
                continue
            hour_int = int(hour)
            minute = int((hour - hour_int) * 60)
            ecltimes.append(datetime(year, month, day, hour_int, minute))

        # Initilizing eclipse object
        eclipse = SolarEclipse()
        eclipse.get_type(retflag)

        eclipse.magnitude = attr[8]
        eclipse.obscuration = attr[2]
        eclipse.gamma = attr[7]
        
        eclipse.t_c1 = ecltimes[1]
        eclipse.t_c2 = ecltimes[2]
        eclipse.t_max = ecltimes[0]
        eclipse.t_c3 = ecltimes[3] 
        eclipse.t_c4 = ecltimes[4]

        return eclipse
    
    def create_lunar_eclipse(self, t, location):
        retflag, tret, attr = self.eph.observe_lunar_eclipse(t, location)

        ecltimes = []
        for i in range(len(tret)):
            year, month, day, hour = tret[i]
            if year < 0:
                ecltimes.append(None)
                continue
            hour_int = int(hour)
            minute = int((hour - hour_int) * 60)
            ecltimes.append(datetime(year, month, day, hour_int, minute))

        # Initilizing eclipse object
        eclipse = LunarEclipse()
        eclipse.get_type(retflag)

        eclipse.magnitude = attr[8]
        eclipse.obscuration = attr[2]
        eclipse.gamma = attr[7]
        
        eclipse.t_p1 = ecltimes[6]
        eclipse.t_u1 = ecltimes[2]
        eclipse.t_u2 = ecltimes[4]
        eclipse.t_max = ecltimes[0]
        eclipse.t_u3 = ecltimes[5]
        eclipse.t_u4 = ecltimes[3]
        eclipse.t_p2 = ecltimes[7]

        return eclipse

    