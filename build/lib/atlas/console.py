from atlas.atlas import Atlas
from atlas.chart import Chart
from atlas.aspects import aspect, house
from atlas.topo import locator, utc
from PyInquirer import prompt, Token, style_from_dict
from datetime import datetime
from tabulate import tabulate
import configparser
import traceback
import os


class Console:
	def __init__(self):
		self.atlas = Atlas()
		self.aspect_symbols = {'Opposition': '☍ Opposition', 'Trine': '△ Trine', 'Square': '□ Square', 
						 'Sextile': '⚹ Sextile', 'Conjunction': '☌ Conjunction'}
		self.config = configparser.ConfigParser()
		
		config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config/config.ini')
		self.config.read(config_path)

		self.prompt_style = style_from_dict({
			Token.Separator: '#6C6C6C',
			Token.QuestionMark: '#AC87C5 bold',
			Token.Selected: '#E0AED0',
			Token.Pointer: '#FF9D00 bold',
			Token.Instruction: '',
			Token.Answer: '#5F819D bold',
		})

	def clear(self):
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def main_menu(self):
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
			['3', "⚙ Configuration"],
			['4', "≡ Exit"],
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			# User Input
			choices = ['1', '2', '3', '4']
			choice = input("\n Choose menu option:\n")
			if choice in choices:
				self.clear()
				return choice
				break
			else:
				print("Error: Invalid Input")

	def datetime_input(self):
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

	def location_input(self):
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
					
				except Exception as e:
					print(f"Error: {e}")
					traceback.print_exc()
					continue

	def info_menu(self):
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
			['7', "🝴  Lots"],
			['8', "★ Aspects"],
			['9', "📈 Chart"],
			['0', "≡  Main Menu"],
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			choices = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
			choice = input("\nChoose ephemeris:\n")
			if choice in choices:
				return choice
			else:
				self.clear()
				print("Error: Invalid Input")
				continue
	
	def config_menu(self):
		self.clear()
		while True:
			print("""
|====================|
| ⚙ Configuration ⚙ |
|====================|
		 """)
			
			menu = [
			['1', "📈 Chart Settings"],
			['2', "≡ Main Menu"]
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			choices = ['1', '2']
			choice = input("\nChoose configuration:\n")
			if choice in choices:
				return choice
			else:
				self.clear()
				print("Error: Invalid Input")
				continue

	def config_chart(self):
		self.clear()
		while True:
			print("""
|======================|
| 📈 Chart Settings 📈 |
|======================|
		 """)
			
			menu = [
			['1', "🪐 Bodies"],
			['2', "≡ Configuration Menu"]
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			choices = ['1', '2']
			choice = input("\nChoose configuration:\n")
			if choice in choices:
				return choice
			else:
				self.clear()
				print("Error: Invalid Input")
				continue

	def config_chart_bodies(self):
		self.clear()

		visible_bodies = self.config['Chart']['bodies'].split(', ')

		questions = [
			{
			'type': 'checkbox',
			'message': 'Select Celestial Bodies',
			'name': 'Celestial Bodies',
			'choices': [
				{'name': '☉ Sun', 'checked': '☉ Sun' in visible_bodies},
				{'name': '☽ Moon', 'checked': '☽ Moon' in visible_bodies},
				{'name': '☿ Mercury', 'checked': '☿ Mercury' in visible_bodies},
				{'name': '♀ Venus', 'checked': '♀ Venus' in visible_bodies},
				{'name': '♂ Mars', 'checked': '♂ Mars' in visible_bodies},
				{'name': '♃ Jupiter', 'checked': '♃ Jupiter' in visible_bodies},
				{'name': '♄ Saturn', 'checked': '♄ Saturn' in visible_bodies},
				{'name': '♅ Uranus', 'checked': '♅ Uranus' in visible_bodies},
				{'name': '♆ Neptune', 'checked': '♆ Neptune' in visible_bodies},
				{'name': '⯓ Pluto', 'checked': '⯓ Pluto' in visible_bodies},
				{'name': '⚸ Lilith', 'checked': '⚸ Lilith' in visible_bodies},
				{'name': '⯝ Selena', 'checked': '⯝ Selena' in visible_bodies},
				{'name': '☊ Lunar ASC', 'checked': '☊ Lunar ASC' in visible_bodies},
				{'name': '☋ Lunar DSC', 'checked': '☋ Lunar DSC' in visible_bodies},
				{'name': '⚳ Ceres', 'checked': '⚳ Ceres' in visible_bodies},
				{'name': '⚴ Pallas', 'checked': '⚴ Pallas' in visible_bodies},
				{'name': '⚵ Juno', 'checked': '⚵ Juno' in visible_bodies},
				{'name': '⚶ Vesta', 'checked': '⚶ Vesta' in visible_bodies},
				{'name': '⯙ Astraea', 'checked': '⯙ Astraea' in visible_bodies},
				{'name': '⚷ Chiron', 'checked': '⚷ Chiron' in visible_bodies},
			],
			'validate': lambda answer: 'You must choose at least one body.' if len(answer) == 0 else True,
			}
		]

		answers = prompt(questions, style=self.prompt_style)

		self.config['Chart']['bodies'] = ', '.join(answers['Celestial Bodies'])
		with open('config.ini', 'w') as configfile:
			self.config.write(configfile)

			

	def placidus(self, atlas_data):
		placidus = [[f"{house.symbol} {house.name}", f"{house.zodiac_symbol} {house.zodiac}", f"{house.zodiac_orb}°"] for house in atlas_data['Placidus'].values()]

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
		celestial = [[f"{body.symbol} {body.name}", f"{body.zodiac_symbol} {body.zodiac}", f"{body.zodiac_orb}°", f"{body.retrograde}"] for body in atlas_data['Celestial'].values()]

		celestial_tab = tabulate(celestial, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(celestial_tab)

	def asteroid(self, atlas_data):
		asteroid = [[f"{body.symbol} {body.name}", f"{body.zodiac_symbol} {body.zodiac}", f"{body.zodiac_orb}°", f"{body.retrograde}"] for body in atlas_data['Asteroid'].values()]

		asteroid_tab = tabulate(asteroid, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(asteroid_tab)

	def centaur(self, atlas_data):
		centaur = [[f"{body.symbol} {body.name}", f"{body.zodiac_symbol} {body.zodiac}", f"{body.zodiac_orb}°", f"{body.retrograde}"] for body in atlas_data['Centaur'].values()]

		centaur_tab = tabulate(centaur, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(centaur_tab)

	def neptunian(self, atlas_data):
		neptunian = [[f"{body.symbol} {body.name}", f"{body.zodiac_symbol} {body.zodiac}", f"{body.zodiac_orb}°", f"{body.retrograde}"] for body in atlas_data["Neptunian"].values()]

		neptunian_tab = tabulate(neptunian, headers=['Celestial Body', 'Zodiac', 'Orb', 'Retrograde'])
		print(neptunian_tab)

	def lunar(self, atlas_data):
		phase = [
		["☽ Lunar Phase", f"{atlas_data['Celestial']['Moon'].phase_symbol} {atlas_data['Celestial']['Moon'].phase}", f"{atlas_data['Celestial']['Moon'].phase_longitude}°"],
		]
		
		node = [[f"{body.symbol} {body.name}", f"{body.zodiac_symbol} {body.zodiac}", f"{body.zodiac_orb}°"] for body in atlas_data["Lunar"].values()]

		phase_tab = tabulate(phase, headers=['Moon', 'Phase', 'Phase Angle'])
		node_tab = tabulate(node, headers=['Node', 'Zodiac', 'Orb'])
		print(phase_tab + "\n\n" + node_tab)

	def lot(self, atlas_data):
		lot = [[f"{lot.symbol} {lot.name}", f"{lot.zodiac_symbol} {lot.zodiac}", f"{lot.zodiac_orb}°"] for lot in atlas_data['Lot'].values()]

		lot_tab = tabulate(lot, headers=['Lot', 'Zodiac', 'Orb'])
		print(lot_tab)

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
		7: self.lot,
		8: self.aspect,
		9: lambda _: 'chart',
		0: lambda _: 'exit'
		}

		if choice_info != None:
			choice_info = int(choice_info)
		if choice_info in portal:
			return portal[choice_info](atlas_data)

	def generate_data(self, t, location): # Generating Ephemeris
		placidus = self.atlas.placidus(t, location)
		celestial = self.atlas.celestial(t, location)
		asteroid = self.atlas.asteroid(t, location)
		centaur = self.atlas.centaur(t, location)
		neptunian = self.atlas.neptunian(t, location)
		lunar = self.atlas.lunar(t, location)
		aspects = aspect({**celestial, **lunar})
		lots = self.atlas.lot(placidus, celestial)
		houses = house(placidus, {**celestial, **lunar})

		atlas_data = {
		'Placidus': placidus, 'Celestial': celestial, 'Asteroid': asteroid, 
		'Centaur': centaur, 'Neptunian': neptunian, 'Lunar': lunar, 
		'Lot': lots, 'Aspect': aspects, 'House': houses
		}

		return atlas_data

	def start(self):
		while True:
			choice_main = self.main_menu()
			if choice_main == '1':
				t_i = datetime.now() # Initializing current time
				location = self.location_input() # Enter location
				t = utc(t_i, location)
				atlas_data = self.generate_data(t, location)

				while True:
					choice_info = self.info_menu()
					portal = self.portal(choice_info, atlas_data)
					if portal == 'exit':
						break
					elif portal == 'chart':
						chart = Chart(atlas_data['Placidus'], {**atlas_data['Celestial'], **atlas_data['Lunar'], **atlas_data['Lot']})
						chart.generate(show=True, save=False)
						continue

			elif choice_main == '2':
				t_i = self.datetime_input()
				location = self.location_input()
				t = utc(t_i, location)
				atlas_data = self.generate_data(t, location)
				
				while True:
					choice_info = self.info_menu()
					portal = self.portal(choice_info, atlas_data)
					if portal == 'exit':
						break
					elif portal == 'chart':
						chart = Chart(atlas_data['Placidus'], {**atlas_data['Celestial'], **atlas_data['Lunar'], **atlas_data['Lot']})
						chart.generate(show=True, save=False)
						continue

			elif choice_main == '3':
				while True:
					choice_config = self.config_menu()
					if choice_config == '1':
						choice_config_chart = self.config_chart()
						if choice_config_chart == '1':
							self.config_chart_bodies()
						elif choice_config_chart == '2':
							break
					elif choice_config == '2':
						break

			elif choice_main == '4':
				break

