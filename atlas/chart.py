from atlas.analysis import find_aspects

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

matplotlib.use('Agg')

class Chart:
    DPI = 100

    def __init__(self, id=0, dir=""):
        self.id = id
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-1.1, 1.1)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        self.fig.patch.set_facecolor('black')

        self.font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/fonts/NotoSans-Regular.ttf')
        self.font_prop = fm.FontProperties(fname=self.font_path)

        self.celestial_colors = {
            'Sun': '#F6FFC1', 'Moon': '#CCCCCC', 'Mercury': '#B4CDF3', 'Venus': '#FFC9E9',
            'Mars': '#CBC9FF', 'Jupiter': '#F3D8B4', 'Saturn': '#EDBAE1', 'Uranus': '#B4EDF3',
            'Neptune': '#AFBEE7', 'Pluto': '#CAA6F0', 'Lilith': 'grey'
        }

    def draw_circle(self, radius, linestyle='-'):
        circle = plt.Circle((0, 0), radius, color='white', fill=False, linestyle=linestyle)
        self.ax.add_artist(circle)

    def draw_line(self, angle, inner_radius, outer_radius, linewidth=0.5, linestyle='-', color='white'):
        inner_point = (inner_radius * np.cos(angle), inner_radius * np.sin(angle))
        outer_point = (outer_radius * np.cos(angle), outer_radius * np.sin(angle))
        line = plt.Line2D((inner_point[0], outer_point[0]), (inner_point[1], outer_point[1]), color=color, linewidth=linewidth, linestyle=linestyle)
        self.ax.add_artist(line)


# NATAL CHART
class NatalChart(Chart):
    def __init__(self, houses, celestials, id=0, dir=""):
        super().__init__(id, dir)
        self.celestials = celestials
        self.houses = houses
        self.aspects = find_aspects(celestials)
        self.asc_rad = np.radians(self.houses['House 1'].longitude) + np.pi if self.houses else np.pi
        self.house_longitudes = [house.longitude for house in self.houses.values()]

        self.ascmc = {'ASC': self.houses['House 1'], 'DSC': self.houses['House 7'], 'MC': self.houses['House 10'], 'IC': self.houses['House 4']}
        self.nodes = {**self.celestials, **self.ascmc}
        self.adjusted_nodes = {}

        self.zodiac_angles = (np.linspace(0, 2 * np.pi, 12, endpoint=False) - self.asc_rad) % (2 * np.pi)
        self.zodiac_symbols = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']

    def draw_ticks(self, n_ticks, length=0.05, rotation=0, linewidth=1):
        for angle in np.linspace(0, 2*np.pi, n_ticks, endpoint=False) + np.radians(15) - self.asc_rad:
            inner_radius = (0.8)
            outer_radius = (0.8 + length / 2) + length
            self.draw_line(angle + rotation, inner_radius, outer_radius, linewidth)

    
    def draw_zodiac(self):
        # Initializing zodiac boundaries
        for angle in self.zodiac_angles:
            self.draw_line(angle, 0.8, 1)

        # Initializing zodiac labels
        for i, angle in enumerate(self.zodiac_angles):
            angle += np.radians(15)
            x = np.cos(angle) * 0.9
            y = np.sin(angle) * 0.9

            color_map = {
                '♈': '#756AB6', '♌': '#756AB6', '♐': '#756AB6',
                '♉': '#AC87C5', '♍': '#AC87C5', '♑': '#AC87C5',
                '♊': '#E0AED0', '♎': '#E0AED0', '♒': '#E0AED0',
                '♋': '#FFE5E5', '♏': '#FFE5E5', '♓': '#FFE5E5'
            }
            color = color_map[self.zodiac_symbols[i]]
            self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color=color, fontproperties=self.font_prop, weight='bold')

    def draw_houses(self):
        if self.houses:
            for house in self.houses.values():
                self.draw_line(np.radians(house.longitude) - self.asc_rad, 0.3, 0.8, linewidth=0.25)

            for i, angle in enumerate(self.house_longitudes):
                next_angle = self.house_longitudes[(i + 1) % len(self.house_longitudes)]
                diff = next_angle - angle
                if diff > 180:
                    diff -= 360
                elif diff < -180:
                    diff += 360
                mid_angle = np.radians(angle + diff / 2) - self.asc_rad
                x = np.cos(mid_angle) * 0.35
                y = np.sin(mid_angle) * 0.35
                self.ax.text(x, y, str(i + 1), ha='center', va='center', color='white', fontsize=6)

            # ASC, DSC, MC, IC Labels
            for house, label in zip(['House 1', 'House 7', 'House 10', 'House 4'], ['ASC', 'DSC', 'MC', 'IC']):
                x = np.cos(np.radians(self.houses[house].longitude) - self.asc_rad) * 0.35
                y = np.sin(np.radians(self.houses[house].longitude) - self.asc_rad) * 0.35
                self.ax.text(x, y, label, ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor=(1, 1, 1, 0))

            self.draw_line(np.pi, 0.4, 0.8, linewidth=1.5)  # Ascendant
            self.draw_line(0, 0.4, 0.8, linewidth=1.5)  # Descendant
            self.draw_line(np.radians(self.houses['House 10'].longitude) - self.asc_rad, 0.4, 0.8, linewidth=1.5)  # Medium Coeli
            self.draw_line(np.radians(self.houses['House 4'].longitude) - self.asc_rad, 0.4, 0.8, linewidth=1.5)  # Imum Coeli
    
    def draw_celestial(self, celestial, color='white'):
        angle = np.radians(celestial.longitude) - self.asc_rad
        
        # Celestial Tick
        self.draw_line(angle, 0.775, 0.8, color=color)
        self.draw_line(angle, 0.275, 0.3, color=color)
        
        # Celestial Label Position Adjustment
        for node in self.nodes.values():
            if node.name != celestial.name:
                diff = abs(angle - (np.radians(node.longitude) - self.asc_rad))
                if diff < 0.05:
                    adjustment = 0.05 - diff
                    if angle < (np.radians(node.longitude) - self.asc_rad):
                        angle -= adjustment
                    else:
                        angle += adjustment
                    self.adjusted_nodes[celestial.name] = angle
                    
        # Celestial Symbol Label
        x = np.cos(angle)
        y = np.sin(angle)

        self.ax.text(x*0.7, y*0.7, celestial.symbol, ha='center', va='center', fontsize=18, color=color, fontproperties=self.font_prop)
        if hasattr(celestial, 'retrograde'):
            self.ax.text(x*0.65, y*0.65, '℞' if celestial.retrograde else '', ha='center', va='center', fontsize=7, color=color, fontproperties=self.font_prop)
        self.ax.text(x*0.525, y*0.525, celestial.zodiac_symbol, ha='center', va='center', fontsize=15, color=color, fontproperties=self.font_prop)
        self.ax.text(x*0.45, y*0.45, str(round((float(celestial.zodiac_orb)))) + '°', ha='center', va='center', fontsize=7, color=color)

    def draw_aspects(self):
        for aspect in self.aspects.values():
            if aspect.body_one.name in self.celestials and aspect.body_two.name in self.celestials:
                body_one_angle = np.radians(aspect.body_one.longitude) - self.asc_rad
                body_two_angle = np.radians(aspect.body_two.longitude) - self.asc_rad

                body_one_x = np.cos(body_one_angle)*0.275
                body_one_y = np.sin(body_one_angle)*0.275

                body_two_x = np.cos(body_two_angle)*0.275
                body_two_y = np.sin(body_two_angle)*0.275
                
                if aspect.name == 'Opposition':
                    self.ax.plot([body_one_x, body_two_x], [body_one_y, body_two_y], color='#756AB6', linewidth=0.5)
                    self.ax.text((body_one_x + body_two_x)/2, (body_one_y + body_two_y)/2, aspect.symbol, ha='center', va='center', fontsize=8, color='white')
                elif aspect.name == 'Trine':
                    self.ax.plot([body_one_x, body_two_x], [body_one_y, body_two_y], color='#AC87C5', linewidth=0.5)
                    self.ax.text((body_one_x + body_two_x)/2, (body_one_y + body_two_y)/2, aspect.symbol, ha='center', va='center', fontsize=8, color='white')
                elif aspect.name == 'Square':
                    self.ax.plot([body_one_x, body_two_x], [body_one_y, body_two_y], color='#E0AED0', linewidth=0.5)
                    self.ax.text((body_one_x + body_two_x)/2, (body_one_y + body_two_y)/2, aspect.symbol, ha='center', va='center', fontsize=8, color='white')
                elif aspect.name == 'Sextile':
                    self.ax.plot([body_one_x, body_two_x], [body_one_y, body_two_y], color='#FFE5E5', linewidth=0.5)
                    self.ax.text((body_one_x + body_two_x)/2, (body_one_y + body_two_y)/2, aspect.symbol, ha='center', va='center', fontsize=8, color='white')

    def generate(self, show=False, save=False):
        self.draw_circle(1)
        self.draw_circle(0.8)
        self.draw_circle(0.4)
        self.draw_circle(0.3)

        self.draw_ticks(360, length=0.02, rotation=np.radians(15), linewidth=0.1)  # 1° ticks
        self.draw_ticks(36, length=0.02, rotation=np.radians(10), linewidth=0.25)  # 10° ticks minor
        self.draw_ticks(36, length=0.03, rotation=np.radians(15), linewidth=0.4)  # 10° ticks major

        self.draw_aspects()  # Draw aspects
        self.draw_houses()  # Draw houses
        self.draw_zodiac()  # Draw zodiacs

        # Drawing Celestials
        for celestial in self.celestials.values():
            if celestial:
                color = self.celestial_colors.get(celestial.name, 'white')
                self.draw_celestial(celestial, color=color)

        if save:
            plt.savefig(f'static/charts/{self.id}.png', facecolor=self.fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0, dpi=self.DPI)
        if show:
            self.fig.patch.set_facecolor('black')
            plt.rc('axes', unicode_minus=False)
            plt.show()

# CELESTIAL CHART
class CelestialChart(Chart):
    def __init__(self, houses, celestials, id=0, dir=""):
        super().__init__(id, dir)
        self.id = '_'.join([celestial.name for celestial in celestials]) if isinstance(celestials, list) else celestials.name
        self.celestials = celestials if isinstance(celestials, list) else [celestials]
        self.houses = houses
        self.dir = dir
        
        self.asc_rad = np.radians(self.houses['House 1'].longitude) + np.pi if self.houses else np.pi
        self.dsc_rad = np.radians(self.houses['House 7'].longitude) + np.pi if self.houses else -np.pi

        self.zodiac_angles = (np.linspace(0, 2 * np.pi, 12, endpoint=False) - self.asc_rad) % (2 * np.pi)
        self.zodiac_symbols = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']

    def draw_earth(self):
        self.ax.plot(0, 0, 'o', color='#AFBEE7', markersize=20, zorder=4)

    def draw_celestials(self):

        for idx, celestial in enumerate(self.celestials):
            self.id = celestial.name

            # Celestial's ecliptic coordinates
            longitude = celestial.longitude
            longitude_rad = np.radians(longitude) - self.asc_rad

            radius = 0.8 + (idx * 0.05)  # Offset radius for each celestial
            x = radius * np.cos(longitude_rad)
            y = radius * np.sin(longitude_rad)
            color = self.celestial_colors.get(celestial.name, 'white')
            self.ax.plot(x, y, 'o', color=color, markersize=10, zorder=4)

    def draw_cone(self):
        # Generate angles from ascendant to descendant
        cone_angle = np.linspace(0, np.pi, 100)

        # Coordinates
        x = np.cos(cone_angle)
        y = np.sin(cone_angle)

        self.draw_line(np.pi, 0, 1, linewidth=0.5, linestyle='--')  # ASC
        self.draw_line(0, 0, 1, linewidth=0.5, linestyle='--') # DSC
        
        self.ax.fill(np.concatenate(([0], x, [0])), np.concatenate(([0], y, [0])), 'grey', alpha=0.2)

    def draw_labels(self):
        x_asc = np.cos(np.pi) * 0.9
        y_asc = np.sin(np.pi) * 0.9
        self.ax.text(x_asc, y_asc, 'ASC', ha='center', va='center', fontsize=10, color='white', fontproperties=self.font_prop, weight='bold')

        x_dsc = np.cos(0) * 0.9
        y_dsc = np.sin(0) * 0.9
        self.ax.text(x_dsc, y_dsc, 'DSC', ha='center', va='center', fontsize=10, color='white', fontproperties=self.font_prop, weight='bold')

    def draw_ticks(self, n_ticks, length=0.05, rotation=0, linewidth=1):
        for angle in np.linspace(0, 2*np.pi, n_ticks, endpoint=False) + np.radians(15) - self.asc_rad:
            inner_radius = (0.8)
            outer_radius = (0.8 + length / 2) + length
            self.draw_line(angle + rotation, inner_radius, outer_radius, linewidth)

    
    def draw_zodiac(self):
        # Initializing zodiac boundaries
        for angle in self.zodiac_angles:
            self.draw_line(angle, 0.8, 1)

        # Initializing zodiac labels
        for i, angle in enumerate(self.zodiac_angles):
            angle += np.radians(15)
            x = np.cos(angle) * 0.9
            y = np.sin(angle) * 0.9

            color_map = {
                '♈': '#756AB6', '♌': '#756AB6', '♐': '#756AB6',
                '♉': '#AC87C5', '♍': '#AC87C5', '♑': '#AC87C5',
                '♊': '#E0AED0', '♎': '#E0AED0', '♒': '#E0AED0',
                '♋': '#FFE5E5', '♏': '#FFE5E5', '♓': '#FFE5E5'
            }
            color = color_map[self.zodiac_symbols[i]]
            self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color=color, fontproperties=self.font_prop, weight='bold')

    def generate(self, show=False, save=False):
        self.draw_earth()
        self.draw_celestials()
        self.draw_zodiac()

        self.draw_ticks(360, length=0.02, rotation=np.radians(15), linewidth=0.1) # 1° ticks
        self.draw_ticks(36, length=0.02, rotation=np.radians(10), linewidth=0.25) # 10° ticks minor
        self.draw_ticks(36, length=0.03, rotation=np.radians(15), linewidth=0.4) # 10° ticks major

        self.draw_cone()
        self.draw_labels()

        if save:
            plt.savefig(f'{self.dir}/{self.id}', facecolor=self.fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0, dpi=self.DPI)
        if show:
            self.fig.patch.set_facecolor('black')
            plt.rc('axes', unicode_minus=False)
            plt.show()

