from scapy.all import *


# Scope issue, doesn't update
lastdb = -100

def setLastdb(db):
    lastdb = db

def getLastdb():
    return lastdb

def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
    if pkt.type == 0 and pkt.subtype == 8 :
      if (pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp)):
        try:
            extra = pkt.notdecoded
            # Investigate RSSI
            rssi = -(256-ord(extra[-4:-3]))
        except:
            rssi = -1000
            print("Error recieved obtaining signal strength for " + pkt.addr2)
        if(pkt.addr2.find("ec:08:6b:bf:30:5a") != -1):
        ##if(1==1):
            print("WiFi signal strength:", rssi, "dBm of", pkt.addr2, pkt.info)
            if(getLastdb() > rssi):
                print("hot")
            elif(getLastdb() == rssi):
                print("no change")
            else:
                print("cold + " + str(rssi) + " " + str(getLastdb()))
            setLastdb(rssi)
sniff(iface="wlp0s20f0u1mon", prn = PacketHandler)
