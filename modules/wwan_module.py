#  Created on: Oct 7, 2023
#  Author: selina

import subprocess

class wwan:
    # Contructor function
    def __init__(self):
        # Module connect's status
        self.module_connect = 0
        # nmcli module number
        self.module_id = 1
        # Connect status
        self.net_status = 0
        # Sim's connection tech (LTE, 3G)
        self.connect_tech = ""
        # Module's signal quality (-1: No Signal, 0-100%: signal percent)
        self.signal = 0
        # Sim's phone number
        self.phoneNum = ""
        # Sim's network operator name
        self.operator = ""    
        if(self.check_module_connect()):
            self.get_info()
        
    def check_module_connect(self):
        try:
            responce = subprocess.check_output("mmcli -L", shell=True)
            responce = responce.decode()
            # print(responce)

            if (responce != "No modems were found"):
                self.module_connect = 1       
                self.module_id = int(responce[41])   
                print("") 
                print("Found module at id: ", self.module_id)
                return 1
                # print(type(self.module_id))
            else:
                print("No wwan card found")
                self.module_connect = 0 
                return 0
        except:
            print("No wwan card found")
            self.module_connect = 0
            return 0

        

    def get_status(self):
        if(self.module_connect):
            command = "mmcli -m " + str(self.module_id)
            responce = subprocess.check_output(command, shell=True)
            responce = responce.decode()
            # print(responce)
            responce = responce.replace(":", " ")
            responce = responce.replace("\n", " ")
            responce = responce.replace("-", " ")
            responce = responce.replace("|", " ")
            responce = responce.replace("[0m", " ")
            responce = responce.replace("[32m", " ")
            responce = responce.replace("\x1b", " ")
            analysis = responce.split("  ")
            # print(analysis)

            result = []
            for i in range(len(analysis)):
                if(analysis[i] != ''):
                    result.append(analysis[i])
            # print(result)
            for i in range(len(result)):
                if(result[i][0] == ' '):
                    result[i] = str(result[i]).replace(' ', '', 1)
            # print(result)
                
            # print(result.index('state'))

            self.operator = result[(result.index('operator name') + 1)]

            if(result[(result.index('state') + 1)] != "connected"):
                self.net_status = 0
            else:
                self.net_status = 1

            if(self.operator == ""):
                self.signal = -1
            else:
                # ' signal quality'
                self.signal = str(result[(result.index('signal quality') + 1)]).replace("% (recent)", "")
                self.signal = self.signal.replace("% (cached)", "")

                self.phoneNum = result[(result.index('own') + 1)]
                self.connect_tech = str(result[(result.index('access tech') +1)]).upper()
            
    def get_info(self):
        self.get_status()
        print("WWAN information:")
        if(self.net_status == 1):
            print("+ Status: Connected")
            print("+ Phone number:", self.phoneNum)
            print("+ Network operator:", self.operator)
            if(self.signal == -1):
                print("+ Signal: No signal")
            else:    
                print("+ Connection tech:", self.connect_tech)
                print("+ Signal:", self.signal, "%")
        else:
            print("+ Status: Disconnected")
    
    def sendSMS(self, phoneNumber, Message):
        if(self.module_connect):
            if(self.signal != -1):
                command = "mmcli -m " + str(self.module_id) + " --messaging-create-sms=\"text='"+ str(Message) + "',number='"+ str(phoneNumber) +"'\""
                print(command)
                responce = subprocess.check_output(command, shell=True)
                responce = responce.decode()
                # Remove the last \n character
                responce = responce.replace("\n", "")

                print(responce)
                analysis = responce.split("/")
                # print(c[5])

                command = "mmcli -s " + str(analysis[5]) + " --send"
                print(command)
                try:
                    responce = subprocess.check_output(command, shell=True, timeout = 1000)
                    responce = responce.decode()
                except:
                    print("Send SMS Error")
                    return 0
                print(responce)
                if(responce == "successfully sent the SMS\n"):
                    print("Send SMS OK")
                    return 1
                else:
                    print("Send SMS Error")
                    return 0
            else:
                print("No signal")
        else:
            print("No wwan card found")
            return 0



                    # nmcli -f NAME,UUID,AUTOCONNECT,AUTOCONNECT-PRIORITY c

