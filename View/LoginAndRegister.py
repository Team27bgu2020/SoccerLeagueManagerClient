from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui


class LoginAndRegister(QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, controller):
        QWidget.__init__(self)
        self.controller = controller
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 564, 537)
        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.login)
        self.loginLabel = QtWidgets.QLabel(self)
        self.loginLabel.setGeometry(QtCore.QRect(30, 30, 71, 31))
        self.loginLabel.setScaledContents(False)
        self.loginLabel.setWordWrap(False)
        self.loginLabel.setObjectName("loginLabel")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 60, 151, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.loginForm = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.loginForm.setContentsMargins(0, 0, 0, 0)
        self.loginForm.setObjectName("loginForm")
        self.usernameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.loginForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.loginForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.loginBtn = QtWidgets.QPushButton(self)
        self.loginBtn.setGeometry(QtCore.QRect(30, 110, 151, 23))
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn")
        # register form, label and btn
        self.registerLabel = QtWidgets.QLabel(self)
        self.registerLabel.setGeometry(QtCore.QRect(330, 30, 91, 31))
        self.registerLabel.setObjectName("registerLabel")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(330, 60, 161, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.registerForm = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.registerForm.setContentsMargins(0, 0, 0, 0)
        self.registerForm.setObjectName("registerForm")
        self.usernameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.usernameLabel_2.setObjectName("usernameLabel_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel_2)
        self.usernameLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.usernameLineEdit_2.setObjectName("usernameLineEdit_2")
        self.registerForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit_2)
        self.passwordLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.passwordLabel_2.setObjectName("passwordLabel_2")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel_2)
        self.passwordLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.passwordLineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit_2.setObjectName("passwordLineEdit_2")
        self.registerForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit_2)
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.nameLabel.setObjectName("nameLabel")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.registerForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.birthDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.registerForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthDateLabel)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.registerForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.registerBtn = QtWidgets.QPushButton(self)
        self.registerBtn.setGeometry(QtCore.QRect(330, 170, 161, 23))
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setObjectName("registerBtn")
        # guest btn
        self.guestBtn = QtWidgets.QPushButton(self)
        self.guestBtn.setGeometry(QtCore.QRect(390, 480, 131, 23))
        self.guestBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.guestBtn.setAutoDefault(False)
        self.guestBtn.setDefault(False)
        self.guestBtn.setObjectName("guestBtn")
        # main screen styling
        self.backgroundLabel = QtWidgets.QLabel(self)
        self.backgroundLabel.setGeometry(QtCore.QRect(20, 20, 511, 491))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setPixmap(QtGui.QPixmap("../Resources/coolSoccerField.jpg"))
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.logoLabel = QtWidgets.QLabel(self)
        self.logoLabel.setGeometry(QtCore.QRect(408, 364, 91, 91))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("../Resources/football federation.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(260, 20, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(27, 310, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.backgroundLabel.lower()

        self.retranslateUi()

        self.connect_buttons()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # retranslate MainScreen
        self.registerLabel.setText(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Register</span></p></body></html>"))
        self.loginLabel.setText(_translate("MainWindow",
                                           "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Login</span></p></body></html>"))
        self.guestBtn.setText(_translate("MainWindow", "Sign-In as a guest"))
        self.usernameLabel_2.setText(_translate("MainWindow", "username:"))
        self.passwordLabel_2.setText(_translate("MainWindow", "password:"))
        self.nameLabel.setText(_translate("MainWindow", "name:"))
        self.birthDateLabel.setText(_translate("MainWindow", "birth date:"))
        self.usernameLabel.setText(_translate("MainWindow", "username:"))
        self.passwordLabel.setText(_translate("MainWindow", "password:"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.registerBtn.setText(_translate("MainWindow", "Register"))

    def login(self):
        self.switch_window.emit()

    def connect_buttons(self):
        self.registerBtn.clicked.connect(self.register)
        self.guestBtn.clicked.connect(self.guest_login)
        self.loginBtn.clicked.connect(self.login)
        pass

    def guest_login(self):
        self.controller.set_user_win('Guest')
        self.controller.user_id = 'Guest'
        self.controller.show_user_win()

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
            'user_name': self.usernameLineEdit_2.text(),
            'password': self.passwordLineEdit_2.text(),
            'name': self.nameLineEdit.text(),
            'birth_date': self.dateEdit.date().toPyDate().strftime("%Y-%m-%d")
        }
        answer = self.controller.user_register(filled_info)
        if answer == 'Error':
            pass
        else:
            self.controller.set_user_win(answer['user_type'])
            self.controller.user_id = answer['user_name']
            self.controller.show_user_win()

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, con):
        self.__controller = con
