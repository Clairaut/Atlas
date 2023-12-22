from spice import SpiceEphemeris
from swiss import SwissEphemeris
from cyclical import zodiac, phase
import swisseph as swe

class Atlas:
	class AtlasObject:
		def __init__(self, name, symbol):
			# Name
			self.name = name
			self.symbol = symbol

			# Ecliptic football programme ryan reynoldsInformation
			self.distance = None
			self.longitude = None
			self.latitude = None
			self.retrograde = None

			# Zodiac Information
			self.zodiac = None
			self.zodiac_symbol = None
			self.zodiac_orb = None

			# Phase Information
			self.phase = None
			self.phase_symbol = None
			self.phase_longitude = None

	def __init__(self):
		self.spice_eph = SpiceEphemeris()
		self.swiss_eph = SwissEphemeris()

	def geo_main(self, t, location): # Geocentric | Main Celestials
		# Initialize
		sun = self.AtlasObject('Sun', '☉')
		moon = self.AtlasObject('Moon', '☽')
		mercury = self.AtlasObject('Mercury', '☿')
		venus = self.AtlasObject('Venus', '♀')
		mars = self.AtlasObject('Mars', '♂')
		jupiter = self.AtlasObject('Jupiter', '♃')
		saturn = self.AtlasObject('Saturn', '♄')
		uranus = self.AtlasObject('Uranus', '♅')
		neptune = self.AtlasObject('Neptune', '♆')
		pluto = self.AtlasObject('Pluto', '♇')

		# Location
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.swiss_eph.ecliptic(t, location, swe.SUN, swe.FLG_SWIEPH)
		moon.distance, moon.longitude, moon.latitude, moon.retrograde = self.swiss_eph.ecliptic(t, location, swe.MOON, swe.FLG_SWIEPH)
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.swiss_eph.ecliptic(t, location, swe.MERCURY, swe.FLG_SWIEPH)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.swiss_eph.ecliptic(t, location, swe.VENUS, swe.FLG_SWIEPH)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.swiss_eph.ecliptic(t, location, swe.MARS, swe.FLG_SWIEPH)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.swiss_eph.ecliptic(t, location, swe.JUPITER, swe.FLG_SWIEPH)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.swiss_eph.ecliptic(t, location, swe.SATURN, swe.FLG_SWIEPH)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.swiss_eph.ecliptic(t, location, swe.URANUS, swe.FLG_SWIEPH)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.swiss_eph.ecliptic(t, location, swe.NEPTUNE, swe.FLG_SWIEPH)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.swiss_eph.ecliptic(t, location, swe.PLUTO, swe.FLG_SWIEPH)

		# Zodiac
		sun.zodiac, sun.zodiac_symbol, sun.zodiac_orb = zodiac(sun.longitude)
		moon.zodiac, moon.zodiac_symbol, moon.zodiac_orb = zodiac(moon.longitude)
		mercury.zodiac, mercury.zodiac_symbol, mercury.zodiac_orb = zodiac(mercury.longitude)
		venus.zodiac, venus.zodiac_symbol, venus.zodiac_orb = zodiac(venus.longitude)
		mars.zodiac, mars.zodiac_symbol, mars.zodiac_orb = zodiac(mars.longitude)
		jupiter.zodiac, jupiter.zodiac_symbol, jupiter.zodiac_orb = zodiac(jupiter.longitude)
		saturn.zodiac, saturn.zodiac_symbol, saturn.zodiac_orb = zodiac(saturn.longitude)
		uranus.zodiac, uranus.zodiac_symbol, uranus.zodiac_orb = zodiac(uranus.longitude)
		neptune.zodiac, neptune.zodiac_symbol, neptune.zodiac_orb = zodiac(neptune.longitude)
		pluto.zodiac, pluto.zodiac_symbol, pluto.zodiac_orb = zodiac(pluto.longitude)

		# Phase
		moon.phase, moon.phase_symbol, moon.phase_longitude = phase(moon.longitude, sun.longitude)
		mercury.phase, mercury.phase_symbol, mercury.phase_longitude = phase(mercury.longitude, sun.longitude)
		venus.phase, venus.phase_symbol, venus.phase_longitude = phase(venus.longitude, sun.longitude)

		return {
		'Sun': sun,
		'Moon': moon,
		'Mercury': mercury,
		'Venus': venus,
		'Mars': mars,
		'Jupiter': jupiter,
		'Saturn': saturn,
		'Uranus': uranus,
		'Neptune': neptune,
		'Pluto': pluto
		}

	def geo_lunar(self, t, location): # Geocentric Lunar
		# Initialize
		sun = self.AtlasObject('Sun', '☉')
		lunar_asc = self.AtlasObject('Lunar ASC', '☊')
		lunar_dsc = self.AtlasObject('Lunar DSC', '☋')
		lilith = self.AtlasObject('Lilith', '⚸')
		selena = self.AtlasObject('Selena', '⯝')
		priapus = self.AtlasObject('Priapus', '⯝')

		# Location
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.swiss_eph.ecliptic(t, location, swe.SUN, swe.FLG_SWIEPH)
		lunar_asc.distance, lunar_asc.longitude, lunar_asc.latitude, lunar_asc.retrograde = self.swiss_eph.ecliptic(t, location, swe.MEAN_NODE, swe.FLG_SWIEPH)
		lunar_dsc.longitude = (lunar_asc.longitude + 180) % 360
		lilith.distance, lilith.longitude, lilith.latitude, lilith.retrograde = self.swiss_eph.ecliptic(t, location, swe.MEAN_APOG, swe.FLG_SWIEPH)
		selena.distance, selena.longitude, selena.latitude, selena.retrograde = self.swiss_eph.ecliptic(t, location, swe.WHITE_MOON, swe.FLG_SWIEPH)
		
		# Zodiac
		lunar_asc.zodiac, lunar_asc.zodiac_symbol, lunar_asc.zodiac_orb = zodiac(lunar_asc.longitude)
		lunar_dsc.zodiac, lunar_dsc.zodiac_symbol, lunar_dsc.zodiac_orb = zodiac(lunar_dsc.longitude)
		lilith.zodiac, lilith.zodiac_symbol, lilith.zodiac_orb = zodiac(lilith.longitude)
		selena.zodiac, selena.zodiac_symbol, selena.zodiac_orb = zodiac(selena.longitude)

		# Phase
		lunar_asc.phase, lunar_asc.phase_symbol, lunar_asc.phase_orb = phase(lunar_asc.longitude, sun.longitude)
		lunar_dsc.phase, lunar_dsc.phase_symbol, lunar_dsc.phase_orb = phase(lunar_dsc.longitude, sun.longitude)
		lilith.phase, lilith.phase_symbol, lilith.phase_orb = phase(lilith.longitude, sun.longitude)
		selena.phase, selena.phase_symbol, selena.phase_orb = phase(selena.longitude, sun.longitude)

		return {
		'Lunar ASC': lunar_asc,
		'Lunar DSC': lunar_dsc,
		'Lilith': lilith,
		'Selena': selena,
		}
	

	def geo_asteroid(self, t, location): # Geocentric | Asteroid Belt
		# Initialize
		ceres = self.AtlasObject('Ceres', '⚳')
		pallas = self.AtlasObject('Pallas', '⚴')
		juno = self.AtlasObject('Juno', '⚵')
		vesta = self.AtlasObject('Vesta', '⚶')
		astraea = self.AtlasObject('Astraea', '⯙')
		hygiea = self.AtlasObject('Hygiea', '⯚')
		psyche = self.AtlasObject('Psyche', '♡')
		prosperina = self.AtlasObject('Prosperina', '⯘')
		eros = self.AtlasObject('Eros', '➳')
		selene = self.AtlasObject('Selene', '☽')
		asclepius = self.AtlasObject('Asclepius', '⚕')

		# Location
		ceres.distance, ceres.longitude, ceres.latitude, ceres.retrograde = self.swiss_eph.ecliptic(t, location, 20000001, swe.FLG_SWIEPH)
		pallas.distance, pallas.longitude, pallas.latitude, pallas.retrograde = self.swiss_eph.ecliptic(t, location, 20000002, swe.FLG_SWIEPH)
		juno.distance, juno.longitude, juno.latitude, juno.retrograde = self.swiss_eph.ecliptic(t, location, 20000003, swe.FLG_SWIEPH)
		vesta.distance, vesta.longitude, vesta.latitude, vesta.retrograde = self.swiss_eph.ecliptic(t, location, 20000004, swe.FLG_SWIEPH)
		astraea.distance, astraea.longitude, astraea.latitude, astraea.retrograde = self.swiss_eph.ecliptic(t, location, 20000005, swe.FLG_SWIEPH)
		hygiea.distance, hygiea.longitude, hygiea.latitude, hygiea.retrograde = self.swiss_eph.ecliptic(t, location, 20000010, swe.FLG_SWIEPH)
		psyche.distance, psyche.longitude, psyche.latitude, psyche.retrograde = self.swiss_eph.ecliptic(t, location, 20000016, swe.FLG_SWIEPH)
		prosperina.distance, prosperina.longitude, prosperina.latitude, prosperina.retrograde = self.swiss_eph.ecliptic(t, location, 20000026, swe.FLG_SWIEPH)
		eros.distance, eros.longitude, eros.latitude, eros.retrograde = self.swiss_eph.ecliptic(t, location, 20000433, swe.FLG_SWIEPH)
		selene.distance, selene.longtiude, selene.latitude, selene.retrograde = self.swiss_eph.ecliptic(t, location, 20000580, swe.FLG_SWIEPH)
		asclepius.distance, asclepius.longitude, asclepius.latitude, asclepius.retrograde = self.swiss_eph.ecliptic(t, location, 20004581, swe.FLG_SWIEPH)

		# Zodiac
		ceres.zodiac, ceres.zodiac_symbol, ceres.zodiac_orb = zodiac(ceres.longitude)
		pallas.zodiac, pallas.zodiac_symbol, pallas.zodiac_orb = zodiac(pallas.longitude)
		juno.zodiac, juno.zodiac_symbol, juno.zodiac_orb = zodiac(juno.longitude)
		vesta.zodiac, vesta.zodiac_symbol, vesta.zodiac_orb = zodiac(vesta.longitude)
		astraea.zodiac, astraea.zodiac_symbol, astraea.zodiac_orb = zodiac(astraea.longitude)
		hygiea.zodiac, hygiea.zodiac_symbol, hygiea.zodiac_orb = zodiac(hygiea.longitude)
		psyche.zodiac, psyche.zodiac_symbol, psyche.zodiac_orb = zodiac(psyche.longitude)
		prosperina.zodiac, prosperina.zodiac_symbol, prosperina.zodiac_orb = zodiac(prosperina.longitude)
		eros.zodiac, eros.zodiac_symbol, eros.zodiac_orb = zodiac(eros.longitude)
		selene.zodiac, selene.zodiac_symbol, selene.zodiac_orb = zodiac(selene.longitude)
		asclepius.zodiac, asclepius.zodiac_symbol, asclepius.zodiac_orb = zodiac(asclepius.longitude)

		return {
		'Ceres': ceres,
		'Pallas': pallas,
		'Juno': juno,
		'Vesta': vesta, 
		'Astraea': astraea,
		'Hygiea': hygiea,
		'Psyche': psyche,
		'Prosperina': prosperina,
		'Eros': eros,
		'Selene': selene,
		'Asclepius': asclepius
		}

	def helio_main(self, t, location): # Heliocentric | Main Celestials
		# Initialize
		mercury = self.AtlasObject('Mercury', '☿')
		venus = self.AtlasObject('Venus', '♀')
		earth = self.AtlasObject('Earth', '♁')
		mars = self.AtlasObject('Mars', '♂')
		jupiter = self.AtlasObject('Jupiter', '♃')
		saturn = self.AtlasObject('Saturn', '♄')
		uranus = self.AtlasObject('Uranus', '♅')
		neptune = self.AtlasObject('Neptune', '♆')
		pluto = self.AtlasObject('Pluto', '♇')

		# Location
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.swiss_eph.ecliptic(t, location, swe.MERCURY, swe.FLG_HELCTR)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.swiss_eph.ecliptic(t, location, swe.VENUS, swe.FLG_HELCTR)
		earth.distance, earth.longitude, earth.latitude, earth.retrograde = self.swiss_eph.ecliptic(t, location, swe.EARTH, swe.FLG_HELCTR)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.swiss_eph.ecliptic(t, location, swe.MARS, swe.FLG_HELCTR)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.swiss_eph.ecliptic(t, location, swe.JUPITER, swe.FLG_HELCTR)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.swiss_eph.ecliptic(t, location, swe.SATURN, swe.FLG_HELCTR)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.swiss_eph.ecliptic(t, location, swe.URANUS, swe.FLG_HELCTR)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.swiss_eph.ecliptic(t, location, swe.NEPTUNE, swe.FLG_HELCTR)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.swiss_eph.ecliptic(t, location, swe.PLUTO, swe.FLG_HELCTR)

		# Zodiac
		mercury.zodiac, mercury.zodiac_symbol, mercury.zodiac_orb = zodiac(mercury.longitude)
		venus.zodiac, venus.zodiac_symbol, venus.zodiac_orb = zodiac(venus.longitude)
		earth.zodiac, earth.zodiac_symbol, earth.zodiac_orb = zodiac(earth.longitude)
		mars.zodiac, mars.zodiac_symbol, mars.zodiac_orb = zodiac(mars.longitude)
		jupiter.zodiac, jupiter.zodiac_symbol, jupiter.zodiac_orb = zodiac(jupiter.longitude)
		saturn.zodiac, saturn.zodiac_symbol, saturn.zodiac_orb = zodiac(saturn.longitude)
		uranus.zodiac, uranus.zodiac_symbol, uranus.zodiac_orb = zodiac(uranus.longitude)
		neptune.zodiac, neptune.zodiac_symbol, neptune.zodiac_orb = zodiac(neptune.longitude)
		pluto.zodiac, pluto.zodiac_symbol, pluto.zodiac_orb = zodiac(pluto.longitude)

		return {
		'Mercury': mercury,
		'Venus': venus,
		'Earth': earth,
		'Mars': mars,
		'Jupiter': jupiter,
		'Saturn': saturn,
		'Uranus': uranus,
		'Neptune': neptune,
		'Pluto': pluto
		}