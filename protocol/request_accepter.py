import socket
#import dns.resolver
from ftplib import FTP

def protocol_handler(protocol):
    match protocol:
        case "HTTP":
            return "Handling HTTP..."
        case "FTP":
            return "Handling FTP..."
        case "DNS":
            return "Handling DNS..."
        case _:
            return "Error..."


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(5)
print("Listening...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection made from {address}") #Here, 'f' means that when '{}' are found to use variable values for output.
    #NOTE: Since python can return a tuple, we can respectively assign the returned values to multiple variables.
    #In this case, .accept() returns the client_socket object, and a tuple of the address {"ip", portNumber}
    if not address:
        client_socket.close()
        break;
    #This is an example of handling a connection via the address.
    data = client_socket.recv(1024)
    protocol = data.decode('utf-8')
    #NOTE: utf-8 is the current standard for character exchange, supporting 1-4 bytes for character assignment.
    #NOTE: 'match' statements are functionally equivalent to switch statements, and are only supported by Python 3.10+
    if protocol == "exit":
        print("Client exiting...")
        break;
    else:
       response = protocol_handler(protocol)
       print(response)

client_socket.close()
print("Finished.")        

