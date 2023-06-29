import socket

server = socket.socket()

host = socket.gethostbyname(socket.gethostname())
port = 9090

server.bind((host, port))

server.listen(1)
client, addr = server.accept()

print(f"{addr} Connected to the server!")
print("""
      ==================================
                MAC:
                full name: id -F
                CPU info: sysctl -a | grep machdep.cpu
      
                WINDOWS:
                name: whoami
                list fies in directory: dir
      """)

while True:
    command = input("Enter command: ")
    client.send(command.encode())
    print("sent")
    
    output = client.recv(1024).decode()
    print(f"Output:\n {output}")