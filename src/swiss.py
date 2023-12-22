import swisseph as swe
import numpy as np

class SwissEphemeris:
	def placidus(self, t, location):
		t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600) # Julian Date

		# Cusps and ASC/MC
		cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, b'P')

		return cusps, ascmc

	def ecliptic(self, t, location, target, flag):
		t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600)

		swe.set_topo(location.longitude, location.latitude, 100)
		swe.set_ephe_path('../eph')

		lon, lat, r, lon_speed, lat_speed, r_speed = swe.calc_ut(t_jd, target, flag)[0]

		retro = None
		if lon_speed > 0:
			retro = False
		else: 
			retro = True

		return r, lon, lat, retro


