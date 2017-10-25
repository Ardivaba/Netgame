import socket
from net import Net

class Client(Net):
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sendto("Hello".encode(), (ip, port))
