import socket
import threading

HOST = 'localhost'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

while True:
    client, addr = server.accept()
    client.send(b'Sala')
    sala = client.recv(1024).decode()
    name = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    else:
        sala[sala].append(client)
        print(sala)