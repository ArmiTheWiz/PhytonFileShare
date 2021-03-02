from socket import socket, AF_INET, SOCK_DGRAM
import json
import datetime

PORT = 5000

s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', PORT))

while 1:
    data, addr = s.recvfrom(1024) #wait for a packet
    now = datetime.datetime.now()
    print(" got service announcement from \t", (data).decode())
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
    data = (data).decode()
    f = open("log.txt", "w+")
    f.write( data + " " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n" )
    f.close()
