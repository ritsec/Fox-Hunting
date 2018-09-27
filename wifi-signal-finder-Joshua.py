from scapy.all import *


def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
    if pkt.type == 0 and pkt.subtype == 8 :
      if (pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp)):
        try:
            extra = pkt.notdecoded
            rssi = -(256-ord(extra[-4:-3]))
        except:
            rssi = -1000
            printf("Error recieved obtaining signal strength for " + pkt.addr2)
        if(pkt.addr2.find("34:fc:b9:09:e0:80") != -1):
            print "WiFi signal strength:", rssi, "dBm of", pkt.addr2, pkt.info

sniff(iface="wlp0s20f0u1mon", prn = PacketHandler)
