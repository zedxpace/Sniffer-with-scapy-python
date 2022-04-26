from scapy.all import *

#callback function that will recieve each sniffed packet
def packet_callback(packet):
    print(packet.show())

#fire up the sniffer on all interfaces with no filtering
sniff(prn=packet_callback ,count=1)
