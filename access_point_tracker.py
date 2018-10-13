import argparse
import datetime
from access_points import get_scanner


def scan(all, clear, tracked_bssid):
    last_quality, message = 0, ''
    wifi_scanner = get_scanner()
    print('All Access Points:\n%s\n' % wifi_scanner.get_access_points() if all else '', end='')
    print('Tracking %s' % tracked_bssid)
    try:
        while True:
            for ap in wifi_scanner.get_access_points():
                if ap.bssid == tracked_bssid:
                    if (last_quality < ap.quality):
                        message = 'Hotter'
                    elif (last_quality > ap.quality):
                        message = 'Colder'
                    else:
                        message = 'Same  '
                    print('%s%s  | %s @ %s' % ('\r' if clear else '', message, ap, datetime.datetime.now().time()), end=('' if clear else '\n'))
                    last_quality = ap.quality
    except KeyboardInterrupt:
        print('Halting Scanning')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('bssid', help='the bssid to track', type=str)
    parser.add_argument('-a', '--all', help='print all available access points', action='store_true')
    parser.add_argument('-c', '--clear', help='clear tracking line on each update', action='store_true')
    args = parser.parse_args()
    scan(args.all, args.clear, args.bssid)


if __name__ == '__main__':
    main()