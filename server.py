from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from os import listdir
import time
import sys

PORT = 7777
# FOLDER = "/home/pallavi/SEM_5/CN/Project/new/shareall"
SIP = '0.0.0.0'
def handle_client(client,FOLDER):
    print("thread started")
    files = listdir(FOLDER)
    print(files)
    for fl in files:
        fname = FOLDER + "/" + fl
        with open(fname, "rb") as f:
            l = f.read(4096)
            while (l):
                client.send(l)
                l = f.read(4096)
            time.sleep(0.5)
            client.send(b"$$qwertyuiopasdfghjklzxcvbnm,./")
            print("Sent 1 file")
    # client.send(b"$$$$")
    print("EOD")
    client.close()
    print("thread closed")


def serve(FOLDER):
    server = socket(AF_INET, SOCK_STREAM)
    addr = (SIP, PORT)
    server.bind(addr)
    server.listen(3)

    while True:
        cl, adr = server.accept()
        t = Thread(target=handle_client, args=(cl,FOLDER))
        t.start()
      



if __name__ == "__main__":
    serve(FOLDER)
