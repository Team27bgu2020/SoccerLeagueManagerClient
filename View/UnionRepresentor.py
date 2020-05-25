from PyQt5 import QtWidgets, QtCore, QtGui
from View.UserWindow import UserWindow


class UnionRepresentorWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.setWindowTitle('UnionRepresentor')
        self.setGeometry(100, 100, 564, 537)
        self.helloUnionRepresentor = QtWidgets.QLabel(self)
        self.helloUnionRepresentor.setGeometry(QtCore.QRect(150, -10, 251, 41))
        self.helloUnionRepresentor.setObjectName("helloUnionRepresentor")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 521, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.leagueBtn = QtWidgets.QPushButton(self.mainTab)
        self.leagueBtn.setGeometry(QtCore.QRect(220, 60, 75, 23))
        self.leagueBtn.setObjectName("leagueBtn")
        self.seasonBtn = QtWidgets.QPushButton(self.mainTab)
        self.seasonBtn.setGeometry(QtCore.QRect(220, 90, 75, 23))
        self.seasonBtn.setObjectName("seasonBtn")
        self.refsBtn = QtWidgets.QPushButton(self.mainTab)
        self.refsBtn.setGeometry(QtCore.QRect(220, 120, 75, 23))
        self.refsBtn.setObjectName("refsBtn")
        self.budgetBtn = QtWidgets.QPushButton(self.mainTab)
        self.budgetBtn.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.budgetBtn.setObjectName("budgetBtn")
        self.optionsLbl = QtWidgets.QLabel(self.mainTab)
        self.optionsLbl.setGeometry(QtCore.QRect(180, 20, 151, 31))
        self.optionsLbl.setObjectName("optionsLbl")
        self.picMainTab = QtWidgets.QLabel(self.mainTab)
        self.picMainTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picMainTab.setText("")
        self.picMainTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picMainTab.setScaledContents(True)
        self.picMainTab.setObjectName("picMainTab")
        self.picMainTab.lower()
        self.tabWidget.addTab(self.mainTab, "")
        self.leagueTab = QtWidgets.QWidget()
        self.leagueTab.setObjectName("leagueTab")
        self.leaguesTable = QtWidgets.QTableWidget(self.leagueTab)
        self.leaguesTable.setGeometry(QtCore.QRect(10, 30, 256, 321))
        self.leaguesTable.setStyleSheet("background-color: transparent")
        self.leaguesTable.setObjectName("leaguesTable")
        self.leaguesTable.setColumnCount(1)
        self.leaguesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.leaguesTable.setHorizontalHeaderItem(0, item)
        self.addLeagueBtn = QtWidgets.QPushButton(self.leagueTab)
        self.addLeagueBtn.setGeometry(QtCore.QRect(350, 110, 75, 23))
        self.addLeagueBtn.setObjectName("addLeagueBtn")
        self.formLayoutWidget = QtWidgets.QWidget(self.leagueTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(280, 30, 231, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.newLeague = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.newLeague.setContentsMargins(0, 0, 0, 0)
        self.newLeague.setObjectName("newLeague")
        self.leagueNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.leagueNameLabel.setObjectName("leagueNameLabel")
        self.newLeague.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.leagueNameLabel)
        self.leagueNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leagueNameLineEdit.setObjectName("leagueNameLineEdit")
        self.newLeague.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leagueNameLineEdit)
        self.pointsPolicyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.pointsPolicyLabel.setObjectName("pointsPolicyLabel")
        self.newLeague.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pointsPolicyLabel)
        self.pointsPolicyComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.pointsPolicyComboBox.setObjectName("pointsPolicyComboBox")
        self.pointsPolicyComboBox.addItem("")
        self.pointsPolicyComboBox.addItem("")
        self.pointsPolicyComboBox.addItem("")
        self.newLeague.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pointsPolicyComboBox)
        self.gameSchedulingPolicyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.gameSchedulingPolicyLabel.setObjectName("gameSchedulingPolicyLabel")
        self.newLeague.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gameSchedulingPolicyLabel)
        self.gameSchedulingPolicyComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.gameSchedulingPolicyComboBox.setObjectName("gameSchedulingPolicyComboBox")
        self.gameSchedulingPolicyComboBox.addItem("")
        self.gameSchedulingPolicyComboBox.addItem("")
        self.gameSchedulingPolicyComboBox.addItem("")
        self.newLeague.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gameSchedulingPolicyComboBox)
        self.NewLeagueLbl = QtWidgets.QLabel(self.leagueTab)
        self.NewLeagueLbl.setGeometry(QtCore.QRect(326, 10, 131, 20))
        self.NewLeagueLbl.setObjectName("NewLeagueLbl")
        self.picLeagueTab = QtWidgets.QLabel(self.leagueTab)
        self.picLeagueTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picLeagueTab.setText("")
        self.picLeagueTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picLeagueTab.setScaledContents(True)
        self.picLeagueTab.setObjectName("picLeagueTab")
        self.picLeagueTab.lower()
        self.tabWidget.addTab(self.leagueTab, "")
        self.seasonTab = QtWidgets.QWidget()
        self.seasonTab.setObjectName("seasonTab")
        self.seasonsTable = QtWidgets.QTableWidget(self.seasonTab)
        self.seasonsTable.setGeometry(QtCore.QRect(10, 30, 211, 321))
        self.seasonsTable.setStyleSheet("background-color: transparent")
        self.seasonsTable.setObjectName("seasonsTable")
        self.seasonsTable.setColumnCount(2)
        self.seasonsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.seasonsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.seasonsTable.setHorizontalHeaderItem(1, item)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.seasonTab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(300, 30, 160, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.seasonYearLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.seasonYearLabel.setObjectName("seasonYearLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.seasonYearLabel)
        self.seasonYearSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.seasonYearSpinBox.setMinimum(1990)
        self.seasonYearSpinBox.setMaximum(2050)
        self.seasonYearSpinBox.setObjectName("seasonYearSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.seasonYearSpinBox)
        self.assignTeamsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignTeamsLabel.setObjectName("assignTeamsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.assignTeamsLabel)
        self.assignTeamsWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignTeamsWidget.setObjectName("assignTeamsWidget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.assignTeamsWidget)
        self.assignRefereesLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignRefereesLabel.setObjectName("assignRefereesLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.assignRefereesLabel)
        self.assignRefereesWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignRefereesWidget.setObjectName("assignRefereesWidget")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.assignRefereesWidget)
        self.assignToLeagueLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignToLeagueLabel.setObjectName("assignToLeagueLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.assignToLeagueLabel)
        self.assignToLeagueWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignToLeagueWidget.setObjectName("assignToLeagueWidget")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.assignToLeagueWidget)
        self.newSeasonLbl = QtWidgets.QLabel(self.seasonTab)
        self.newSeasonLbl.setGeometry(QtCore.QRect(310, 10, 131, 20))
        self.newSeasonLbl.setObjectName("newSeasonLbl")
        self.addSeasonBtn = QtWidgets.QPushButton(self.seasonTab)
        self.addSeasonBtn.setGeometry(QtCore.QRect(340, 120, 81, 23))
        self.addSeasonBtn.setObjectName("addSeasonBtn")
        self.picSeasonTab = QtWidgets.QLabel(self.seasonTab)
        self.picSeasonTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picSeasonTab.setText("")
        self.picSeasonTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picSeasonTab.setScaledContents(True)
        self.picSeasonTab.setObjectName("picSeasonTab")
        self.picSeasonTab.lower()
        self.tabWidget.addTab(self.seasonTab, "")
        self.refTab = QtWidgets.QWidget()
        self.refTab.setObjectName("refTab")
        self.refTable = QtWidgets.QTableWidget(self.refTab)
        self.refTable.setGeometry(QtCore.QRect(10, 30, 211, 321))
        self.refTable.setStyleSheet("background-color: transparent")
        self.refTable.setObjectName("refTable")
        self.refTable.setColumnCount(2)
        self.refTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.refTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.refTable.setHorizontalHeaderItem(1, item)
        self.addRefBtn = QtWidgets.QPushButton(self.refTab)
        self.addRefBtn.setGeometry(QtCore.QRect(330, 100, 91, 23))
        self.addRefBtn.setObjectName("addRefBtn")
        self.removeRefBtn = QtWidgets.QPushButton(self.refTab)
        self.removeRefBtn.setGeometry(QtCore.QRect(330, 290, 91, 23))
        self.removeRefBtn.setObjectName("removeRefBtn")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.refTab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(300, 50, 160, 51))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.newRefForm = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.newRefForm.setContentsMargins(0, 0, 0, 0)
        self.newRefForm.setObjectName("newRefForm")
        self.refUsernameLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.refUsernameLabel.setObjectName("refUsernameLabel")
        self.newRefForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.refUsernameLabel)
        self.refUsernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.refUsernameLineEdit.setObjectName("refUsernameLineEdit")
        self.newRefForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refUsernameLineEdit)
        self.refPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.refPasswordLabel.setObjectName("refPasswordLabel")
        self.newRefForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.refPasswordLabel)
        self.refPasswordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.refPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.refPasswordLineEdit.setObjectName("refPasswordLineEdit")
        self.newRefForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.refPasswordLineEdit)
        self.newRefLbl = QtWidgets.QLabel(self.refTab)
        self.newRefLbl.setGeometry(QtCore.QRect(310, 30, 131, 20))
        self.newRefLbl.setObjectName("newRefLbl")
        self.delRefLbl = QtWidgets.QLabel(self.refTab)
        self.delRefLbl.setGeometry(QtCore.QRect(320, 220, 131, 20))
        self.delRefLbl.setObjectName("delRefLbl")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.refTab)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(310, 240, 160, 51))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.delRefForm = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.delRefForm.setContentsMargins(0, 0, 0, 0)
        self.delRefForm.setObjectName("delRefForm")
        self.refUsernameLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.refUsernameLabel_2.setObjectName("refUsernameLabel_2")
        self.delRefForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.refUsernameLabel_2)
        self.refUsernameLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.refUsernameLineEdit_2.setObjectName("refUsernameLineEdit_2")
        self.delRefForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refUsernameLineEdit_2)
        self.refPasswordLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.refPasswordLabel_2.setObjectName("refPasswordLabel_2")
        self.delRefForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.refPasswordLabel_2)
        self.refPasswordLineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.refPasswordLineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.refPasswordLineEdit_2.setObjectName("refPasswordLineEdit_2")
        self.delRefForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.refPasswordLineEdit_2)
        self.picRefTab = QtWidgets.QLabel(self.refTab)
        self.picRefTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picRefTab.setText("")
        self.picRefTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picRefTab.setScaledContents(True)
        self.picRefTab.setObjectName("picRefTab")
        self.picRefTab.lower()
        self.tabWidget.addTab(self.refTab, "")
        self.teamBudgetTab = QtWidgets.QWidget()
        self.teamBudgetTab.setObjectName("teamBudgetTab")
        self.picTeamBudgetTab = QtWidgets.QLabel(self.teamBudgetTab)
        self.picTeamBudgetTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picTeamBudgetTab.setText("")
        self.picTeamBudgetTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picTeamBudgetTab.setScaledContents(True)
        self.picTeamBudgetTab.setObjectName("picTeamBudgetTab")
        self.picTeamBudgetTab.lower()
        self.tabWidget.addTab(self.teamBudgetTab, "")
        self.unionBudgetTab = QtWidgets.QWidget()
        self.unionBudgetTab.setObjectName("unionBudgetTab")
        self.picUnionBudgetTab = QtWidgets.QLabel(self.unionBudgetTab)
        self.picUnionBudgetTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picUnionBudgetTab.setText("")
        self.picUnionBudgetTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picUnionBudgetTab.setScaledContents(True)
        self.picUnionBudgetTab.setObjectName("picUnionBudgetTab")
        self.picUnionBudgetTab.lower()
        self.tabWidget.addTab(self.unionBudgetTab, "")
        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(450, 430, 101, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Resources/football federation.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.pointsPolicyComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.helloUnionRepresentor.setText(_translate("Form",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hello Union Representor</span></p></body></html>"))
        self.leagueBtn.setText(_translate("Form", "Leagues"))
        self.seasonBtn.setText(_translate("Form", "Seasons"))
        self.refsBtn.setText(_translate("Form", "Refereas"))
        self.budgetBtn.setText(_translate("Form", "Budget"))
        self.optionsLbl.setText(_translate("Form",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Options</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main"))
        item = self.leaguesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "League"))
        self.addLeagueBtn.setText(_translate("Form", "create league"))
        self.leagueNameLabel.setText(_translate("Form", "league name:"))
        self.pointsPolicyLabel.setText(_translate("Form", "points policy:"))
        self.pointsPolicyComboBox.setToolTip(_translate("Form",
                                                        "<html><head/><body><p><span style=\" text-decoration: underline;\">Soccer</span></p><p>Win - 3 points</p><p>Draw - 1 point</p><p>Lose - 0 points</p><p><span style=\" text-decoration: underline;\">Basketball</span></p><p>Win - 2 points</p><p>Draw - 0 points</p><p>Lose - 1 point</p></body></html>"))
        self.pointsPolicyComboBox.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pointsPolicyComboBox.setItemText(0, _translate("Form", "choose policy.."))
        self.pointsPolicyComboBox.setItemText(1, _translate("Form", "Soccer"))
        self.pointsPolicyComboBox.setItemText(2, _translate("Form", "Basketball"))
        self.gameSchedulingPolicyLabel.setText(_translate("Form", "game scheduling policy: "))
        self.gameSchedulingPolicyComboBox.setToolTip(_translate("Form",
                                                                "<html><head/><body><p><span style=\" text-decoration: underline;\">Home and Away:</span></p><p>two games against each team, once at home and once away.<br/></p><p><span style=\" text-decoration: underline;\">Knockout:</span></p><p>one game against each team.</p></body></html>"))
        self.gameSchedulingPolicyComboBox.setItemText(0, _translate("Form", "choose policy.."))
        self.gameSchedulingPolicyComboBox.setItemText(1, _translate("Form", "Home and Away"))
        self.gameSchedulingPolicyComboBox.setItemText(2, _translate("Form", "Knockout"))
        self.NewLeagueLbl.setText(_translate("Form",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Create new league</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.leagueTab), _translate("Form", "Leagues"))
        item = self.seasonsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Season"))
        item = self.seasonsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "League"))
        self.seasonYearLabel.setText(_translate("Form", "season year:"))
        self.assignTeamsLabel.setText(_translate("Form", "assign teams:"))
        self.assignRefereesLabel.setText(_translate("Form", "assign referees:"))
        self.assignToLeagueLabel.setText(_translate("Form", "assign to league:"))
        self.newSeasonLbl.setText(_translate("Form",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Create new season</span></p></body></html>"))
        self.addSeasonBtn.setText(_translate("Form", "create season"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.seasonTab), _translate("Form", "Seasons"))
        item = self.refTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Referee"))
        item = self.refTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Qualification"))
        self.addRefBtn.setText(_translate("Form", "add referee"))
        self.removeRefBtn.setText(_translate("Form", "remove referee"))
        self.refUsernameLabel.setText(_translate("Form", "referee username:"))
        self.refPasswordLabel.setText(_translate("Form", "referee password:"))
        self.newRefLbl.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Create new referee</span></p></body></html>"))
        self.delRefLbl.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Delete referee</span></p></body></html>"))
        self.refUsernameLabel_2.setText(_translate("Form", "referee username:"))
        self.refPasswordLabel_2.setText(_translate("Form", "referee password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.refTab), _translate("Form", "Referees"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teamBudgetTab), _translate("Form", "TeamBudget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unionBudgetTab), _translate("Form", "UnionBudget"))
