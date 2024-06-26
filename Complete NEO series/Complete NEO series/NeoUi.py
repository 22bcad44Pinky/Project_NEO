# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NeoUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, -10, 751, 551))
        self.bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.bg_border = QtWidgets.QLabel(self.centralwidget)
        self.bg_border.setGeometry(QtCore.QRect(0, 0, 731, 521))
        self.bg_border.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border : 2px Solid White\n"
"")
        self.bg_border.setText("")
        self.bg_border.setObjectName("bg_border")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 460, 131, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(76, 223, 13);\n"
"border : 2px Solid Green")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 460, 131, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(76, 223, 13);\n"
"border : 2px Solid Green")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(80, -20, 571, 391))
        self.gif.setStyleSheet("")
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("DataBase/Gui/VoiceReg/Siri_1.gif"))
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        self.terminal = QtWidgets.QLabel(self.centralwidget)
        self.terminal.setGeometry(QtCore.QRect(10, 380, 431, 131))
        self.terminal.setStyleSheet("border-color: rgb(36, 191, 54);\n"
"border : 2px Solid Green")
        self.terminal.setText("")
        self.terminal.setObjectName("terminal")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(450, 410, 271, 41))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"\n"
"color: rgb(0, 200, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"border : 2px Solid Green")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "CLOSE"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
