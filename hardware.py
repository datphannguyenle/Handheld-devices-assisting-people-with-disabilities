#  Created on: Oct 10, 2023
#  Author: selina

from modules import lan_modules
from modules import wwan_module
from modules import bluetooth_module

class network():
    lan = lan_modules.lan()
    wwan = wwan_module.wwan()
    bluetooth = bluetooth_module.bluetooth()

    def __init__(self):
        pass
        # # Network status
        # self.status = 0
        # # Connection tech
        # self.connect_tech = ""
        # # RSSI (-1: No Signal, 0-100%: signal percent)
        # self.signal = 0
        
class hardware(network):
    pass