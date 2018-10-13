from access_points import get_scanner

wifi_scanner = get_scanner()
for ap in wifi_scanner.get_access_points():
    print(ap)