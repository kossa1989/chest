# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pkkos\PycharmProjects\Chest\main-chest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
import Hashconf
import conf


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ikony chest/png/017-safe-box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(280, 50, 490, 460))
        self.tableView.setObjectName("tableView")

        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(140, 320, 100, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ikony chest/png/031-gloves.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon1)
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.pushButton_find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find.setGeometry(QtCore.QRect(450, 18, 100, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ikony chest/png/008-magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_find.setIcon(icon2)
        self.pushButton_find.setObjectName("pushButton_find")

        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setGeometry(QtCore.QRect(280, 520, 100, 30))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ikony chest/png/045-coins.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_edit.setIcon(icon3)
        self.pushButton_edit.setObjectName("pushButton_edit")

        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(400, 520, 100, 30))
        self.pushButton_refresh.setObjectName("pushButton_refresh")

        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(770, 50, 20, 460))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.plainTextEdit_notes = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_notes.setGeometry(QtCore.QRect(20, 200, 220, 101))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit_notes.setFont(font)
        self.plainTextEdit_notes.setPlainText("")
        self.plainTextEdit_notes.setObjectName("plainTextEdit_notes")

        self.lineEdit_account = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_account.setGeometry(QtCore.QRect(20, 50, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_account.setFont(font)
        self.lineEdit_account.setText("")
        self.lineEdit_account.setMaxLength(100)
        self.lineEdit_account.setObjectName("lineEdit_account")

        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(20, 100, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setMaxLength(100)
        self.lineEdit_login.setObjectName("lineEdit_login")

        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(20, 150, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setMaxLength(100)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.label_notes = QtWidgets.QLabel(self.centralwidget)
        self.label_notes.setGeometry(QtCore.QRect(20, 185, 28, 13))
        self.label_notes.setObjectName("label_notes")

        self.label_password = QtWidgets.QLabel(self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(20, 135, 52, 13))
        self.label_password.setObjectName("label_password")

        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(20, 83, 47, 13))
        self.label_login.setObjectName("label_login")

        self.label_account = QtWidgets.QLabel(self.centralwidget)
        self.label_account.setGeometry(QtCore.QRect(20, 30, 72, 13))
        self.label_account.setObjectName("label_account")

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(20, 320, 100, 30))
        self.pushButton_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ikony chest/png/037-badge-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon4)
        self.pushButton_save.setObjectName("pushButton_save")

        self.lineEdit_gen_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gen_password.setGeometry(QtCore.QRect(20, 400, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_gen_password.setFont(font)
        self.lineEdit_gen_password.setMaxLength(100)
        self.lineEdit_gen_password.setClearButtonEnabled(False)
        self.lineEdit_gen_password.setObjectName("lineEdit_gen_password")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 380, 100, 13))
        self.label_5.setObjectName("label_5")

        self.checkBox_lowerletters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_lowerletters.setGeometry(QtCore.QRect(20, 440, 110, 20))
        self.checkBox_lowerletters.setAutoFillBackground(False)
        self.checkBox_lowerletters.setChecked(True)
        self.checkBox_lowerletters.setObjectName("checkBox_lowerletters")

        self.checkBox_upperletters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_upperletters.setGeometry(QtCore.QRect(20, 460, 110, 20))
        self.checkBox_upperletters.setObjectName("checkBox_upperletters")

        self.checkBox_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_symbols.setGeometry(QtCore.QRect(20, 480, 110, 20))
        self.checkBox_symbols.setObjectName("checkBox_symbols")

        self.lineEdit_find = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_find.setGeometry(QtCore.QRect(280, 18, 150, 30))
        self.lineEdit_find.setObjectName("lineEdit_find")

        self.pushButton_generate_password = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_generate_password.setGeometry(QtCore.QRect(140, 445, 100, 30))
        self.pushButton_generate_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ikony chest/png/028-key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_generate_password.setIcon(icon5)
        self.pushButton_generate_password.setObjectName("pushButton_generate_password")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 510, 90, 20))
        self.label_6.setObjectName("label_6")

        self.lineEdit_no_characters = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_no_characters.setGeometry(QtCore.QRect(20, 505, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_no_characters.setFont(font)
        self.lineEdit_no_characters.setMaxLength(2)
        self.lineEdit_no_characters.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_characters.setObjectName("lineEdit_no_characters")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew_Account = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ikony chest/png/001-detective.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Account.setIcon(icon6)
        self.actionNew_Account.setObjectName("actionNew_Account")

        self.actionEdit_Account = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ikony chest/png/004-dna.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Account.setIcon(icon7)
        self.actionEdit_Account.setObjectName("actionEdit_Account")

        self.actionChange_SuperPassword = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ikony chest/png/002-badge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_SuperPassword.setIcon(icon8)
        self.actionChange_SuperPassword.setObjectName("actionChange_SuperPassword")

        self.actionDelete_Account = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ikony chest/png/005-gun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Account.setIcon(icon9)
        self.actionDelete_Account.setObjectName("actionDelete_Account")

        self.actionClose_App = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ikony chest/png/016-handcuffs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_App.setIcon(icon10)
        self.actionClose_App.setObjectName("actionClose_App")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ikony chest/png/033-glasses.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon11)
        self.actionAbout.setObjectName("actionAbout")

        self.menuMenu.addAction(self.actionNew_Account)
        self.menuMenu.addAction(self.actionEdit_Account)
        self.menuMenu.addAction(self.actionDelete_Account)
        self.menuMenu.addAction(self.actionChange_SuperPassword)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClose_App)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chest - safe place for your account"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_find.setText(_translate("MainWindow", "Find"))
        self.pushButton_edit.setText(_translate("MainWindow", "Edit"))
        self.pushButton_refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_notes.setText(_translate("MainWindow", "Notes"))
        self.label_password.setText(_translate("MainWindow", "Passowrd"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_account.setText(_translate("MainWindow", "Account Name"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Generate password"))
        self.checkBox_lowerletters.setText(_translate("MainWindow", "lowercase letters"))
        self.checkBox_upperletters.setText(_translate("MainWindow", "uppercase letters"))
        self.checkBox_symbols.setText(_translate("MainWindow", "symbols"))
        self.pushButton_generate_password.setText(_translate("MainWindow", "Generate"))
        self.label_6.setText(_translate("MainWindow", " characters (8-20)"))
        self.lineEdit_no_characters.setText(_translate("MainWindow", "8"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionNew_Account.setText(_translate("MainWindow", "New Account"))
        self.actionEdit_Account.setText(_translate("MainWindow", "Edit Account"))
        self.actionChange_SuperPassword.setText(_translate("MainWindow", "Change SuperPassword"))
        self.actionDelete_Account.setText(_translate("MainWindow", "Delete Account"))
        self.actionClose_App.setText(_translate("MainWindow", "Close App"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


    def clear_data:
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

