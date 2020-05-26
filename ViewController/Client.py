from PyQt5.QtNetwork import QUdpSocket
import json
import socket


class Client:

    def __init__(self, server_address):
        self.server_address = server_address
        self.controller = None
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.settimeout(2)


    def send_to_server(self, message):
        """ Sends the given message to the server """
        answer = json.dumps('')
        times_to_try = 5
        while answer == '""' and times_to_try > 0:
            self.client_socket.sendto(bytes(message, encoding="utf-8"), self.server_address)
            try:
                server_ans = json.loads(self.client_socket.recv(4096))
                answer = json.dumps(server_ans['message'])
                self.controller.handle_notifications(server_ans['notifications'])
            except socket.timeout:
                print('Server Response Timeout, Trying again...')
                times_to_try -= 1
                continue
        return answer

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

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, controller):
        self.__controller = controller