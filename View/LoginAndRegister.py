from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtWidgets


class LoginAndRegister(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        self.controller = controller
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, con):
        self.__controller = con