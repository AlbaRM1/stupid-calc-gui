# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'perimTriangle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_perimTriangle(object):
    def setupUi(self, perimTriangle):
        perimTriangle.setObjectName("perimTriangle")
        perimTriangle.resize(513, 195)
        perimTriangle.setMinimumSize(QtCore.QSize(513, 195))
        perimTriangle.setMaximumSize(QtCore.QSize(513, 195))
        perimTriangle.setStyleSheet("background: black; color: white;")
        self.centralwidget = QtWidgets.QWidget(perimTriangle)
        self.centralwidget.setStyleSheet("QLineEdit{\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    height: 25px;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(85, 87, 83);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(136, 138, 133);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 511, 191))
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
        perimTriangle.setCentralWidget(self.centralwidget)

        self.retranslateUi(perimTriangle)
        QtCore.QMetaObject.connectSlotsByName(perimTriangle)

    def retranslateUi(self, perimTriangle):
        _translate = QtCore.QCoreApplication.translate
        perimTriangle.setWindowTitle(_translate("perimTriangle", "Периметр треугольника"))
        self.lineEdit.setPlaceholderText(_translate("perimTriangle", "1 сторона (см)"))
        self.lineEdit_2.setPlaceholderText(_translate("perimTriangle", "2 сторона (см)"))
        self.lineEdit_3.setPlaceholderText(_translate("perimTriangle", "3 сторона (см)"))
        self.pushButton.setText(_translate("perimTriangle", "PushButton"))
