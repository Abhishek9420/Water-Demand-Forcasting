import tkinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import PyQt5.QtWidgets as QtWidgets
from tkinter import filedialog
from tkinter import messagebox
from PyQt5 import QtCore, QtGui , QtWidgets
import cv2
from PyQt5.QtGui import QPixmap

import sys
app1 = QtWidgets.QApplication(sys.argv)
screen = app1.primaryScreen()
size = screen.size()

# fit an ARIMA model and plot residual errors
from pandas import read_csv
from pandas import to_datetime
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
import pandas
from pandas import DataFrame
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import time

# load dataset
def parser(x):
	return pandas.to_datetime(x)

print('******Start*****')
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

class Ui_MainWindow1(object):
    
    def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(size.width(),size.height())
        BG_Image='III1.jpg'
        image = cv2.imread(BG_Image)
        image=cv2.resize(image, (size.width(),size.height()))
        cv2.imwrite('B.png', image) 
        MainWindow.setStyleSheet(_fromUtf8("\n""background-image: url(B.png);\n"""))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        # TITLE
        self.u_user_label2 = QtWidgets.QLabel(MainWindow)
        self.u_user_label2.setGeometry(QtCore.QRect(400, 500, 500, 50))
        self.u_user_label2.setObjectName(_fromUtf8("u_user_label2"))
        self.u_user_label2.setFont(QFont('Times', 13))
        self.u_user_label2.setStyleSheet("background-image: url(milkwhite.jpg);;border: 2px solid magneta")
        entered_text='WATER DEMAND'
        self.u_user_label2.setText(f"Project Name: {entered_text}")

        #IMAGE
        self.L = QtWidgets.QLabel(MainWindow)
        self.L.setGeometry(QtCore.QRect(1000, 10, 50, 50))
        # Load image
        self.pixmap = QPixmap('logo.png')
        # Set image to label
        self.L.setPixmap(self.pixmap)
        self.L.resize(self.pixmap.width(),self.pixmap.height())


        
        '''
        # EDIT TEXT
        self.b = QtWidgets.QPlainTextEdit(MainWindow)
        self.b.setGeometry(QtCore.QRect(900, 200, 300, 300))
        self.b.insertPlainText("You can write text here.\n")
        self.b.setStyleSheet("background-image: url(milkwhite.jpg);;border: 2px solid magneta")
        '''
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 300, 131, 27))
        self.pushButton.clicked.connect(self.quit)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton.setStyleSheet("background-image: url(blue.jpg);;border: 2px solid red")
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 180, 131, 27))
        self.pushButton_2.clicked.connect(self.show1)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 220, 131, 27))
        self.pushButton_4.clicked.connect(self.show2)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 260, 131, 27))
        self.pushButton_5.clicked.connect(self.show3)
        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n""color: rgb(0, 0, 0);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.setStyleSheet("background-image: url(white.jpg);;border: 2px solid red")
        
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WATER DEMAND", None))
        self.pushButton_2.setText(_translate("MainWindow", "TEST", None))
        self.pushButton_4.setText(_translate("MainWindow", "PREDICT", None))
        self.pushButton_5.setText(_translate("MainWindow", "PEFORMANCE", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))

    def quit(self):
        print ('Process end')
        print ('******End******')
        app.quit()
        self.close()
        quit()

         
    def show1(self):
        print('TEST\n')
        # Read DATA
        dateparse = lambda dates: pd.to_datetime(dates)
        data = pd.read_csv('Dam_out.csv', parse_dates=['Date'], index_col='Date',date_parser=dateparse)
        data=data[:800]
        data.isnull().sum()

        Q_Koyna = data['Stage_1_2']
        ORIG=Q_Koyna;
        pyplot.figure()
        pyplot.title('Demand');pyplot.plot(Q_Koyna);pyplot.xlabel('YEAR'),pyplot.ylabel('Stage_1_2'),pyplot.show()
        time.sleep(1)
        pyplot.figure()
        Q_Koyna.hist(),pyplot.xlabel('Histogram of Daily'),pyplot.ylabel('Stage_1_2'),pyplot.title('Histogram'),pyplot.show()
        time.sleep(1)
            
        series = read_csv('Dam_out.csv', header=0, index_col=0, parse_dates=True, date_parser=parser)
        series=series[:800]
        series.index = series.index.to_period('M')
        # fit model
        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()
        # summary of fit model
        print(model_fit.summary())
        # line plot of residuals
        residuals = DataFrame(model_fit.resid)
        # summary stats of residuals
        print(residuals.describe())

        X = series.values
        size = int(len(X) * 0.90)
        train, test = X[0:size], X[size:len(X)]
        history = [x for x in train]
        predictions = list()
        # walk-forward validation
        for t in range(len(test)):
                model = ARIMA(history, order=(5,1,0))
                model_fit = model.fit()
                output = model_fit.forecast()
                yhat = output[0]
                predictions.append(yhat)
                obs = test[t]
                history.append(obs)
                print('predicted=%f, expected=%f' % (yhat, obs))
        # evaluate forecasts
        rmse = np.sqrt(mean_squared_error(test, predictions))
        print('Test RMSE: %.3f' % rmse)



    def show2(self):
        print('Train\n')
        series = read_csv('Dam_out.csv', header=0, index_col=0, parse_dates=True, date_parser=parser)
        series=series[:800]
        series.index = series.index.to_period('M')
        # fit model
        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()
        # summary of fit model
        print(model_fit.summary())
        # line plot of residuals
        residuals = DataFrame(model_fit.resid)
        #pyplot.figure()
        #residuals.plot()
        #pyplot.show()
        # density plot of residuals
        residuals.plot(kind='kde')
        pyplot.show()
        # summary stats of residuals
        print(residuals.describe())

        

    def show3(self):
        print('Performance')
        # Read DATA
        dateparse = lambda dates: pd.to_datetime(dates)
        data = pd.read_csv('Dam_out.csv', parse_dates=['Date'], index_col='Date',date_parser=dateparse)
        data=data[:800]
        data.isnull().sum()

        Q_Koyna = data['Stage_1_2']
        ORIG=Q_Koyna;
            
        series = read_csv('Dam_out.csv', header=0, index_col=0, parse_dates=True, date_parser=parser)
        series=series[:800]
        series.index = series.index.to_period('M')
        # fit model
        model = ARIMA(series, order=(5,1,0))
        model_fit = model.fit()
        # line plot of residuals
        residuals = DataFrame(model_fit.resid)
        X = series.values
        size = int(len(X) * 0.99)
        train, test = X[0:size], X[size:len(X)]
        history = [x for x in train]
        predictions = list()
        # walk-forward validation
        for t in range(len(test)):
                model = ARIMA(history, order=(5,1,0))
                model_fit = model.fit()
                output = model_fit.forecast()
                yhat = output[0]
                predictions.append(yhat)
                obs = test[t]
                history.append(obs)
        # evaluate forecasts
        rmse = np.sqrt(mean_squared_error(test, predictions))
        pyplot.figure()
        # plot forecasts against actual outcomes
        pyplot.plot(test)
        pyplot.plot(predictions, color='red')
        pyplot.show()


        
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    MainWindow = QtWidgets.QMainWindow()
    #MainWindow.showFullScreen()
    ui = Ui_MainWindow1()
    ui.setupUii(MainWindow)
    MainWindow.move(0, 0)
    MainWindow.show()
    sys.exit(app.exec_())


