import socket
import os
import math

se = socket.socket()

port = 5001

contype = input("Enter 1 for manual ip entering 2 for automatic ip configuration : ")
if contype == "1":
    hostip = input("Enter virtual network ip : ")
elif contype == "2":
    hostip = socket.gethostbyname(socket.gethostname())

se.bind((hostip,port))
se.listen(1)
print("Host Adress : " + str(hostip))
print("Port : " + str(port))
print("waiting for any incoming connections..")


conn, addr = se.accept()
print(addr,"Has connected to the server")


def filetransfer():
    try:
        filedata = file.read(1024)
        conn.send(filedata)
        print("Data transmitted succesfully")
    except socket.error as msg:
        print("File couldn't found " + str(msg) + "\n" + "Retry...")
        filetransfer()



filename = input(str("Enter the name of the file to send: "))
if filename[-4:] == ".png":
    c = os.path.getsize(filename)
    # print(c)
    CHUNK_SIZE = math.ceil(math.ceil(c) / 5)
    # print(CHUNK_SIZE)
    index = 1
    with open(filename, 'rb') as infile:
        chunk = infile.read(int(CHUNK_SIZE))
        while chunk:
            chunkname = filename[0:-4] + '_' + str(index)
            print("chunk name is: " + chunkname + "\n")
            with open(chunkname, 'wb+') as chunk_file:
                chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))
    chunk_file.close()
    i = 0
    while (i < 5):
        file = open(chunkname,'rb')
        filetransfer()
        i += 1
else:
    file = open(filename, 'rb')
    filetransfer()


