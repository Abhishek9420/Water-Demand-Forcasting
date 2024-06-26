# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtCore import *
import PyQt5.QtWidgets as QtWidgets



import sqlite3
from MAIN_CODE import Ui_MainWindow1 as Ui_HomePage
from signup import Ui_signUp as Ui_SignPage
from PyQt5.QtGui import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    
    def UserHomeCheck(self):
        self.userHomeWindow=QtWidgets.QMainWindow()
        self.ui=Ui_HomePage()
        self.ui.setupUii(self.userHomeWindow)
        self.userHomeWindow.show()

        

    def SignupCheck(self):
        self.userHomeWindow=QtWidgets.QDialog()
        self.ui=Ui_SignPage()
        self.ui.setupUi(self.userHomeWindow)
        self.userHomeWindow.show()

           
    def loginCheck(self):
        username1=self.uname_lineEdit.text()
        username =str(username1)
        password1=self.pass_lineEdit.text()
        password = str(password1)
        print("password is:"+password)
        connection=sqlite3.connect("multiD.db")
        s="select *from userdetails where username='"+username+"' and password='"+password+"'"
        print("query is:"+s)
        result=connection.execute(s)
        if(len(result.fetchall())>0):
         print("user found!")
         self.UserHomeCheck()

        else:
         print("user not fount!")
         self.showmsg()
    
    def signupCheck(self):
        self.signUpShow()
        print("Signup button clicked !")

    def showmsg(self):
        self.showdialog1()

    def showdialog1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Login failed")
        msg.setInformativeText("Please enter correct details ")
        msg.setWindowTitle("Status")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        print
        "value of pressed message box button:", retval

    def setinUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(size.width(), size.height())
        Dialog.setStyleSheet(_fromUtf8("background-image: url(B.png); border: 2px solid blue"))
        self.u_user_label = QtWidgets.QLabel(Dialog)
        self.u_user_label.setGeometry(QtCore.QRect(400, 150, 91, 31))
        self.u_user_label.setObjectName(_fromUtf8("u_user_label"))
        self.u_user_label.setStyleSheet("background-image: url(milkwhite.jpg);;border: 2px solid red")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(400, 190, 81, 31))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
        self.pass_label.setStyleSheet("background-image: url(milkwhite.jpg);;border: 2px solid red")
       
        
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(510, 149, 201, 31))
        self.uname_lineEdit.setText(_fromUtf8(""))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.uname_lineEdit.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
       
        
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(510, 190, 201, 31))
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        
        ##################################################################
        # LOGIN
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(510, 250, 201, 31))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.login_btn.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        self.login_btn.clicked.connect(self.loginCheck)
        ####################################################################
        # SIGNUP
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(510, 300, 201, 31))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        self.signup_btn.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        self.signup_btn.clicked.connect(self.SignupCheck)
        ####################################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LOGIN FORM", None))
        self.u_user_label.setText(_translate("Dialog", "NAME", None))
        self.pass_label.setText(_translate("Dialog", "PASSWORD", None))
        self.login_btn.setText(_translate("Dialog", "LOGIN TO SYSTEM", None))
        self.signup_btn.setText(_translate("Dialog", "SIGN UP", None))

        
    def quit(self):
        print ('Process end')
        print ('******End******')
        quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    Dialog = QtWidgets.QDialog()
    Dialog.move(10, 10)
    ui = Ui_Dialog()
    ui.setinUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

