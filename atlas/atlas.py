from atlas.eph import Ephemeris
from atlas.cyclical import zodiac, phase

import swisseph as swe
import traceback

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

			# Equatorial Information
			self.ra = None
			self.dec = None

			# Zodiac Information
			self.zodiac = None
			self.zodiac_symbol = None
			self.zodiac_orb = None

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
		self.celestials = {
			'sun': ['Sun', '☉'], 'moon': ['Moon', '☽'], 'mercury': ['Mercury', '☿'], # Main Celestials
			'venus': ['Venus', '♀'], 'mars': ['Mars', '♂'], 'jupiter': ['Jupiter', '♃'], 
			'saturn': ['Saturn', '♄'], 'uranus': ['Uranus', '♅'], 'neptune': ['Neptune', '♆'], 
			'pluto': ['Pluto', '⯓'],

			'lilith': ['Lilith', '⚸'], 'selena': ['Selena', '⯝'], 'lunar_asc': ['Lunar ASC', '☊'], # Lunar
			'lunar_dsc': ['Lunar DSC', '☋'],
			
			'ceres': ['Ceres', '⚳'], 'pallas': ['Pallas', '⚴'], 'juno': ['Juno', '⚵'], # Asteroid Belt
			'vesta': ['Vesta', '⚶'], 'astraea': ['Astraea', '⯙'], 'hygiea': ['Hygiea', '⯚'], 
			'psyche': ['Psyche', 'Ψ'], 'proserpina': ['Proserpina', '⯘'], 'eros': ['Eros', '➳'],
			
			'chiron': ['Chiron', '⚷'], 'pholus': ['Pholus', '⯛'], 'nessus': ['Nessus', '⯜'], # Centaurs

			'quaoar': ['Quaoar', '✧'], 'logos': ['Logos & Zoe', '†'], 'sedna': ['Sedna', '⯲'], # Neptunians
			'orcus': ['Orcus', '🗝'], 'salacia': ['Salacia', '∿'], 'eris': ['Eris', '⯱'],
			'haumea': ['Haumea', '୭'], 'makemake': ['Makemake', '𓆇'], 'gonggong': ['Gonggong', '༄']
		}

	def body(self, t, target, location=None, flag=None): # Geocentric | Single/Multiple Bodies
		target = target.lower().replace(' ', '_')
		if target in self.celestials.keys():
			body = self.AtlasObject(self.celestials[target.lower()][0], self.celestials[target.lower()][1])
		else:
			body = self.AtlasObject(target.capitalize(), '🪐')

		try:
			if flag:
				body.distance, body.longitude, body.latitude, body.retrograde = self.eph.observe(t, target, location=location, flag=flag)
			else:
				body.distance, body.longitude, body.latitude, body.retrograde = self.eph.observe(t, target, location=location)
				body.ra, body.dec = self.eph.observe(t, target, location=location, flag=2048)
		except Exception as e:
			print(f"Error: {e}")
			traceback.print_exc()
			exit()
		
		body.zodiac, body.zodiac_symbol, body.zodiac_orb = zodiac(body.longitude)
		
		return body

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
		house_one.zodiac, house_one.zodiac_symbol, house_one.zodiac_orb = zodiac(house_one.longitude)
		house_two.zodiac, house_two.zodiac_symbol, house_two.zodiac_orb = zodiac(house_two.longitude)
		house_three.zodiac, house_three.zodiac_symbol, house_three.zodiac_orb  = zodiac(house_three.longitude)
		house_four.zodiac, house_four.zodiac_symbol, house_four.zodiac_orb  = zodiac(house_four.longitude)
		house_five.zodiac, house_five.zodiac_symbol, house_five.zodiac_orb  = zodiac(house_five.longitude)
		house_six.zodiac, house_six.zodiac_symbol, house_six.zodiac_orb  = zodiac(house_six.longitude)
		house_seven.zodiac, house_seven.zodiac_symbol, house_seven.zodiac_orb  = zodiac(house_seven.longitude)
		house_eight.zodiac, house_eight.zodiac_symbol, house_eight.zodiac_orb = zodiac(house_eight.longitude)
		house_nine.zodiac, house_nine.zodiac_symbol, house_nine.zodiac_orb = zodiac(house_nine.longitude)
		house_ten.zodiac, house_ten.zodiac_symbol, house_ten.zodiac_orb = zodiac(house_ten.longitude)
		house_eleven.zodiac, house_eleven.zodiac_symbol, house_eleven.zodiac_orb = zodiac(house_eleven.longitude)
		house_twelve.zodiac, house_twelve.zodiac_symbol, house_twelve.zodiac_orb = zodiac(house_twelve.longitude)

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

		# Ecliptic Positions
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.eph.observe(t, 'sun', location=location)
		moon.distance, moon.longitude, moon.latitude, moon.retrograde = self.eph.observe(t, 'moon', location=location)
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.eph.observe(t, 'mercury', location=location)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.eph.observe(t, 'venus', location=location)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.eph.observe(t, 'mars', location=location)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.eph.observe(t, 'jupiter', location=location)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.eph.observe(t, 'saturn', location=location)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.eph.observe(t, 'uranus', location=location)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.eph.observe(t, 'neptune', location=location)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.eph.observe(t, 'pluto', location=location)

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
		ceres.distance, ceres.longitude, ceres.latitude, ceres.retrograde = self.eph.observe(t, 'ceres', location=location)
		pallas.distance, pallas.longitude, pallas.latitude, pallas.retrograde = self.eph.observe(t, 'pallas', location=location)
		juno.distance, juno.longitude, juno.latitude, juno.retrograde = self.eph.observe(t, 'juno', location=location)
		vesta.distance, vesta.longitude, vesta.latitude, vesta.retrograde = self.eph.observe(t, 'vesta', location=location)
		astraea.distance, astraea.longitude, astraea.latitude, astraea.retrograde = self.eph.observe(t, 'astraea', location=location)
		hygiea.distance, hygiea.longitude, hygiea.latitude, hygiea.retrograde = self.eph.observe(t, 'hygiea', location=location)
		psyche.distance, psyche.longitude, psyche.latitude, psyche.retrograde = self.eph.observe(t, 'psyche', location=location)
		proserpina.distance, proserpina.longitude, proserpina.latitude, proserpina.retrograde = self.eph.observe(t, 'proserpina', location=location)
		eros.distance, eros.longitude, eros.latitude, eros.retrograde = self.eph.observe(t, 'eros', location=location)


		# Zodiac
		ceres.zodiac, ceres.zodiac_symbol, ceres.zodiac_orb = zodiac(ceres.longitude)
		pallas.zodiac, pallas.zodiac_symbol, pallas.zodiac_orb = zodiac(pallas.longitude)
		juno.zodiac, juno.zodiac_symbol, juno.zodiac_orb = zodiac(juno.longitude)
		vesta.zodiac, vesta.zodiac_symbol, vesta.zodiac_orb = zodiac(vesta.longitude)
		astraea.zodiac, astraea.zodiac_symbol, astraea.zodiac_orb = zodiac(astraea.longitude)
		hygiea.zodiac, hygiea.zodiac_symbol, hygiea.zodiac_orb = zodiac(hygiea.longitude)
		psyche.zodiac, psyche.zodiac_symbol, psyche.zodiac_orb = zodiac(psyche.longitude)
		proserpina.zodiac, proserpina.zodiac_symbol, proserpina.zodiac_orb = zodiac(proserpina.longitude)
		eros.zodiac, eros.zodiac_symbol, eros.zodiac_orb = zodiac(eros.longitude)

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

		chiron.distance, chiron.longitude, chiron.latitude, chiron.retrograde = self.eph.observe(t, 'chiron', location=location)
		pholus.distance, pholus.longitude, pholus.latitude, pholus.retrograde = self.eph.observe(t, 'pholus', location=location)
		nessus.distance, nessus.longitude, nessus.latitude, nessus.retrograde = self.eph.observe(t, 'nessus', location=location)

		chiron.zodiac, chiron.zodiac_symbol, chiron.zodiac_orb = zodiac(chiron.longitude)
		pholus.zodiac, pholus.zodiac_symbol, pholus.zodiac_orb = zodiac(pholus.longitude)
		nessus.zodiac, nessus.zodiac_symbol, nessus.zodiac_orb = zodiac(nessus.longitude)

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
		quaoar.distance, quaoar.longitude, quaoar.latitude, quaoar.retrograde = self.eph.observe(t, 'quaoar', location=location)
		logos.distance, logos.longitude, logos.latitude, logos.retrograde = self.eph.observe(t, 'logos', location=location)
		sedna.distance, sedna.longitude, sedna.latitude, sedna.retrograde = self.eph.observe(t, 'sedna', location=location)
		orcus.distance, orcus.longitude, orcus.latitude, orcus.retrograde = self.eph.observe(t, 'orcus', location=location)
		salacia.distance, salacia.longitude, salacia.latitude, salacia.retrograde = self.eph.observe(t, 'salacia', location=location)
		eris.distance, eris.longitude, eris.latitude, eris.retrograde = self.eph.observe(t, 'eris', location=location)
		haumea.distance, haumea.longitude, haumea.latitude, haumea.retrograde = self.eph.observe(t, 'haumea', location=location)
		makemake.distance, makemake.longitude, makemake.latitude, makemake.retrograde = self.eph.observe(t, 'makemake', location=location)
		gonggong.distance, gonggong.longitude, gonggong.latitude, gonggong.retrograde = self.eph.observe(t, 'gonggong', location=location)

		quaoar.zodiac, quaoar.zodiac_symbol, quaoar.zodiac_orb = zodiac(quaoar.longitude)
		logos.zodiac, logos.zodiac_symbol, logos.zodiac_orb = zodiac(logos.longitude)
		sedna.zodiac, sedna.zodiac_symbol, sedna.zodiac_orb = zodiac(sedna.longitude)
		orcus.zodiac, orcus.zodiac_symbol, orcus.zodiac_orb = zodiac(orcus.longitude)
		salacia.zodiac, salacia.zodiac_symbol, salacia.zodiac_orb = zodiac(salacia.longitude)
		eris.zodiac, eris.zodiac_symbol, eris.zodiac_orb = zodiac(eris.longitude)
		haumea.zodiac, haumea.zodiac_symbol, haumea.zodiac_orb = zodiac(haumea.longitude)
		makemake.zodiac, makemake.zodiac_symbol, makemake.zodiac_orb = zodiac(makemake.longitude)
		gonggong.zodiac, gonggong.zodiac_symbol, gonggong.zodiac_orb = zodiac(gonggong.longitude)

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
		sun.distance, sun.longitude, sun.latitude, sun.retrograde = self.eph.observe(t, 'sun', location=location)
		moon.distance, moon.longitude, moon.latitude, moon.retrograde = self.eph.observe(t, 'moon', location=location)
		lunar_asc.distance, lunar_asc.longitude, lunar_asc.latitude, lunar_asc.retrograde = self.eph.observe(t, 'rahu', location=location)
		lunar_dsc.longitude, lunar_dsc.retrograde = ((lunar_asc.longitude + 180) % 360, '℞')
		lilith.distance, lilith.longitude, lilith.latitude, lilith.retrograde = self.eph.observe(t, 'lilith', location=location)
		selena.distance, selena.longitude, selena.latitude, selena.retrograde = self.eph.observe(t, 'selena', location=location)
		
		# Zodiac
		moon.zodiac, moon.zodiac_symbol, moon.zodiac_orb = zodiac(moon.longitude)
		lunar_asc.zodiac, lunar_asc.zodiac_symbol, lunar_asc.zodiac_orb = zodiac(lunar_asc.longitude)
		lunar_dsc.zodiac, lunar_dsc.zodiac_symbol, lunar_dsc.zodiac_orb = zodiac(lunar_dsc.longitude)
		lilith.zodiac, lilith.zodiac_symbol, lilith.zodiac_orb = zodiac(lilith.longitude)
		selena.zodiac, selena.zodiac_symbol, selena.zodiac_orb = zodiac(selena.longitude)

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
		mercury.distance, mercury.longitude, mercury.latitude, mercury.retrograde = self.eph.observe(t, 'mercury', swe.FLG_HELCTR)
		venus.distance, venus.longitude, venus.latitude, venus.retrograde = self.eph.observe(t, 'venus', swe.FLG_HELCTR)
		earth.distance, earth.longitude, earth.latitude, earth.retrograde = self.eph.observe(t, 'earth', swe.FLG_HELCTR)
		mars.distance, mars.longitude, mars.latitude, mars.retrograde = self.eph.observe(t, 'mars', swe.FLG_HELCTR)
		jupiter.distance, jupiter.longitude, jupiter.latitude, jupiter.retrograde = self.eph.observe(t, 'jupiter', swe.FLG_HELCTR)
		saturn.distance, saturn.longitude, saturn.latitude, saturn.retrograde = self.eph.observe(t, 'saturn', swe.FLG_HELCTR)
		uranus.distance, uranus.longitude, uranus.latitude, uranus.retrograde = self.eph.observe(t, 'uranus', swe.FLG_HELCTR)
		neptune.distance, neptune.longitude, neptune.latitude, neptune.retrograde = self.eph.observe(t, 'neptune', swe.FLG_HELCTR)
		pluto.distance, pluto.longitude, pluto.latitude, pluto.retrograde = self.eph.observe(t, 'pluto', swe.FLG_HELCTR)

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