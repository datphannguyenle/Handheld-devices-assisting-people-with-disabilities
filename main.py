#  Created on: Oct 7, 2023
#  Author: selina

from hardware import *



print(hardware.wwan.phoneNum)
# hardware.wwan.sendSMS("0919806788", "Hello World")


# import platform

# # printing the Architecture of the OS
# print("[+] Architecture :", platform.architecture()[0])

# # Displaying the machine
# print("[+] Machine :", platform.machine())

# # printing the Operating System release information
# print("[+] Operating System Release :", platform.release())

# # prints the currently using system name
# print("[+] System Name :",platform.system())

# # This line will print the version of your Operating System
# print("[+] Operating System Version :", platform.version())

# # This will print the Node or hostname of your Operating System
# print("[+] Node: " + platform.node())

# # This will print your system platform
# print("[+] Platform :", platform.platform())

# # This will print the processor information
# print("[+] Processor :",platform.processor())

# # importing the required modules
# import psutil

# # writing a function to convert the bytes into gigabytes
# def bytes_to_GB(bytes):
#     gb = bytes/(1024*1024*1024)
#     gb = round(gb, 2)
#     return gb

# # gathering all network interfaces (virtual and physical) from the system
# if_addrs = psutil.net_if_addrs()

# # printing the information of each network interfaces
# for interface_name, interface_addresses in if_addrs.items():
#     for address in interface_addresses:
#         print("\n")
#         print(f"Interface :", interface_name)
#         if str(address.family) == 'AddressFamily.AF_INET':
#             print("[+] IP Address :", address.address)
#             print("[+] Netmask :", address.netmask)
#             print("[+] Broadcast IP :", address.broadcast)
#         elif str(address.family) == 'AddressFamily.AF_PACKET':
#             print("[+] MAC Address :", address.address)
#             print("[+] Netmask :", address.netmask)
#             print("[+] Broadcast MAC :",address.broadcast)

# # getting the read/write statistics of network since boot
# print("\n")
# net_io = psutil.net_io_counters()
# print("[+] Total Bytes Sent :", bytes_to_GB(net_io.bytes_sent))
# print("[+] Total Bytes Received :", bytes_to_GB(net_io.bytes_recv))