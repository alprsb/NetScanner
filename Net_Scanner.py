import scapy.all as scapy
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest = "ip_adress",help = "help")
    (user_input,argument) = parse_object.parse_args()
    if not user_input.ip_adress:
        print("Enter IP adress:")
    return user_input
def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst = str(ip))
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout = 1)
    answered_list.summary()

print("Scannig is started...")
user_ip_adress = get_user_input()
scan_my_network(user_ip_adress.ip_adress)
