from PyQt5 import QtCore, QtWidgets


class UserWindow(QtWidgets.QWidget):

    def __init__(self, controller):
        QtWidgets.QWidget.__init__(self)
        self.switcher = QtCore.pyqtSignal(str)
        self.controller = controller

    def switch(self):
        self.switcher.emit()

    def connect_switcher(self, fun):
        self.switcher.connect(fun)

    @property
    def switcher(self):
        return self.__switcher

    @switcher.setter
    def switcher(self, win):
        self.__switcher = win

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, con):
        self.__controller = con
