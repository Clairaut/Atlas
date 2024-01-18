import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

class Chart:
    def __init__(self, houses, celestials, id=0):
        self.houses = houses
        self.celestials = celestials
        self.id=id

        self.asc = self.houses['I'].longitude
        self.dsc = self.houses['VII'].longitude
        self.mc = self.houses['X'].longitude
        self.ic = self.houses['IV'].longitude
        self.ascmc = {'House I': self.houses['I'], 'House VII': self.houses['VII'], 'House X': self.houses['X'], 'House IV': self.houses['IV']}

        self.nodes = {**self.celestials, **self.ascmc}
        self.adjusted_nodes = {}
        
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.fig.patch.set_facecolor('black')

        self.house_longitudes = list(house.longitude for house in self.houses.values())
        
        self.zodiac_angles = (np.linspace(0, 2*np.pi, 12, endpoint=False) - np.radians(self.asc) + np.pi) % (2*np.pi)
        self.zodiac_symbols = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']
        
        self.font_path = 'static/fonts/NotoSans-Regular.ttf'
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
        for angle in np.linspace(0, 2*np.pi, n_ticks, endpoint=False) + np.radians(15) - np.radians(self.asc) + np.pi:
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
        # House boundaries
        for house in self.houses.values():
            self.draw_line(np.radians(house.longitude) - np.radians(self.asc) + np.pi, 0.3, 0.4)

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

            mid_angle = np.radians(angle + diff / 2) - np.radians(self.asc) + np.pi

            x = np.cos(mid_angle)*0.35
            y = np.sin(mid_angle)*0.35


            self.ax.text(x, y, str(i+1), ha='center', va='center', color='white', fontsize=6)

        # ASC, DSC, MC, IC Labels
        x = np.cos(np.radians(self.houses['I'].longitude) - np.radians(self.asc) + np.pi)*0.35 # ASC
        y = np.sin(np.radians(self.houses['I'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'ASC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor='black')

        x = np.cos(np.radians(self.houses['VII'].longitude) - np.radians(self.asc) + np.pi)*0.35 # DSC
        y = np.sin(np.radians(self.houses['VII'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'DSC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor='black')

        x = np.cos(np.radians(self.houses['X'].longitude) - np.radians(self.asc) + np.pi)*0.35 # MC
        y = np.sin(np.radians(self.houses['X'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'MC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor='black')

        x = np.cos(np.radians(self.houses['IV'].longitude) - np.radians(self.asc) + np.pi)*0.35 # IC
        y = np.sin(np.radians(self.houses['IV'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'IC', ha='center', va='center', fontsize=7, weight='bold', color='white', backgroundcolor='black')

    def draw_celestial(self, celestial, color='white'):
        angle = np.radians(celestial.longitude) - np.radians(self.asc) + np.pi
        
        # Celestial Tick
        self.draw_line(angle, 0.75, 0.8, color=color)
        
        # Celestial Label Position Adjustment
        for node in self.nodes.values():
            if node.name != celestial.name:
                diff = abs(angle - (np.radians(node.longitude) - np.radians(self.asc) + np.pi))
                while diff < 0.05:
                    if angle < (np.radians(node.longitude) - np.radians(self.asc) + np.pi):
                        angle -= 0.01
                    else:
                        angle += 0.01
                    diff = abs(angle - (np.radians(node.longitude) - np.radians(self.asc) + np.pi))
                    self.adjusted_nodes[celestial.name] = angle

        for node_name, node_angle in self.adjusted_nodes.items():
            if node_name != celestial.name:
                diff = abs(angle - node_angle)
                while diff < 0.1:
                    if angle < (np.radians(self.nodes[node_name].longitude) - np.radians(self.asc) + np.pi):
                        angle -= 0.01
                    else:
                        angle += 0.01
                    diff = abs(angle - node_angle)


        # Celestial Symbol Label
        x = np.cos(angle)
        y = np.sin(angle)

        self.ax.text(x*0.7, y*0.7, celestial.symbol, ha='center', va='center', fontsize=18, color=color, fontproperties=self.font_prop)
        self.ax.text(x*0.65, y*0.65, celestial.retrograde, ha='center', va='center', fontsize=7, color=color, fontproperties=self.font_prop)
        self.ax.text(x*0.525, y*0.525, celestial.zodiac_symbol, ha='center', va='center', fontsize=15, color=color, fontproperties=self.font_prop)
        self.ax.text(x*0.45, y*0.45, str(round((float(celestial.zodiac_orb)))) + '°', ha='center', va='center', fontsize=7, color=color)

    # Create chart
    def create_chart(self, show=True):
        self.draw_houses()
        self.draw_zodiac()

        # Drawing Chart
        self.draw_circle(1)
        self.draw_circle(0.8)
        self.draw_circle(0.4)
        self.draw_circle(0.3)

        self.draw_ticks(360, length=0.02, rotation=np.radians(15), linewidth=0.1) # 1° ticks
        self.draw_ticks(36, length=0.02, rotation=np.radians(10), linewidth=0.25) # 10° ticks minor
        self.draw_ticks(36, length=0.03, rotation=np.radians(15), linewidth=0.4) # 10° ticks major

        self.draw_line(np.pi, 0.3, 0.8, linewidth=1.5) # Ascendant
        self.draw_line(0, 0.3, 0.8, linewidth=1.5) # Descendant
        self.draw_line(np.radians(self.houses['X'].longitude) - np.radians(self.asc) + np.pi, 0.3, 0.8, linewidth=1.5) # Medium Coeli
        self.draw_line(np.radians(self.houses['IV'].longitude) - np.radians(self.asc) + np.pi, 0.3, 0.8, linewidth=1.5) # Imum Coeli

        # Drawing Celestials
        for celestial in self.celestials.values():
            self.draw_celestial(celestial)
            if celestial.name == 'Sun':
                self.draw_celestial(celestial, color='#F6FFC1')
            elif celestial.name == 'Moon':
                self.draw_celestial(celestial, color='#CCCCCC')
            elif celestial.name == 'Mercury':
                self.draw_celestial(celestial, color='#B4CDF3')
            elif celestial.name == 'Venus':
                self.draw_celestial(celestial, color='#FFC9E9')
            elif celestial.name == 'Mars':
                self.draw_celestial(celestial, color='#CBC9FF')
            elif celestial.name == 'Jupiter':
                self.draw_celestial(celestial, color='#F3D8B4')
            elif celestial.name == 'Saturn':
                self.draw_celestial(celestial, color='#EDBAE1')
            elif celestial.name == 'Uranus':
                self.draw_celestial(celestial, color='#B4EDF3')
            elif celestial.name == 'Neptune':
                self.draw_celestial(celestial, color='#AFBEE7')
            elif celestial.name == 'Pluto':
                self.draw_celestial(celestial, color='#CAA6F0')
            elif celestial.name == 'Lilith':
                self.draw_celestial(celestial, color='grey')

       
        plt.savefig(f'static/charts/{self.id}.png', facecolor=self.fig.get_facecolor(), edgecolor='none', bbox_inches='tight', pad_inches=0, dpi=300)
        if show:
            plt.show()