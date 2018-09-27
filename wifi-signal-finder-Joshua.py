from scapy.all import *
import argparse


def setLastdb(db):
    global lastdb
    lastdb = db


def getLastdb():
    global lastdb
    return lastdb


def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            if (pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp)):
                try:
                    extra = pkt.notdecoded
                    # Investigate RSSI
                    rssi = -(256-ord(extra[-4:-3]))
                except:
                    rssi = -1000
                    print("Error recieved obtaining signal strength for ", pkt.addr2)
                if(pkt.addr2.find(access_point) != -1):
                    print("WiFi signal strength:", rssi, "dBm for", pkt.addr2 + ",", pkt.info.decode())
                    if(getLastdb() < rssi):
                        print("Hotter. Current:", str(rssi), "Last:", str(getLastdb()))
                    elif(getLastdb() == rssi):
                        print("No change. Current:", str(rssi))
                    else:
                        print("Colder. Current:", str(rssi), "Last:", str(getLastdb()))
                    setLastdb(rssi)


def main():
    global lastdbm, interface, access_point
    lastdb, interface, access_point = -100, 'wlan0mon', '34:fc:b9:0f:58:c0'
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', help='interface to use')
    parser.add_argument('-a', '--accesspoint', help='access point to track')
    parser.add_argument('-v', '--values', help='display default values for the interface and access point', action='store_true')
    args = parser.parse_args()
    if args.interface:
        interface = args.interface
    if args.accesspoint:
        access_point = args.accesspoint
    if args.values:
        print('Interface: %s\nAccess Point: %s' % (interface, access_point))
    sniff(iface=transport, prn = PacketHandler)


if __name__ == '__main__':
    main()
