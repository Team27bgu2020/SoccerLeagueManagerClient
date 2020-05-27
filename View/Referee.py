from PyQt5 import QtCore, QtGui, QtWidgets

from View.UserWindow import UserWindow


class RefereeWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.create_layout()

    def create_layout(self):
        Form = self
        Form.setObjectName("MainWindow")
        self.setWindowIcon(QtGui.QIcon('../Resources/football federation.png'))
        Form.resize(758, 441)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.label_referee = QtWidgets.QLabel(self.centralwidget)
        self.label_referee.setGeometry(QtCore.QRect(280, 60, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_referee.setFont(font)
        self.label_referee.setObjectName("label_referee")
        self.edit_personal_details = QtWidgets.QPushButton(self.centralwidget)
        self.edit_personal_details.setGeometry(QtCore.QRect(90, 200, 211, 41))
        self.edit_personal_details.setObjectName("edit_personal_details")
        self.personal_games = QtWidgets.QPushButton(self.centralwidget)
        self.personal_games.setGeometry(QtCore.QRect(90, 280, 211, 41))
        self.personal_games.setObjectName("personal_games")
        self.update_game_event = QtWidgets.QPushButton(self.centralwidget)
        self.update_game_event.setGeometry(QtCore.QRect(450, 280, 211, 41))
        self.update_game_event.setObjectName("update_game_event")
        self.add_game_event = QtWidgets.QPushButton(self.centralwidget)
        self.add_game_event.setGeometry(QtCore.QRect(450, 200, 211, 41))
        self.add_game_event.setObjectName("add_game_event")
        #Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_referee.setText(_translate("Form", "Referee"))
        self.edit_personal_details.setText(_translate("Form", "Edit My Personal Details"))
        self.personal_games.setText(_translate("Form", "Games in which I am inlaid"))
        self.update_game_event.setText(_translate("Form", "Show and Update Games Events"))
        self.add_game_event.setText(_translate("Form", "Add Game Event"))
