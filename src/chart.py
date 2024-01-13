import matplotlib.pyplot as plt
import numpy as np

class AtlasChart:
    def __init__(self, houses, celestials):
        self.houses = houses
        self.celestials = celestials
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect('equal')
        self.ax.axis('off')

        self.house_longitudes = list(house.longitude for house in self.houses.values())
        self.asc = self.houses['I'].longitude
        self.dsc = self.houses['VII'].longitude
        self.mc = self.houses['X'].longitude
        self.ic = self.houses['IV'].longitude

        self.label_positions = [np.radians(self.asc), np.radians(self.dsc), np.radians(self.mc), np.radians(self.ic)]
        
        self.zodiac_angles = (np.linspace(0, 2*np.pi, 12, endpoint=False) - np.radians(self.asc) + np.pi) % (2*np.pi)
        self.zodiac_symbols = ['♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓']

    # Drawing functions
    def draw_circle(self, radius, linestyle='-'):
        circle = plt.Circle((0, 0), radius, color="black", fill=False, linestyle=linestyle)
        self.ax.add_artist(circle)

    def draw_line(self, angle, inner_radius, outer_radius, linewidth=0.5, color='black'):
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

            self.ax.text(x, y, self.zodiac_symbols[i], ha='center', va='center', fontsize=14)
    
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

            self.ax.text(x, y, str(i+1), ha='center', va='center', fontsize=6)

        # ASC, DSC, MC, IC Labels
        x = np.cos(np.radians(self.houses['I'].longitude) - np.radians(self.asc) + np.pi)*0.35 # ASC
        y = np.sin(np.radians(self.houses['I'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'ASC', ha='center', va='center', fontsize=7, backgroundcolor='white')

        x = np.cos(np.radians(self.houses['VII'].longitude) - np.radians(self.asc) + np.pi)*0.35 # DSC
        y = np.sin(np.radians(self.houses['VII'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'DSC', ha='center', va='center', fontsize=7, backgroundcolor='white')

        x = np.cos(np.radians(self.houses['X'].longitude) - np.radians(self.asc) + np.pi)*0.35 # MC
        y = np.sin(np.radians(self.houses['X'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'MC', ha='center', va='center', fontsize=7, backgroundcolor='white')

        x = np.cos(np.radians(self.houses['IV'].longitude) - np.radians(self.asc) + np.pi)*0.35 # IC
        y = np.sin(np.radians(self.houses['IV'].longitude) - np.radians(self.asc) + np.pi)*0.35
        self.ax.text(x, y, 'IC', ha='center', va='center', fontsize=7, backgroundcolor='white')

    def draw_celestial(self, celestial, color='black'):
        angle = np.radians(celestial.longitude) - np.radians(self.asc) + np.pi
        
        # Celestial Tick
        self.draw_line(angle, 0.75, 0.8, color=color)

        # Celestial Label Position Adjustment
        for pos in self.label_positions:
            diff = abs(angle-pos)
            if diff < 0.1:
                if angle < pos:
                    angle -= 0.1 * diff
                else:
                    angle += 0.1 * diff

        # Celestial Label
        x = np.cos(angle)*0.65
        y = np.sin(angle)*0.65

        self.label_positions.append(angle)

        self.ax.text(x, y, celestial.symbol, ha='center', va='center', fontsize=18, color=color)


    # Create chart
    def create_chart(self):
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

        plt.show()