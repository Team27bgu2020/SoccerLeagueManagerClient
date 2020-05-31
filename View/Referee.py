from PyQt5 import QtCore, QtGui, QtWidgets

from View.UserWindow import UserWindow


class RefereeWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.create_layout()
        self.game_on_going = self.get_on_going_games()
        if self.game_on_going is not None:
            self.fill_on_going_games(self.game_on_going)
        self.connect_buttons()


    def create_layout(self):
        Form = self
        Form.setObjectName("Form")
        Form.resize(725, 570)
        self.Referee = QtWidgets.QTabWidget(Form)
        self.Referee.setGeometry(QtCore.QRect(50, 100, 611, 411))
        self.Referee.setObjectName("Referee")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.edit_personal_details = QtWidgets.QPushButton(self.main)
        self.edit_personal_details.setGeometry(QtCore.QRect(200, 40, 211, 41))
        self.edit_personal_details.setObjectName("edit_personal_details")
        self.personal_games = QtWidgets.QPushButton(self.main)
        self.personal_games.setGeometry(QtCore.QRect(200, 110, 211, 41))
        self.personal_games.setObjectName("personal_games")
        self.add_game_event = QtWidgets.QPushButton(self.main)
        self.add_game_event.setGeometry(QtCore.QRect(200, 180, 211, 41))
        self.add_game_event.setObjectName("add_game_event")
        self.update_game_event = QtWidgets.QPushButton(self.main)
        self.update_game_event.setGeometry(QtCore.QRect(200, 260, 211, 41))
        self.update_game_event.setObjectName("update_game_event")
        self.on_going_games = QtWidgets.QPushButton(self.main)
        self.on_going_games.setGeometry(QtCore.QRect(200, 330, 211, 41))
        self.on_going_games.setObjectName("on_going_games")
        self.Referee.addTab(self.main, "")
        self.add_game_event1 = QtWidgets.QWidget()
        self.add_game_event1.setObjectName("add_game_event1")
        self.event_type_label = QtWidgets.QLabel(self.add_game_event1)
        self.event_type_label.setGeometry(QtCore.QRect(70, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_type_label.setFont(font)
        self.event_type_label.setObjectName("event_type_label")
        self.event_des_label = QtWidgets.QLabel(self.add_game_event1)
        self.event_des_label.setGeometry(QtCore.QRect(70, 160, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_des_label.setFont(font)
        self.event_des_label.setObjectName("event_des_label")
        self.game_min_label = QtWidgets.QLabel(self.add_game_event1)
        self.game_min_label.setGeometry(QtCore.QRect(70, 210, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_min_label.setFont(font)
        self.game_min_label.setObjectName("game_min_label")
        self.min_in_game_box = QtWidgets.QSpinBox(self.add_game_event1)
        self.min_in_game_box.setGeometry(QtCore.QRect(320, 210, 211, 31))
        self.min_in_game_box.setMinimum(1)
        self.min_in_game_box.setMaximum(130)
        self.min_in_game_box.setObjectName("min_in_game_box")
        self.game_id_label = QtWidgets.QLabel(self.add_game_event1)
        self.game_id_label.setGeometry(QtCore.QRect(70, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_id_label.setFont(font)
        self.game_id_label.setObjectName("game_id_label")
        self.label1 = QtWidgets.QLabel(self.add_game_event1)
        self.label1.setGeometry(QtCore.QRect(150, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.event_dec_text = QtWidgets.QTextEdit(self.add_game_event1)
        self.event_dec_text.setGeometry(QtCore.QRect(320, 160, 211, 41))
        self.event_dec_text.setObjectName("event_dec_text")
        self.event_type_box_add = QtWidgets.QComboBox(self.add_game_event1)
        self.event_type_box_add.setGeometry(QtCore.QRect(320, 120, 211, 31))
        self.event_type_box_add.setObjectName("event_type_box_add")
        self.event_type_box_add.addItem("")
        self.event_type_box_add.addItem("")
        self.event_type_box_add.addItem("")
        self.submit = QtWidgets.QPushButton(self.add_game_event1)
        self.submit.setGeometry(QtCore.QRect(230, 310, 141, 51))
        self.submit.setObjectName("submit")
        self.game_id_box_add = QtWidgets.QComboBox(self.add_game_event1)
        self.game_id_box_add.setGeometry(QtCore.QRect(320, 80, 211, 31))
        self.game_id_box_add.setObjectName("game_id_box_add")
        self.Referee.addTab(self.add_game_event1, "")
        self.edit_dame_event = QtWidgets.QWidget()
        self.edit_dame_event.setObjectName("edit_dame_event")
        self.event_type_label_2 = QtWidgets.QLabel(self.edit_dame_event)
        self.event_type_label_2.setGeometry(QtCore.QRect(70, 160, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_type_label_2.setFont(font)
        self.event_type_label_2.setObjectName("event_type_label_2")
        self.game_min_label_2 = QtWidgets.QLabel(self.edit_dame_event)
        self.game_min_label_2.setGeometry(QtCore.QRect(70, 240, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_min_label_2.setFont(font)
        self.game_min_label_2.setObjectName("game_min_label_2")
        self.submit_2 = QtWidgets.QPushButton(self.edit_dame_event)
        self.submit_2.setGeometry(QtCore.QRect(230, 310, 141, 51))
        self.submit_2.setObjectName("submit_2")
        self.game_id_label_2 = QtWidgets.QLabel(self.edit_dame_event)
        self.game_id_label_2.setGeometry(QtCore.QRect(70, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_id_label_2.setFont(font)
        self.game_id_label_2.setObjectName("game_id_label_2")
        self.min_in_game_box_2 = QtWidgets.QSpinBox(self.edit_dame_event)
        self.min_in_game_box_2.setGeometry(QtCore.QRect(320, 250, 211, 31))
        self.min_in_game_box_2.setMinimum(1)
        self.min_in_game_box_2.setMaximum(130)
        self.min_in_game_box_2.setObjectName("min_in_game_box_2")
        self.event_type_box_edit = QtWidgets.QComboBox(self.edit_dame_event)
        self.event_type_box_edit.setGeometry(QtCore.QRect(320, 160, 211, 31))
        self.event_type_box_edit.setObjectName("event_type_box_edit")
        self.event_type_box_edit.addItem("")
        self.event_type_box_edit.addItem("")
        self.event_type_box_edit.addItem("")
        self.label1_2 = QtWidgets.QLabel(self.edit_dame_event)
        self.label1_2.setGeometry(QtCore.QRect(150, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.event_des_label_2 = QtWidgets.QLabel(self.edit_dame_event)
        self.event_des_label_2.setGeometry(QtCore.QRect(70, 200, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.event_des_label_2.setFont(font)
        self.event_des_label_2.setObjectName("event_des_label_2")
        self.event_dec_text_2 = QtWidgets.QTextEdit(self.edit_dame_event)
        self.event_dec_text_2.setGeometry(QtCore.QRect(320, 200, 211, 41))
        self.event_dec_text_2.setObjectName("event_dec_text_2")
        self.game_id_box_edit_2 = QtWidgets.QComboBox(self.edit_dame_event)
        self.game_id_box_edit_2.setGeometry(QtCore.QRect(320, 80, 211, 31))
        self.game_id_box_edit_2.setObjectName("game_id_box_edit_2")
        self.game_event_id_label = QtWidgets.QLabel(self.edit_dame_event)
        self.game_event_id_label.setGeometry(QtCore.QRect(70, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_event_id_label.setFont(font)
        self.game_event_id_label.setObjectName("game_event_id_label")
        self.game_event_id_box_edit = QtWidgets.QComboBox(self.edit_dame_event)
        self.game_event_id_box_edit.setGeometry(QtCore.QRect(320, 120, 211, 31))
        self.game_event_id_box_edit.setObjectName("game_event_id_box_edit")
        self.Referee.addTab(self.edit_dame_event, "")
        self.on_going_game = QtWidgets.QWidget()
        self.on_going_game.setObjectName("on_going_game")
        self.on_going_game_list = QtWidgets.QListWidget(self.on_going_game)
        self.on_going_game_list.setGeometry(QtCore.QRect(0, 0, 601, 381))
        self.on_going_game_list.setObjectName("on_going_game_list")
        self.Referee.addTab(self.on_going_game, "")
        self.all_games = QtWidgets.QWidget()
        self.all_games.setObjectName("all_games")
        self.listWidget_3 = QtWidgets.QListWidget(self.all_games)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 0, 601, 381))
        self.listWidget_3.setObjectName("listWidget_3")
        self.Referee.addTab(self.all_games, "")
        self.label_referee = QtWidgets.QLabel(Form)
        self.label_referee.setGeometry(QtCore.QRect(260, 10, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_referee.setFont(font)
        self.label_referee.setObjectName("label_referee")
        self.logout_btn = QtWidgets.QPushButton(Form)
        self.logout_btn.setGeometry(QtCore.QRect(570, 40, 93, 28))
        self.logout_btn.setObjectName("logout_btn")

        self.retranslateUi(Form)
        self.Referee.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edit_personal_details.setText(_translate("Form", "Edit My Personal Details"))
        self.personal_games.setText(_translate("Form", "Games in which I am inlaid"))
        self.add_game_event.setText(_translate("Form", "Add Game Event"))
        self.update_game_event.setText(_translate("Form", "Update Games Events"))
        self.on_going_games.setText(_translate("Form", "On Going Games"))
        self.Referee.setTabText(self.Referee.indexOf(self.main), _translate("Form", "Main"))
        self.event_type_label.setText(_translate("Form", "Event Type:"))
        self.event_des_label.setText(_translate("Form", "Event description:"))
        self.game_min_label.setText(_translate("Form", "Min in the game:"))
        self.game_id_label.setText(_translate("Form", "Game ID:"))
        self.label1.setText(_translate("Form", "Add Game Event"))
        self.event_dec_text.setHtml(_translate("Form",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.event_type_box_add.setItemText(0, _translate("Form", "Goal"))
        self.event_type_box_add.setItemText(1, _translate("Form", "Yellow Card"))
        self.event_type_box_add.setItemText(2, _translate("Form", "Red Card"))
        self.submit.setText(_translate("Form", "Submit"))
        self.Referee.setTabText(self.Referee.indexOf(self.add_game_event1), _translate("Form", "Add Game Event"))
        self.event_type_label_2.setText(_translate("Form", "Event Type:"))
        self.game_min_label_2.setText(_translate("Form", "Min in the game:"))
        self.submit_2.setText(_translate("Form", "Submit"))
        self.game_id_label_2.setText(_translate("Form", "Game ID:"))
        self.event_type_box_edit.setItemText(0, _translate("Form", "Goal"))
        self.event_type_box_edit.setItemText(1, _translate("Form", "Yellow Card"))
        self.event_type_box_edit.setItemText(2, _translate("Form", "Red Card"))
        self.label1_2.setText(_translate("Form", "Edit Game Event"))
        self.event_des_label_2.setText(_translate("Form", "Event description:"))
        self.event_dec_text_2.setHtml(_translate("Form",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.game_event_id_label.setText(_translate("Form", "Game event ID:"))
        self.Referee.setTabText(self.Referee.indexOf(self.edit_dame_event), _translate("Form", "Edit Game Event"))
        self.Referee.setTabText(self.Referee.indexOf(self.on_going_game), _translate("Form", "On Going Games"))
        self.Referee.setTabText(self.Referee.indexOf(self.all_games), _translate("Form", "All My Games"))
        self.label_referee.setText(_translate("Form", "Referee"))
        self.logout_btn.setText(_translate("Form", "LogOut"))

    def connect_buttons(self):
        self.logout_btn.clicked.connect(self.controller.user_logout)
        self.add_game_event.clicked.connect(self.add_game_event_tab)
        self.update_game_event.clicked.connect(self.edit_game_event_tab)
        self.submit.clicked.connect(self.add_game_event_func)
        self.game_id_box_edit_2.activated(self.fill_events_of_game(str(self.game_id_box_add.currentText())))
        pass

    def add_game_event_tab(self):
        self.all_tabs.setCurrentIndex(1)

    def edit_game_event_tab(self):
        self.all_tabs.setCurrentIndex(2)

    def on_going_games_tab(self):
        self.all_tabs.setCurrentIndex(3)


    def add_game_event_func(self):
        referee_id = self.controller.user_id
        game_id = str(self.game_id_box_add.currentText())
        event_type = str(self.event_type_box.currentText())
        event_des = self.event_dec_text.toPlainText()
        min_in_game = str(self.min_in_game_box.value())
        filled_info = {
            # all data
            'referee_id': referee_id,
            'game_id': game_id,
            'event_type': event_type,
            'event_description': event_des,
            'min_in_game': min_in_game
        }

        answer = self.controller.add_event(filled_info)
        if answer == 'Success':
            self.controller.success_window('Event added successfully.\n')
        else:
            self.controller.error_window('Game ID is not correct.\n')


    def get_on_going_games(self):
        referee_id = self.controller.user_id
        filled_info = {
            'referee_id': referee_id
        }
        answer = self.controller.get_on_going_games(filled_info)
        if answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        else:
            return answer

    def fill_on_going_games(self, games):
        for i in games:
            game_info = ""
            game_info += games[i].get('game_id')
            game_info += ": "
            game_info += games[i].get('home_team')
            game_info += "_"
            game_info += games[i].get('away_team')
            self.game_id_box_add.addItems(game_info)
            self.game_id_box_edit_2.addItems(game_info)
            self.on_going_game_list.addItems(game_info)
            self.game_event_box.addItems(game_info)

    def get_game_events(self, game_id):
        referee_id = self.controller.user_id

        filled_info = {
            'referee_id': referee_id,
            'game_id': game_id
        }
        answer = self.controller.get_game_events(filled_info)
        if answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        else:
            return answer


    def fill_events_of_game(self, game_id):
        all_events_in_game = self.get_game_events(game_id)
        if all_events_in_game is not None:
            self.game_event_id_box_edit.addItems(all_events_in_game)
        else:
            self.controller.error_window('No events for this Game ID.\n')

