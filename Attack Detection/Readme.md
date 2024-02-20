# ARP Spoof Detection with Scapy

## Introduction
This Python script is designed to detect ARP (Address Resolution Protocol) spoofing attacks on a local network. ARP spoofing is a type of cyber attack in which an attacker sends falsified ARP messages over a local area network. This results in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network. Once the attacker's MAC address is linked to an authentic IP address, the attacker will begin receiving any data that is intended for the legitimate computer.

The script uses the Scapy library, which is a powerful packet manipulation tool for Python. Scapy allows you to forge, dissect, send, and capture network packets.

## Prerequisites
- Python 3.x
- Scapy library

## Usage
1. Install the required library by running the following command:

```bash
pip install scapy
```
2. Save the script to a file with a `.py` extension, e.g., `arp_spoof_detection.py`.
3. Run the script using Python:
```bash
python arp_spoof_detection.py
```

## Code Overview
The script consists of two main functions: `get_mac` and `sniff`.

### `get_mac(ip)`
This function takes an IP address as input and returns the MAC address associated with that IP address. It uses the ARP protocol to send an ARP request packet to the specified IP address. The function constructs an ARP request packet using Scapy's `ARP` class and a broadcast Ethernet frame using Scapy's `Ether` class. It then sends the final packet using Scapy's `srp` function, which sends and receives packets at the same time. The `srp` function returns a list of two lists: the first list contains the packets that were answered, and the second list contains the packets that were unanswered. In this case, we are only interested in the answered packets, so we access the first list with `[0]`. The function then returns the MAC address of the target IP address.

### `sniff(interface)`
This function takes a network interface name as input and starts sniffing packets on that interface. It uses Scapy's `sniff` function, which captures packets off the wire and decodes them. The `sniff` function takes several arguments, including the interface to sniff on (`iface`), whether to store the captured packets (`store`), and a callback function to process each packet (`prn`). In this case, we pass the `process_sniffed_packet` function as the callback.

### `process_sniffed_packet(packet)`
This function is the callback function passed to the `sniff` function. It takes a packet as input and processes it. The function first checks if the packet has an ARP layer and if the ARP operation is a reply (`op == 2`). If both conditions are met, the function calls the `get_mac` function to get the real MAC address associated with the source IP address in the ARP packet. It then compares the real MAC address with the MAC address in the ARP packet. If they are different, it prints a message indicating that an ARP spoofing attack has been detected and displays the contents of the packet using Scapy's `show` method.

## Conclusion
This script demonstrates how to use the Scapy library to detect ARP spoofing attacks on a local network. By analyzing ARP packets and comparing the MAC addresses, the script can identify when an attacker is attempting to spoof the MAC address of a legitimate device. This can help network administrators take appropriate action to mitigate the attack and protect the integrity of the network.
