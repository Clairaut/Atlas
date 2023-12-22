import swisseph as swe 

def placidus(t, location):
	t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600) # Julian Date

	# Cusps and ASC/MC
	cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, b'P')

	return cusps, ascmc
