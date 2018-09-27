from scapy.all import *


lastdb = -100


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
        if(pkt.addr2.find("34:fc:b9:0f:58:c0") != -1):
        ##if(1==1):
            print("WiFi signal strength:", rssi, "dBm for", pkt.addr2 + ",", pkt.info.decode())
            if(getLastdb() < rssi):
                print("Hotter. Current:", str(rssi), "Last:", str(getLastdb()))
            elif(getLastdb() == rssi):
                print("No change. Current:", str(rssi))
            else:
                print("Colder. Current:", str(rssi), "Last:", str(getLastdb()))
            setLastdb(rssi)


sniff(iface="wlan0mon", prn = PacketHandler)
