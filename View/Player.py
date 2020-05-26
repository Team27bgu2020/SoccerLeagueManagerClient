from PyQt5 import QtWidgets, QtCore, QtGui
from View.UserWindow import UserWindow


class PlayerWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.create_layout()

    def create_layout(self):

        Form = self
        Form.setObjectName("Form")
        Form.resize(800, 450)

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)

        self.update_info_btn = QtWidgets.QPushButton(Form)
        self.update_info_btn.setGeometry(QtCore.QRect(440, 230, 160, 70))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.update_info_btn.sizePolicy().hasHeightForWidth())

        self.update_info_btn.setSizePolicy(sizePolicy)
        self.update_info_btn.setFont(font)

        self.upload_content_btn = QtWidgets.QPushButton(Form)
        self.upload_content_btn.setGeometry(QtCore.QRect(200, 230, 160, 70))

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 50, 300, 60))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.connect_buttons()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.update_info_btn.setText(_translate("Form", "Update Inormation"))
        self.upload_content_btn.setText(_translate("Form", "Upload Site Content"))
        self.label.setText(_translate("Form", "Hello Player"))

    def connect_buttons(self):
        self.upload_content_btn.clicked.connect(self.upload_content)
        self.update_info_btn.clicked.connect(self.update_info)

    def upload_content(self):
        self.controller.error_window('UC is not Implemented')

    def update_info(self):
        self.controller.error_window('UC is not Implemented')
        # self.controller.get_user_info()
