import socket
from time import sleep

HOST = 'localhost'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

mensagem = client.recv(1024)
if mensagem == b'SALA':
    client.send(b'Jogos')
    sleep[1]
    client.send(b'Lucas')