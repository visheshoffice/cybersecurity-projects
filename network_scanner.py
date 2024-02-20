import scapy.all as scapy
import argparse

def get_arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range.")
	options=parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	final_packet = broadcast/arp_request
	answered_list = scapy.srp(final_packet, timeout=1, verbose=False)[0]
	
	clients_list=[]
	for element in answered_list:
		client_dict={"ip":element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def printing(result_list):
	print("IP\t\t\tMAC Address\n-----------------------------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])

options=get_arguments()
scan_result= scan(options.target)
print(options.target)
printing(scan_result)