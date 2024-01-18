from atlas import Atlas
from chart import AtlasChart
from topo import locator
from datetime import datetime

location = locator('London')
t = datetime.now()

atlas = Atlas()

lunar = atlas.lunar(t, location)
celestials = atlas.celestial(t, location)
houses = atlas.placidus(t, location)

chart = AtlasChart(houses, {**celestials, **lunar})

chart.create_chart()