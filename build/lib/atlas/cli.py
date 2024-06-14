import argparse
from tabulate import tabulate
from datetime import datetime
import traceback

from atlas.atlas import Atlas
from atlas.chart import Chart
from atlas.console import Console
from atlas.topo import Location
from atlas.chrono import utc

class CLI:
    def __init__(self):
        self.default_location = Location(51, 0, 0)
        self.chart_celestials = ['sun', 'moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto', 'lilith', 'selena', 'rahu']

    def handle_align(self, args):
        try:
            t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
        except:
            print("Invalid date, time or location")
            exit()

        atlas = Atlas() # Initializing Atlas

        targets = []
        for target in args.target:
            if target in atlas.celestial_symbols:
                targets.append(target)
            else:
                print(f"Invalid target: {target}")
                exit()

        results = atlas.create_celestials(t, args.location, targets)
        celestials = [[f"{result.symbol} {result.name}", f"{result.zodiac_symbol} {result.zodiac[:3]}", f"{result.zodiac_orb}°", "℞" if result.retrograde else ''] for result in results.values()]
        print(tabulate(celestials, headers=['Celestial', 'Zodiac', 'Orb', 'Retrograde']))

    def handle_observe(self, args):
        try:
            t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
        except:
            print("Invalid date, time or location")
            exit()

        atlas = Atlas() # Initializing Atlas

        targets = []
        for target in args.target:
            if target in atlas.celestial_symbols:
                targets.append(target)
            else:
                print(f"Invalid target: {target}")
                exit()

        results = atlas.create_celestials(t, args.location, targets)
        celestials = [[f"{result.symbol} {result.name}", f"{round(result.ra, 2)}°", f"{round(result.dec, 2)}", f"{round(result.distance, 2)}"] for result in results.values()]
        print(tabulate(celestials, headers=['Body', 'Right Ascension', 'Declination', 'Distance']))

    def handle_eclipse(self, args):
        try:
            t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
        except:
            print("Invalid date, time or location")
            exit()

        atlas = Atlas()
        
        if args.type == 'solar':
            eclipse = atlas.create_solar_eclipse(t, args.location)
        else:
            eclipse = atlas.create_lunar_eclipse(t, args.location)

        if args.type == 'solar':
            phases = [["First Contact", f"{eclipse.t_c1.month}/{eclipse.t_c1.day}/{eclipse.t_c1.year}" if eclipse.t_c1 else 'N/A', f"{eclipse.t_c1.hour}:{eclipse.t_c1.minute}" if eclipse.t_c1 else 'N/A'], 
                    ["Second Contact", f"{eclipse.t_c2.month}/{eclipse.t_c2.day}/{eclipse.t_c2.year}" if eclipse.t_c2 else 'N/A', f"{eclipse.t_c2.hour}:{eclipse.t_c2.minute}" if eclipse.t_c2 else 'N/A'], 
                    ["Maximum", f"{eclipse.t_max.month}/{eclipse.t_max.day}/{eclipse.t_max.year}" if eclipse.t_max else 'N/A', f"{eclipse.t_max.hour}:{eclipse.t_max.minute}" if eclipse.t_max else 'N/A'], 
                    ["Third Contact", f"{eclipse.t_c3.month}/{eclipse.t_c3.day}/{eclipse.t_c3.year}" if eclipse.t_c3 else 'N/A', f"{eclipse.t_c3.hour}:{eclipse.t_c3.minute}" if eclipse.t_c3 else 'N/A'], 
                    ["Fourth Contact", f"{eclipse.t_c4.month}/{eclipse.t_c4.day}/{eclipse.t_c4.year}" if eclipse.t_c4 else 'N/A', f"{eclipse.t_c4.hour}:{eclipse.t_c4.minute}" if eclipse.t_c4 else 'N/A']]
        else:
            phases = [["First Contact",  f"{eclipse.t_p1.month}/{eclipse.t_p1.day}/{eclipse.t_p1.year}" if eclipse.t_p1 else 'N/A', f"{eclipse.t_p1.hour}:{eclipse.t_p1.minute}" if eclipse.t_p1 else 'N/A'], 
                    ["Second Contact", f"{eclipse.t_u1.month}/{eclipse.t_u1.day}/{eclipse.t_u1.year}" if eclipse.t_u1 else 'N/A', f"{eclipse.t_u1.hour}:{eclipse.t_u1.minute}" if eclipse.t_u1 else 'N/A'],
                    ["Third Contact", f"{eclipse.t_u2.month}/{eclipse.t_u2.day}/{eclipse.t_u2.year}" if eclipse.t_u2 else 'N/A', f"{eclipse.t_u2.hour}:{eclipse.t_u2.minute}" if eclipse.t_u2 else 'N/A'], 
                    ["Maximum", f"{eclipse.t_max.month}/{eclipse.t_max.day}/{eclipse.t_max.year}" if eclipse.t_max else 'N/A', f"{eclipse.t_max.hour}:{eclipse.t_max.minute}" if eclipse.t_max else 'N/A'], 
                    ["Fourth Contact", f"{eclipse.t_u3.month}/{eclipse.t_u3.day}/{eclipse.t_u3.year}" if eclipse.t_u3 else 'N/A', f"{eclipse.t_u3.hour}:{eclipse.t_u3.minute}" if eclipse.t_u3 else 'N/A'],
                    ["Fifth Contact", f"{eclipse.t_u4.month}/{eclipse.t_u4.day}/{eclipse.t_u4.year}" if eclipse.t_u4 else 'N/A', f"{eclipse.t_u4.hour}:{eclipse.t_u4.minute}" if eclipse.t_u4 else 'N/A'],
                    ["Sixth Contact", f"{eclipse.t_p2.month}/{eclipse.t_p2.day}/{eclipse.t_p2.year}" if eclipse.t_p2 else 'N/A', f"{eclipse.t_p2.hour}:{eclipse.t_p2.minute}" if eclipse.t_p2 else 'N/A'],]

        type = [["Type", f"{eclipse.type}"], ["Magnitude", f"{round(eclipse.magnitude, 3)}"], ["Obscuration", f"{round(eclipse.obscuration, 3)}"], ["Gamma", f"{round(eclipse.gamma, 3)}"]]

        print(tabulate(type) + '\n') 
        print(tabulate(phases, headers=['Phase', 'Date', 'Time']))

    def handle_chart(self, args):
        try:
            t = utc(datetime.combine(args.date, args.time), args.location) if args.location else datetime.combine(args.date, args.time)
        except:
            print("Invalid date, time or location")
            exit()

        atlas = Atlas()

        houses = atlas.create_placidus(t, args.location)
        celestials = atlas.create_celestials(t,  args.location, self.chart_celestials)

        chart = Chart(houses, celestials)
        chart.generate(show=True, save=args.save)

    def handle_console(self):
        console = Console()
        console.start()

    def main(self):
        # Top level parser
        parser = argparse.ArgumentParser(description='Atlas | Swiss Ephemeris Interface')
        subparsers = parser.add_subparsers(dest='command')

        # 'Align' command
        align_parser = subparsers.add_parser('align', help='Find zodiac sign of a celestial body')
        align_parser.add_argument('target', help='Celestial body/bodies to observe', nargs='+')
        align_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
        align_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
        align_parser.add_argument('-l', '--location', help='Location of observation', nargs='?', default=self.default_location)

        # 'Observe' command
        observe_parser = subparsers.add_parser('observe', help='Observe celestial body')
        observe_parser.add_argument('target', help='Celestial body to observe', nargs='+')
        observe_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
        observe_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
        observe_parser.add_argument('-l', '--location', help='Location of observation', nargs='?', default=self.default_location)

        # 'Eclipse' command
        eclipse_parser = subparsers.add_parser('eclipse', help='Find next eclipse')
        eclipse_parser.add_argument('-e', '--type', help='Type of eclipse', nargs='?', default='solar')
        eclipse_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
        eclipse_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
        eclipse_parser.add_argument('-l', '--location', help='Location of observation', nargs='?', default=self.default_location)

        # 'Chart' command
        chart_parser = subparsers.add_parser('chart', help='Generate a chart')
        chart_parser.add_argument('-d', '--date', help='Date of observation', nargs='?', default=datetime.now().date().strftime('%Y-%m-%d'))
        chart_parser.add_argument('-t', '--time', help='Time of observation', nargs='?', default=datetime.now().time().strftime('%H:%M'))
        chart_parser.add_argument('-l', '--location', help='Location of observation', nargs='?', default=self.default_location)
        chart_parser.add_argument('-s', '--save', help='Save chart', action='store_true')

        # 'Console' command
        console_parser = subparsers.add_parser('console', help='Start the Atlas console')

        # Parse arguments
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
                geo_location = Location()
                if isinstance(args.location, str):
                    args.location = geo_location.locator(args.location)
                    print(f'Location: {args.location}')
                else:
                    args.location = self.default_location
            except Exception as e:
                print(f'Error: {e}')
                traceback.print_exc()
                exit()

        if args.command == 'align':
            self.handle_align(args)
        elif args.command == 'observe':
            self.handle_observe(args)
        elif args.command == 'chart':
            self.handle_chart(args)
        elif args.command == 'eclipse':
            self.handle_eclipse(args)
        elif args.command == 'console':
            self.handle_console()

if __name__ == '__main__':
    cli = CLI()
    cli.main()


def main():
    cli = CLI()
    cli.main()