import json
from PyQt5.QtWidgets import QMessageBox
from View.LoginAndRegister import LoginAndRegister
from View.UserWindow import UserWindow
from View.Guest import GuestWindow
from View.Coach import CoachWindow
from View.Fan import FanWindow
from View.Guest import GuestWindow
from View.Player import PlayerWindow
from View.Referee import RefereeWindow
from View.SystemAdmin import SystemAdminWindow
from View.TeamManager import TeamManagerWindow
from View.TeamOwner import TeamOwnerWindow
from View.UnionRepresentor import UnionRepresentorWindow


class ViewController:

    def __init__(self, client):
        self.log_reg_win = LoginAndRegister(self)
        self.user_win = None
        self.client = client
        self.user_id = None

    def show_login(self):
        """ This method display the login screen """
        self.log_reg_win.switch_window.connect(self.show_user_win)
        self.log_reg_win.show()

    def show_user_win(self):
        """ This method display the user main screen """
        self.log_reg_win.close()
        self.user_win.show()

    def error_window(self, message, error_title='Error'):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error_title)
        msg.setInformativeText(message)
        msg.setWindowTitle(error_title)
        msg.exec_()

    def success_window(self, message, success_title='Success'):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(success_title)
        msg.setInformativeText(message)
        msg.setWindowTitle(success_title)
        msg.exec_()

    def user_logout(self):
        """ This method logs-out user from system and shows him the login-register window"""
        self.user_win.close()
        self.log_reg_win.show()

    def user_login(self, user_info):
        """ This method sends the server the user login information and gets from the server the relevant
            user information """
        message = self.new_message('user_login', user_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def user_register(self, user_info):
        """ This method sends the server a request from the user to register in the system and receives an answer
          whether it was successful or not """
        message = self.new_message('user_register', user_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def ref_register(self, ref_info):
        """ This method sends the server a request from the user to register referee in the system and receives an
        answer whether it was successful or not """
        message = self.new_message('ref_register', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def remove_user(self, ref_info):
        """ This method sends the server a request to remove a user in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('remove_user', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_user_info(self):
        """ This method gets from the server the user information """
        message = self.new_message('get_user_info')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def update_user_info(self, user_info):
        """ This method sends to the server the user information """
        message = self.new_message('update_user_info', user_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_logs(self):
        """ This method sends the server the user login information and gets from the server the relevant
            user information """
        message = self.new_message('get_logs')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def new_message(self, message_type, data=None):
        """ This method returns a new message in the relevant format """
        return {
                    'type': message_type,
                    'user_id': self.user_id,
                    'data': data
                }

    def set_user_win(self, user_type):
        """ setter for the user window by user type (string) """
        self.user_win = get_user_win(user_type, self)

    @property
    def user_win(self):
        return self.__user_win

    @user_win.setter
    def user_win(self, user_win):
        self.__user_win = user_win

    @property
    def log_reg_win(self):
        return self.__log_reg_win

    @log_reg_win.setter
    def log_reg_win(self, win):
        self.__log_reg_win = win

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id


def get_user_win(user_type, controller):
    """ This function returns an instance of the user window that were created by the given user type """
    if user_type == 'Guest':
        return GuestWindow(controller)
    elif user_type == 'Coach':
        return CoachWindow(controller)
    elif user_type == 'Fan':
        return FanWindow(controller)
    elif user_type == 'Player':
        return PlayerWindow(controller)
    elif user_type == 'Referee':
        return RefereeWindow(controller)
    elif user_type == 'SystemAdmin':
        return SystemAdminWindow(controller)
    elif user_type == 'TeamManager':
        return TeamManagerWindow(controller)
    elif user_type == 'TeamOwner':
        return TeamOwnerWindow(controller)
    elif user_type == 'UnionRepresentor':
        return UnionRepresentorWindow(controller)
    else:
        raise ValueError
