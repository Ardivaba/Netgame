import sys
from server import Server
from client import Client

is_server = sys.argv[1] == "server"

net = None

if(is_server):
    net = Server(8085)
else:
    net = Client("localhost", 8085)

net.start_listening()
