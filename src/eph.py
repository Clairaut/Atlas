import swisseph as swe
import numpy as np

class Ephemeris:
	def __init__(self):
		self.celestial_dictionary = { 
		# Main Celestials
		'sun': swe.SUN, 'moon': swe.MOON, 'mercury': swe.MERCURY, 'venus': swe.VENUS, 
		'earth': swe.EARTH, 'mars': swe.MARS, 'jupiter': swe.JUPITER, 'saturn': swe.SATURN, 
		'uranus': swe.URANUS, 'neptune': swe.NEPTUNE, 'pluto': swe.PLUTO, 
		
		# Asteroids
		'ceres': swe.CERES, 'pallas': swe.PALLAS, 'juno': swe.JUNO, 'vesta': swe.VESTA, 
		'astraea': swe.AST_OFFSET+5, 'hygiea': swe.AST_OFFSET+10, 'psyche': swe.AST_OFFSET+16,
		'proserpina': swe.AST_OFFSET+26, 'eros': swe.AST_OFFSET+433,
		
		# Centaur
		'chiron': swe.CHIRON, 'pholus': swe.PHOLUS, 'nessus': swe.AST_OFFSET+7066,
		
		# Neptunian
		'quaoar': swe.AST_OFFSET+50000, 'logos': swe.AST_OFFSET+58534, 'sedna': swe.AST_OFFSET+90377,
		'orcus': swe.AST_OFFSET+90482, 'salacia': swe.AST_OFFSET+120347, 'haumea': swe.AST_OFFSET+136108, 
		'eris': swe.AST_OFFSET+136199, 'makemake': swe.AST_OFFSET+136472, 'gonggong': swe.AST_OFFSET+225088,
		
		# Lunar
		'rahu': swe.MEAN_NODE, 'lilith': swe.MEAN_APOG, 'selena': swe.WHITE_MOON
		}

	def placidus(self, t, location):
		t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600) # Julian Date

		# Cusps and ASC/MC
		cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, b'P')

		return cusps, ascmc

	def ecliptic(self, t, location, target, flag):
		if target.lower() in self.celestial_dictionary.keys():
			target = self.celestial_dictionary[target]
		else:
			print("Error: Cannot find target")


		t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600)

		swe.set_topo(location.longitude, location.latitude, 100)
		swe.set_ephe_path('../eph')

		if flag is None:
			lon, lat, r, lon_speed, lat_speed, r_speed = swe.calc_ut(t_jd, target)[0]
		else:
			lon, lat, r, lon_speed, lat_speed, r_speed = swe.calc_ut(t_jd, target, flag)[0]
			
		retro = None
		if lon_speed > 0:
			retro = ''
		else: 
			retro = '℞'

		return r, lon, lat, retro


