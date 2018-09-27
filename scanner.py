import os 
import logging
from scapy.all import *
 
def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            print("Available SSID: %s" % (pkt.info))
 
sniff(iface ="mon0", prn =PacketHandler)