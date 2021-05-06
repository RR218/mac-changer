#!/usr/bin/env python2

import subprocess
import optparse

import re
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, argumentsgit) = parser.parse_args()

    if not options.interface:

        subprocess.call(["ifconfig"])
        # Interface = input("please specify the interface:\n\n")
        # New_mac = input("\nplease specify a new MAC address:\n\n")
        # subprocess.call(["sudo", "ifconfig", Interface, "down"])
        # subprocess.call(["sudo", "ifconfig", Interface, "hw", "ether", New_mac])
        # subprocess.call(["sudo", "ifconfig", Interface, "up"])
        # print("\n[+] Changing MAC for " + str(Interface) + " to: " + str(New_mac) + "\n")
        # time.sleep(2)
        # exit(("\n[+] MAC address was successfully changed to: " + str(New_mac)))

        
        exit("\n[-] Please specify an interface with -i followed by new MAC with -m."
                    "\nEXAMPLE: python mac_changer.py -i eth0 -m 00:11:22:33:44:55"
                    "\nUse --help for more info.")

    return options


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    print("")
    print(ifconfig_result)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)

    else:
        parser = optparse.OptionParser()
        print("[-] ERROR: CURRENT MAC NOT FOUND\n")
        subprocess.call(["ifconfig"])
        parser.error("\n[-] Could not read current MAC address in stated interface."
        "\nPlease specify an interface with -i followed by new MAC with -m."
        "\nEXAMPLE: python mac_changer.py -i eth0 -m 00:11:22:33:44:55"
        "\nUse --help for more info.")


def change_mac(interface, new_mac):
    print("[+] Changing MAC for " + interface + " to " + new_mac)

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC:" + str(current_mac))
print("")
change_mac(options.interface, options.new_mac)

current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + str(current_mac))
else:
    print("[-] MAC address was not successfully changed.\n")
    print("[-] Please review the arguments and specify an interface with -i followed by new MAC with -m.\n")
    print("    EXAMPLE: python mac_changer.py -i eth0 -m 00:11:22:33:44:55\n")    
    print("    Use --help for more info.\n")    
