from cyclical import zodiac, phase
import swisseph as swe
from swiss import SwissEphemeris
from spice import SpiceEphemeris
from locator import locator, utc
from datetime import datetime, timedelta
import numpy as np
from atlas import Atlas

t = datetime.now()

location = locator("London")
if location is not None:
	print("Longitude: " + str(location.longitude))
	print("Latitude: " + str(location.latitude))

t = utc(t, location)
print("UTC: " + str(t))

#=======#
# SPICE #
#=======#

spice_eph = SpiceEphemeris()
swiss_eph = SwissEphemeris()
atlas = Atlas()

# Sun
sun = spice_eph.ecliptic(t, location, None, 'Earth', 'Sun')
sun_sign = zodiac(np.mod(np.degrees(sun[1]), 360))

# Moon
moon = spice_eph.ecliptic(t, location, None, 'Earth', 'Moon')
moon_zodiac = zodiac(np.mod(np.degrees(moon[1]), 360))
moon_phase = phase(np.mod(np.degrees(moon[1]), 360), np.mod(np.degrees(sun[1]),360))

moon_apogee, moon_perigee, moon_asc_node, moon_dsc_node = spice_eph.orbit(t, None, 'Earth', 'Moon', 31)

moon_apogee_zodiac = zodiac(np.mod(np.degrees(moon_apogee[1]), 360))
moon_perigee_zodiac = zodiac(np.mod(np.degrees(moon_perigee[1]), 360))
moon_asc_node_zodiac = zodiac(np.mod(np.degrees(moon_asc_node[1]), 360))
moon_dsc_node_zodiac = zodiac(np.mod(np.degrees(moon_dsc_node[1]), 360))

print("\nMoon")
print("Zodiac:" + str(moon_zodiac))
print("Phase: " + str(moon_phase))
print("Lilith: " + str(moon_apogee_zodiac))
print("Priapus: " + str(moon_perigee_zodiac))
print("Ascending Node: " + str(moon_asc_node_zodiac))
print("Descending Node: " + str(moon_dsc_node_zodiac))
print("Latitude: " + str(np.degrees(moon[2])) + "°")

# Jupiter
jupiter = spice_eph.ecliptic(t, location, None, 'Earth', 'Jupiter Barycenter')
jupiter_zodiac = zodiac(np.mod(np.degrees(jupiter[1]), 360))
jupiter_opp, jupiter_con, jupiter_asc_node, jupiter_dsc_node = spice_eph.orbit(t, None, 'Earth', 'Jupiter Barycenter', 4329)

print("\nJupiter")
print("Zodiac: " + str(jupiter_zodiac))
print("Current Distance: " + str(jupiter[0]) + " km")
print("Opposition Distance: " + str(jupiter_opp[0]) + " km")
print("Conjunction Distance: " + str(jupiter_con[0]) + " km")
print("Latitude: " + str(np.degrees(jupiter[2])) + "°")

#==========#
# SWISSEPH #
#==========#

lilith = atlas.geo_lunar(t, location)['Lilith']
selena = atlas.geo_lunar(t, location)['Selena']
print("Lilith: " + lilith.zodiac_symbol + lilith.zodiac + " " + lilith.zodiac_orb)
print(f"Lilith Phase: {lilith.phase_symbol} {lilith.phase}")
print(f"Selena Phase: {selena.phase_symbol} {selena.phase}")




