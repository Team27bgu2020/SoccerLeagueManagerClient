from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

from View.UserWindow import UserWindow


class UnionRepresentorWindow(UserWindow):

    def __init__(self, controller):
        super().__init__(controller)
        self.setWindowTitle('UnionRepresentor')
        self.setWindowIcon(QtGui.QIcon('../Resources/football federation.png'))
        self.setGeometry(100, 100, 564, 537)
        self.helloUnionRepresentor = QtWidgets.QLabel(self)
        self.helloUnionRepresentor.setGeometry(QtCore.QRect(150, -10, 251, 41))
        self.helloUnionRepresentor.setObjectName("helloUnionRepresentor")
        self.onlyInt = QIntValidator()
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 521, 461))
        self.tabWidget.setObjectName("tabWidget")
        # main tab
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
        self.unionBudgetBtn = QtWidgets.QPushButton(self.mainTab)
        self.unionBudgetBtn.setGeometry(QtCore.QRect(220, 180, 75, 23))
        self.unionBudgetBtn.setObjectName("unionBudgetBtn")
        self.policiesBtn = QtWidgets.QPushButton(self.mainTab)
        self.policiesBtn.setGeometry(QtCore.QRect(220, 210, 75, 23))
        self.policiesBtn.setObjectName("policiesBtn")
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
        # league tab
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
        self.addLeagueBtn.setGeometry(QtCore.QRect(350, 172, 75, 23))
        self.addLeagueBtn.setObjectName("addLeagueBtn")
        self.formLayoutWidget = QtWidgets.QWidget(self.leagueTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 30, 241, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.newLeague = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.newLeague.setContentsMargins(0, 0, 0, 0)
        self.newLeague.setObjectName("newLeague")
        self.leagueNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.leagueNameLabel.setObjectName("leagueNameLabel")
        self.leagueNameLabel.setStyleSheet('color: white')
        self.newLeague.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.leagueNameLabel)
        self.leagueNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leagueNameLineEdit.setObjectName("leagueNameLineEdit")
        self.newLeague.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leagueNameLineEdit)
        self.seasonLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.seasonLabel.setObjectName("seasonLabel")
        self.seasonLabel.setStyleSheet('color: white')
        self.newLeague.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.seasonLabel)
        self.assignPointsPolicyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.assignPointsPolicyLabel.setObjectName("assignPointsPolicyLabel")
        self.assignPointsPolicyLabel.setStyleSheet('color: white')
        self.newLeague.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.assignPointsPolicyLabel)
        self.assignPointPolicyBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.assignPointPolicyBtn.setObjectName("assignPointPolicyBtn")
        self.assignPointPolicyBtn.setText('Points policy')
        self.newLeague.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.assignPointPolicyBtn)
        self.assignGamePolicyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.assignGamePolicyLabel.setObjectName("assignGamePolicyLabel")
        self.assignGamePolicyLabel.setStyleSheet('color: white')
        self.newLeague.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.assignGamePolicyLabel)
        self.assignGamePolicyBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.assignGamePolicyBtn.setObjectName("assignGamePolicyBtn")
        self.assignGamePolicyBtn.setText('Game policy')
        self.newLeague.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.assignGamePolicyBtn)
        self.assignBudgetPolicyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.assignBudgetPolicyLabel.setObjectName("assignBudgetPolicyLabel")
        self.assignBudgetPolicyLabel.setStyleSheet('color: white')
        self.newLeague.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.assignBudgetPolicyLabel)
        self.assignBudgetPolicyBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.assignBudgetPolicyBtn.setObjectName("assignBudgetPolicyBtn")
        self.assignBudgetPolicyBtn.setText('Budget policy')
        self.newLeague.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.assignBudgetPolicyBtn)
        self.seasonSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.seasonSpinBox.setMinimum(1990)
        self.seasonSpinBox.setMaximum(2050)
        self.seasonSpinBox.setObjectName("seasonSpinBox")
        self.newLeague.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seasonSpinBox)
        self.NewLeagueLbl = QtWidgets.QLabel(self.leagueTab)
        self.NewLeagueLbl.setGeometry(QtCore.QRect(326, 10, 131, 20))
        self.NewLeagueLbl.setObjectName("NewLeagueLbl")
        self.NewLeagueLbl.setStyleSheet('color: white')

        self.picLeagueTab = QtWidgets.QLabel(self.leagueTab)
        self.picLeagueTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picLeagueTab.setText("")
        self.picLeagueTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picLeagueTab.setScaledContents(True)
        self.picLeagueTab.setObjectName("picLeagueTab")
        self.picLeagueTab.lower()
        self.tabWidget.addTab(self.leagueTab, "")
        # season tab
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
        self.seasonYearLabel.setStyleSheet('color: white')
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.seasonYearLabel)
        self.seasonYearSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.seasonYearSpinBox.setMinimum(1990)
        self.seasonYearSpinBox.setMaximum(2050)
        self.seasonYearSpinBox.setObjectName("seasonYearSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.seasonYearSpinBox)
        self.assignTeamsLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignTeamsLabel.setObjectName("assignTeamsLabel")
        self.assignTeamsLabel.setStyleSheet('color: white')
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.assignTeamsLabel)
        self.assignTeamsWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignTeamsWidget.setObjectName("assignTeamsWidget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.assignTeamsWidget)
        self.assignRefereesLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignRefereesLabel.setObjectName("assignRefereesLabel")
        self.assignRefereesLabel.setStyleSheet('color: white')
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.assignRefereesLabel)
        self.assignRefereesWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignRefereesWidget.setObjectName("assignRefereesWidget")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.assignRefereesWidget)
        self.assignToLeagueLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.assignToLeagueLabel.setObjectName("assignToLeagueLabel")
        self.assignToLeagueLabel.setStyleSheet('color: white')
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.assignToLeagueLabel)
        self.assignToLeagueWidget = QtWidgets.QWidget(self.formLayoutWidget_2)
        self.assignToLeagueWidget.setObjectName("assignToLeagueWidget")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.assignToLeagueWidget)
        self.newSeasonLbl = QtWidgets.QLabel(self.seasonTab)
        self.newSeasonLbl.setGeometry(QtCore.QRect(310, 10, 131, 20))
        self.newSeasonLbl.setObjectName("newSeasonLbl")
        self.newSeasonLbl.setStyleSheet('color: white')
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
        # referee tab
        self.refTab = QtWidgets.QWidget()
        self.refTab.setObjectName("refTab")
        self.showRefereesBtn = QtWidgets.QPushButton(self.refTab)
        self.showRefereesBtn.setGeometry(QtCore.QRect(30, 380, 91, 23))
        self.showRefereesBtn.setObjectName("showRefereesBtn")
        self.showRefereesBtn.setText('Show referees')
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
        self.addRefBtn.setGeometry(QtCore.QRect(340, 160, 91, 23))
        self.addRefBtn.setObjectName("addRefBtn")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.refTab)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(300, 50, 200, 100))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.newRefForm = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.newRefForm.setContentsMargins(0, 0, 0, 0)
        self.newRefForm.setObjectName("newRefForm")
        self.refUsernameLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.refUsernameLabel.setObjectName("refUsernameLabel")
        self.refUsernameLabel.setStyleSheet('color: white')
        self.newRefForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.refUsernameLabel)
        self.refUsernameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.refUsernameLineEdit.setObjectName("refUsernameLineEdit")
        self.newRefForm.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.refUsernameLineEdit)
        self.refPasswordLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.refPasswordLabel.setObjectName("refPasswordLabel")
        self.refPasswordLabel.setStyleSheet('color: white')
        self.newRefForm.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.refPasswordLabel)
        self.refPasswordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.refPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.refPasswordLineEdit.setObjectName("refPasswordLineEdit")
        self.newRefForm.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.refPasswordLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setStyleSheet('color: white')
        self.newRefForm.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.newRefForm.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.birthDateLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.birthDateLabel.setStyleSheet('color: white')
        self.newRefForm.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthDateLabel)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.dateEdit.setObjectName("dateEdit")
        self.newRefForm.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.refQualificationLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.refQualificationLabel.setObjectName("refQualificationLabel")
        self.refQualificationLabel.setStyleSheet('color: white')
        self.newRefForm.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.refQualificationLabel)
        self.refComboBox = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.refComboBox.setObjectName("refComboBox")
        self.refComboBox.addItem("")
        self.refComboBox.addItem("")
        self.refComboBox.addItem("")
        self.newRefForm.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.refComboBox)
        self.newRefLbl = QtWidgets.QLabel(self.refTab)
        self.newRefLbl.setGeometry(QtCore.QRect(320, 27, 131, 20))
        self.newRefLbl.setObjectName("newRefLbl")
        self.newRefLbl.setStyleSheet('color: white')
        self.delRefLbl = QtWidgets.QLabel(self.refTab)
        self.delRefLbl.setGeometry(QtCore.QRect(320, 210, 131, 20))
        self.delRefLbl.setObjectName("delRefLbl")
        self.delRefLbl.setStyleSheet('color: white')
        self.refUsernameLineEdit_2 = QtWidgets.QLineEdit(self.refTab)
        self.refUsernameLineEdit_2.setObjectName("refUsernameLineEdit")
        self.refUsernameLineEdit_2.setGeometry(QtCore.QRect(300, 240, 91, 23))
        self.removeRefBtn = QtWidgets.QPushButton(self.refTab)
        self.removeRefBtn.setGeometry(QtCore.QRect(400, 240, 91, 23))
        self.removeRefBtn.setObjectName("removeRefBtn")
        self.picRefTab = QtWidgets.QLabel(self.refTab)
        self.picRefTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picRefTab.setText("")
        self.picRefTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picRefTab.setScaledContents(True)
        self.picRefTab.setObjectName("picRefTab")
        self.picRefTab.lower()
        self.tabWidget.addTab(self.refTab, "")
        # team budget tab
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
        # union budget tab
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
        # policies tab
        self.policyTab = QtWidgets.QWidget()
        self.policyTab.setObjectName("policyTab")
        self.toolBox = QtWidgets.QToolBox(self.policyTab)
        self.toolBox.setGeometry(QtCore.QRect(20, 10, 400, 370))
        self.toolBox.setStyleSheet("background-color: transparent; color:white")
        self.toolBox.setObjectName("toolBox")
        self.pointsPolicy = QtWidgets.QWidget()
        self.pointsPolicy.setGeometry(QtCore.QRect(0, 0, 241, 100))
        self.pointsPolicy.setObjectName("pointsPolicy")
        self.winPointsLbl = QtWidgets.QLabel(self.pointsPolicy)
        self.winPointsLbl.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.winPointsLbl.setObjectName("winPointsLbl")
        self.drawPointsLbl = QtWidgets.QLabel(self.pointsPolicy)
        self.drawPointsLbl.setGeometry(QtCore.QRect(10, 35, 81, 16))
        self.drawPointsLbl.setObjectName("drawPointsLbl")
        self.losePointsLbl = QtWidgets.QLabel(self.pointsPolicy)
        self.losePointsLbl.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.losePointsLbl.setObjectName("losePointsLbl")
        self.winPointsSpinBox = QtWidgets.QLineEdit(self.pointsPolicy)
        self.winPointsSpinBox.setGeometry(QtCore.QRect(100, 0, 42, 22))
        self.winPointsSpinBox.setObjectName("winPointsSpinBox")
        self.winPointsSpinBox.setValidator(self.onlyInt)
        self.drawPointsSpinBox = QtWidgets.QLineEdit(self.pointsPolicy)
        self.drawPointsSpinBox.setGeometry(QtCore.QRect(100, 35, 42, 22))
        self.drawPointsSpinBox.setObjectName("drawPointsSpinBox")
        self.drawPointsSpinBox.setValidator(self.onlyInt)
        self.losePointsSpinBox = QtWidgets.QLineEdit(self.pointsPolicy)
        self.losePointsSpinBox.setGeometry(QtCore.QRect(100, 70, 42, 22))
        self.losePointsSpinBox.setObjectName("losePointsSpinBox")
        self.losePointsSpinBox.setValidator(self.onlyInt)
        self.savePointsPolicyBtn = QtWidgets.QPushButton(self.pointsPolicy)
        self.savePointsPolicyBtn.setGeometry(QtCore.QRect(10, 105, 91, 23))
        self.savePointsPolicyBtn.setObjectName("savePointsPolicyBtn")
        self.savePointsPolicyBtn.setStyleSheet('background-color: white; color: black')
        self.toolBox.addItem(self.pointsPolicy, "")
        self.gamePolicy = QtWidgets.QWidget()
        self.gamePolicy.setGeometry(QtCore.QRect(0, 0, 241, 100))
        self.gamePolicy.setObjectName("gamePolicy")
        self.gamePolicy.setStyleSheet("background-color: transparent")
        self.numOfGamesLbl = QtWidgets.QLabel(self.gamePolicy)
        self.numOfGamesLbl.setGeometry(QtCore.QRect(10, 0, 181, 16))
        self.numOfGamesLbl.setObjectName("numOfGamesLbl")
        self.gamesNumSpinBox = QtWidgets.QLineEdit(self.gamePolicy)
        self.gamesNumSpinBox.setGeometry(QtCore.QRect(193, 0, 42, 22))
        self.gamesNumSpinBox.setValidator(self.onlyInt)
        self.gamesNumSpinBox.setObjectName("gamesNumSpinBox")
        self.gamesPerWeeksLbl = QtWidgets.QLabel(self.gamePolicy)
        self.gamesPerWeeksLbl.setGeometry(QtCore.QRect(10, 35, 181, 16))
        self.gamesPerWeeksLbl.setObjectName("gamesPerWeeksLbl")
        self.gamesPerWeekSpinBox = QtWidgets.QLineEdit(self.gamePolicy)
        self.gamesPerWeekSpinBox.setGeometry(QtCore.QRect(193, 35, 42, 22))
        self.gamesPerWeekSpinBox.setValidator(self.onlyInt)
        self.gamesPerWeekSpinBox.setObjectName("gamesPerWeekSpinBox")
        self.gameStadiumLbl = QtWidgets.QLabel(self.gamePolicy)
        self.gameStadiumLbl.setGeometry(QtCore.QRect(10, 70, 141, 16))
        self.gameStadiumLbl.setObjectName("gameStadiumLbl")
        self.stadiumComboBox = QtWidgets.QComboBox(self.gamePolicy)
        self.stadiumComboBox.setGeometry(QtCore.QRect(108, 67, 131, 22))
        self.stadiumComboBox.setObjectName("StadiumcomboBox")
        self.stadiumComboBox.addItem("")
        self.stadiumComboBox.addItem("")
        self.stadiumComboBox.addItem("")
        self.saveGamePolicyBtn = QtWidgets.QPushButton(self.gamePolicy)
        self.saveGamePolicyBtn.setGeometry(QtCore.QRect(10, 105, 91, 23))
        self.saveGamePolicyBtn.setObjectName("saveGamePolicyBtn")
        self.saveGamePolicyBtn.setStyleSheet('background-color: white; color: black')
        self.toolBox.addItem(self.gamePolicy, "")
        self.teamBudgetPolicy = QtWidgets.QWidget()
        self.teamBudgetPolicy.setObjectName("teamBudgetPolicy")
        self.minBudgetLbl = QtWidgets.QLabel(self.teamBudgetPolicy)
        self.minBudgetLbl.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.minBudgetLbl.setObjectName("minBudget")
        self.minBudgetLineEdit = QtWidgets.QLineEdit(self.teamBudgetPolicy)
        self.minBudgetLineEdit.setGeometry(QtCore.QRect(140, 10, 85, 22))
        self.minBudgetLineEdit.setObjectName("minBudgetLineEdit")

        self.minBudgetLineEdit.setValidator(self.onlyInt)
        self.saveBudgetPolicyBtn = QtWidgets.QPushButton(self.teamBudgetPolicy)
        self.saveBudgetPolicyBtn.setGeometry(QtCore.QRect(10, 40, 91, 23))
        self.saveBudgetPolicyBtn.setObjectName("saveGamePolicyBtn")
        self.saveBudgetPolicyBtn.setStyleSheet('background-color: white; color: black')
        self.toolBox.addItem(self.teamBudgetPolicy, "")
        self.picPolicyTab = QtWidgets.QLabel(self.policyTab)
        self.picPolicyTab.setGeometry(QtCore.QRect(0, 0, 534, 431))
        self.picPolicyTab.setText("")
        self.picPolicyTab.setPixmap(QtGui.QPixmap("../Resources/city.jpg"))
        self.picPolicyTab.setScaledContents(True)
        self.picPolicyTab.setObjectName("picPolicyTab")
        self.picPolicyTab.lower()
        self.tabWidget.addTab(self.policyTab, "")

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(450, 430, 101, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Resources/football federation.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.backBtn = QtWidgets.QPushButton(self)
        self.backBtn.setGeometry(QtCore.QRect(25, 495, 95, 23))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setObjectName("backBtn")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.connect_buttons()

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.helloUnionRepresentor.setText(_translate("Form",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Hello Union Representor</span></p></body></html>"))
        self.leagueBtn.setText(_translate("Form", "Leagues"))
        self.seasonBtn.setText(_translate("Form", "Seasons"))
        self.refsBtn.setText(_translate("Form", "Referees"))
        self.budgetBtn.setText(_translate("Form", "Team Budget"))
        self.unionBudgetBtn.setText(_translate("Form", "Union Budget"))
        self.policiesBtn.setText(_translate("Form", "Policies"))
        self.optionsLbl.setText(_translate("Form",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Options</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("Form", "Main"))
        item = self.leaguesTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "League"))
        self.addLeagueBtn.setText(_translate("Form", "create league"))
        self.leagueNameLabel.setText(_translate("Form", "league name:"))
        self.seasonLabel.setText(_translate("Form", "season year:"))
        self.assignPointsPolicyLabel.setText(_translate("Form", "assign points policy:"))
        self.assignGamePolicyLabel.setText(_translate("Form", "assign game scheduling policy:"))
        self.assignBudgetPolicyLabel.setText(_translate("Form", "assign team budget policy:"))
        self.NewLeagueLbl.setText(_translate("Form",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Create new league</span></p></body></html>"))
        self.winPointsLbl.setText(_translate("Form", "Points for win:"))
        self.drawPointsLbl.setText(_translate("Form", "Points for draw:"))
        self.losePointsLbl.setText(_translate("Form", "Points for lose:"))
        self.savePointsPolicyBtn.setText(_translate("Form", "Save policy"))
        self.saveGamePolicyBtn.setText(_translate("Form", "Save policy"))
        self.saveBudgetPolicyBtn.setText(_translate("Form", "Save policy"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pointsPolicy), _translate("Form", "Points policy:"))
        self.numOfGamesLbl.setText(_translate("Form", "Number of games against each team:"))
        self.gamesPerWeeksLbl.setText(_translate("Form", "Number of games per week:"))
        self.gameStadiumLbl.setText(_translate("Form", "Game stadium:"))
        self.stadiumComboBox.setItemText(0, _translate("Form", "choose stadium.."))
        self.stadiumComboBox.setItemText(1, _translate("Form", "Home & Away Stadiums"))
        self.stadiumComboBox.setItemText(2, _translate("Form", "Random Stadium"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.gamePolicy), _translate("Form", "Game scheduling policy: "))
        self.minBudgetLbl.setText(_translate("Form", "Minimum budget for team:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.teamBudgetPolicy), _translate("Form", "Team budget policy:"))
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
        self.nameLabel.setText(_translate("Form", "referee name:"))
        self.birthDateLabel.setText(_translate("Form", "referee birth date:"))
        self.refQualificationLabel.setText(_translate("Form", "qualification:"))
        self.refComboBox.setItemText(0, _translate("MainWindow", "qualification.."))
        self.refComboBox.setItemText(1, _translate("MainWindow", "Main"))
        self.refComboBox.setItemText(2, _translate("MainWindow", "Regular"))
        self.newRefLbl.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Create new referee</span></p></body></html>"))
        self.delRefLbl.setText(_translate("Form",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Delete referee</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.refTab), _translate("Form", "Referees"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.teamBudgetTab), _translate("Form", "TeamBudget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unionBudgetTab), _translate("Form", "UnionBudget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.policyTab), _translate("Form", "Policies"))
        self.backBtn.setText(_translate("MainWindow", "Logout"))

    def connect_buttons(self):
        self.backBtn.clicked.connect(self.controller.user_logout)
        self.addRefBtn.clicked.connect(self.add_ref)
        self.leagueBtn.clicked.connect(self.showLeagues)
        self.seasonBtn.clicked.connect(self.showSeasons)
        self.budgetBtn.clicked.connect(self.showBudget)
        self.unionBudgetBtn.clicked.connect(self.showUnionBudget)
        self.refsBtn.clicked.connect(self.showRefs)
        self.removeRefBtn.clicked.connect(self.delete_ref)
        self.savePointsPolicyBtn.clicked.connect(self.addPointsPolicy)
        self.saveGamePolicyBtn.clicked.connect(self.addGamePolicy)
        self.saveBudgetPolicyBtn.clicked.connect(self.addBudgetPolicy)
        self.policiesBtn.clicked.connect(self.display_policies)

        self.showRefereesBtn.clicked.connect(self.showRefs)
        self.assignBudgetPolicyBtn.clicked.connect(lambda: self.showPolicies('Budget'))
        self.assignPointPolicyBtn.clicked.connect(lambda: self.showPolicies('Points'))
        self.assignGamePolicyBtn.clicked.connect(lambda: self.showPolicies('Games'))
        pass


    def save_game_policy(self):
        self.saveGamePolicyBtn.click()

    def save_points_policy(self):
        self.savePointsPolicyBtn.click()

    def save_budget_policy(self):
        self.saveBudgetPolicyBtn.click()

    def set_game_policy(self, games_num, games_per_week, stadium_combination):
        self.gamesNumSpinBox.setText(str(games_num))
        self.gamesPerWeekSpinBox.setText(str(games_per_week))
        self.stadiumComboBox.setCurrentIndex(stadium_combination)

    def set_budget_policy(self, budget):
        self.minBudgetLineEdit.setText(str(budget))

    def set_points_policy(self, win, tie, lose):
        self.winPointsSpinBox.setText(str(win))
        self.drawPointsSpinBox.setText(str(tie))
        self.losePointsSpinBox.setText(str(lose))

    def add_ref(self):
        filled_info = {
            'user_name': self.refUsernameLineEdit.text(),
            'password': self.refPasswordLineEdit.text(),
            'name': self.nameLineEdit.text(),
            'birth_date': self.dateEdit.date().toPyDate().strftime("%Y-%m-%d"),
            'qualification': self.refComboBox.currentText()
        }
        if filled_info.get('qualification') == 'qualification..':
            self.controller.error_window('Invalid ref registration info: \n'
                                         '# Make sure you choose qualification', 'Ref Register Error')
            return
        answer = self.controller.ref_register(filled_info)
        if answer == 'Error':
            self.controller.error_window('Invalid ref registration info: \n'
                                         '# Make sure ref username is longer than 3 letters.\n'
                                         '# Make sure ref password is longer than 3 letters.\n'
                                         '# Make sure ref name doesnt contain numbers and is longer than 2 letters.\n'
                                         '# Make sure you choose qualification',
                                         'Ref Register Error')
        elif answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        elif answer == 'Username Error':
            self.controller.error_window('User with the same username already exists.\n'
                                         'Please try a different username.', 'Ref Register Error')
        else:
            self.controller.success_window('referee added successfully.\n')

    def delete_ref(self):
        filled_info = {
            'user_name': self.refUsernameLineEdit_2.text(),
        }
        answer = self.controller.remove_user(filled_info)
        if answer == 'Error':
            self.controller.error_window('Invalid info: \n'
                                         '# Make sure ref username is correct.\n'
                                         'Ref deletion Error')
        elif answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        else:
            self.controller.success_window('referee deleted successfully.\n')

    def addPointsPolicy(self):
        filled_info = {
            'policy_type': 'points',
            'pointsWin': self.winPointsSpinBox.text(),
            'pointsDraw': self.drawPointsSpinBox.text(),
            'pointsLose': self.losePointsSpinBox.text(),
        }
        if self.filled_info_check(filled_info) is True:
            return
        answer = self.controller.add_policy(filled_info)
        self.policy_ans_check(answer)

    def addGamePolicy(self):
        filled_info = {
            'policy_type': 'games',
            'game_against_each_team': self.gamesNumSpinBox.text(),
            'games_per_week': self.gamesPerWeekSpinBox.text(),
            'stadium': self.stadiumComboBox.currentText(),
        }
        if self.filled_info_check(filled_info) is True:
            return
        answer = self.controller.add_policy(filled_info)
        self.policy_ans_check(answer)

    def addBudgetPolicy(self):
        filled_info = {
            'policy_type': 'budget',
            'min_budget': self.minBudgetLineEdit.text(),
        }
        if self.filled_info_check(filled_info) is True:
            return
        answer = self.controller.add_policy(filled_info)
        self.policy_ans_check(answer)

    def showLeagues(self):
        self.tabWidget.setCurrentIndex(1)

    def showSeasons(self):
        self.tabWidget.setCurrentIndex(2)

    def showRefs(self):
        self.tabWidget.setCurrentIndex(3)
        answer = self.controller.get_refs()
        row_count = len(answer)
        column_count = max([len(p) for p in answer])
        self.refTable.setRowCount(row_count)
        self.refTable.setColumnCount(column_count)
        self.refTable.setHorizontalHeaderLabels((list(answer[0].keys())))
        for row in range(row_count):
            for column in range(column_count):
                item = (list(answer[row].values())[column])
                self.refTable.setItem(row, column, QTableWidgetItem(item))
        self.refTable.resizeColumnsToContents()

    def showBudget(self):
        self.tabWidget.setCurrentIndex(4)

    def showUnionBudget(self):
        self.tabWidget.setCurrentIndex(5)

    def display_policies(self):
        self.tabWidget.setCurrentIndex(6)

    def policy_ans_check(self, answer):
        if answer == 'Error':
            self.controller.error_window('Invalid policy info: \n'
                                         'Please choose stadium',
                                         'New Policy Error')
        elif answer == '':
            self.controller.error_window('The Server is not responding\nPlease try again later...', 'Connection Error')
        elif answer == 'Error policy exists':
            self.controller.error_window('Policy with the same attributes already exists.\n'
                                         'Please try a different name.', 'New policy Error')
        else:
            self.controller.success_window('Policy added successfully.\n')

    def filled_info_check(self, filled_info):
        for info in filled_info:
            if filled_info.get(info) == "":
                self.controller.error_window('Invalid policy info:\n'
                                             'Please fill all fields in order to create a policy.',
                                             'New policy Error')
                return True
        return False

    def showPolicies(self, typeOf):
        self.dialog = QDialog()
        self.dialog.setWindowIcon(QtGui.QIcon('../Resources/football federation.png'))
        self.dialog.setWindowTitle(typeOf + ' policies')
        self.dialog.setGeometry(450, 150, 280, 340)
        self.dialog.PolicyLbl = QtWidgets.QLabel(self.dialog)
        self.dialog.PolicyLbl.setGeometry(QtCore.QRect(35, 0, 251, 41))
        self.dialog.PolicyLbl.setObjectName("PolicyLbl")
        self.dialog.PolicyLbl.setText(typeOf + ' policies - please choose one')
        self.dialog.PolicyLbl.setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
        self.dialog.PolicyTable = QtWidgets.QTableWidget(self.dialog)
        self.dialog.PolicyTable.setGeometry(QtCore.QRect(10, 30, 256, 300))
        self.dialog.PolicyTable.setStyleSheet("background-color: transparent")
        self.dialog.PolicyTable.setObjectName("PolicyTable")
        self.get_policies(typeOf)
        self.dialog.exec_()

    def get_policies(self, typeOf):
        answer = self.controller.get_policy(typeOf)
        row_count = len(answer)
        column_count = max([len(p) for p in answer])
        self.dialog.PolicyTable.setRowCount(row_count)
        self.dialog.PolicyTable.setColumnCount(column_count)
        self.dialog.PolicyTable.setHorizontalHeaderLabels((list(answer[0].keys())))
        for row in range(row_count):
            for column in range(column_count):
                item = (list(answer[row].values())[column])
                self.dialog.PolicyTable.setItem(row, column, QTableWidgetItem(item))
        self.dialog.PolicyTable.resizeColumnsToContents()