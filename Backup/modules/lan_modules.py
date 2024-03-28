#  Created on: Oct 10, 2023
#  Author: selina

import subprocess
import wifimangement_linux

class lan:
    def __init__(self):
        # LAN connection status
        self.net_status = 0
        # LAN connection tech (wireless LAN, ethernet)
        self.connect_tech = ""
        # Module signal status (-1: No Signal, 0-100%: signal quality (percent), -2: Ethernet)
        self.signal = 0
        # LAN conenction name
        self.connection_name = ""

        self.get_info()

    def get_status(self):
        responce = wifimangement_linux.interface_status()
        # print(responce)

        responce = responce.replace('\n', ' ')
        analysis = responce.split('  ')
        result = []
        for i in range(len(analysis)):
            if(analysis[i] != ''):
                result.append(analysis[i])
        # print(result)

        if(result[6] == 'connected'):
            self.net_status = 1
        else:
            self.net_status = 0

        self.connect_tech = str(result[5]).title().replace(' ', '')
        # print(self.connect_tech)
        self.connection_name = str(result[7]).replace(' ', '', 1)
        
        command = "nmcli connection modify \""+ self.connection_name + "\" connection.autoconnect-priority 10"
        subprocess.check_output(command, shell=True)

        if(self.connect_tech == 'Wifi'):
            self.get_wifi_signal()
        elif(self.connect_tech == "Ethernet"):
            self.signal = -2
        else: 
            self.signal = -1
        # print(responce)

    def get_info(self):
        self.get_status()

        print("LAN information:")
        if(self.net_status == 1):
            print("+ Network Status: Connected")
            print("+ Connection tech:", self.connect_tech) 
            if(self.signal != -2):
                print("+ Signal:", self.signal, "%")
            print("+ Connection name:", self.connection_name)
        else:
            print("+ Status: Disconnected")
        
    def get_wifi_signal(self):
        if(self.connect_tech == "Wifi"):
            # pass
            responce = subprocess.check_output("iwconfig", shell=True)
            responce = responce.decode()
            print(responce)
            responce = responce.replace("\n", " ")
            responce = responce.replace(":", " ")
            responce = responce.replace("=", "  ")

            analysis = responce.split("  ")
            result = []
            for i in range(len(analysis)):
                if(analysis[i] != ''):
                    result.append(analysis[i])
            for i in range(len(result)):
                if(result[i][0] == ' '):
                    result[i] = str(result[i]).replace(' ', '', 1)

            # print(result)
            signal_dBm = str(result[(result.index('Signal level') + 1)]).replace(" dBm", "")
            # print(signal_dBm)
            try:
                signal_dBm = int(signal_dBm)
                if(signal_dBm <= -100):
                    self.signal = 0
                elif(signal_dBm >= -50):
                    self.signal = 100
                else:
                    # print("cal signal")
                    self.signal = 2 * (signal_dBm + 100)
            except:
                print("Analysis signal errror")
            
# DEVICE          TYPE      STATE         CONNECTION   
# wlp4s0          wifi      connected     DAI GIA DINH 
# p2p-dev-wlp4s0  wifi-p2p  disconnected  --           
# eno1            ethernet  unavailable   --           
# lo              loopback  unmanaged     -- 


# DEVICE          TYPE      STATE         CONNECTION         
# eno1            ethernet  connected     Wired connection 1 
# wlp4s0          wifi      connected     LVHN               
# p2p-dev-wlp4s0  wifi-p2p  disconnected  --                 
# lo              loopback  unmanaged     --                 

# <class 'str'>