#import requests
#from ftplib import FTP
import socket
#import dns.resolver

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))
#NOTE: clients use .connect(), servers use .bind()

while True:
    protocol_choice = input("Enter the protocol (HTTP/FTP/DNS/exit): ")
    if protocol_choice == "exit":
        print("Exiting...")
        client_socket.sendall(protocol_choice.encode('utf-8'))
        break;
    else:
        client_socket.sendall(protocol_choice.encode('utf-8'))
        response = client.socket.recv(1024) #1024 bytes for buffer
        print(f"Response: {response.decode('utf-8')}")
        
client_socket.close()
