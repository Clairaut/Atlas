import swisseph as swe
import numpy as np

def placidus(t, location):
	t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600) # Julian Date

	# Cusps and ASC/MC
	cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, b'P')

	lilith = swe.calc_ut(t_jd, swe.MEAN_APOG)
	print(np.mod(np.degrees(lilith[0][0]), 360))

	return cusps, ascmc

def lunar(t):
	t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600)

	lilith = swe.calc_ut(t_jd, swe.MEAN_APOG)

	return lilith
