# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(511, 274)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lcdSunsetTime = QtGui.QLCDNumber(self.groupBox)
        self.lcdSunsetTime.setGeometry(QtCore.QRect(100, 100, 101, 31))
        self.lcdSunsetTime.setDigitCount(8)
        self.lcdSunsetTime.setObjectName(_fromUtf8("lcdSunsetTime"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdCurrentTime = QtGui.QLCDNumber(self.groupBox)
        self.lcdCurrentTime.setGeometry(QtCore.QRect(100, 20, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdCurrentTime.setFont(font)
        self.lcdCurrentTime.setAutoFillBackground(False)
        self.lcdCurrentTime.setDigitCount(8)
        self.lcdCurrentTime.setObjectName(_fromUtf8("lcdCurrentTime"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdSunriseTime = QtGui.QLCDNumber(self.groupBox)
        self.lcdSunriseTime.setGeometry(QtCore.QRect(100, 60, 101, 31))
        self.lcdSunriseTime.setDigitCount(8)
        self.lcdSunriseTime.setObjectName(_fromUtf8("lcdSunriseTime"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 211, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lcdTimeLapsed = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdTimeLapsed.setGeometry(QtCore.QRect(100, 20, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdTimeLapsed.setFont(font)
        self.lcdTimeLapsed.setAutoFillBackground(False)
        self.lcdTimeLapsed.setDigitCount(8)
        self.lcdTimeLapsed.setObjectName(_fromUtf8("lcdTimeLapsed"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lcdUntilSunset = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdUntilSunset.setGeometry(QtCore.QRect(100, 60, 101, 31))
        self.lcdUntilSunset.setDigitCount(8)
        self.lcdUntilSunset.setObjectName(_fromUtf8("lcdUntilSunset"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 180, 221, 81))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(240, 20, 261, 131))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("img/sunset-clouds-sun-sky-evening-dusk.jpg")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.label_11.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Time Display", None))
        self.groupBox.setTitle(_translate("Dialog", "RSA Time Zone", None))
        self.label_2.setText(_translate("Dialog", "Sunrise Time: ", None))
        self.label.setText(_translate("Dialog", "Current Time: ", None))
        self.label_3.setText(_translate("Dialog", "Sunset Time: ", None))
        self.groupBox_2.setTitle(_translate("Dialog", "CPT Lapsed / Sunset Information", None))
        self.label_7.setText(_translate("Dialog", "Time Until Sunset:", None))
        self.label_8.setText(_translate("Dialog", "Time Lapsed:", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Student Information:", None))
        self.label_10.setText(_translate("Dialog", "Student Number:", None))
        self.lineEdit_2.setText(_translate("Dialog", "57728828", None))
        self.lineEdit.setText(_translate("Dialog", "Leroy Petersen", None))
        self.label_9.setText(_translate("Dialog", "Name:", None))

