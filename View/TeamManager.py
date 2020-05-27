from PyQt5 import QtWidgets, QtCore
from qtconsole.qt import QtGui

from View.UserWindow import UserWindow


class TeamManagerWindow(UserWindow):

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
        self.team_manager_referee = QtWidgets.QLabel(self.centralwidget)
        self.team_manager_referee.setGeometry(QtCore.QRect(210, 40, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.team_manager_referee.setFont(font)
        self.team_manager_referee.setObjectName("team_manager_referee")
        self.edit_personal_details = QtWidgets.QPushButton(self.centralwidget)
        self.edit_personal_details.setGeometry(QtCore.QRect(90, 150, 211, 41))
        self.edit_personal_details.setObjectName("edit_personal_details")
        self.delete_coach = QtWidgets.QPushButton(self.centralwidget)
        self.delete_coach.setGeometry(QtCore.QRect(430, 290, 211, 41))
        self.delete_coach.setObjectName("delete_coach")
        self.change_court = QtWidgets.QPushButton(self.centralwidget)
        self.change_court.setGeometry(QtCore.QRect(430, 150, 211, 41))
        self.change_court.setObjectName("change_court")
        self.delete_player = QtWidgets.QPushButton(self.centralwidget)
        self.delete_player.setGeometry(QtCore.QRect(430, 220, 211, 41))
        self.delete_player.setObjectName("delete_player")
        self.add_coach = QtWidgets.QPushButton(self.centralwidget)
        self.add_coach.setGeometry(QtCore.QRect(90, 290, 211, 41))
        self.add_coach.setObjectName("add_coach")
        self.add_player = QtWidgets.QPushButton(self.centralwidget)
        self.add_player.setGeometry(QtCore.QRect(90, 220, 211, 41))
        self.add_player.setObjectName("add_player")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.team_manager_referee.setText(_translate("Form", "Team Manager"))
        self.edit_personal_details.setText(_translate("Form", "Edit My Personal Details"))
        self.delete_coach.setText(_translate("Form", "Delete Coach"))
        self.change_court.setText(_translate("Form", "Change court"))
        self.delete_player.setText(_translate("Form", "Delete Player"))
        self.add_coach.setText(_translate("Form", "Add Coach"))
        self.add_player.setText(_translate("Form", "Add Player"))
