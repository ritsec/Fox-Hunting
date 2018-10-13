# Fox-Hunting

## Idea
You have a rogue access point.  You take the bssid, and use the signal strength to locate said access point.


## Initialization
`pip3 install access_points --user`

On linux systems you might want to install nmcli (recommended) or iwlist:
```
apt-get install network-manager # Ubuntu
pacman -S networkmanager        # Arch Linux
```


## Usage
```
usage: access_point_tracker.py [-h] [-a] [-c] [-s] bssid

positional arguments:
  bssid        the bssid to track

optional arguments:
  -h, --help   show this help message and exit
  -a, --all    print all available access points
  -c, --clear  clear tracking line on each update
  -s, --same   hide same updates
```
