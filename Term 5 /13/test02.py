#!/usr/bin/python
from scapy.all import * 

s = scapy.all


TIMEOUT = 2
conf.verb = 0
for ip in range(0, 256):
    packet = s.IP(dst="192.168.100." + str(ip), ttl=128)/s.ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    if not (reply is None):
         print(reply.dst, "is online")
    else:
         print("Timeout waiting for %s" % packet[s.IP].dst)