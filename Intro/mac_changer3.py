#!/usr/bin/env python

import subprocess

#variable declaration

interface= raw_input("interface > ")
new_mac = raw_input("new_mac> ")

print(" [+] Changing MAC address for " + interface + " to " + new_mac)

# INSECURE MODE
#
# subprocess.call("ifconfig " + interface + " down ", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up ", shell=True)

#SECURE MODE
subprocess.call(["ifconfig", interface, "down",])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up",])
