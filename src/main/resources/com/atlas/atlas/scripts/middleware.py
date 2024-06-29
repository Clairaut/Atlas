from atlas.atlas import Atlas
from atlas.topo import Location
from atlas.chrono import utc
from atlas.chart import CelestialChart
from multiprocessing import Pool
import os
import time

atlas = Atlas()
DIR = f'{os.getcwd()}/src/main/resources/com/atlas/atlas/charts/temp/'

def delete_old_charts(): # Delete old temporary charts
    for filename in os.listdir(DIR):
        if filename.endswith(".png") or filename.endswith(".done"):
            file_path = os.path.join(DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {str(e)}")

def process_charts(celestials, placidus, chart_type): # Process celestial charts using multiprocessing
    delete_old_charts()
    generate_chart_dir()
    
    if chart_type == 'individual':
        with Pool(5) as pool:
            args = [(celestial, placidus, celestial.name) for celestial in celestials.values()]
            pool.starmap(generate_celestial_chart, args)
        chart_validation(celestials.keys()) # Validate that all charts have been generated
    
    elif chart_type == 'combined':
        chart_name = '_'.join([celestial.name for celestial in celestials.values()]) # Combined chart name
        generate_celestial_chart(list(celestials.values()), placidus, chart_name)
        chart_validation([chart_name]) # Validate that the combined chart has been generated

def generate_chart_dir(): # Generate chart directory
    if not os.path.exists(DIR): # Create directory if it doesn't exist
        os.makedirs(DIR)

def generate_celestial_chart(celestials, placidus, chart_name): # Generate celestial chart
    try:
        chart = CelestialChart(placidus, celestials, dir=DIR)
        chart.generate(show=False, save=True)

        # Create .done file to indicate that the chart has been generated
        with open(os.path.join(DIR, f"{chart_name}.done"), 'w') as f:
            f.write('done')
    except Exception as e:
        print(f"Error generating chart for {chart_name}: {str(e)}")

def chart_validation(chart_names, timeout=10): # Validating that charts have been generated
    start_time = time.time()
    while True:
        all_done = all(os.path.exists(os.path.join(DIR, f"{name}.done")) for name in chart_names)
        if all_done:
            break
        if time.time() - start_time > timeout:
            raise TimeoutError("Timeout waiting for chart generation to complete")
        time.sleep(1)  # Check every second

def get_celestial_data(t, location, targets, tropical): # Retrieving celestial ephemeris data
    celestials = atlas.create_celestials(t, location, targets, tropical)
    return celestials

def get_placidus_data(t, location, tropical):
    placidus = atlas.create_placidus(t, location, tropical)
    return placidus

def get_eclipse_data(t, location, solar=True):
    if solar:
        eclipse = atlas.create_solar_eclipse(t, location)
    else:
        eclipse = atlas.create_lunar_eclipse(t, location)

    return eclipse.to_dict()

def parse_location(location_str):
    if ',' in location_str and '(' in location_str and ')' in location_str:
        location_str = location_str.strip('(').strip(')')
        longitude, latitude = location_str.split(',')
        return Location(float(longitude), float(latitude))
    else:
        city = location_str
        location = Location()
        location.locator(city)
        return location
