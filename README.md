# Fox-Hunting

## Initialization
* Plug in the wifi card, and forward it into vmware.
* Use `ip addr` to find the id of the wifi card. Like `wlan0`, or `wlp5s0`.
* `sudo airmon-ng start <interface>`
* If there was a failure, make sure the interface name is correct and NetworkManager is not running.
* `sudo python3 Scapy-enabled-file.py`

## Usage
```
usage: wifi-signal-finder.py [-h] [-i INTERFACE] [-a ACCESSPOINT] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        interface to use
  -a ACCESSPOINT, --accesspoint ACCESSPOINT
                        access point to track
  -v, --values          display default values for the interface and access
                        point
```