from eph import Ephemeris
from cyclical import zodiac, phase
import swisseph as swe

class Atlas:
	class AtlasObject:
		def __init__(self, name, symbol):
			# Name
			self.name = name
			self.symbol = symbol

			# Eclitpic Information
			self.distance = None
			self.longitude = None
			self.latitude = None
			self.retrograde = None

			# Zodiac Information
			self.zodiac = None
			self.zodiac_symbol = None
			self.zodiac_orb = None
			self.zodiac_element = None

			# Phase Information
			self.phase = None
			self.phase_symbol = None
			self.phase_longitude = None

		def to_dict(self):
			return {
			'name': self.name,
			'symbol': self.symbol,
			'distance': self.distance,
			'longitude': self.longitude,
			'latitude': self.latitude,
			'retrograde': self.retrograde,
			'zodiac': self.zodiac,
			'zodiac_symbol': self.zodiac_symbol,
			'zodiac_orb': self.zodiac_orb,
			'phase': self.phase,
			'phase_symbol': self.phase_symbol,
			'phase_longitude': self.phase_longitude
			}

	def __init__(self):
		self.eph = Ephemeris()

	def placidus(self, t, location): # Geocentric | Placidus
		t_jd = swe.julday(t.year, t.month, t.day, t.hour + t.minute/60 + t.second/3600) # Julian Date

		# Cusps and ASC/MC
		cusps, ascmc = swe.houses(t_jd, location.latitude, location.longitude, b'P')

		# Initialize
		house_one = self.AtlasObject('I', '⌂')
		house_two = self.AtlasObject('II', '⌂')
		house_three = self.AtlasObject('III', '⌂')
		house_four = self.AtlasObject('IV', '⌂')
		house_five = self.AtlasObject('V', '⌂')
		house_six = self.AtlasObject('VI', '⌂')
		house_seven = self.AtlasObject('VII', '⌂')
		house_eight = self.AtlasObject('VIII', '⌂')
		house_nine = self.AtlasObject('IX', '⌂')
		house_ten = self.AtlasObject('X', '⌂')
		house_eleven = self.AtlasObject('XI', '⌂')
		house_twelve = self.AtlasObject('XII', '⌂')

		# Location
		house_one.longitude = cusps[0]
		house_two.longitude = cusps[1]
		house_three.longitude = cusps[2]
		house_four.longitude = cusps[3]
		house_five.longitude = cusps[4]
		house_six.longitude = cusps[5]
		house_seven.longitude = cusps[6]
		house_eight.longitude = cusps[7]
		house_nine.longitude = cusps[8]
		house_ten.longitude = cusps[9]
		house_eleven.longitude = cusps[10]
		house_twelve.longitude = cusps[11]

		# Zodiac
		house_one.zodiac, house_one.zodiac_symbol, house_one.zodiac_orb, house_one.zodiac_element = zodiac(house_one.longitude)
		house_two.zodiac, house_two.zodiac_symbol, house_two.zodiac_orb, house_two.zodiac_element = zodiac(house_two.longitude)
		house_three.zodiac, house_three.zodiac_symbol, house_three.zodiac_orb, house_three.zodiac_element  = zodiac(house_three.longitude)
		house_four.zodiac, house_four.zodiac_symbol, house_four.zodiac_orb, house_four.zodiac_element  = zodiac(house_four.longitude)
		house_five.zodiac, house_five.zodiac_symbol, house_five.zodiac_orb, house_five.zodiac_element  = zodiac(house_five.longitude)
		house_six.zodiac, house_six.zodiac_symbol, house_six.zodiac_orb, house_six.zodiac_element  = zodiac(house_six.longitude)
		house_seven.zodiac, house_seven.zodiac_symbol, house_seven.zodiac_orb, house_seven.zodiac_element  = zodiac(house_seven.longitude)
		house_eight.zodiac, house_eight.zodiac_symbol, house_eight.zodiac_orb, house_eight.zodiac_element = zodiac(house_eight.longitude)
		house_nine.zodiac, house_nine.zodiac_symbol, house_nine.zodiac_orb, house_nine.zodiac_element = zodiac(house_nine.longitude)
		house_ten.zodiac, house_ten.zodiac_symbol, house_ten.zodiac_orb, house_ten.zodiac_element = zodiac(house_ten.longitude)
		house_eleven.zodiac, house_eleven.zodiac_symbol, house_eleven.zodiac_orb, house_eleven.zodiac_element = zodiac(house_eleven.longitude)
		house_twelve.zodiac, house_twelve.zodiac_symbol, house_twelve.zodiac_orb, house_twelve.zodiac_element = zodiac(house_twelve.longitude)

		return {
		'I': house_one,
		'II': house_two,
		'III': house_three,
		'IV': house_four,
		'V': house_five,
		'VI': house_six,
		'VII': house_seven,
		'VIII': house_eight,
		'IX': house_nine,
		'X': house_ten,
		'XI': house_eleven,
		'XII': house_twelve
		}

	def celestial(self, t, location): # Geocentric | Main Celestials
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
		pluto = self.AtlasObject('Pluto', '⯓')

		# Location
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.eph.ecliptic(t, location, 'sun', None)
		moon.distance, moon.longitude, moon.latitude, moon.retrograde = self.eph.ecliptic(t, location, 'moon', None)
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.eph.ecliptic(t, location, 'mercury', None)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.eph.ecliptic(t, location, 'venus', None)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.eph.ecliptic(t, location, 'mars', None)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.eph.ecliptic(t, location, 'jupiter', None)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.eph.ecliptic(t, location, 'saturn', None)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.eph.ecliptic(t, location, 'uranus', None)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.eph.ecliptic(t, location, 'neptune', None)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.eph.ecliptic(t, location, 'pluto', None)

		# Zodiac
		sun.zodiac, sun.zodiac_symbol, sun.zodiac_orb, sun.zodiac_element = zodiac(sun.longitude)
		moon.zodiac, moon.zodiac_symbol, moon.zodiac_orb, moon.zodiac_element = zodiac(moon.longitude)
		mercury.zodiac, mercury.zodiac_symbol, mercury.zodiac_orb, mercury.zodiac_element = zodiac(mercury.longitude)
		venus.zodiac, venus.zodiac_symbol, venus.zodiac_orb, venus.zodiac_element = zodiac(venus.longitude)
		mars.zodiac, mars.zodiac_symbol, mars.zodiac_orb, mars.zodiac_element = zodiac(mars.longitude)
		jupiter.zodiac, jupiter.zodiac_symbol, jupiter.zodiac_orb, jupiter.zodiac_element = zodiac(jupiter.longitude)
		saturn.zodiac, saturn.zodiac_symbol, saturn.zodiac_orb, saturn.zodiac_element = zodiac(saturn.longitude)
		uranus.zodiac, uranus.zodiac_symbol, uranus.zodiac_orb, uranus.zodiac_element = zodiac(uranus.longitude)
		neptune.zodiac, neptune.zodiac_symbol, neptune.zodiac_orb, neptune.zodiac_element = zodiac(neptune.longitude)
		pluto.zodiac, pluto.zodiac_symbol, pluto.zodiac_orb, pluto.zodiac_element = zodiac(pluto.longitude)

		# Phase
		moon.phase, moon.phase_symbol, moon.phase_longitude = phase(moon.longitude, sun.longitude, moon.name)
		mercury.phase, mercury.phase_symbol, mercury.phase_longitude = phase(mercury.longitude, sun.longitude, mercury.name)
		venus.phase, venus.phase_symbol, venus.phase_longitude = phase(venus.longitude, sun.longitude, venus.name)

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
	
	def asteroid(self, t, location): # Geocentric | Asteroid Belt
		# Initialize
		ceres = self.AtlasObject('Ceres', '⚳')
		pallas = self.AtlasObject('Pallas', '⚴')
		juno = self.AtlasObject('Juno', '⚵')
		vesta = self.AtlasObject('Vesta', '⚶')
		astraea = self.AtlasObject('Astraea', '⯙')
		hygiea = self.AtlasObject('Hygiea', '⯚')
		psyche = self.AtlasObject('Psyche', 'Ψ')
		proserpina = self.AtlasObject('Proserpina', '⯘')
		eros = self.AtlasObject('Eros', '➳')

		# Location
		ceres.distance, ceres.longitude, ceres.latitude, ceres.retrograde = self.eph.ecliptic(t, location, 'ceres', None)
		pallas.distance, pallas.longitude, pallas.latitude, pallas.retrograde = self.eph.ecliptic(t, location, 'pallas', None)
		juno.distance, juno.longitude, juno.latitude, juno.retrograde = self.eph.ecliptic(t, location, 'juno', None)
		vesta.distance, vesta.longitude, vesta.latitude, vesta.retrograde = self.eph.ecliptic(t, location, 'vesta', None)
		astraea.distance, astraea.longitude, astraea.latitude, astraea.retrograde = self.eph.ecliptic(t, location, 'astraea', None)
		hygiea.distance, hygiea.longitude, hygiea.latitude, hygiea.retrograde = self.eph.ecliptic(t, location, 'hygiea', None)
		psyche.distance, psyche.longitude, psyche.latitude, psyche.retrograde = self.eph.ecliptic(t, location, 'psyche', None)
		proserpina.distance, proserpina.longitude, proserpina.latitude, proserpina.retrograde = self.eph.ecliptic(t, location, 'proserpina', None)
		eros.distance, eros.longitude, eros.latitude, eros.retrograde = self.eph.ecliptic(t, location, 'eros', None)


		# Zodiac
		ceres.zodiac, ceres.zodiac_symbol, ceres.zodiac_orb, ceres.zodiac_element = zodiac(ceres.longitude)
		pallas.zodiac, pallas.zodiac_symbol, pallas.zodiac_orb, pallas.zodiac_element = zodiac(pallas.longitude)
		juno.zodiac, juno.zodiac_symbol, juno.zodiac_orb, juno.zodiac_element = zodiac(juno.longitude)
		vesta.zodiac, vesta.zodiac_symbol, vesta.zodiac_orb, vesta.zodiac_element = zodiac(vesta.longitude)
		astraea.zodiac, astraea.zodiac_symbol, astraea.zodiac_orb, astraea.zodiac_element = zodiac(astraea.longitude)
		hygiea.zodiac, hygiea.zodiac_symbol, hygiea.zodiac_orb, hygiea.zodiac_element = zodiac(hygiea.longitude)
		psyche.zodiac, psyche.zodiac_symbol, psyche.zodiac_orb, psyche.zodiac_element = zodiac(psyche.longitude)
		proserpina.zodiac, proserpina.zodiac_symbol, proserpina.zodiac_orb, proserpina.zodiac_element = zodiac(proserpina.longitude)
		eros.zodiac, eros.zodiac_symbol, eros.zodiac_orb, eros.zodiac_element = zodiac(eros.longitude)

		return {
		'Ceres': ceres,
		'Pallas': pallas,
		'Juno': juno,
		'Vesta': vesta,
		'Astraea': astraea,
		'Hygiea': hygiea,
		'Psyche': psyche,
		'Proserpina': proserpina,
		'Eros': eros
		}

	def centaur(self, t, location): # Geocentric | Centaurs
		# Initialize
		chiron = self.AtlasObject('Chiron', '⚷')
		pholus = self.AtlasObject('Pholus', '⯛')
		nessus = self.AtlasObject('Nessus', '⯜')

		chiron.distance, chiron.longitude, chiron.latitude, chiron.retrograde = self.eph.ecliptic(t, location, 'chiron', None)
		pholus.distance, pholus.longitude, pholus.latitude, pholus.retrograde = self.eph.ecliptic(t, location, 'pholus', None)
		nessus.distance, nessus.longitude, nessus.latitude, nessus.retrograde = self.eph.ecliptic(t, location, 'nessus', None)

		chiron.zodiac, chiron.zodiac_symbol, chiron.zodiac_orb, chiron.zodiac_element = zodiac(chiron.longitude)
		pholus.zodiac, pholus.zodiac_symbol, pholus.zodiac_orb, chiron.zodiac_element = zodiac(pholus.longitude)
		nessus.zodiac, nessus.zodiac_symbol, nessus.zodiac_orb, chiron.zodiac_element = zodiac(nessus.longitude)

		return {
		'Chiron': chiron,
		'Pholus': pholus,
		'Nessus': nessus
		}

	def neptunian(self, t, location): # Geocentric | Trans-Neptunian Objects
		# Initialize
		quaoar = self.AtlasObject('Quaoar', '✧')
		logos = self.AtlasObject('Logos & Zoe', '†')
		sedna = self.AtlasObject('Sedna', '⯲')
		orcus = self.AtlasObject('Orcus', '🗝')
		salacia = self.AtlasObject('Salacia', '∿')
		eris = self.AtlasObject('Eris', '⯱')
		haumea = self.AtlasObject('Haumea', '୭')
		makemake = self.AtlasObject('Makemake', '𓆇')
		gonggong = self.AtlasObject('Gonggong', '༄')
		
		# Location
		quaoar.distance, quaoar.longitude, quaoar.latitude, quaoar.retrograde = self.eph.ecliptic(t, location, 'quaoar', None)
		logos.distance, logos.longitude, logos.latitude, logos.retrograde = self.eph.ecliptic(t, location, 'logos', None)
		sedna.distance, sedna.longitude, sedna.latitude, sedna.retrograde = self.eph.ecliptic(t, location, 'sedna', None)
		orcus.distance, orcus.longitude, orcus.latitude, orcus.retrograde = self.eph.ecliptic(t, location, 'orcus', None)
		salacia.distance, salacia.longitude, salacia.latitude, salacia.retrograde = self.eph.ecliptic(t, location, 'salacia', None)
		eris.distance, eris.longitude, eris.latitude, eris.retrograde = self.eph.ecliptic(t, location, 'eris', None)
		haumea.distance, haumea.longitude, haumea.latitude, haumea.retrograde = self.eph.ecliptic(t, location, 'haumea', None)
		makemake.distance, makemake.longitude, makemake.latitude, makemake.retrograde = self.eph.ecliptic(t, location, 'makemake', None)
		gonggong.distance, gonggong.longitude, gonggong.latitude, gonggong.retrograde = self.eph.ecliptic(t, location, 'gonggong', None)

		quaoar.zodiac, quaoar.zodiac_symbol, quaoar.zodiac_orb, quaoar.zodiac_element = zodiac(quaoar.longitude)
		logos.zodiac, logos.zodiac_symbol, logos.zodiac_orb, logos.zodiac_element = zodiac(logos.longitude)
		sedna.zodiac, sedna.zodiac_symbol, sedna.zodiac_orb, sedna.zodiac_element = zodiac(sedna.longitude)
		orcus.zodiac, orcus.zodiac_symbol, orcus.zodiac_orb, orcus.zodiac_element = zodiac(orcus.longitude)
		salacia.zodiac, salacia.zodiac_symbol, salacia.zodiac_orb, salacia.zodiac_element = zodiac(salacia.longitude)
		eris.zodiac, eris.zodiac_symbol, eris.zodiac_orb, eris.zodiac_element = zodiac(eris.longitude)
		haumea.zodiac, haumea.zodiac_symbol, haumea.zodiac_orb, haumea.zodiac_element = zodiac(haumea.longitude)
		makemake.zodiac, makemake.zodiac_symbol, makemake.zodiac_orb, makemake.zodiac_element = zodiac(makemake.longitude)
		gonggong.zodiac, gonggong.zodiac_symbol, gonggong.zodiac_orb, gonggong.zodiac_element = zodiac(gonggong.longitude)

		return {
		'Quaoar': quaoar,
		'Logos': logos,
		'Sedna': sedna,
		'Salacia': salacia,
		'Orcus': orcus,
		'Eris': eris,
		'Haumea': haumea,
		'Makemake': makemake,
		'Gonggong': gonggong
		}
	
	def lunar(self, t, location): # Geocentric Lunar
		# Initialize
		sun = self.AtlasObject('Sun', '☉')
		moon = self.AtlasObject('Moon', '☽')
		lunar_asc = self.AtlasObject('Lunar ASC', '☊')
		lunar_dsc = self.AtlasObject('Lunar DSC', '☋')
		lilith = self.AtlasObject('Lilith', '⚸')
		selena = self.AtlasObject('Selena', '⯝')

		# Location
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.eph.ecliptic(t, location, 'sun', None)
		moon.distance, moon.longitude, moon.latitude, moon.retrograde = self.eph.ecliptic(t, location, 'moon', None)
		lunar_asc.distance, lunar_asc.longitude, lunar_asc.latitude, lunar_asc.retrograde = self.eph.ecliptic(t, location, 'rahu', None)
		lunar_dsc.longitude, lunar_dsc.retrograde = ((lunar_asc.longitude + 180) % 360, '℞')
		lilith.distance, lilith.longitude, lilith.latitude, lilith.retrograde = self.eph.ecliptic(t, location, 'lilith', None)
		selena.distance, selena.longitude, selena.latitude, selena.retrograde = self.eph.ecliptic(t, location, 'selena', None)
		
		# Zodiac
		moon.zodiac, moon.zodiac_symbol, moon.zodiac_orb, moon.zodiac_element = zodiac(moon.longitude)
		lunar_asc.zodiac, lunar_asc.zodiac_symbol, lunar_asc.zodiac_orb, lunar_asc.zodiac_element = zodiac(lunar_asc.longitude)
		lunar_dsc.zodiac, lunar_dsc.zodiac_symbol, lunar_dsc.zodiac_orb, lunar_dsc.zodiac_element = zodiac(lunar_dsc.longitude)
		lilith.zodiac, lilith.zodiac_symbol, lilith.zodiac_orb, lilith.zodiac_element = zodiac(lilith.longitude)
		selena.zodiac, selena.zodiac_symbol, selena.zodiac_orb, selena.zodiac_element = zodiac(selena.longitude)

		# Phase
		moon.phase, moon.phase_symbol, moon.phase_longitude = phase(moon.longitude, sun.longitude, moon.name)
		lunar_asc.phase, lunar_asc.phase_symbol, lunar_asc.phase_longitude = phase(lunar_asc.longitude, sun.longitude, lunar_asc.name)
		lunar_dsc.phase, lunar_dsc.phase_symbol, lunar_dsc.phase_longitude = phase(lunar_dsc.longitude, sun.longitude, lunar_dsc.name)
		lilith.phase, lilith.phase_symbol, lilith.phase_longitude = phase(lilith.longitude, sun.longitude, lilith.name)
		selena.phase, selena.phase_symbol, selena.phase_longitude = phase(selena.longitude, sun.longitude, selena.name)

		return {
		'Moon': moon,
		'ASC': lunar_asc,
		'DSC': lunar_dsc,
		'Lilith': lilith,
		'Selena': selena,
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
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.eph.ecliptic(t, location, 'mercury', swe.FLG_HELCTR)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.eph.ecliptic(t, location, 'venus', swe.FLG_HELCTR)
		earth.distance, earth.longitude, earth.latitude, earth.retrograde = self.eph.ecliptic(t, location, 'earth', swe.FLG_HELCTR)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.eph.ecliptic(t, location, 'mars', swe.FLG_HELCTR)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.eph.ecliptic(t, location, 'jupiter', swe.FLG_HELCTR)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.eph.ecliptic(t, location, 'saturn', swe.FLG_HELCTR)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.eph.ecliptic(t, location, 'uranus', swe.FLG_HELCTR)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.eph.ecliptic(t, location, 'neptune', swe.FLG_HELCTR)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.eph.ecliptic(t, location, 'pluto', swe.FLG_HELCTR)

		# Zodiac
		mercury.zodiac, mercury.zodiac_symbol, mercury.zodiac_orb, mercury.zodiac_element = zodiac(mercury.longitude)
		venus.zodiac, venus.zodiac_symbol, venus.zodiac_orb, venus.zodiac_element = zodiac(venus.longitude)
		earth.zodiac, earth.zodiac_symbol, earth.zodiac_orb, earth.zodiac_element = zodiac(earth.longitude)
		mars.zodiac, mars.zodiac_symbol, mars.zodiac_orb, mars.zodiac_element = zodiac(mars.longitude)
		jupiter.zodiac, jupiter.zodiac_symbol, jupiter.zodiac_orb, jupiter.zodiac_element = zodiac(jupiter.longitude)
		saturn.zodiac, saturn.zodiac_symbol, saturn.zodiac_orb, saturn.zodiac_element = zodiac(saturn.longitude)
		uranus.zodiac, uranus.zodiac_symbol, uranus.zodiac_orb, uranus.zodiac_element = zodiac(uranus.longitude)
		neptune.zodiac, neptune.zodiac_symbol, neptune.zodiac_orb, neptune.zodiac_element = zodiac(neptune.longitude)
		pluto.zodiac, pluto.zodiac_symbol, pluto.zodiac_orb, pluto.zodiac_element = zodiac(pluto.longitude)

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