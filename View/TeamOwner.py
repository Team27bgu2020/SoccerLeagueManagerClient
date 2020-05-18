from PyQt5 import QtWidgets, QtCore
from View.UserWindow import UserWindow


class TeamOwnerWindow(UserWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)