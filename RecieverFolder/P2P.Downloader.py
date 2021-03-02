import socket
import os
import math
import datetime

do = socket.socket()
i = 0
def connecttohost():
    try:
        log = open('log.txt','r')
        line = log.readline() # if called again will read the next line
        ba = line.find("<")+1
        bi = line.find(">")
        host = line[ba:bi]
        port = 5001
        do.connect((host,port))
        print("Connected to "+str(host))
    except socket.error as msg:
        print("Connection failed wrong host"+ str(msg) + "\n" + "Retry...")
        connecttohost1()

def connecttohost1(): # If not get the ip from log file connect manually
    try:
        host = input(str("Please enter the host adress of the sender : "))
        port = 5001
        do.connect((host, port))
        print("Connected to " + str(host))
    except socket.error as msg:
        print("Connection failed wrong host" + str(msg) + "\n" + "Retry...")
        connecttohost1()

connecttohost()

def filetransfer():
    try:
        filedata = do.recv(1024)
        file.write(filedata)
        file.close()
        print("File has recieved succesfully")
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        f = open("downloadlog.txt", "w+")
        f.write(filename + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    except socket.error:
        connecttohost()

log = open('log.txt','r')
line = log.readline() # if called again will read the next line
print(line[line.find("Files"):])
filename = input(str("Please enter a filename for the incoming file : "))
chunknames = [filename[0:-4] + '_1', filename[0:-4] + '_2', filename[0:-4] + '_3', filename[0:-4] + '_4',filename[0:-4] + '_5']
if filename[-4:] == ".png":
    while (i < 5):
        try:
            file = open(chunknames[i],'wb')
            filetransfer()
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            f = open("downloadlog.txt", "w+")
            now = datetime.datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            f.write(chunknames[i] + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.close()
            i += 1
        except socket.error as msg1:
            print("Chunk " + chunknames[i] + " cannot downloaded from online peers" + "\n")
            connecttohost() # if connection fail it will try to connect to the other peer
            # and because i is reserved at the beginning the chunk where connection lost will be downloaded again
    with open(filename, 'wb') as outfile:
        for chunk in chunknames:
            with open(chunk) as infile:
                outfile.write(infile.read())
else:
    file = open(filename, 'wb')
    filetransfer()

