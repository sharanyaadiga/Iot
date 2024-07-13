# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
import network
import time
import ubinascii


from wifikeys import ssid
from wifikeys import key


import dht
import machine

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points
wlan.isconnected()      # check if the station is connected to an AP
wlan.connect(ssid, key) # connect to an AP
wlan.config('mac')
print('------ifconfig----------------')# get the interface's MAC address
print(wlan.ifconfig())         # get the interface's IP/netmask/gw/DNS addresses
print('---------------------------')

print('-----------Sensor Readout----------------')
d = dht.DHT22(machine.Pin(4))
d.measure()

print('Temperature and Humidity is: ')
print(d.temperature()) # eg. 23 (°C)
print(d.humidity())

"""ap = network.WLAN(network.AP_IF) # create access-point interface
ap.active(True)         # activate the interface
ap.config(ssid='ESP-AP') # set the SSID of the access point"""
