#! /usr/bin/env/ python3
from scapy.all import sniff, IP, TCP, UDP, ICMP
def packet_callback(packet):
    """
    This function is called for every packet that is sniffed.
    """
    # This will check if the packet has an IP layer
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)

        # This will print the source and destination ip addresses
        print(f"\n[+] Packet Captured!")
        print(f"     Source IP: {ip_layer.src}")
        print(f"     Destination IP: {ip_layer.dst}")
        
        # To check for different protocols
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"    Protocol: TCP")
            print(f"    Source Port: {tcp_layer.sport}")
            print(f"    Destination Port: {tcp_layer.dport}")
            payload = bytes(packet[TCP].payload)
            if payload:
                print(f"    Payload: {payload.hex()}")

        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"    Protocol: UDP")
            print(f"    Source Port: {udp_layer.sport}")
            print(f"    Destination Port: {udp_layer.dport}")
            payload = bytes(packet[UDP].payload)
            if payload:
                print(f"    Payload: {payload.hex()}")

        elif packet.haslayer(ICMP):
            icmp_layer = packet.getlayer(ICMP)
            print(f"    Protocol: ICMP (Type: {icmp_layer.type}, Code: {icmp_layer.code})")

def main():
    print("Starting packet sniffer... (Press Ctrl+C to stop)")
    sniff(iface="ens33", prn=packet_callback, store=0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping sniffer.")

