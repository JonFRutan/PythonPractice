import re, sys
from socket import *

args = sys.argv
if len(args) > 1:
    port_number = int(args[1])
else: 
    print("Usage: \n> python3 Server.py port")
    print("*Remember to use a port of at least 4 digits*")
    exit()

init_socket = socket(AF_INET, SOCK_STREAM)
init_socket.bind((gethostname(), port_number))
init_socket.listen()
print(f"Listening on port {port_number}...")

running = True
while running:
    #Stuff while running here...
    print("Server started. Exiting...")
    exit()
