from atlas.node import Aspect, Node

ORB_LIMIT = 5
ASPECTS = [
    (180, 'Opposition', '☍'),
    (120, 'Trine', '△'),
    (90, 'Square', '□'),
    (60, 'Sextile', '⚹'),
    (0, 'Conjunction', '☌')
]

def find_aspects(celestials):
    aspects = dict()

    # Loop through celestials
    for i, body_one in enumerate(celestials.values()):
        for j, body_two in enumerate(celestials.values()):
            if i >= j:
                continue # Skips duplicates

            lon_one = body_one.longitude
            lon_two = body_two.longitude

            # Difference between ecliptic longitudes
            diff = abs(lon_one - lon_two) % 360
            if diff > 180:
                diff = 360 - diff # Differences past 180° are mirrored

            # Establishing aspects
            for angle, aspect_type, symbol in ASPECTS:
                orb = round(abs(diff - angle), 2)
                if orb < ORB_LIMIT:
                    aspect = Aspect(aspect_type, symbol, body_one, body_two, orb)
                    aspects[f"{body_one.name} {aspect_type} {body_two.name}"] = aspect

    return aspects

def find_lots(placidus, celestials):
    is_day = celestials['Sun'].longitude < placidus['House 1'].longitude

    # Initialize
    fortune = Node('Lot of Fortune', '🝴')
    spirit = Node('Lot of Spirit', 'Φ')
    eros = Node('Lot of Eros', '♡')

    # Location
    if is_day:
        fortune.longitude = (placidus['House 1'].longitude + (celestials['Moon'].longitude - celestials['Sun'].longitude)) % 360
        spirit.longitude = (placidus['House 1'].longitude + (celestials['Sun'].longitude - celestials['Moon'].longitude)) % 360
        eros.longitude = (placidus['House 1'].longitude + (celestials['Venus'].longitude - spirit.longitude)) % 360

    else:
        fortune.longitude = (placidus['House 1'].longitude + (celestials['Sun'].longitude - celestials['Moon'].longitude)) % 360
        spirit.longitude = (placidus['House 1'].longitude + (celestials['Moon'].longitude - celestials['Sun'].longitude)) % 360
        eros.longitude = (placidus['House 1'].longitude + (spirit.longitude - celestials['Venus'].longitude)) % 360
    
    # Zodiac
    fortune.get_zodiac()
    spirit.get_zodiac()
    eros.get_zodiac()

    return {
        'Fortune': fortune,
        'Spirit': spirit,
        'Eros': eros
    }