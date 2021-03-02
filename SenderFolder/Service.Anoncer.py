
from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, gethostbyname, gethostname
import json
import glob

PORT = 5000

my_ip= gethostbyname(gethostname())
print(my_ip)
"""
if (my_ip[-2]=="."):
    broadcast_ip = my_ip[:-2]+".255"
elif (my_ip[-3]=="."):
    broadcast_ip = my_ip[:-3]+".255"
elif (my_ip[-4] == "."):
    broadcast_ip = my_ip[:-4] + ".255"
# Broadcast IP programmed its last decimal is .255 now
"""
broadcast_ip = my_ip
username = input(str("Enter username : "))
s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', 0))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #this is a broadcast socket

def filebrowser(ext=""):
    # Returns files with an extension
    return [f for f in glob.glob(f"*{ext}")]

text = filebrowser(".txt")
png = filebrowser(".png")
filesinfolder = text + png
contents = json.dumps({"Username": username, "Files": filesinfolder})

while 1:
    data = (" --<"+ broadcast_ip +">-- "+contents).encode()
    s.sendto(data, (broadcast_ip, PORT))
    print("sent service announcement")
    sleep(5)