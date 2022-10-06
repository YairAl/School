import socket

import md5
from md5 import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def main():
    while True:
        msg = input("Would You Like To Begin?: (Y/N )")
        if msg == "Y":
            send("!START")
            start_num, end_num = client.recv(2048).decode(FORMAT)
            thread = threading.Thread(target=md5.MD5, args=(start_num, end_num))
            thread.start()


send(DISCONNECT_MESSAGE)

if __name__ == '__main__':
    main()
