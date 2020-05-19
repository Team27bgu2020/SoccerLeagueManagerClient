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

    def __init__(self):
        self.log_reg_win = LoginAndRegister(self)
        self.__user_win = None

    def show_login(self):
        self.log_reg_win.switch_window.connect(self.show_user_win)
        self.log_reg_win.show()

    def show_user_win(self):
        self.log_reg_win.close()
        self.user_win.show()

    @property
    def user_win(self):
        return self.__user_win

    @user_win.setter
    def user_win(self, user_type):
        if self.user_win is None:
            self.__user_win = get_user_win(user_type)

    @property
    def log_reg_win(self):
        return self.__log_reg_win

    @log_reg_win.setter
    def log_reg_win(self, win):
        self.__log_reg_win = win


def get_user_win(user_type, controller):
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
