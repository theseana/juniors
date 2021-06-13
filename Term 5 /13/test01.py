import scapy.all as scapy


s = scapy


# s.UDP().show()
# s.TCP().show()
s.IP().show()
# s.Ether().show()

# s.ICMP().show()
# counter = 0



# s.IP(ttl=128).show()



# while True:
#     tcp = s.TCP(sport=700, dport=22)
#     ip = s.IP(src="192.168.100." + str(counter), dst="192.168.100.53")
#     ether = s.Ether()
#     s.sendp(ether/ip/tcp)