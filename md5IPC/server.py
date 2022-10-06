import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
START_MESSAGE = "!START"
CONNECTION_NUMBER = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []


def handle_client(conn, addr, index):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:  # receive message from this client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            elif msg == START_MESSAGE:
                end_num = (index + 1) * 9999999999/len(connections) - 1
                start_num = index * 9999999999/len(connections)
                conn.send(f"{start_num}, {end_num}").encode(FORMAT)
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        connections[CONNECTION_NUMBER] = conn
        CONNECTION_NUMBER += 1
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
