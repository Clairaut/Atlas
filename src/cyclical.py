def zodiac(lon):
	if lon is None:
		return None, '', None

	zodiacs = [
	(0, 30, 'Aries', '♈', f'{round(lon, 2)}'),
	(30, 60, 'Taurus', '♉', f'{round(lon - 30, 2)}'),
	(60, 90, 'Gemini', '♊', f'{round(lon - 60, 2)}'),
	(90, 120, 'Cancer', '♋', f'{round(lon - 90, 2)}'),
	(120, 150, 'Leo', '♌', f'{round(lon - 120, 2)}'),
	(150, 180, 'Virgo', '♍', f'{round(lon - 150, 2)}'),
	(180, 210, 'Libra', '♎', f'{round(lon - 180, 2)}'),
	(210, 240, 'Scorpio', '♏', f'{round(lon - 210, 2)}'),
	(240, 270, 'Sagittarius', '♐', f'{round(lon - 240, 2)}'),
	(270, 300, 'Capricorn', '♑', f'{round(lon - 270, 2)}'),
	(300, 330, 'Aquarius', '♒', f'{round(lon - 300, 2)}'),
	(330, 360, 'Pisces', '♓', f'{round(lon - 330, 2)}')
	]

	for start, end, sign, symbol, orb in zodiacs:
		if start <= lon < end:
			return sign, symbol, orb

def phase(lon_target, lon_sun, target):
	if lon_target is None or lon_sun is None:
		return None, '', None

	lon_phase = (lon_target - lon_sun) % 360

	phases = [
	(0, 22.5, f'New {target}', '🌑︎'),
	(22.5, 67.5, 'Waxing Crescent', '🌒︎'),
	(67.5, 112.5, 'First Quarter', '🌓︎'),
	(112.5, 157.5, 'Waxing Gibbous', '🌔︎'),
	(157.5, 202.5, f'Full {target}', '🌕︎'),
	(202.5, 247.5, 'Waning Gibbous', '🌖︎'),
	(247.5, 292.5, 'Last Quarter', '🌗︎'),
	(292.5, 337.5, 'Waning Crescent', '🌘︎'),
	(337.5, 360, f'New {target}', '🌑︎')
	]

	for start, end, phase, symbol in phases:
		if start <= lon_phase < end:
			return phase, symbol, round(lon_phase, 2)

