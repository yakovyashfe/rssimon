#!/usr/bin/python

import rssi
import sys

interface = 'wlp2s0'

rssi_scanner = rssi.RSSI_Scan(interface)
ap_info = rssi_scanner.getAPinfo(sudo=True)

sys.exit(ap_info)
