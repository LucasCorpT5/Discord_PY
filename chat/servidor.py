import socket
import threading

HOST = 'localhost'
PORT = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        i.send(mensagem)

while True:
    client, addr = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f"{nome} se conectou na sala {sala}! INFO {addr}")