from PyQt5 import QtWidgets, QtCore


class PlayerWindow(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)