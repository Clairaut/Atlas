#!/usr/bin/env python3
import argparse
from tabulate import tabulate
from datetime import datetime
import traceback

from atlas.atlas import Atlas
from atlas.chart import Chart
from atlas.console import Console
from atlas.topo import locator, utc

atlas = Atlas()

def handle_observe(args):
    try:
        t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
    except:
        print('Error: Invalid date/time')
        exit()
    
    results = [[f"{result.symbol} {result.name}", f"{round(result.distance, 3)} AU,", f"{round(result.ra, 2)}°", f"{round(result.dec, 2)}°"] for target in args.target for result in [atlas.body(t, target, args.location)]]
    print(tabulate(results, headers=['Body', 'Dist', 'RA (Deg)', 'Dec']))

def handle_align(args):
    try:
        t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
    except:
        print('Error: Invalid date/time')
        exit()

    results = [[f"{result.symbol} {result.name}", f"{result.zodiac_symbol} {result.zodiac[:3]}", f"{result.zodiac_orb}°", f"{result.retrograde}"] for target in args.target for result in [atlas.body(t, target, args.location)]]
    print(tabulate(results, headers=['Body', 'Zodiac', 'Orb', 'Retrograde']))

def handle_chart(args):
    try:
        t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
    except:
        print('Error: Invalid date/time')
        exit()

    houses = atlas.placidus(t, args.location)
    celestials = atlas.celestial(t, args.location)
    chart = Chart(houses, celestials) # Generate Chart
    chart.generate(show=True, save=args.save)

def handle_console(args):
    console = Console()
    console.start()

def main():
    # Top level parser
    parser = argparse.ArgumentParser(description='Atlas Wizard')
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
        try:
            args.date = datetime.strptime(args.date, '%Y-%m-%d').date()
        except ValueError:
            print('Error: Invalid date format')
            exit()
    if hasattr(args, 'time') and args.time:
        try:
            args.time = datetime.strptime(args.time, '%H:%M').time()
        except ValueError:
            print('Error: Invalid time format')
            exit()
    if hasattr(args, 'location') and args.location:
        try:
            args.location = locator(args.location)
        except Exception as e:
            print(f'Error: {e}')
            traceback.print_exc()
            exit()

    if args.command == 'observe':
        handle_observe(args)
    elif args.command == 'align':
        handle_align(args)
    elif args.command == 'chart':
        handle_chart(args)
    elif args.command == 'console':
        handle_console(args)

if __name__ == '__main__':
    main()
