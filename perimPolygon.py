# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perimPolygon.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PerimPolygon(object):
    def setupUi(self, PerimPolygon):
        PerimPolygon.setObjectName("PerimPolygon")
        PerimPolygon.resize(513, 195)
        PerimPolygon.setMinimumSize(QtCore.QSize(513, 195))
        PerimPolygon.setMaximumSize(QtCore.QSize(513, 195))
        PerimPolygon.setStyleSheet("background-color: black;")
        PerimPolygon.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(PerimPolygon)
        self.centralwidget.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}\n"
"QLineEdit{\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    height: 25px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton{\n"
"    color: white;\n"
"    height: 25px;\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(136, 138, 133);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
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
        PerimPolygon.setCentralWidget(self.centralwidget)

        self.retranslateUi(PerimPolygon)
        QtCore.QMetaObject.connectSlotsByName(PerimPolygon)

    def retranslateUi(self, PerimPolygon):
        _translate = QtCore.QCoreApplication.translate
        PerimPolygon.setWindowTitle(_translate("PerimPolygon", "Периметр прямоугольника"))
        self.lineEdit.setPlaceholderText(_translate("PerimPolygon", "Первая сторона (в см, можно и в дм, но будет написано \"см\" :))"))
        self.lineEdit_2.setPlaceholderText(_translate("PerimPolygon", "Вторая сторона (в см, можно и в дм, но будет написано \"см\" :))"))
        self.pushButton.setText(_translate("PerimPolygon", "Расчитать"))