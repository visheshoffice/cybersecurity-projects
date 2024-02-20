import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Input the interface who's value need to be changed")
	parser.add_option("-m", "--mac", dest="new_mac_address", help="Input the new MAC address for the interface")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("please enter an interface vale (Use --help to know more)")
	elif not options.new_mac_address:
		parser.error("please enter the new MAC vale (Use --help to know more)")
	return options

def change_mac(interface, new_mac_address):
	print("Changing the original MAC address of "+interface+" to new MAC address: "+new_mac_address)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
	subprocess.call(["ifconfig", interface, "up"])

def current_mac(interface):
	if_config_result = subprocess.check_output(["ifconfig", options.interface])
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(if_config_result))
	if mac_address_search_result:
		print(mac_address_search_result.group(0))
	else:
		print("Unable to read MAC address")

options = get_arguments()
the_current_mac = current_mac(options.interface)
print("Current MAC: "+ str(the_current_mac))

change_mac(options.interface, options.new_mac_address)

the_current_mac = current_mac(options.interface)
if the_current_mac == options.new_mac_address:
	print("MAC address has been successfully changed")
else:
	print("MAC address has NOT been changed")