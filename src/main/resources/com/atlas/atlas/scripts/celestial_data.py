from atlas.chrono import utc
from middleware import get_celestial_data, get_placidus_data, process_charts, parse_location
from datetime import datetime
import sys
import json

def main():
    if len(sys.argv) < 7:
        print("Usage: python celestial_data.py <date> <time> <location> <targets> <tropical> <chart_type>")
        sys.exit(1)

    date_str = sys.argv[1]
    time_str = sys.argv[2]
    location_str = sys.argv[3]
    targets_str = sys.argv[4]
    tropical_str = sys.argv[5]
    chart_type = sys.argv[6]

    targets = targets_str.split(',') # List of celestial targets
    tropical = tropical_str.lower() == 'true' # Tropical boolean input
    location = parse_location(location_str) # Parsing location
    
    t = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
    t = utc(t, location) # Converting to UTC

    celestials = get_celestial_data(t, location, targets, tropical)

    if chart_type != 'none':
        placidus = get_placidus_data(t, location, tropical)
        process_charts(celestials, placidus, chart_type)

    json_output = json.dumps([celestial.to_dict() for celestial in celestials.values()])
    print(json_output)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
