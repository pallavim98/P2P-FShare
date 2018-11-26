from socket import socket, AF_INET, SOCK_STREAM
import os

PORT = 7777


def cli(IP,FOLDER):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((IP, PORT))
    ii = 0
    f = open("%s/File-%d" % (FOLDER, ii), 'wb')
    alldata = b""
    data = client.recv(4096)
    while data:
        if data == b"$$qwertyuiopasdfghjklzxcvbnm,./":
            print("file end")
        alldata += data
        data = client.recv(4096)

    files = alldata.split(b"$$qwertyuiopasdfghjklzxcvbnm,./")
    print("No. of files:", len(files))
    for ii, fl in enumerate(files):
        if not fl:
            continue
        with open("%s/File-%d" % (FOLDER, ii), 'wb') as f:
            f.write(fl)
        print("1 file written")
        
# method2
    """
    while True:
        if data == b"$$$$":
            print("All files received")
            break
        if data == b"$$":
            print("1 file received")
            f.close()
            ii += 1
            f = open("%s/File-%d" % (FOLDER, ii), 'wb')
            continue
        f.write(data)
    """
    # return ii
    # os.remove("%s/File-%d" % (FOLDER, ii))

    return "All files received"
