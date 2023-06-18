import socket
import struct
import fcntl
import os
import netifaces

def set_promiscuous_mode(interface):
    SIOCGIFFLAGS = 0x8913
    SIOCSIFFLAGS = 0x8914

    # Get current interface flags
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ifreq = struct.pack('16sH', interface.encode('utf-8'), 0)

    try:
        flags = fcntl.ioctl(sock.fileno(), SIOCGIFFLAGS, ifreq)
        current_flags = struct.unpack('16sH', flags)[1]

        # Set interface to promiscuous mode
        ifreq = struct.pack('16sH', interface.encode('utf-8'), current_flags | 0x100)  # Set IFF_PROMISC flag
        fcntl.ioctl(sock.fileno(), SIOCSIFFLAGS, ifreq)
        sock.close()

        return True
    except OSError:
        return False

def sniff_packets(interface):
    # Create a raw socket and bind it to the network interface
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((interface, 0))

    # Include IP headers in the captured packets
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Enable promiscuous mode on the socket
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        # Receive a packet
        packet = s.recvfrom(65565)
        raw_packet = packet[0]

        # Process the raw packet as needed
        # Example: Print the packet's hexadecimal representation
        print(raw_packet.hex())

# Get all available network interfaces
interfaces = netifaces.interfaces()

# Find the first valid interface and set it to promiscuous mode
for interface in interfaces:
    print(f"Interface {interface} set to promiscuous mode.")
    sniff_packets(interface)
