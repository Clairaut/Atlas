from datetime import datetime
from tabulate import tabulate
import traceback
import os

from atlas.atlas import Atlas
from atlas.topo import Location
from atlas.chrono import utc
from atlas.analysis import find_aspects, find_lots
from atlas.chart import NatalChart
from atlas.objects import Location


class Console:
    def __init__(self):
        self.CELESTIAL_LIST = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto',]
        self.ASTEROID_LIST = ['ceres', 'pallas', 'juno', 'vesta', 'astraea', 'hygiea', 'psyche', 'proserpina', 'eros', 'icarus',]
        self.CENTAUR_LIST = ['chiron', 'pholus', 'nessus',]
        self.NEPTUNIAN_LIST = ['quaoar', 'logos', 'sedna', 'orcus', 'salacia', 'haumea', 'eris', 'makemake', 'gonggong',]
        self.LUNAR_LIST = ['moon', 'rahu', 'lilith', 'selena',]
        self.DEFAULT_LOCATION = Location()
        self.DEFAULT_LOCATION.set_location(51, 0, 0)


    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def datetime_input(self):
        self.clear()
        while True:
            try:
                print("""
====================
| 🗓 Date Input 🗓  |
====================\n
            """)
                input_date = input("Insert date below (YYYY-MM-DD):\n")
                if not input_date:
                    date = datetime.now()
                else:
                    date = datetime.strptime(input_date, "%Y-%m-%d")

                input_time = input("Insert time below (HH:MM):\n")
                if not input_time:
                    time = datetime.now().time()
                else:
                    time = datetime.strptime(input_time, "%H:%M").time()
                dt = datetime.combine(date, time) # Combines date and time

                if input_date == None or input_time == None:
                    ("Error: Date or time not recognized\n")
                    continue

            except Exception as e:
                self.clear()
                print(f"Error: {e}\n")
                continue

            self.clear()
            return dt

    def location_input(self):
        self.clear()
        while True:
            print("""
|=====================|
| 🖈 Location Input 🖈 |
|=====================|\n
                """)

            location_input = input("Enter a location (Ex: 'New Orleans, USA'):\n")
            if not location_input:
                location = self.DEFAULT_LOCATION
                return location

            try:
                location = Location()
                location.locator(location_input)
                self.clear()
                return location
                
            except Exception as e:
                self.clear()
                print(f"Error: {e}")
                traceback.print_exc()
                continue

    def eclipse_input(self):
        self.clear()
        while True:
            print("""
|====================|
| 🝵 Eclipse Input 🝶 |
|====================|\n
                """)
            
            eclipses = [['1', '🝵 Solar'], ['2', '🝶 Lunar']]
            eclipse_tab = tabulate(eclipses)
            print(eclipse_tab + "\n")

            eclipse_input = input("Enter eclipse type:\n")

            if eclipse_input == '1': # True if solar
                return True
            elif eclipse_input.lower() == '2':
                return False # False if lunar
            else:
                self.clear()
                print("Error: Invalid eclipse type. Please try again.")
                continue

    
    def placidus_input(self):
        self.clear()
        while True:
            print("""
|=====================|
| 🜨︎ Placidus Input 🜨︎ |
|=====================|\n
                """)
            
            placidus = [['1', '🌴 Tropical'], ['2', '🛞 Sidereal']]
            placidus_tab = tabulate(placidus)
            print(placidus_tab + "\n")

            placidus_input = input("Enter placidus type:\n")

            if placidus_input == '1': # True if tropical
                return True
            elif placidus_input.lower() == '2': # False if sidereal
                return False
            else:
                self.clear()
                print("Error: Invalid placidus type. Please try again.")
                continue

    def main_menu(self):
        self.clear()
        while True:
            print("""
|====================|
| ☾ Atlas ★ Wizard ☽ |
|====================|\n
					""")
            
            menu = [
            ['1', "🜨︎ Horoscope"],
            ['2', "🝵 Occultation"],
            ['0', "≡ Exit"],
            ]

            menu_tab = tabulate(menu)
            print(menu_tab)

            # User Input
            choices = ['0', '1', '2']
            choice = input("\n Choose Ephemeris:\n")
            if choice in choice:
                self.clear()
                return choice
            else:
                print("Invalid choice. Please try again.")
                continue
    
    def horoscope_menu(self):
        while True:
            print("""
|================|
| 🜨︎ Horoscope 🜨︎ |
|================|
                """)

            menu = [
            ['1', "⌂  Placidus"],
            ['2', "☉  Major Bodies"],
            ['3', "☄  Minor Bodies"],
            ['4', "☾  Lunar"],
            ['5', "🝴  Lots"],
            ['6', "☌  Aspects"],
            ['7', "🖉  Chart"],
            ['0', "≡  Main Menu"],
            ]

            menu_tab = tabulate(menu)
            print(menu_tab)

            choices = ['0', '1', '2','3', '4', '5', '6', '7']
            choice = input("\nChoose ephemeris:\n")
            if choice in choices:
                return choice
            else:
                self.clear()
                print("Error: Invalid Input")
                continue

    def eclipse_menu(self):
        while True:
            print("""
|=========================|
| 🝵 Eclipse Ephemeris 🝶  |
|=========================|
            """)

            menu = [
            ['1', "🝵 General"],
            ['2', "🌕︎ Phases"],
            ['0', "≡ Main Menu"]
            ]

            menu_tab = tabulate(menu)
            print(menu_tab)

            choices = ['0', '1', '2']
            choice = input("\nChoose eclipse:\n")
            if choice in choices:
                return choice
            else:
                self.clear()
                print("Error: Invalid choice. Please try again.")
                continue

    def main_portal(self, choice_main): # Main Portal
        portal = {
            1: self.horoscope,
            2: self.eclipse,
            0: lambda: 'exit',
        }

        if choice_main != None:
            choice_main = int(choice_main)
        if choice_main in portal:
            return portal[choice_main]()
        
    def horoscope_portal(self, choice_info, celestial_data): # Ephemeris Portal
        self.clear()
        portal = { 
            1: self.placidus_data,
            2: self.major_body_data,
            3: self.minor_body_data,
            4: self.lunar_data,
            5: self.lot_data,
            6: self.aspect_data,
            7: lambda _: 'chart',
            0: lambda _: 'exit',
        }

        if choice_info != None:
            choice_info = int(choice_info)
        if choice_info in portal:
            return portal[choice_info](celestial_data)
        
    def eclipse_portal(self, choice_info, eclipse_data): # Eclipse Portal
        self.clear()
        portal = {
            1: self.eclipse_general_data,
            2: self.phase_phase_data,
            0: lambda _: 'exit',
        }

        if choice_info != None:
            choice_info = int(choice_info)
        if choice_info in portal:
            return portal[choice_info](eclipse_data)

    def generate_celestial_data(self, t, location, tropical): # Generate Data

        atlas = Atlas() # Initializing Atlas
        placidus = atlas.create_placidus(t, location, tropical) # Intializing Placidus
        celestials = atlas.create_celestials(t, location, self.CELESTIAL_LIST, tropical) # Initializing Celestials
        asteroids = atlas.create_celestials(t, location, self.ASTEROID_LIST, tropical) # Initializing Asteroids
        centaurs = atlas.create_celestials(t, location, self.CENTAUR_LIST, tropical) # Initializing Centaurs
        neptunians = atlas.create_celestials(t, location, self.NEPTUNIAN_LIST, tropical) # Initializing Neptunians
        lunars = atlas.create_celestials(t, location, self.LUNAR_LIST, tropical) # Initializing Lunars
        aspects = find_aspects({**celestials, **lunars}) # Aspects
        lots = find_lots(placidus, celestials)

        celestial_data = {
            'Placidus': placidus,
            'Celestial': celestials,
            'Asteroid': asteroids,
            'Centaur': centaurs,
            'Neptunian': neptunians,
            'Lunar': lunars,
            'Aspect': aspects,
            'Lot': lots,
        }

        return celestial_data
    
    def generate_eclipse_data(self, t, location, solar): # Generate Eclipse Data
        atlas = Atlas()

        if solar == True:
            eclipse = atlas.create_solar_eclipse(t, location)
        else:
            eclipse = atlas.create_lunar_eclipse(t, location)

        return eclipse

    def horoscope(self): # Ephemeris
        tropical = self.placidus_input()
        t_i = self.datetime_input()
        location = self.location_input()
        
        t = utc(t_i, location)
        celestial_data = self.generate_celestial_data(t, location, tropical)

        self.clear()
        while True:
            choice_info = self.horoscope_menu()
            portal = self.horoscope_portal(choice_info, celestial_data)
            if portal == 'chart':
                self.clear()
                chart = NatalChart(celestial_data['Placidus'], {**celestial_data['Celestial'], **celestial_data['Lunar']})
                chart.generate(show=True, save=False)
                continue
            elif portal == 'exit':
                break

    def eclipse(self): # Eclipse
        solar = self.eclipse_input()
        t_i = self.datetime_input()
        location = self.location_input()
        t = utc(t_i, location)
        eclipse_data = self.generate_eclipse_data(t, location, solar)

        self.clear()
        while True:
            choice_info = self.eclipse_menu()
            portal = self.eclipse_portal(choice_info, eclipse_data)
            if portal == 'exit':
                break

    def placidus_data(self, celestial_data): # Placidus Data
        placidus = [[f"{house.symbol} {house.name}", f"{house.zodiac_symbol} {house.zodiac}", f"{house.zodiac_orb}°"] for house in celestial_data['Placidus'].values()]

        placidus_tab = tabulate(placidus, headers=['House', 'Zodiac', 'Orb'])
        print(placidus_tab)

    def major_body_data(self, celestial_data): # Celestial Data
        celestials = [[f"{celestial.symbol} {celestial.name}", f"{celestial.zodiac_symbol} {celestial.zodiac}", f"{celestial.zodiac_orb}°", f"℞" if celestial.retrograde else ''] for celestial in celestial_data['Celestial'].values()]

        celestials_tab = tabulate(celestials, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
        print(celestials_tab)

    def minor_body_data(self, celestial_data): # Asteroid Data
        asteroids = [[f"{asteroid.symbol} {asteroid.name}", f"{asteroid.zodiac_symbol} {asteroid.zodiac}", f"{asteroid.zodiac_orb}°", f"℞" if asteroid.retrograde else ''] for asteroid in celestial_data['Asteroid'].values()]
        centaurs = [[f"{centaur.symbol} {centaur.name}", f"{centaur.zodiac_symbol} {centaur.zodiac}", f"{centaur.zodiac_orb}°", f"℞" if centaur.retrograde else ''] for centaur in celestial_data['Centaur'].values()]
        neptunians = [[f"{neptunian.symbol} {neptunian.name}", f"{neptunian.zodiac_symbol} {neptunian.zodiac}", f"{neptunian.zodiac_orb}°", f"℞" if neptunian.retrograde else ''] for neptunian in celestial_data['Neptunian'].values()]
        
        asteroids_tab = tabulate(asteroids, headers=['Asteroid', 'Zodiac', 'Orb', 'Retrograde'])
        centaurs_tab = tabulate(centaurs, headers=['Centaur', 'Zodiac', 'Orb', 'Retrograde'])
        neptunians_tab = tabulate(neptunians, headers=['Neptunian', 'Zodiac', 'Orb', 'Retrograde'])
        
        print(neptunians_tab + "\n" + "\n" + centaurs_tab + "\n" + "\n" + asteroids_tab)

    def lunar_data(self, celestial_data): # Lunar Data
        moon = celestial_data['Celestial']['Moon']
        phase = [[f"{moon.symbol} {moon.name}", f"{moon.phase_symbol} {moon.phase}", f"{moon.phase_angle}°"]]
        nodes = [[f"{lunar.symbol} {lunar.name}", f"{lunar.zodiac_symbol} {lunar.zodiac}", f"{lunar.zodiac_orb}°", f"℞" if lunar.retrograde else ''] for lunar in celestial_data['Lunar'].values()]

        phase_tab = tabulate(phase, headers=['Celestial', 'Phase', 'Phase Angle'])
        node_tab = tabulate(nodes, headers=['Node', 'Zodiac', 'Orb', 'Retrograde'])
        print(phase_tab + "\n" + "\n" + node_tab)

    def aspect_data(self, celestial_data): # Aspect Data
        aspects = []

        for aspect in celestial_data['Aspect'].values():
            aspects.append([f"{aspect.body_one.symbol} {aspect.body_one.name}", f"{aspect.symbol} {aspect.name}", f"{aspect.body_two.symbol} {aspect.body_two.name}", f"{aspect.orb}°"])
        
        aspects_tab = tabulate(aspects, headers=['Body', 'Aspect', 'Body', 'Orb'])
        print(aspects_tab)

    def lot_data(self, celestial_data): # Lot Data
        lots = [[f"{lot.symbol} {lot.name}", f"{lot.zodiac_symbol} {lot.zodiac}", f"{lot.zodiac_orb}°"] for lot in celestial_data['Lot'].values()]

        lots_tab = tabulate(lots, headers=['Lot', 'Zodiac', 'Orb'])
        print(lots_tab)

    def eclipse_general_data(self, eclipse_data): # Eclipse General Data
        eclipse = [[f"Type", f"{eclipse_data.type}"], [f"Magnitude", f"{round(eclipse_data.magnitude, 3)}"], [f"Obscuration", f"{round(eclipse_data.obscuration, 3)}"], [f"Gamma", f"{round(eclipse_data.gamma, 3)}"]]
        eclipse_tab = tabulate(eclipse)
        print(eclipse_tab)

    def phase_phase_data(self, eclipse_data): # Eclipse Phase Data
        if eclipse_data.celestial == 'Solar':
            phases = [["First Contact", f"{eclipse_data.t_c1.month}/{eclipse_data.t_c1.day}/{eclipse_data.t_c1.year}" if eclipse_data.t_c1 else 'N/A', f"{eclipse_data.t_c1.hour}:{eclipse_data.t_c1.minute}" if eclipse_data.t_c1 else 'N/A'], 
                    ["Second Contact", f"{eclipse_data.t_c2.month}/{eclipse_data.t_c2.day}/{eclipse_data.t_c2.year}" if eclipse_data.t_c2 else 'N/A', f"{eclipse_data.t_c2.hour}:{eclipse_data.t_c2.minute}" if eclipse_data.t_c2 else 'N/A'], 
                    ["Maximum", f"{eclipse_data.t_max.month}/{eclipse_data.t_max.day}/{eclipse_data.t_max.year}" if eclipse_data.t_max else 'N/A', f"{eclipse_data.t_max.hour}:{eclipse_data.t_max.minute}" if eclipse_data.t_max else 'N/A'], 
                    ["Third Contact", f"{eclipse_data.t_c3.month}/{eclipse_data.t_c3.day}/{eclipse_data.t_c3.year}" if eclipse_data.t_c3 else 'N/A', f"{eclipse_data.t_c3.hour}:{eclipse_data.t_c3.minute}" if eclipse_data.t_c3 else 'N/A'], 
                    ["Fourth Contact", f"{eclipse_data.t_c4.month}/{eclipse_data.t_c4.day}/{eclipse_data.t_c4.year}" if eclipse_data.t_c4 else 'N/A', f"{eclipse_data.t_c4.hour}:{eclipse_data.t_c4.minute}" if eclipse_data.t_c4 else 'N/A']]
        else:
            phases = [["First Contact",  f"{eclipse_data.t_p1.month}/{eclipse_data.t_p1.day}/{eclipse_data.t_p1.year}" if eclipse_data.t_p1 else 'N/A', f"{eclipse_data.t_p1.hour}:{eclipse_data.t_p1.minute}" if eclipse_data.t_p1 else 'N/A'], 
                    ["Second Contact", f"{eclipse_data.t_u1.month}/{eclipse_data.t_u1.day}/{eclipse_data.t_u1.year}" if eclipse_data.t_u1 else 'N/A', f"{eclipse_data.t_u1.hour}:{eclipse_data.t_u1.minute}" if eclipse_data.t_u1 else 'N/A'],
                    ["Third Contact", f"{eclipse_data.t_u2.month}/{eclipse_data.t_u2.day}/{eclipse_data.t_u2.year}" if eclipse_data.t_u2 else 'N/A', f"{eclipse_data.t_u2.hour}:{eclipse_data.t_u2.minute}" if eclipse_data.t_u2 else 'N/A'], 
                    ["Maximum", f"{eclipse_data.t_max.month}/{eclipse_data.t_max.day}/{eclipse_data.t_max.year}" if eclipse_data.t_max else 'N/A', f"{eclipse_data.t_max.hour}:{eclipse_data.t_max.minute}" if eclipse_data.t_max else 'N/A'], 
                    ["Fourth Contact", f"{eclipse_data.t_u3.month}/{eclipse_data.t_u3.day}/{eclipse_data.t_u3.year}" if eclipse_data.t_u3 else 'N/A', f"{eclipse_data.t_u3.hour}:{eclipse_data.t_u3.minute}" if eclipse_data.t_u3 else 'N/A'],
                    ["Fifth Contact", f"{eclipse_data.t_u4.month}/{eclipse_data.t_u4.day}/{eclipse_data.t_u4.year}" if eclipse_data.t_u4 else 'N/A', f"{eclipse_data.t_u4.hour}:{eclipse_data.t_u4.minute}" if eclipse_data.t_u4 else 'N/A'],
                    ["Sixth Contact", f"{eclipse_data.t_p2.month}/{eclipse_data.t_p2.day}/{eclipse_data.t_p2.year}" if eclipse_data.t_p2 else 'N/A', f"{eclipse_data.t_p2.hour}:{eclipse_data.t_p2.minute}" if eclipse_data.t_p2 else 'N/A'],]

        phases_tab = tabulate(phases, headers=['Phase', 'Date', 'Time'])
        print(phases_tab)
    
    def start(self): # Run
        while True:
            choice_main = self.main_menu()
            main_portal = self.main_portal(choice_main)
            if main_portal == 'exit':
                break

if __name__ == '__main__':
    console = Console()
    console.run()