import socket

running = True
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter host IP or localhost: ")
port = int(input("Enter the port (8000 default): "))
client_socket.connect((host, port))

while running:
    message = input("> ")
    if message == "q":
        running = False
        client_socket.sendall("client:quit".encode('utf-8'))
        print("Exiting...")
    else:
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(128)
        print(f"System: {data.decode('utf-8')}")
    
client_socket.close()
