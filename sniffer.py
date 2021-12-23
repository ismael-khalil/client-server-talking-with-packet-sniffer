import scapy.all as scapy  #imported scapy library
def sniffer():
    number = 1
    result = scapy.sniff(count=number, filter="port 6666")   # telling scapy to sniff only the number of packets
                                                                # specified in the previous step and which port number to
                                                                #be used,which is the port number that packets is sent on it.
    for i in range(0, number):  # one time loop (because we need 1 packet each time) to show the complete result of the sniffed packet
        result[i].show()

