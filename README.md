# Fox-Hunting
Initialization
plug in the wifi card, and forward it into vmware.
Then, use "ip addr" command to find the id of the wifi card.  Like wlan0, or wlp5s0
run : sudo airmon-ng start <interface>
If there was a failure, make sure the interface name is correct and NetworkManager is not running

Next: run: sudo python3 Scapy-enabled-file.py


