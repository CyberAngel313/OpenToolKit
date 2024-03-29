import socket
from os import system

system("color 0a")

HOST = '127.0.0.1'
PORT = 8081

insesh = False

new_port = input('Input Host Port (Blank if default).')
if (new_port != "\n"):
    REMOTE_PORT = new_port

# Binding the IP to the Port
# Creating a Socket
server = socket.socket()
server.bind((HOST, PORT))

# Starting the Listener
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

# Sending and receiving commands in an infinite loop
while insesh == True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")