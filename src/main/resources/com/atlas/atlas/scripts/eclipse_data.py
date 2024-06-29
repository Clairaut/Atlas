from atlas.chrono import utc
from middleware import get_eclipse_data, parse_location
from datetime import datetime
import sys
import json

def main():
    if len(sys.argv) < 5:
        print("Usage: python eclipse_data.py <date> <time> <location> <solar>")
        sys.exit(1)

    date_str = sys.argv[1]
    time_str = sys.argv[2]
    location_str = sys.argv[3]
    solar_str = sys.argv[4]

    try:
        solar = solar_str.lower() == 'true'
        location = parse_location(location_str)
        
        t = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')
        t = utc(t, location)

        eclipse = get_eclipse_data(t, location, solar)
        
        if eclipse is None:
            print("No eclipse data returned.")
            sys.exit(1)
        
        json_output = json.dumps(eclipse.to_dict())
        print(json_output)
    except Exception as e:
        print(f"Error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
