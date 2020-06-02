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
        self.client.controller = self
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
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText(error_title)
        self.msg.setInformativeText(message)
        self.msg.setWindowTitle(error_title)
        self.msg.show()

    def popup_window(self, message, message_title='New Notification!'):
        self.msg = QMessageBox()
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setText(message)
        self.msg.setWindowTitle(message_title)
        self.msg.show()

    def success_window(self, message, success_title='Success'):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(success_title)
        self.msg.setInformativeText(message)
        self.msg.setWindowTitle(success_title)
        self.msg.show()

    def close_popup(self):
        self.msg.close()

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
        """ This method sends the server a request for the logs information and gets from the server the relevant
        information """
        message = self.new_message('get_logs')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_users(self):
        """ This method sends the server a request for the users information and gets from the server the relevant
        information """
        message = self.new_message('get_users')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_refs(self):
        """ This method sends the server a request for the referees information and gets from the server the relevant
        information """
        message = self.new_message('get_refs')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_teams(self):
        """ This method sends the server a request for the teams information and gets from the server the relevant
        information """
        message = self.new_message('get_teams')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_policy(self, typeOfPolicy):
        """ This method sends the server a request for the teams information and gets from the server the relevant
        information """
        message = self.new_message('get_policy', typeOfPolicy)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def add_policy(self, policy_info):
        """ This method sends the server new policy information and gets from the server the relevant answer """
        message = self.new_message('add_policy', policy_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def team_register(self, team_info):
        """ This method sends the server new team information and gets from the server the relevant answer """
        message = self.new_message('add_team', team_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def add_league(self, league_info):
        """ This method sends the server new league information and gets from the server the relevant answer """
        message = self.new_message('add_league', league_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_policies(self):
        """ This method sends the server new league information and gets from the server the relevant answer """
        message = self.new_message('get_policies')
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

    def get_on_going_games(self):
        """ This method sends the server a request to get on going games by referee in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('get_on_going_games')
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def add_event(self, ref_info):
        """ This method sends the server a request to add event by referee in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('add_event', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def edit_event(self, ref_info):
        """ This method sends the server a request to edit event by referee in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('edit_event', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def get_game_events(self, ref_info):
        """ This method sends the server a request to all events in the game in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('get_all_game_events', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def delete_event(self, ref_info):
        """ This method sends the server a request to delete event by referee in the system and receives an answer
        whether it was successful or not """
        message = self.new_message('delete_event', ref_info)
        answer = self.client.send_to_server(json.dumps(message))
        return json.loads(answer)

    def handle_notifications(self, notifications):
        if notifications == 'Error' or not notifications:
            return
        else:
            notification_message = 'Notifications:\n\n'
            notification_counter = 1
            for notification in notifications:
                notification_message += str(notification_counter) + '. ' + notification + '\n'
                notification_counter += 1
            self.popup_window(notification_message)

    def close(self):
        self.close()

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

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, msg):
        self.__msg = msg


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
