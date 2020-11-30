# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'areaTrapezia.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_areaTrapezia(object):
    def setupUi(self, areaTrapezia):
        areaTrapezia.setObjectName("areaTrapezia")
        areaTrapezia.resize(513, 195)
        areaTrapezia.setMinimumSize(QtCore.QSize(513, 195))
        areaTrapezia.setMaximumSize(QtCore.QSize(513, 195))
        areaTrapezia.setStyleSheet("background: black; color: white;")
        self.centralwidget = QtWidgets.QWidget(areaTrapezia)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"}")
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
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        areaTrapezia.setCentralWidget(self.centralwidget)

        self.retranslateUi(areaTrapezia)
        QtCore.QMetaObject.connectSlotsByName(areaTrapezia)

    def retranslateUi(self, areaTrapezia):
        _translate = QtCore.QCoreApplication.translate
        areaTrapezia.setWindowTitle(_translate("areaTrapezia", "Площадь трапеции"))
        self.lineEdit.setPlaceholderText(_translate("areaTrapezia", "Высота трапеции"))
        self.lineEdit_2.setPlaceholderText(_translate("areaTrapezia", "Первое основание"))
        self.lineEdit_3.setPlaceholderText(_translate("areaTrapezia", "Второе основание"))
        self.pushButton.setText(_translate("areaTrapezia", "Расчитать"))