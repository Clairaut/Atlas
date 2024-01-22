def aspect(celestials):
	aspects = dict()

	# Loop through celestials
	for i, body_one in enumerate(celestials.keys()):
		for j, body_two in enumerate(celestials.keys()):
			if i >= j:
				continue # Skips duplicates

			lon_one = celestials[body_one].longitude
			lon_two = celestials[body_two].longitude

			# Difference between ecliptic longitudes
			diff = abs(lon_one - lon_two) % 360
			if diff > 180:
				diff = 360 - diff # Differences past 180° are mirrored

			# Initializing aspect parameters
			opposition_diff = round(abs(diff-180), 2)
			trine_diff = round(abs(diff-120), 2)
			square_diff = round(abs(diff-90), 2)
			sextile_diff = round(abs(diff-60), 2)
			conjunction_diff = round(abs(diff-0), 2)

			# Establishing aspects
			if opposition_diff < 10:
				aspects.setdefault(celestials[body_one], []).append(["Opposition", celestials[body_two], opposition_diff])
			elif trine_diff < 10:
				aspects.setdefault(celestials[body_one], []).append(["Trine", celestials[body_two], trine_diff])
			elif square_diff < 10:
				aspects.setdefault(celestials[body_one], []).append(["Square", celestials[body_two], square_diff])
			elif sextile_diff < 10:
				aspects.setdefault(celestials[body_one], []).append(["Sextile", celestials[body_two], sextile_diff])
			elif conjunction_diff < 10:
				aspects.setdefault(celestials[body_one], []).append(["Conjunction", celestials[body_two], conjunction_diff])

	return aspects

def element(celestials):
	elements = dict()
	genders = dict()

	for celestial in celestials.values():
		# Fire | Masculine
		if celestial.zodiac in ['Aries', 'Leo','Sagittarius']:
			elements['Fire'] += 1
			genders['Male'] += 1
		elif celestial.zodiac in ['Capricorn', 'Virgo', 'Taurus']:
			elements['Earth'] += 1
			genders['Feminine'] += 1
		elif celestial.zodiac in ['Libra', 'Gemini', 'Aquarius']:
			elements['Air'] += 1 
			genders['Masculine'] += 1
		elif celestial.zodiac in ['Cancer', 'Pisces', 'Scorpio']:
			elements['Water'] += 1
			genders['Feminine'] += 1

	return elements, genders

def house(placidus, celestials):
	scope = [
		(placidus['I'].longitude, placidus['II'].longitude, 'I'), # House One - House Two
		(placidus['II'].longitude, placidus['III'].longitude, 'II'), # House Two - House Three
		(placidus['III'].longitude, placidus['IV'].longitude, 'III'), # House Three - House Hour
		(placidus['IV'].longitude, placidus['V'].longitude, 'IV'), # House Four - House Five
		(placidus['V'].longitude, placidus['VI'].longitude, 'V'), # House Five - House Six
		(placidus['VI'].longitude, placidus['VII'].longitude, 'VI'), # House Six - House Seven
		(placidus['VII'].longitude, placidus['VIII'].longitude, 'VII'), # House Seven - House Eight
		(placidus['VIII'].longitude, placidus['IX'].longitude, 'VIII'), # House Eight - House Nine
		(placidus['IX'].longitude, placidus['X'].longitude, 'IX'), # House Nine - House Ten
		(placidus['X'].longitude, placidus['XI'].longitude, 'X'), # House Ten - House Eleven
		(placidus['XI'].longitude, placidus['XII'].longitude, 'XI'), # House Eleven - House Twelve
		(placidus['XII'].longitude, placidus['I'].longitude, 'XII'), # House Twelve - House One
	]

	houses = dict()

	for key, value in celestials.items():
	    longitude = (value.longitude + 360) % 360
	    for lon_one, lon_two, house in scope:
	        if lon_one > lon_two:
	            if lon_one <= longitude or longitude < lon_two: # Handles the wrap-around case
	                houses[key] = house
	        else:
	            if lon_one <= longitude < lon_two:
	                houses[key] = house

	return houses
