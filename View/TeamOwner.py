from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QLabel
from qtconsole.qt import QtGui

from View.UserWindow import UserWindow


class TeamOwnerWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.create_layout()

    def create_layout(self):
        Form = self
        Form.setObjectName("Form")
        Form.resize(838, 583)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("Form")
        self.setWindowIcon(QtGui.QIcon('../Resources/football federation.png'))
        self.team_owner = QtWidgets.QLabel(self.centralwidget)
        self.team_owner.setGeometry(QtCore.QRect(310, 10, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.team_owner.setFont(font)
        self.team_owner.setObjectName("team_owner")
        self.edit_personal_details = QtWidgets.QPushButton(self.centralwidget)
        self.edit_personal_details.setGeometry(QtCore.QRect(310, 100, 211, 41))
        self.edit_personal_details.setObjectName("edit_personal_details")
        self.edit_team_managers = QtWidgets.QPushButton(self.centralwidget)
        self.edit_team_managers.setGeometry(QtCore.QRect(70, 240, 211, 41))
        self.edit_team_managers.setObjectName("edit_team_managers")
        self.labael_show_edit = QtWidgets.QLabel(self.centralwidget)
        self.labael_show_edit.setGeometry(QtCore.QRect(70, 150, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labael_show_edit.setFont(font)
        self.labael_show_edit.setObjectName("labael_show_edit")
        self.edit_coaches = QtWidgets.QPushButton(self.centralwidget)
        self.edit_coaches.setGeometry(QtCore.QRect(70, 300, 211, 41))
        self.edit_coaches.setObjectName("edit_coaches")
        self.edit_players = QtWidgets.QPushButton(self.centralwidget)
        self.edit_players.setGeometry(QtCore.QRect(70, 360, 211, 41))
        self.edit_players.setObjectName("edit_players")
        self.edit_courts = QtWidgets.QPushButton(self.centralwidget)
        self.edit_courts.setGeometry(QtCore.QRect(70, 420, 211, 41))
        self.edit_courts.setObjectName("edit_courts")
        self.label_reporting = QtWidgets.QLabel(self.centralwidget)
        self.label_reporting.setGeometry(QtCore.QRect(340, 150, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_reporting.setFont(font)
        self.label_reporting.setObjectName("label_reporting")
        self.rep_enterings = QtWidgets.QPushButton(self.centralwidget)
        self.rep_enterings.setGeometry(QtCore.QRect(310, 240, 211, 41))
        self.rep_enterings.setObjectName("rep_enterings")
        self.rep_court_maintenance = QtWidgets.QPushButton(self.centralwidget)
        self.rep_court_maintenance.setGeometry(QtCore.QRect(310, 300, 211, 41))
        self.rep_court_maintenance.setObjectName("rep_court_maintenance")
        self.rep_salary_payment = QtWidgets.QPushButton(self.centralwidget)
        self.rep_salary_payment.setGeometry(QtCore.QRect(310, 360, 211, 41))
        self.rep_salary_payment.setObjectName("rep_salary_payment")
        self.rep_player_transfer = QtWidgets.QPushButton(self.centralwidget)
        self.rep_player_transfer.setGeometry(QtCore.QRect(310, 420, 211, 41))
        self.rep_player_transfer.setObjectName("rep_player_transfer")
        self.labael_show_edit_2 = QtWidgets.QLabel(self.centralwidget)
        self.labael_show_edit_2.setGeometry(QtCore.QRect(620, 150, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labael_show_edit_2.setFont(font)
        self.labael_show_edit_2.setObjectName("labael_show_edit_2")
        self.add_team_owner = QtWidgets.QPushButton(self.centralwidget)
        self.add_team_owner.setGeometry(QtCore.QRect(550, 240, 211, 41))
        self.add_team_owner.setObjectName("add_team_owner")
        self.add_team_manager = QtWidgets.QPushButton(self.centralwidget)
        self.add_team_manager.setGeometry(QtCore.QRect(550, 360, 211, 41))
        self.add_team_manager.setObjectName("add_team_manager")
        self.delete_team_owner = QtWidgets.QPushButton(self.centralwidget)
        self.delete_team_owner.setGeometry(QtCore.QRect(550, 300, 211, 41))
        self.delete_team_owner.setObjectName("delete_team_owner")
        self.delete_team_manager = QtWidgets.QPushButton(self.centralwidget)
        self.delete_team_manager.setGeometry(QtCore.QRect(550, 420, 211, 41))
        self.delete_team_manager.setObjectName("delete_team_manager")
        self.rep_player_transfer_2 = QtWidgets.QPushButton(self.centralwidget)
        self.rep_player_transfer_2.setGeometry(QtCore.QRect(310, 490, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rep_player_transfer_2.setFont(font)
        self.rep_player_transfer_2.setObjectName("rep_player_transfer_2")

        self.open_team_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_team_btn.setGeometry(20, 20, 90, 40)
        self.open_team_btn.setObjectName('open_team_btn')

        self.connect_buttons()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TeamOwner"))
        self.team_owner.setText(_translate("Form", "Team Owner"))
        self.edit_personal_details.setText(_translate("Form", "Edit My Personal Details"))
        self.edit_team_managers.setText(_translate("Form", "Team Managers"))
        self.labael_show_edit.setText(_translate("Form", "Show and Edit"))
        self.edit_coaches.setText(_translate("Form", "Coaches"))
        self.edit_players.setText(_translate("Form", "Players"))
        self.edit_courts.setText(_translate("Form", "Courts"))
        self.label_reporting.setText(_translate("Form", "Reporting"))
        self.rep_enterings.setText(_translate("Form", "Enterings"))
        self.rep_court_maintenance.setText(_translate("Form", "Courts maintenance"))
        self.rep_salary_payment.setText(_translate("Form", "Salary payment"))
        self.rep_player_transfer.setText(_translate("Form", "Player transfer"))
        self.labael_show_edit_2.setText(_translate("Form", "Edit"))
        self.add_team_owner.setText(_translate("Form", "Add Team Owner"))
        self.add_team_manager.setText(_translate("Form", "Add Team Managers"))
        self.delete_team_owner.setText(_translate("Form", "Delete Team Owner"))
        self.delete_team_manager.setText(_translate("Form", "Delete Team Managers"))
        self.rep_player_transfer_2.setText(_translate("Form", "Close Team"))
        self.open_team_btn.setText(_translate("Form", "Open Team"))

    def connect_buttons(self):
        self.open_team_btn.clicked.connect(self.open_team)
        # self.edit_players.clicked.connect(self.add_player)

    def open_team(self):
        self.dialog = QDialog()
        self.dialog.setWindowIcon(QtGui.QIcon('../Resources/football federation.png'))
        self.dialog.setWindowTitle('New Team')
        self.dialog.setGeometry(560, 180, 235, 120)
        self.dialog.TeamNameLbl = QtWidgets.QLabel(self.dialog)
        self.dialog.TeamNameLbl.setGeometry(QtCore.QRect(10, 20, 100, 16))
        self.dialog.TeamNameLbl.setObjectName("TeamNameLbl")
        self.dialog.TeamNameLbl.setText('Enter team name:')
        self.dialog.TeamNameLineEdit = QtWidgets.QLineEdit(self.dialog)
        self.dialog.TeamNameLineEdit.setGeometry(QtCore.QRect(120, 20, 100, 16))
        self.dialog.TeamNameLineEdit.setObjectName("TeamNameLineEdit")
        self.dialog.createTeamBtn = QtWidgets.QPushButton(self.dialog)
        self.dialog.createTeamBtn.setGeometry(QtCore.QRect(70, 60, 100, 26))
        self.dialog.createTeamBtn.setObjectName("TeamNameLbl")
        self.dialog.createTeamBtn.setText('Create team')
        self.dialog.createTeamBtn.clicked.connect(self.new_team)
        self.dialog.show()

    def close_open_team_dialog(self):
        self.dialog.close()

    def click_create_team(self):
        self.dialog.createTeamBtn.click()

    def set_team_name(self, team_name):
        self.dialog.TeamNameLineEdit.setText(team_name)

    def new_team(self):
        filled_info = {
            'team_name': self.dialog.TeamNameLineEdit.text(),
        }
        answer = self.controller.team_register(filled_info)
        if answer == 'Error':
            self.controller.error_window('Invalid team registration info: \n'
                                         '# Team with the same name already exists.\n\n'
                                         'Team Registration Error')
        elif answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        else:
            self.controller.success_window('Team added successfully.\n')
            self.close_open_team_dialog()