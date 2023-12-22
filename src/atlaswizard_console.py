from atlas import Atlas
from locator import locator
from datetime import datetime
from tabulate import tabulate
import traceback
import os


class AtlasWizardConsole:
	def __init__(self):
		self.atlas = Atlas()

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
|====================|
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


	def location(self):
		self.clear()
		while True:
			print("""
|===============|
| 🖈 Location 🖈 |
|===============|
				""")

			choice = input("\nEnter a location (Ex: 'New Orleans, USA'):\n")
			if choice:
				try:
					location = locator(choice)
					return location
					break
					
				except Exception as e:
					print(f"Error: {e}")
					traceback.print_exc()
					continue

	def info(self):
		self.clear()
		while True:
			print("""
|=================|
| 🪐 Ephemeris 🪐 |
|=================|
				""")

			menu = [
			['1', "🜨︎ MC and ASC"],
			['2', "⌂ Placidus"],
			['3', "☉ Celestial Bodies"],
			['4', "☄️ Asteroid Belt"],
			['5', "⚷ Centaur"],
			['6', "🪐 Trans-Neptunian"],
			['7', "☽ Lunar"],
			['8', "≡ Main Menu"],
			]

			menu_tab = tabulate(menu)
			print(menu_tab)

			choices = ['1', '2', '3', '4', '5', '6', '7', '8']
			choice = input("\nChoose ephemeris:\n")
			if choice in choices:
				return choice
				break
			else:
				print("Error: Invalid Input")
				continue

	def run(self):
		choice_main = self.main()

		if choice_main == '1':
			t_input = datetime.now()
			location = self.location()


console = AtlasWizardConsole()
console.run()
