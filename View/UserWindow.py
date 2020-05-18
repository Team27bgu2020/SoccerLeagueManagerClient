from PyQt5 import QtCore, QtWidgets


class UserWindow(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.switcher = QtCore.pyqtSignal(str)

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

