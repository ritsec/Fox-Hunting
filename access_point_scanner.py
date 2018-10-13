from access_points import get_scanner


def main():
    wifi_scanner = get_scanner()
    for ap in wifi_scanner.get_access_points():
        print(ap)


if __name__ == '__main__':
    main()