# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'areaRectangle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_areaRectangle(object):
    def setupUi(self, areaRectangle):
        areaRectangle.setObjectName("areaRectangle")
        areaRectangle.resize(513, 195)
        areaRectangle.setMinimumSize(QtCore.QSize(513, 195))
        areaRectangle.setMaximumSize(QtCore.QSize(513, 195))
        areaRectangle.setStyleSheet("color: white;background-color: black;")
        areaRectangle.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.centralwidget = QtWidgets.QWidget(areaRectangle)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"    background-color: rgb(85, 87, 83);\n"
"    height: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    height: 25px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
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
        areaRectangle.setCentralWidget(self.centralwidget)

        self.retranslateUi(areaRectangle)
        QtCore.QMetaObject.connectSlotsByName(areaRectangle)

    def retranslateUi(self, areaRectangle):
        _translate = QtCore.QCoreApplication.translate
        areaRectangle.setWindowTitle(_translate("areaRectangle", "Нахождение площади прямоугольника"))
        self.lineEdit.setPlaceholderText(_translate("areaRectangle", "1 сторона прямоугольника (в см)"))
        self.lineEdit_2.setPlaceholderText(_translate("areaRectangle", "2 сторона прямоугольника (в см)"))
        self.pushButton.setText(_translate("areaRectangle", "Рассчитать"))

