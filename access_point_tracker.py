import argparse
import datetime
from access_points import get_scanner


def scan(all, clear, tracked_bssid):
    last_quality = 0
    wifi_scanner = get_scanner()
    print('All Access Points:\n%s\n' % wifi_scanner.get_access_points() if all else '', end='')
    print('Tracking %s' % tracked_bssid)
    try:
        while True:
            for ap in wifi_scanner.get_access_points():
                if ap.bssid == tracked_bssid:
                    if (last_quality < ap.quality):
                        print('\rHotter | %s @ %s' % (ap, datetime.datetime.now().time()), end='')
                    elif (last_quality > ap.quality):
                        print('\rColder | %s @ %s' % (ap, datetime.datetime.now().time()), end='')
                    else:
                        print('\rSame   | %s @ %s' % (ap, datetime.datetime.now().time()), end='')
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