from PyQt5 import QtWidgets, QtCore, QtGui
from View.UserWindow import UserWindow


class GuestWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)

        self.setWindowTitle('GuestScreen')
        self.setGeometry(100, 100, 564, 537)
        self.formLayoutWidget_5 = QtWidgets.QWidget(self)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(70, 120, 151, 51))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.loginForm_2 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.loginForm_2.setContentsMargins(0, 0, 0, 0)
        self.loginForm_2.setObjectName("loginForm_2")
        self.usernameLabel_4 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.usernameLabel_4.setObjectName("usernameLabel_4")
        self.loginForm_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel_4)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.usernameLineEdit.setObjectName("usernameLineEdit_4")
        self.loginForm_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel_4 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.passwordLabel_4.setObjectName("passwordLabel_4")
        self.loginForm_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel_4)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit_4")
        self.loginForm_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.loginLabel_2 = QtWidgets.QLabel(self)
        self.loginLabel_2.setGeometry(QtCore.QRect(60, 80, 71, 51))
        self.loginLabel_2.setObjectName("loginLabel_2")
        self.loginBtn = QtWidgets.QPushButton(self)
        self.loginBtn.setGeometry(QtCore.QRect(70, 170, 151, 23))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn_2")
        # register form, label and btn
        self.registerLabel_2 = QtWidgets.QLabel(self)
        self.registerLabel_2.setGeometry(QtCore.QRect(320, 90, 91, 31))
        self.registerLabel_2.setObjectName("registerLabel_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(320, 120, 161, 101))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.registerForm_2 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.registerForm_2.setContentsMargins(0, 0, 0, 0)
        self.registerForm_2.setObjectName("registerForm_2")
        self.usernameLabel_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.usernameLabel_3.setObjectName("usernameLabel_3")
        self.registerForm_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel_3)
        self.usernameLineEditReg = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.usernameLineEditReg.setObjectName("usernameLineEdit_3")
        self.registerForm_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEditReg)
        self.passwordLabel_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.passwordLabel_3.setObjectName("passwordLabel_3")
        self.registerForm_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel_3)
        self.passwordLineEditReg = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.passwordLineEditReg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEditReg.setObjectName("passwordLineEdit_3")
        self.registerForm_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEditReg)
        self.nameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.registerForm_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.nameLineEditReg = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.nameLineEditReg.setObjectName("nameLineEdit_2")
        self.registerForm_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEditReg)
        self.birthDateLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.birthDateLabel_2.setObjectName("birthDateLabel_2")
        self.registerForm_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthDateLabel_2)
        self.dateEditReg = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.dateEditReg.setObjectName("dateEdit_2")
        self.registerForm_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEditReg)
        self.registerBtn = QtWidgets.QPushButton(self)
        self.registerBtn.setGeometry(QtCore.QRect(320, 220, 161, 23))
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setObjectName("registerBtn_2")
        # search form, label and btn
        self.searchLabel = QtWidgets.QLabel(self)
        self.searchLabel.setGeometry(QtCore.QRect(210, 310, 131, 31))
        self.searchLabel.setObjectName("searchLabel")
        self.searchLabel.setStyleSheet('color: black')
        self.formLayoutWidget_4 = QtWidgets.QWidget(self)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(190, 340, 151, 80))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.searchForm = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.searchForm.setContentsMargins(0, 0, 0, 0)
        self.searchForm.setObjectName("searchForm")
        self.nameLabel_3 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.nameLabel_3.setObjectName("nameLabel_3")
        self.nameLabel_3.setStyleSheet('color: white')
        self.searchForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel_3)
        self.nameLineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.nameLineEdit_3.setObjectName("nameLineEdit_3")
        self.searchForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit_3)
        self.roleLabel = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.roleLabel.setObjectName("roleLabel")
        self.roleLabel.setStyleSheet('color: white')
        self.searchForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.roleComboBox = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.roleComboBox.setObjectName("roleComboBox")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.searchForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roleComboBox)
        self.searchBtn = QtWidgets.QPushButton(self)
        self.searchBtn.setGeometry(QtCore.QRect(188, 400, 156, 23))
        self.searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchBtn.setObjectName("searchBtn")
        # back to main screen btn
        self.backBtn = QtWidgets.QPushButton(self)
        self.backBtn.setGeometry(QtCore.QRect(405, 475, 70, 23))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setObjectName("backBtn")
        # guest screen styling
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(200, 20, 151, 61))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(390, 320, 91, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Resources/football federation.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(37, 300, 481, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(30, 70, 481, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(260, 90, 20, 211))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.backgroundLabel_2 = QtWidgets.QLabel(self)
        self.backgroundLabel_2.setGeometry(QtCore.QRect(20, 20, 511, 491))
        self.backgroundLabel_2.setText("")
        self.backgroundLabel_2.setPixmap(QtGui.QPixmap("../Resources/soccerFieldNorway.jpg"))
        self.backgroundLabel_2.setScaledContents(True)
        self.backgroundLabel_2.setObjectName("backgroundLabel_2")
        self.backgroundLabel_2.lower()

        self.retranslateUi()

        self.connect_buttons()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.searchLabel.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Search Page</span></p></body></html>"))
        self.usernameLabel_3.setText(_translate("MainWindow", "username:"))
        self.passwordLabel_3.setText(_translate("MainWindow", "password:"))
        self.nameLabel_2.setText(_translate("MainWindow", "name:"))
        self.birthDateLabel_2.setText(_translate("MainWindow", "birth date:"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.registerLabel_2.setText(_translate("MainWindow",
                                                "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Register</span></p></body></html>"))
        self.nameLabel_3.setText(_translate("MainWindow", "name:"))
        self.roleLabel.setText(_translate("MainWindow", "role:"))
        self.roleComboBox.setItemText(0, _translate("MainWindow", "choose role.."))
        self.roleComboBox.setItemText(1, _translate("MainWindow", "Team"))
        self.roleComboBox.setItemText(2, _translate("MainWindow", "Player"))
        self.roleComboBox.setItemText(3, _translate("MainWindow", "Coach"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hello Guest</span></p></body></html>"))
        self.usernameLabel_4.setText(_translate("MainWindow", "username:"))
        self.passwordLabel_4.setText(_translate("MainWindow", "password:"))
        self.loginLabel_2.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Login</span></p></body></html>"))
        self.registerBtn.setText(_translate("MainWindow", "Register"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.backBtn.setText(_translate("MainWindow", "Logout"))

    def connect_buttons(self):
        self.registerBtn.clicked.connect(self.register)
        self.backBtn.clicked.connect(self.controller.user_logout)
        self.loginBtn.clicked.connect(self.login)
        # self.searchBtn.clicked.connect()
        pass

    def login(self):
        filled_info = {
                        'user_name': self.usernameLineEdit.text(),
                        'password': self.passwordLineEdit.text()
                     }
        answer = self.controller.user_login(filled_info)
        if answer == 'Error':
            pass
        else:
            self.controller.set_user_win(answer['user_type'])
            self.controller.user_id = answer['user_name']
            self.controller.show_user_win()

    def register(self):
        filled_info = {
                        'user_name': self.usernameLineEditReg.text(),
                        'password': self.passwordLineEditReg.text(),
                        'name': self.nameLineEditReg.text(),
                        'birth_date': self.dateEditReg.date().toPyDate().strftime("%Y-%m-%d")
        }
        answer = self.controller.user_register(filled_info)
        if answer == 'Error':
            pass
        else:
            self.controller.set_user_win(answer['user_type'])
            self.controller.user_id = answer['user_name']
            self.controller.show_user_win()