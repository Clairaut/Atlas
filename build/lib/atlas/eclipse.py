class Eclipse:
    def __init__(self, celestial):
        self.t_max = None
        self.celestial = celestial
        self.type = None
        self.magnitude = None
        self.obscuration = None
        self.gamme = None

        self.FLAGS = [
            (0x0004, 'Total Eclipse'),
            (0x0040, 'Penumbral Eclipse'),
            (0x0010, 'Partial Eclipse'),
        ]

    def to_dict(self):
        return {
            't_max': self.t_max,
            'type': self.type,
            'magnitude': self.magnitude,
            'obscuration': self.obscuration,
            'gamma': self.gamma
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
            't_c4': self.t_c4
        })
        return data

class LunarEclipse(Eclipse):
    def __init__(self):
        super().__init__('Lunar')
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
            't_p2': self.t_p2
        })