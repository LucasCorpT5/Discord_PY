import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self):
        HOST = 'localhost'
        PORT = 55556
        # self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.connect((HOST, PORT))
        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True

        self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.sala = simpledialog.askstring('Sala', 'Digite a sala que deseja etrar!', parent=login)
        self.janela()
    
    def janela(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title('Chat')

        self.caixa_texto = Text(self.root)
        self.caixa_texto.place(relx=0.05, rely=0.01, width=780, height=680)
        self.root.mainloop()
chat = Chat()