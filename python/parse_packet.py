import logging
import sys
import logging.handlers
from scapy.all import *
import pprint
import json

def print_packets(pcap):
    # For each packet in the pcap process the contents
    # Print out the timestamp in UTC
    pkt_structure = {}
    pcap_dict = {}
    pkt_counter = 0
    for pkt in pcap:
        pkt_structure[pkt_counter] = {}
        if pkt.haslayer(Ether):
            pkt_structure[pkt_counter]['src_mac'] =  str(pkt.getlayer(Ether).src)
            pkt_structure[pkt_counter]['dst_mac'] =  str(pkt.getlayer(Ether).dst)
            pkt_structure[pkt_counter]['ethtype'] =  str(hex(pkt.getlayer(Ether).type))
            if pkt.haslayer(Dot1Q):
                pkt_structure[pkt_counter]['outer_vlan_id'] = int(pkt[Dot1Q:1].vlan)
                try:
                    if  pkt[Dot1Q:3].vlan:
                        pkt_structure[pkt_counter]['inner_most_vlan_id'] = int(pkt[Dot1Q:3].vlan)
                except:
                    log.info('Third VLAN does not exist')

                try:
                    if  pkt[Dot1Q:2].vlan:
                        pkt_structure[pkt_counter]['inner_vlan_id'] = int(pkt[Dot1Q:2].vlan)
                except:
                    log.info('Second VLAN does not exist')
        if pkt.haslayer(IP):
            log.info('This is an IP Packet')
            ip = pkt.payload
            pkt_structure[pkt_counter]['src_ip'] = str(ip.src)
            pkt_structure[pkt_counter]['dst_ip'] = str(ip.dst)
            pkt_structure[pkt_counter]['pkt_ttl'] = int(ip.ttl)
            pkt_structure[pkt_counter]['tos'] = str(ip.tos)
            if ip.proto == 1:
                log.info('This is an ICMP Packet')
                icmp = ip.payload
                pkt_structure[pkt_counter]['ip_proto'] = 'ICMP'
                pkt_structure[pkt_counter]['type'] = int(icmp.type)
                pkt_structure[pkt_counter]['code'] = int(icmp.code)
                pkt_structure[pkt_counter]['checksum'] = hex(icmp.chksum)
            if ip.proto == 6:
                log.info('This is an TCP Packet')
                tcp = ip.payload
                pkt_structure[pkt_counter]['ip_proto'] = 'TCP'
                pkt_structure[pkt_counter]['src_port'] = int(tcp.sport)
                pkt_structure[pkt_counter]['dst_port'] = int(tcp.dport)
                pkt_structure[pkt_counter]['checksum'] = hex(tcp.chksum)
                pkt_structure[pkt_counter]['tcp_window'] = int(tcp.window)
            if ip.proto == 17:
                log.info('This is an UDP Packet')
                udp = ip.payload
                pkt_structure[pkt_counter]['ip_proto'] = 'UDP'
                pkt_structure[pkt_counter]['src_port'] = int(udp.sport)
                pkt_structure[pkt_counter]['dst_port'] = int(udp.dport)
                pkt_structure[pkt_counter]['checksum'] = hex(udp.chksum)
                
        pkt_counter =  pkt_counter + 1
    return pkt_structure

def test(pcap_file):
    packets = rdpcap(pcap_file)
    json_data = json.dumps(print_packets(packets))
    print json_data

def usage():
	print "\n Usage: python parse_packet.py <FILENAME>"


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    handler = logging.handlers.SysLogHandler(address = '/dev/log')
    formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    if (len(sys.argv) == 2):
        test(sys.argv[1])
    else:    
        usage()
        sys.exit()
