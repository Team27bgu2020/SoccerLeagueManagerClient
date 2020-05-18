from View.LoginAndRegister import LoginAndRegister
from View.UserWindow import UserWindow


class ViewController:

    def __init__(self):
        self.log_reg_win = LoginAndRegister()
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
            self.__user_win = UserWindow(user_type)

    @property
    def log_reg_win(self):
        return self.__log_reg_win

    @log_reg_win.setter
    def log_reg_win(self, win):
        self.__log_reg_win = win
