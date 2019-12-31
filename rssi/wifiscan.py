#!/usr/bin/python
import rssi
import sys

interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['100so']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=False)

# print(ap_info)
sys.exit(ap_info)
