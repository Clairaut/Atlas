import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
from atlas.analysis import find_aspects

class Chart:
    def __init__(self, houses, celestials, id=0):
        self.houses = houses
        self.celestials = celestials
        self.aspects = find_aspects(celestials)
        self.id=id

        self.celestial_colors = {
            'Sun': '#F6FFC1', 'Moon': '#CCCCCC', 'Mercury': '#B4CDF3', 'Venus': '#FFC9E9',
            'Mars': '#CBC9FF', 'Jupiter': '#F3D8B4', 'Saturn': '#EDBAE1', 'Uranus': '#B4EDF3',
            'Neptune': '#AFBEE7', 'Pluto': '#CAA6F0', 'Lilith': 'grey'
        }
        
        if self.houses:
            self.asc_rad = np.radians(self.houses['House 1'].longitude) + np.pi
        else:
            self.asc_rad = np.pi
        
        self.ascmc = {'ASC': self.houses['House 1'], 'DSC': self.houses['House 7'], 'MC': self.houses['House 10'], 'IC': self.houses['House 4']}
        self.nodes = {**self.celestials, **self.ascmc}
        self.adjusted_nodes = {}
        
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.fig.patch.set_facecolor((1, 1, 1, 0))  # RGBA values: (R, G, B, Alpha)

        self.house_longitudes = list(house.longitude for house in self.houses.values())
        
        self.zodiac_angles = (np.linspace(0, 2*np.pi, 12, endpoint=False) - self.asc_rad) % (2*np.pi)
        self.zodiac_symbols = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']
        
        self.font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/fonts/NotoSans-Regular.ttf')
        self.font_prop = fm.FontProperties(fname=self.font_path)


    # Drawing functions
    def draw_circle(self, radius, linestyle='-'):
        circle = plt.Circle((0, 0), radius, color="white", fill=False, linestyle=linestyle)
        self.ax.add_artist(circle)

    def draw_line(self, angle, inner_radius, outer_radius, linewidth=0.5, color='white'):
        inner_point = (inner_radius * np.cos(angle), inner_radius * np.sin(angle))
        outer_point = (outer_radius * np.cos(angle), outer_radius * np.sin(angle))
        line = plt.Line2D((inner_point[0], outer_point[0]), (inner_point[1], outer_point[1]), color=color, linewidth=linewidth)
        self.ax.add_artist(line)

    def draw_ticks(self, n_ticks, length=0.05, rotation=0, linewidth=1):
        for angle in np.linspace(0, 2*np.pi, n_ticks, endpoint=False) + np.radians(15) - self.asc_rad:
            inner_radius = (0.8)
            outer_radius = (0.8 + length / 2) + length
            self.draw_line(angle + rotation, inner_radius, outer_radius, linewidth)

    def draw_zodiacs(self):
        # Initializing zodiac boundaries
        for angle in self.zodiac_angles:
            self.draw_line(angle, 0.8, 1)

        # Initializing zodiac labels
        for i, angle in enumerate(self.zodiac_angles):
            angle += np.radians(15)
            x = np.cos(angle)*0.9
            y = np.sin(angle)*0.9

            if self.zodiac_symbols[i] == '♈' or self.zodiac_symbols[i] == '♌' or self.zodiac_symbols[i] == '♐':
                self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color='#756AB6', fontproperties=self.font_prop, weight='bold')
            elif self.zodiac_symbols[i] == '♉' or self.zodiac_symbols[i] == '♍' or self.zodiac_symbols[i] == '♑':
                self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color='#AC87C5', fontproperties=self.font_prop, weight='bold')
            elif self.zodiac_symbols[i] == '♊' or self.zodiac_symbols[i] == '♎' or self.zodiac_symbols[i] == '♒':
                self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color='#E0AED0', fontproperties=self.font_prop, weight='bold')
            elif self.zodiac_symbols[i] == '♋' or self.zodiac_symbols[i] == '♏' or self.zodiac_symbols[i] == '♓':
                self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14, color='#FFE5E5', fontproperties=self.font_prop, weight='bold')


    def draw_houses(self):
        if self.houses:
            # House boundaries
            for house in self.houses.values():
                self.draw_line(np.radians(house.longitude) - self.asc_rad, 0.3, 0.8, linewidth=0.25)

            # House labels
            for i, angle in enumerate(self.house_longitudes):
                if i < len(self.house_longitudes) - 1:
                    next_angle = self.house_longitudes[i+1]
                else:
                    next_angle = self.house_longitudes[0]

                diff = next_angle - angle
                if diff > 180:
                    diff -= 360
                elif diff < -180:
                    diff += 360

                mid_angle = np.radians(angle + diff / 2) - self.asc_rad

                x = np.cos(mid_angle)*0.35
                y = np.sin(mid_angle)*0.35


                self.ax.text(x, y, str(i+1), ha='center', va='center', color='white', fontsize=6)

            # ASC, DSC, MC, IC Labels
            x = np.cos(np.radians(self.houses['House 1'].longitude) - self.asc_rad)*0.35 # ASC
            y = np.sin(np.radians(self.houses['House 1'].longitude) - self.asc_rad)*0.35
            self.ax.text(x, y, 'ASC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor=(1, 1, 1, 0))

            x = np.cos(np.radians(self.houses['House 7'].longitude) - self.asc_rad)*0.35 # DSC
            y = np.sin(np.radians(self.houses['House 7'].longitude) - self.asc_rad)*0.35
            self.ax.text(x, y, 'DSC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor=(1, 1, 1, 0))

            x = np.cos(np.radians(self.houses['House 10'].longitude) - self.asc_rad)*0.35 # MC
            y = np.sin(np.radians(self.houses['House 10'].longitude) - self.asc_rad)*0.35
            self.ax.text(x, y, 'MC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor=(1, 1, 1, 0))

            x = np.cos(np.radians(self.houses['House 4'].longitude) - self.asc_rad)*0.35 # IC
            y = np.sin(np.radians(self.houses['House 4'].longitude) - self.asc_rad)*0.35
            self.ax.text(x, y, 'IC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor=(1, 1, 1, 0))

            self.draw_line(np.pi, 0.4, 0.8, linewidth=1.5) # Ascendant
            self.draw_line(0, 0.4, 0.8, linewidth=1.5) # Descendant
            self.draw_line(np.radians(self.houses['House 10'].longitude) - self.asc_rad, 0.4, 0.8, linewidth=1.5) # Medium Coeli
            self.draw_line(np.radians(self.houses['House 4'].longitude) - self.asc_rad, 0.4, 0.8, linewidth=1.5) # Imum Coeli


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

    def generate(self, show=False, save=False):
        # Drawing chart
        self.draw_circle(1)
        self.draw_circle(0.8)
        self.draw_circle(0.4)
        self.draw_circle(0.3)

        self.draw_ticks(360, length=0.02, rotation=np.radians(15), linewidth=0.1) # 1° ticks
        self.draw_ticks(36, length=0.02, rotation=np.radians(10), linewidth=0.25) # 10° ticks minor
        self.draw_ticks(36, length=0.03, rotation=np.radians(15), linewidth=0.4) # 10° ticks major

        self.draw_houses() # Draw houses
        self.draw_zodiacs() # Draw zodiacs
        self.draw_aspects() # Draw aspects

        # Drawing Celestials
        for celestial in self.celestials.values():
            if celestial:
                color = self.celestial_colors.get(celestial.name, 'white')
                self.draw_celestial(celestial, color=color)
            
        if save:
            plt.savefig(f'static/charts/{self.id}.png', facecolor=self.fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0, dpi=300)
        if show:
            self.fig.patch.set_facecolor('black')
            plt.rc('axes', unicode_minus=False)
            plt.show()