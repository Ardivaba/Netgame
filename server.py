from _thread import *
import socket
from net import Net

class Server(Net):
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", port))

    def start_listening(self):
        thread.start_new_thread(accept_connections_thread)

    def accept_connections_thread(self):
        try:
            while True:
                data, address = self.sock.recvfrom(1024)
                print(data.decode())
        except KeyboardInterrupt:
            socket.close()
