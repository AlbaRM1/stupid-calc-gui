# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 645)
        MainWindow.setMinimumSize(QtCore.QSize(430, 645))
        MainWindow.setMaximumSize(QtCore.QSize(430, 645))
        MainWindow.setSizeIncrement(QtCore.QSize(430, 0))
        MainWindow.setBaseSize(QtCore.QSize(430, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("background-color: black;\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QPushButton{\n"
"    height: 100%;\n"
"    background-color: rgb(85, 87, 83);\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    font-size: 25px;\n"
"    color:white;\n"
"}\n"
".QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 185, 411, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton#pushButton_12{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_12:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 5, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("QPushButton#pushButton_18{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_18:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setFlat(False)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_18, 0, 3, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_11:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton#pushButton_13{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_13:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 4, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton#pushButton_16{\n"
"    background-color: rgb(245, 121, 0);\n"
"}\n"
"QPushButton#pushButton_16:hover{\n"
"    background-color: rgb(252, 175, 62);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 5, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet("QPushButton#pushButton_14{\n"
"    background-color: rgb(204, 0, 0);\n"
"}\n"
"QPushButton#pushButton_14:hover{\n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton#pushButton_15{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_15:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_15.setAutoDefault(False)
        self.pushButton_15.setDefault(False)
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 5, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 5, 1, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("QPushButton#pushButton_19{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_19:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setDefault(False)
        self.pushButton_19.setFlat(False)
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_19, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet("QPushButton#pushButton_20{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_20:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_20.setDefault(False)
        self.pushButton_20.setFlat(False)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 0, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("QPushButton#pushButton_21{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_21:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_21.setAutoDefault(False)
        self.pushButton_21.setDefault(False)
        self.pushButton_21.setFlat(False)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 0, 4, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("QPushButton#pushButton_22{\n"
"    background-color: rgb(46, 52, 54);\n"
"}\n"
"QPushButton#pushButton_22:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setDefault(False)
        self.pushButton_22.setFlat(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 1, 4, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setKerning(True)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("QPushButton#pushButton_23{\n"
"    background-color: rgb(52, 101, 164)\n"
"}\n"
"QPushButton#pushButton_23:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.pushButton_23.setAutoDefault(False)
        self.pushButton_23.setDefault(False)
        self.pushButton_23.setFlat(False)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 5, 4, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StupidCalc"))
        self.pushButton_12.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "2"))
        self.pushButton_17.setText(_translate("MainWindow", "."))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_18.setText(_translate("MainWindow", "%"))
        self.pushButton_11.setText(_translate("MainWindow", "-"))
        self.pushButton_13.setText(_translate("MainWindow", "x"))
        self.pushButton_16.setText(_translate("MainWindow", "="))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "8"))
        self.pushButton_14.setText(_translate("MainWindow", "С"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "4"))
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_19.setText(_translate("MainWindow", "<"))
        self.pushButton_20.setText(_translate("MainWindow", "√"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_21.setText(_translate("MainWindow", "("))
        self.pushButton_22.setText(_translate("MainWindow", ")"))
        self.pushButton_23.setText(_translate("MainWindow", "Mode"))
