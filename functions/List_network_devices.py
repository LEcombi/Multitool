from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    """
    Scans the network for devices and returns their IP and MAC addresses.

    Args:
        ip_range (str): The IP range to scan (e.g., "192.168.1.1/24").

    Returns:
        list: A list of dictionaries containing device information.
    """
    # Create an ARP request packet
    arp_request = ARP(pdst=ip_range)
    # Create an Ethernet frame to broadcast the ARP request
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and ARP request
    packet = broadcast / arp_request

    # Send the packet and capture the responses
    answered, _ = srp(packet, timeout=2, verbose=False)

    devices = []
    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "name": received.psrc,
        })

    return devices


