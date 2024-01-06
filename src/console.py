from atlas import Atlas
from aspects import aspect, house
from topo import locator, utc
from datetime import datetime
from tabulate import tabulate
import traceback
import os


class AtlasWizardConsole:
	def __init__(self):
		self.atlas = Atlas()
		self.aspect_symbols = {'Opposition': '☍ Opposition', 'Trine': '△ Trine', 'Square': '□ Square', 'Sextile': '⚹ Sextile', 'Conjunction': '☌ Conjunction'}

	def clear(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def main(self):
		self.clear()
		while True:
			print("""
|====================|
| ☾ Atlas ★ Wizard ☽ |
|====================|\n
					""")

			menu = [
			['1', "⏲ Today's Ephemeris"],
			['2', "🗓 Ephemeris"],
			['3', "≡ Exit"],
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			# User Input
			choices = ['1', '2', '3']
			choice = input("\n Choose menu option:\n")
			if choice in choices:
				self.clear()
				return choice
				break
			else:
				print("Error: Invalid Input")

	def dt(self):
		while True:
			try:
				print("""
====================
| 🗓 Date Input 🗓  |
====================\n
			""")
				input_date = input("Insert date below (YYYY-MM-DD):\n")
				date = datetime.strptime(input_date, "%Y-%m-%d")
				input_time = input("Insert time below (HH:MM):\n")
				time = datetime.strptime(input_time, "%H:%M").time()
				dt = datetime.combine(date, time) # Combines date and time

				if input_date == None or input_time == None:
					("Error: Date or time not recognized\n")
					continue

			except Exception as e:
				self.clear()
				print("Error: Date or time not recognized\n")
				continue

			self.clear()
			return dt

	def location(self):
		self.clear()
		while True:
			print("""
|===============|
| 🖈 Location 🖈 |
|===============|\n
				""")

			choice = input("Enter a location (Ex: 'New Orleans, USA'):\n")
			if choice:
				try:
					location = locator(choice)
					self.clear()
					return location
					break
					
				except Exception as e:
					print(f"Error: {e}")
					traceback.print_exc()
					continue

	def info(self):
		while True:
			print("""
|=================|
| 🪐 Ephemeris 🪐 |
|=================|
				""")

			menu = [
			['1', "⌂  Placidus"],
			['2', "☉  Celestial Bodies"],
			['3', "☄️ Asteroid Belt"],
			['4', "⚷  Centaur"],
			['5', "🪐 Trans-Neptunian"],
			['6', "☽  Lunar"],
			['7', "★ Aspects"],
			['0', "≡  Main Menu"],
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			choices = ['0', '1', '2', '3', '4', '5', '6', '7']
			choice = input("\nChoose ephemeris:\n")
			if choice in choices:
				return choice
				break
			else:
				self.clear()
				print("Error: Invalid Input")
				continue

	def placidus(self, atlas_data):
		placidus = [
		["🜨︎ I", f"{atlas_data['Placidus']['I'].symbol} {atlas_data['Placidus']['I'].zodiac}", f"{atlas_data['Placidus']['I'].zodiac_orb}°"],
		["⌂ II", f"{atlas_data['Placidus']['II'].symbol} {atlas_data['Placidus']['II'].zodiac}", f"{atlas_data['Placidus']['II'].zodiac_orb}°"],
		["⌂ III", f"{atlas_data['Placidus']['III'].symbol} {atlas_data['Placidus']['III'].zodiac}", f"{atlas_data['Placidus']['III'].zodiac_orb}°"],
		["🜨︎ IV", f"{atlas_data['Placidus']['IV'].symbol} {atlas_data['Placidus']['IV'].zodiac}", f"{atlas_data['Placidus']['IV'].zodiac_orb}°"],
		["⌂ V", f"{atlas_data['Placidus']['V'].symbol} {atlas_data['Placidus']['V'].zodiac}", f"{atlas_data['Placidus']['V'].zodiac_orb}°"],
		["⌂ VI", f"{atlas_data['Placidus']['VI'].symbol} {atlas_data['Placidus']['VI'].zodiac}", f"{atlas_data['Placidus']['VI'].zodiac_orb}°"],
		["🜨︎ VII", f"{atlas_data['Placidus']['VII'].symbol} {atlas_data['Placidus']['VII'].zodiac}", f"{atlas_data['Placidus']['VII'].zodiac_orb}°"],
		["⌂ VIII", f"{atlas_data['Placidus']['VIII'].symbol} {atlas_data['Placidus']['VIII'].zodiac}", f"{atlas_data['Placidus']['VIII'].zodiac_orb}°"],
		["⌂ IX", f"{atlas_data['Placidus']['IX'].symbol} {atlas_data['Placidus']['IX'].zodiac}", f"{atlas_data['Placidus']['IX'].zodiac_orb}°"],
		["🜨︎ X", f"{atlas_data['Placidus']['X'].symbol} {atlas_data['Placidus']['X'].zodiac}", f"{atlas_data['Placidus']['X'].zodiac_orb}°"],
		["⌂ XI", f"{atlas_data['Placidus']['XI'].symbol} {atlas_data['Placidus']['XI'].zodiac}", f"{atlas_data['Placidus']['XI'].zodiac_orb}°"],
		["⌂ XII", f"{atlas_data['Placidus']['XII'].symbol} {atlas_data['Placidus']['XII'].zodiac}", f"{atlas_data['Placidus']['XII'].zodiac_orb}°"],
		]

		celestial = [
		["☉ Sun", f"{atlas_data['House']['Sun']}"],
		["☽ Moon", f"{atlas_data['House']['Moon']}"],
		["☿ Mercury", f"{atlas_data['House']['Mercury']}"],
		["♀ Venus", f"{atlas_data['House']['Venus']}"],
		["♂ Mars", f"{atlas_data['House']['Mars']}"],
		["♃ Jupiter", f"{atlas_data['House']['Jupiter']}"],
		["♄ Saturn", f"{atlas_data['House']['Saturn']}"],
		["♅ Uranus", f"{atlas_data['House']['Uranus']}"],
		["♆ Neptune", f"{atlas_data['House']['Neptune']}"],
		["⯓ Pluto", f"{atlas_data['House']['Pluto']}"],
		["⚸ Lilith", f"{atlas_data['House']['Lilith']}"],
		["⯝ Selena", f"{atlas_data['House']['Selena']}"],
		["☊ Lunar ASC", f"{atlas_data['House']['ASC']}"],
		["☋ Lunar DSC", f"{atlas_data['House']['DSC']}"],
		]

		placidus_tab = tabulate(placidus, headers=['House', 'Zodiac', 'Orb'])
		celestial_tab = tabulate(celestial, headers=['Celestial Body', 'House'])
		print(placidus_tab + "\n")
		print(celestial_tab)

	def celestial(self, atlas_data):
		celestial = [
		["☉ Sun", f"{atlas_data['Celestial']['Sun'].zodiac_symbol} {atlas_data['Celestial']['Sun'].zodiac}", f"{atlas_data['Celestial']['Sun'].zodiac_orb}°", f"{atlas_data['Celestial']['Sun'].retrograde}"],
		["☽ Moon", f"{atlas_data['Celestial']['Moon'].zodiac_symbol} {atlas_data['Celestial']['Moon'].zodiac}", f"{atlas_data['Celestial']['Moon'].zodiac_orb}°", f"{atlas_data['Celestial']['Moon'].retrograde}"],
		["☿ Mercury", f"{atlas_data['Celestial']['Mercury'].zodiac_symbol} {atlas_data['Celestial']['Mercury'].zodiac}", f"{atlas_data['Celestial']['Mercury'].zodiac_orb}°", f"{atlas_data['Celestial']['Mercury'].retrograde}"],
		["♀ Venus", f"{atlas_data['Celestial']['Venus'].zodiac_symbol} {atlas_data['Celestial']['Venus'].zodiac}", f"{atlas_data['Celestial']['Venus'].zodiac_orb}°", f"{atlas_data['Celestial']['Venus'].retrograde}"],
		["♂ Mars", f"{atlas_data['Celestial']['Mars'].zodiac_symbol} {atlas_data['Celestial']['Mars'].zodiac}", f"{atlas_data['Celestial']['Mars'].zodiac_orb}°", f"{atlas_data['Celestial']['Mars'].retrograde}"],
		["♃ Jupiter", f"{atlas_data['Celestial']['Jupiter'].zodiac_symbol} {atlas_data['Celestial']['Jupiter'].zodiac}", f"{atlas_data['Celestial']['Jupiter'].zodiac_orb}°", f"{atlas_data['Celestial']['Jupiter'].retrograde}"],
		["♄ Saturn", f"{atlas_data['Celestial']['Saturn'].zodiac_symbol} {atlas_data['Celestial']['Saturn'].zodiac}", f"{atlas_data['Celestial']['Saturn'].zodiac_orb}°", f"{atlas_data['Celestial']['Saturn'].retrograde}"],
		["♅ Uranus", f"{atlas_data['Celestial']['Uranus'].zodiac_symbol} {atlas_data['Celestial']['Uranus'].zodiac}", f"{atlas_data['Celestial']['Uranus'].zodiac_orb}°", f"{atlas_data['Celestial']['Uranus'].retrograde}"],
		["♆ Neptune", f"{atlas_data['Celestial']['Neptune'].zodiac_symbol} {atlas_data['Celestial']['Neptune'].zodiac}", f"{atlas_data['Celestial']['Neptune'].zodiac_orb}°", f"{atlas_data['Celestial']['Neptune'].retrograde}"],
		["⯓ Pluto", f"{atlas_data['Celestial']['Pluto'].zodiac_symbol} {atlas_data['Celestial']['Pluto'].zodiac}", f"{atlas_data['Celestial']['Pluto'].zodiac_orb}°", f"{atlas_data['Celestial']['Pluto'].retrograde}"],
		]

		celestial_tab = tabulate(celestial, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(celestial_tab)

	def asteroid(self, atlas_data):
		asteroid =[
		["⚳ Ceres", f"{atlas_data['Asteroid']['Ceres'].zodiac_symbol} {atlas_data['Asteroid']['Ceres'].zodiac}", f"{atlas_data['Asteroid']['Ceres'].zodiac_orb}°", f"{atlas_data['Asteroid']['Ceres'].retrograde}"],
		["⚴ Pallas", f"{atlas_data['Asteroid']['Pallas'].zodiac_symbol} {atlas_data['Asteroid']['Pallas'].zodiac}", f"{atlas_data['Asteroid']['Pallas'].zodiac_orb}°", f"{atlas_data['Asteroid']['Pallas'].retrograde}"],
		["⚵ Juno", f"{atlas_data['Asteroid']['Juno'].zodiac_symbol} {atlas_data['Asteroid']['Juno'].zodiac}", f"{atlas_data['Asteroid']['Juno'].zodiac_orb}°", f"{atlas_data['Asteroid']['Juno'].retrograde}"],
		["⚶ Vesta", f"{atlas_data['Asteroid']['Vesta'].zodiac_symbol} {atlas_data['Asteroid']['Vesta'].zodiac}", f"{atlas_data['Asteroid']['Vesta'].zodiac_orb}°", f"{atlas_data['Asteroid']['Vesta'].retrograde}"],
		["⯙ Astraea", f"{atlas_data['Asteroid']['Astraea'].zodiac_symbol} {atlas_data['Asteroid']['Astraea'].zodiac}", f"{atlas_data['Asteroid']['Astraea'].zodiac_orb}°", f"{atlas_data['Asteroid']['Astraea'].retrograde}"],
		["⯚ Hygiea", f"{atlas_data['Asteroid']['Hygiea'].zodiac_symbol} {atlas_data['Asteroid']['Hygiea'].zodiac}", f"{atlas_data['Asteroid']['Hygiea'].zodiac_orb}°", f"{atlas_data['Asteroid']['Hygiea'].retrograde}"],
		["Ψ Psyche", f"{atlas_data['Asteroid']['Psyche'].zodiac_symbol} {atlas_data['Asteroid']['Psyche'].zodiac}", f"{atlas_data['Asteroid']['Psyche'].zodiac_orb}°", f"{atlas_data['Asteroid']['Hygiea'].retrograde}"],
		["⯘ Proserpina", f"{atlas_data['Asteroid']['Proserpina'].zodiac_symbol} {atlas_data['Asteroid']['Proserpina'].zodiac}", f"{atlas_data['Asteroid']['Proserpina'].zodiac_orb}°", f"{atlas_data['Asteroid']['Hygiea'].retrograde}"],
		["➳ Eros", f"{atlas_data['Asteroid']['Eros'].zodiac_symbol} {atlas_data['Asteroid']['Eros'].zodiac}", f"{atlas_data['Asteroid']['Eros'].zodiac_orb}°", f"{atlas_data['Asteroid']['Hygiea'].retrograde}"],
		]

		asteroid_tab = tabulate(asteroid, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(asteroid_tab)

	def centaur(self, atlas_data):
		centaur = [
		["⚷ Chiron", f"{atlas_data['Centaur']['Chiron'].zodiac_symbol} {atlas_data['Centaur']['Chiron'].zodiac}", f"{atlas_data['Centaur']['Chiron'].zodiac_orb}°", f"{atlas_data['Centaur']['Chiron'].retrograde}"],
		["⯛ Pholus", f"{atlas_data['Centaur']['Pholus'].zodiac_symbol} {atlas_data['Centaur']['Pholus'].zodiac}", f"{atlas_data['Centaur']['Pholus'].zodiac_orb}°", f"{atlas_data['Centaur']['Pholus'].retrograde}"],
		["⯜ Nessus", f"{atlas_data['Centaur']['Nessus'].zodiac_symbol} {atlas_data['Centaur']['Nessus'].zodiac}", f"{atlas_data['Centaur']['Nessus'].zodiac_orb}°", f"{atlas_data['Centaur']['Nessus'].retrograde}"],
		]

		centaur_tab = tabulate(centaur, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(centaur_tab)

	def neptunian(self, atlas_data):
		neptunian = [
		["✧ Quaoar", f"{atlas_data['Neptunian']['Quaoar'].zodiac_symbol} {atlas_data['Neptunian']['Quaoar'].zodiac}", f"{atlas_data['Neptunian']['Quaoar'].zodiac_orb}°", f"{atlas_data['Neptunian']['Quaoar'].retrograde}"],
		["† Logos & Zoe", f"{atlas_data['Neptunian']['Logos'].zodiac_symbol} {atlas_data['Neptunian']['Logos'].zodiac}", f"{atlas_data['Neptunian']['Logos'].zodiac_orb}°", f"{atlas_data['Neptunian']['Logos'].retrograde}"],
		["⯲ Sedna", f"{atlas_data['Neptunian']['Sedna'].zodiac_symbol} {atlas_data['Neptunian']['Sedna'].zodiac}", f"{atlas_data['Neptunian']['Sedna'].zodiac_orb}°", f"{atlas_data['Neptunian']['Sedna'].retrograde}"],
		["🗝 Orcus", f"{atlas_data['Neptunian']['Orcus'].zodiac_symbol} {atlas_data['Neptunian']['Orcus'].zodiac}", f"{atlas_data['Neptunian']['Orcus'].zodiac_orb}°", f"{atlas_data['Neptunian']['Orcus'].retrograde}"],
		["∿ Salacia", f"{atlas_data['Neptunian']['Salacia'].zodiac_symbol} {atlas_data['Neptunian']['Salacia'].zodiac}", f"{atlas_data['Neptunian']['Salacia'].zodiac_orb}°", f"{atlas_data['Neptunian']['Salacia'].retrograde}"],
		["୭ Haumea", f"{atlas_data['Neptunian']['Haumea'].zodiac_symbol} {atlas_data['Neptunian']['Haumea'].zodiac}", f"{atlas_data['Neptunian']['Haumea'].zodiac_orb}°", f"{atlas_data['Neptunian']['Haumea'].retrograde}"],
		["⯱ Eris", f"{atlas_data['Neptunian']['Eris'].zodiac_symbol} {atlas_data['Neptunian']['Eris'].zodiac}", f"{atlas_data['Neptunian']['Eris'].zodiac_orb}°", f"{atlas_data['Neptunian']['Eris'].retrograde}"],
		["𓆇 Makemake", f"{atlas_data['Neptunian']['Makemake'].zodiac_symbol} {atlas_data['Neptunian']['Makemake'].zodiac}", f"{atlas_data['Neptunian']['Makemake'].zodiac_orb}°", f"{atlas_data['Neptunian']['Makemake'].retrograde}"],
		["༄ Gonggong", f"{atlas_data['Neptunian']['Gonggong'].zodiac_symbol} {atlas_data['Neptunian']['Gonggong'].zodiac}", f"{atlas_data['Neptunian']['Gonggong'].zodiac_orb}°", f"{atlas_data['Neptunian']['Gonggong'].retrograde}"],
		]

		neptunian_tab = tabulate(neptunian, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(neptunian_tab)

	def lunar(self, atlas_data):
		phase = [
		["☽ Lunar Phase", f"{atlas_data['Lunar']['Moon'].phase_symbol} {atlas_data['Lunar']['Moon'].phase}", f"{atlas_data['Lunar']['Moon'].phase_longitude}°"],
		]
		
		node = [
		["☊ Rahu", f"{atlas_data['Lunar']['ASC'].zodiac_symbol} {atlas_data['Lunar']['ASC'].zodiac}", f"{atlas_data['Lunar']['ASC'].zodiac_orb}°"],
		["☋ Ketu", f"{atlas_data['Lunar']['DSC'].zodiac_symbol} {atlas_data['Lunar']['DSC'].zodiac}", f"{atlas_data['Lunar']['DSC'].zodiac_orb}°"],
		["⚸ Lilith", f"{atlas_data['Lunar']['Lilith'].zodiac_symbol} {atlas_data['Lunar']['Lilith'].zodiac}", f"{atlas_data['Lunar']['Lilith'].zodiac_orb}°"],
		["⯝ Selena", f"{atlas_data['Lunar']['Selena'].zodiac_symbol} {atlas_data['Lunar']['Selena'].zodiac}", f"{atlas_data['Lunar']['Selena'].zodiac_orb}°"],
		]

		phase_tab = tabulate(phase, headers=['Moon', 'Phase', 'Phase Angle'])
		node_tab = tabulate(node, headers=['Node', 'Zodiac', 'Orb'])
		print(phase_tab + "\n\n" + node_tab)

	def aspect(self, atlas_data):
		output = []

		for body, aspects in atlas_data['Aspect'].items():
			for aspect in aspects:
				if aspect[0] in self.aspect_symbols.keys():
					aspect[0] = self.aspect_symbols[aspect[0]]
				output.append([f"{body.symbol} {body.name}", f"{aspect[0]}", f"{aspect[1].symbol} {aspect[1].name}", f"{aspect[2]}°"])

		output_tab = tabulate(output, headers=['Object', 'Aspect', 'Object', 'Orb'])
		print(output_tab)

	def portal(self, choice_info, atlas_data):
		self.clear()
		portal = {
		1: self.placidus,
		2: self.celestial,
		3: self.asteroid,
		4: self.centaur,
		5: self.neptunian,
		6: self.lunar,
		7: self.aspect,
		0: lambda _: 'exit'
		}

		if choice_info != None:
			choice_info = int(choice_info)
		if choice_info in portal:
			return portal[choice_info](atlas_data)

	def generate(self, t, location): # Generating Ephemeris
		placidus = self.atlas.placidus(t, location)
		celestial = self.atlas.celestial(t, location)
		asteroid = self.atlas.asteroid(t, location)
		centaur = self.atlas.centaur(t, location)
		neptunian = self.atlas.neptunian(t, location)
		lunar = self.atlas.lunar(t, location)
		aspects = aspect({**celestial, **lunar})
		houses = house(placidus, {**celestial, **lunar})

		atlas_data = {
		'Placidus': placidus, 'Celestial': celestial, 'Asteroid': asteroid, 
		'Centaur': centaur, 'Neptunian': neptunian, 'Lunar': lunar, 
		'Aspect': aspects, 'House': houses
		}

		return atlas_data

	def run(self):
		while True:
			choice_main = self.main()
			if choice_main == '1':
				t_i = datetime.now() # Initializing current time
				location = self.location() # Enter location
				t = utc(t_i, location)
				atlas_data = self.generate(t, location)

				while True:
					choice_info = self.info()
					portal = self.portal(choice_info, atlas_data)
					if portal == 'exit':
						break

			elif choice_main == '2':
				t_i = self.dt()
				location = self.location()
				t = utc(t_i, location)
				atlas_data = self.generate(t, location)
				
				while True:
					choice_info = self.info()
					portal = self.portal(choice_info, atlas_data)
					if portal == 'exit':
						break

			elif choice_main == '3':
				break


console = AtlasWizardConsole()
console.run()
