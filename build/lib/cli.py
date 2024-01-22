#!/usr/bin/env python3
import argparse
from tabulate import tabulate
from datetime import datetime

from atlas.atlas import Atlas
from atlas.chart import Chart
from atlas.console import Console
from atlas.topo import locator

def main():
    # Top level parser
    parser = argparse.ArgumentParser(description='٭ Atlas Wizard ٭')
    subparsers = parser.add_subparsers(dest='command')

    # 'Observe' command
    observe_parser = subparsers.add_parser('observe', help='Observe a celestial body')
    observe_parser.add_argument('target', help='Celestial body/bodies to observe', nargs='+')
    observe_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
    observe_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
    observe_parser.add_argument('-l', '--location', help='Location of observation', nargs='?')

    zodiac_parser = subparsers.add_parser('align', help='Find the zodiac sign of a celestial body')
    zodiac_parser.add_argument('target', help='Celestial body/bodies to observe', nargs='+')
    zodiac_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
    zodiac_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
    zodiac_parser.add_argument('-l', '--location', help='Location of observation', nargs='?')

    chart_parser = subparsers.add_parser('chart', help='Generate a chart')
    chart_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
    chart_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
    chart_parser.add_argument('-l', '--location', help='Location of observation', nargs='?')
    chart_parser.add_argument('-s', '--save', help='Save chart', action='store_true')

    console_parser = subparsers.add_parser('console', help='Start the Atlas console')
    
    args = parser.parse_args()
    if hasattr(args, 'date') and args.date:
        args.date = datetime.strptime(args.date, '%Y-%m-%d').date()
    if hasattr(args, 'time') and args.time:
        args.time = datetime.strptime(args.time, '%H:%M').time()
    if hasattr(args, 'location') and args.location:
        args.location = locator(args.location)

    atlas = Atlas() # Initialize Atlas class

    if args.command == 'observe':
        for target in args.target:
            result = atlas.body(datetime.combine(args.date, args.time), target, args.location)
            print(f"Distance: {round(result.distance, 4)} AU")
            print(f"Longitude: {round(result.longitude, 4)}°")
            print(f"Latitude: {round(result.latitude, 4)}°")

    if args.command == 'align':
        results = []
        for target in args.target:
            result = atlas.body(datetime.combine(args.date, args.time), target, args.location)
            results.append([f"{result.symbol} {result.name}", f"{result.zodiac_symbol} {result.zodiac[:3]}", f"{result.zodiac_orb}°", f"{result.retrograde}"])
        results_tab = tabulate(results, headers=['Body', 'Zodiac', 'Orb', 'Retrograde'])
        print(results_tab)
    
    if args.command == 'chart':
        houses = atlas.placidus(datetime.combine(args.date, args.time), args.location)
        celestials = atlas.celestial(datetime.combine(args.date, args.time), args.location)
    
        chart = Chart(houses, celestials) # Generate Chart
        chart.generate(show=True, save=args.save)

    if args.command == 'console':
        console = Console()
        console.start()

if __name__ == '__main__':
    main()