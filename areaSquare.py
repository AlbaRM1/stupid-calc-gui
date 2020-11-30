# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'areaSquare.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_areaSquare(object):
    def setupUi(self, areaSquare):
        areaSquare.setObjectName("areaSquare")
        areaSquare.resize(513, 195)
        areaSquare.setMinimumSize(QtCore.QSize(513, 195))
        areaSquare.setMaximumSize(QtCore.QSize(513, 195))
        areaSquare.setStyleSheet("color: white;background-color: black;")
        areaSquare.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(areaSquare)
        self.centralwidget.setStyleSheet("QLineEdit{\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;    \n"
"    height: 40px;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(85, 87, 83);\n"
"    height: 40px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
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
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        areaSquare.setCentralWidget(self.centralwidget)

        self.retranslateUi(areaSquare)
        QtCore.QMetaObject.connectSlotsByName(areaSquare)

    def retranslateUi(self, areaSquare):
        _translate = QtCore.QCoreApplication.translate
        areaSquare.setWindowTitle(_translate("areaSquare", "Площадь квадрата"))
        self.lineEdit.setPlaceholderText(_translate("areaSquare", "Сторона квадрата"))
        self.pushButton.setText(_translate("areaSquare", "Рассчитать"))