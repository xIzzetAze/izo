import socket

# Dinleyici IP ve port
server_ip = '192.168.80.135'  # Sunucu IP'si, '0.0.0.0' tüm gelen bağlantıları kabul eder
server_port = 9999     # Sunucu portu

# Socket oluşturuluyor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(1)

print(f"Dinleyici başlatıldı {server_ip}:{server_port}")
client_socket, client_address = server.accept()
print(f"Bağlantı alındı: {client_address}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        break
    client_socket.send(command.encode())
    response = client_socket.recv(4096)
    print(response.decode(), end="")

client_socket.close()
server.close()