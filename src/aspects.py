def aspects(celestials):
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
				aspects.setdefault(body_one, []).append(["Opposition", body_two, opposition_diff])
			elif trine_diff < 10:
				aspects.setdefault(body_one, []).append(["Trine", body_two, trine_diff])
			elif square_diff < 10:
				aspects.setdefault(body_one, []).append(["Square", body_two, square_diff])
			elif sextile_diff < 10:
				aspect.setdefault(body_one, []).append(["Sextile", body_two, sextile_diff])
			elif conjunction_diff < 10:
				aspect.setdefault(body_one, []).append(["Conjunction", body_two, conjunction_diff])

	return aspects

def elements(celestials):
	elements = dict()
	genders = dict()

	for celestial in celestials.values():
		# Fire | Masculine
		if celestial.zodiac in ['Aries', 'Leo','Sagittarius']:
			elements['Fire'] += 1
			genders
