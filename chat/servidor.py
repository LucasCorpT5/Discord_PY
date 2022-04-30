import socket
import threading

HOST = 'localhost'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_ST)
server.bind((HOST, PORT))
server.listen()

while True:
    pass