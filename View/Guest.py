from PyQt5 import QtWidgets, QtCore
from View.UserWindow import UserWindow


class GuestWindow(UserWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel('Window Two')
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)