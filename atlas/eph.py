import swisseph as swe
import os


class Ephemeris:
    def __init__(self, eph_dir=None):
        self.eph_dir = eph_dir
        self.eph_dir_default = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'eph')
        self.celestial_keys = {
        'sun': swe.SUN, 'moon': swe.MOON, 'mercury': swe.MERCURY, 'venus': swe.VENUS,
        'earth': swe.EARTH, 'mars': swe.MARS, 'jupiter': swe.JUPITER, 'saturn': swe.SATURN, 
        'uranus': swe.URANUS, 'neptune': swe.NEPTUNE, 'pluto': swe.PLUTO,
        'ceres': swe.CERES, 'pallas': swe.PALLAS, 'juno': swe.JUNO, 'vesta': swe.VESTA,
        'astraea': swe.AST_OFFSET+5, 'hygiea': swe.AST_OFFSET+10, 'psyche': swe.AST_OFFSET+16,
        'proserpina': swe.AST_OFFSET+26, 'eros': swe.AST_OFFSET+433, 'icarus': swe.AST_OFFSET+1566,
        'chiron': swe.CHIRON, 'pholus': swe.PHOLUS, 'nessus': swe.AST_OFFSET+7066,
        'quaoar': swe.AST_OFFSET+50000, 'logos': swe.AST_OFFSET+58534, 'sedna': swe.AST_OFFSET+90377,
        'orcus': swe.AST_OFFSET+90482, 'salacia': swe.AST_OFFSET+120347, 'haumea': swe.AST_OFFSET+136108, 
        'eris': swe.AST_OFFSET+136199, 'makemake': swe.AST_OFFSET+136472, 'gonggong': swe.AST_OFFSET+225088,
        'rahu': swe.MEAN_NODE, 'lilith': swe.MEAN_APOG, 'selena': swe.WHITE_MOON
        }

    def set_eph_path(self):
        if self.eph_dir is None:
            self.eph_dir = self.eph_dir_default
        swe.set_ephe_path(self.eph_dir)

    def set_location(self, location):
        swe.set_topo(location.longitude, location.latitude, location.altitude)

    def time_to_jd(self, t):
        return swe.julday(t.year, t.month, t.day, t.hour + t.minute / 60 + t.second / 3600)
    
    def find_celestial_id(self, target):
        target_id = self.celestial_keys.get(target.lower())
        if target_id is None:
            raise ValueError(f"Unknown celestial target: {target}")
        return target_id
    
    def get_ayanamsa(self, t):
        t_jd = self.time_to_jd(t)
        return swe.get_ayanamsa(t_jd)
    
    def observe_placidus(self, t, location, system=b'P'):
        self.set_eph_path()
        self.set_location(location) # Setting observer location
        t_jd = self.time_to_jd(t)  # Converting to Julian date

        # Determining house cusps and ASC/MC
        cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, system)

        return cusps, ascmc
    
    def observe_celestial_equatorial(self, t, location, target):
        self.set_eph_path()
        self.set_location(location)
        t_jd = self.time_to_jd(t)
        target_id = self.find_celestial_id(target)
        
        # Computing celestial position
        pos = swe.calc_ut(t_jd, target_id, swe.FLG_EQUATORIAL)

        ra = pos[0][0]
        dec = pos[0][1]

        return ra, dec
    
    def observe_celestial_ecliptic(self, t, location, target):
        self.set_eph_path()
        self.set_location(location)
        t_jd = self.time_to_jd(t)
        target_id = self.find_celestial_id(target)

        # Computing celestial position
        pos = swe.calc_ut(t_jd, target_id)
        
        longitude, latitude, distance, longitude_speed, latitude_speed, distance_speed = pos[0]
        
        return longitude, latitude, distance, longitude_speed, latitude_speed, distance_speed
    
    def observe_celestial_pheno(self, t, location, target):
        self.set_eph_path()
        self.set_location(location)
        t_jd = self.time_to_jd(t)
        target_id = self.find_celestial_id(target)
        
        attr = swe.pheno_ut(t_jd, target_id)

        phase_angle = attr[2]
        magnitude = attr[4]

        return phase_angle, magnitude
        
    def observe_solar_eclipse(self, t, location):
        t_jd = self.time_to_jd(t)

        # Determining solar eclipse
        retflag, tret, attr = swe.sol_eclipse_when_loc(t_jd, (location.longitude, location.latitude, location.altitude))

        tret = tuple(swe.revjul(t) for t in tret)

        return retflag, tret, attr
    
    def observe_lunar_eclipse(self, t, location):
        t_jd = self.time_to_jd(t)

        # Determining lunar eclipse
        retflag, tret, attr = swe.lun_eclipse_when_loc(t_jd, (location.longitude, location.latitude, location.altitude))

        tret = tuple(swe.revjul(t) for t in tret)

        return retflag, tret, attr