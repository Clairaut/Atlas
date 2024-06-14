from datetime import datetime
from objects import Location
from eph import Ephemeris

t = datetime(2021, 6, 10, 10, 0, 0)
location = Location(0, 0)

eph = Ephemeris()
retflag, tret, attr = eph.observe_eclipse(t, location)

print(tret[0])