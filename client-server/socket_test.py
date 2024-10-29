import socket
import signal
import sys

running = True

def signal_handler(sig, frame):
    global running
    print("Closing server...")
    running = False

signal.signal(signal.SIGINT, signal_handler)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000)) #Port number and public host
#NOTE: bind only accepts one argument, hence the double parentheses
server_socket.settimeout(1)

server_socket.listen(5) #Number of queued connections allowed
print ("Server is listening...")

while running:
    try:
        client_socket, address = server_socket.accept()
        print(f"Connection incoming from {address}")
        data = client_socket.recv(128) #Buffer size is 128 bytes
        if not data:
            print("Client disconnected.")
            break

        message = data.decode('utf-8')
        print(f"Received: {message}")
        
        if message == "client:quit":
            print("Client at {address} is closing...")
            client_socket.close()

        else:
            client_socket.sendall(b""+data)
            
    except socket.timeout:
        continue
        
    except OSError as e:
        print("\n OSError: Server closing...")
        if not running:
            break

server_socket.close()
print("Server closed, goodbye.")
