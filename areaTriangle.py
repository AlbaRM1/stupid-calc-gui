# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'areaTriangle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_areaTriangle(object):
    def setupUi(self, areaTriangle):
        areaTriangle.setObjectName("areaTriangle")
        areaTriangle.resize(513, 195)
        areaTriangle.setMinimumSize(QtCore.QSize(513, 195))
        areaTriangle.setMaximumSize(QtCore.QSize(513, 195))
        areaTriangle.setStyleSheet("color: white; background-color:black;")
        self.centralwidget = QtWidgets.QWidget(areaTriangle)
        self.centralwidget.setStyleSheet("QLineEdit{\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    height: 25px;\n"
"}\n"
"QPushButton{\n"
"    height: 25px;\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        areaTriangle.setCentralWidget(self.centralwidget)

        self.retranslateUi(areaTriangle)
        QtCore.QMetaObject.connectSlotsByName(areaTriangle)

    def retranslateUi(self, areaTriangle):
        _translate = QtCore.QCoreApplication.translate
        areaTriangle.setWindowTitle(_translate("areaTriangle", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("areaTriangle", "Высота треугольника"))
        self.lineEdit_2.setPlaceholderText(_translate("areaTriangle", "Ширина треугольника"))
        self.pushButton.setText(_translate("areaTriangle", "Рассчитать"))