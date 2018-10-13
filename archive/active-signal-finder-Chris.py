from scapy.all import *
import threading
import time
import sys

lastdb = -100


def setLastdb(db):
    global lastdb
    lastdb = db


def getLastdb():
    global lastdb
    return lastdb


def PacketHandler(pkt):
  #print(pkt.summary())
  if pkt.haslayer(Dot11):
    if pkt.type == 0 and pkt.subtype == 8:
     if pkt.addr3 == sys.argv[2]:
        rssi = -(256-ord(pkt.notdecoded[-4:-3]))
        message = str(rssi-getLastdb()) + " dBm "
        if rssi > getLastdb():
          message += "hotter. "
        elif rssi <= getLastdb():
          message += "colder. "
        setLastdb(rssi)
        message += (pkt.info.decode() + ": " + pkt.addr3 + ", dBm " + str(rssi))
        print(message)

def broadcast():
  probePacket = RadioTap()/Dot11(type=0,subtype=4,addr1="ff:ff:ff:ff:ff:ff", addr2="00:11:22:33:44:55",addr3="ff:ff:ff:ff:ff:ff")/Dot11Elt(ID="SSID", info="")
  while True:
    sendp(probePacket, verbose = False)
    print("Probe sent")
    time.sleep(10)

def main():
  if len(sys.argv)!=3:
    print("Usage: python3 active-signal-finder-Chris.py <interface> <target BSSID>")
    return

  broadcastThread = threading.Thread(target=broadcast)
  broadcastThread.start()
  
  sniff(iface=sys.argv[1], prn = PacketHandler, store=0)
    
if __name__ == "__main__":
    main()
