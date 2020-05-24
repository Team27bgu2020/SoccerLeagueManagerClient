from PyQt5.QtNetwork import QUdpSocket
import socket


class Client:

    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_to_server(self, message):
        """ Sends the given message to the server """
        self.client_socket.sendto(bytes(message, encoding="utf-8"), self.server_address)

    def get_answer(self):
        """ Waits for the server to return an answer and returns it """
        return self.client_socket.recv(4096)

    @property
    def server_address(self):
        return self.__server_address

    @server_address.setter
    def server_address(self, server_address):
        self.__server_address = server_address

    @property
    def client_socket(self):
        return self.__client_socket

    @client_socket.setter
    def client_socket(self, client_socket):
        self.__client_socket = client_socket



# c = Client(('localhost', 10000))
# c.send(str.encode('Hello, Dor'))
# print(c.get_answer())