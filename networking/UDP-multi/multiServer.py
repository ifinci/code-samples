import socket
import time

ANY = "0.0.0.0"
SENDERPORT=1501
MCAST_ADDR = "224.168.2.9"
MCAST_PORT = 1600

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#The sender is bound on (0.0.0.0:1501)
sock.bind((ANY,SENDERPORT))
#Tell the kernel that we want to multicast and that the data is sent
#to everyone (255 is the level of multicasting)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
#seting the sockets timeout to 0.0, to make it non-blocking, so we can check if someone sent us a reply
sock.settimeout(0.0)
i = 0
while 1:
    try:
        time.sleep(0.5)
        #send the data "hello, world" to the multicast addr: port
        #Any subscribers to the multicast address will receive this data
        sock.sendto("Hello World "    + str(i), (MCAST_ADDR,MCAST_PORT) );
        i=i+1
    except socket.error, e:
        pass
    
    