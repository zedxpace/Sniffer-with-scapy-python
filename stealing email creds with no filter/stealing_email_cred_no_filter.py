from scapy.all import *

#callback function that will recieve each sniffed packet
def packet_callback(packet):
    print(packet.show())

#fire up the sniffer on all interfaces with no filtering
sniff(prn=packet_callback ,count=1)

'''
when the first packet was recieved on the network ,our callback function used the built-in function 'packet.show()'
to display the packet contents and to dissect some of the protocol information.
'''