from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtWidgets
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


class UserWindow(QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, user_type):
        QWidget.__init__(self)
        self.set_win(user_type)

    def switch(self):
        self.switch_window.emit()

    def set_win(self, user_type):
        if user_type == 'Guest':
            self.win = GuestWIndow()
        elif user_type == 'Coach':
            self.win = CoachWindow()
        elif user_type == 'Fan':
            self.win = FanWindow()
        elif user_type == 'Player':
            self.win = PlayerWindow()
        elif user_type == 'Referee':
            self.win = RefereeWindow()
        elif user_type == 'SystemAdmin':
            self.win = SystemAdminWindow()
        elif user_type == 'TeamManager':
            self.win = TeamManagerWindow()
        elif user_type == 'TeamOwner':
            self.win = TeamOwnerWindow
        elif user_type == 'UnionRepresentor':
            self.win = UnionRepresentorWindow()
        else:
            raise ValueError

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, win):
        self.__win = win

