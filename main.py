import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

from ui import Ui_MainWindow                # Подключение главного окна (калькулятора)
from setMode import Ui_SecondWindow         # Подключение окна setMode
from perimPolygon import Ui_PerimPolygon    # Подключение окна нахождения периметра прямоугольника
from perimTriangle import Ui_perimTriangle  # Подключение окна нахождения периметра треугольника
from areaRectangle import Ui_areaRectangle  # Подключение окна нахождения площади прямоугольника
from areaTriangle import Ui_areaTriangle    # Подключение окна нахождения площади треугольника
from areaSquare import Ui_areaSquare        # Подключение окна нахождения площади квадрата
from areaTrapezia import Ui_areaTrapezia    # Подключение окна нахождения площади трапеции

from math import sqrt

class StupidCalc(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(StupidCalc, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()           # Магия иницианилизации главного окна

    def initUi(self):
        def delete():               # удаление предыдущего элемента с экрана калькулятора
            text = self.ui.label.text() 
            text = self.ui.label.setText( text[0:-1] )
        
        def openSetMode(self):      # Открытие окна изменения мода
            global SecondWindow
            SecondWindow = QtWidgets.QMainWindow()
            ui = Ui_SecondWindow()
            ui.setupUi(SecondWindow)
            SecondWindow.show()

            ui.pushButton.clicked.connect( openPerimPoligon )
            ui.pushButton_2.clicked.connect( openTrianglePolygon )
            ui.pushButton_3.clicked.connect( openAreaRectangle )
            ui.pushButton_4.clicked.connect( openAreaTriangle )
            ui.pushButton_5.clicked.connect( openAreaSquare )
            ui.pushButton_6.clicked.connect( openAreaTrapezia )

        def openPerimPoligon(self): # Открытие окна нахождение периметра прямоугольника 
            global PerimPolygon
            PerimPolygon = QtWidgets.QMainWindow()
            ui = Ui_PerimPolygon()
            ui.setupUi(PerimPolygon)
            PerimPolygon.show()

            def resultPerimPolygon():
                try:                # Проверка на наличие ошибок в полях 
                    a = float( ui.lineEdit.text() )
                    b = float( ui.lineEdit_2.text() )

                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )

                else:
                    c = 2 * ( a + b )
                    ui.label.setText( str( c ) + " см²" )

            ui.pushButton.clicked.connect( resultPerimPolygon )

        def openTrianglePolygon(self): # Открытие окна нахождение периметра треугольника 
            global perimTriangle
            perimTriangle = QtWidgets.QMainWindow()
            ui = Ui_perimTriangle()
            ui.setupUi(perimTriangle)
            perimTriangle.show()

            def resultTrianglePolygon():
                try:                    # Проверка на наличие ошибок в полях 
                    a = float( ui.lineEdit.text() )
                    b = float( ui.lineEdit_2.text() )
                    c = float( ui.lineEdit_3.text() )

                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )

                else:
                    d = a + b + c
                    ui.label.setText( str( d ) + " см²" )

            ui.pushButton.clicked.connect( resultTrianglePolygon )

        def openAreaRectangle(self):    # Открытие окна для вычисления площади треугольника
            global areaRectangle
            areaRectangle = QtWidgets.QMainWindow()
            ui = Ui_areaRectangle()
            ui.setupUi(areaRectangle)
            areaRectangle.show()

            def resultAreaRectangle():
                try:                # Проверка на наличие ошибок в полях 
                    a = float( ui.lineEdit.text() )
                    b = float( ui.lineEdit_2.text() )

                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )

                else:
                    c = a * b
                    ui.label.setText( str( c ) + " см³" )

            ui.pushButton.clicked.connect( resultAreaRectangle )
        
        def openAreaTriangle(self):
            global areaTriangle
            areaTriangle = QtWidgets.QMainWindow()
            ui = Ui_areaTriangle()
            ui.setupUi(areaTriangle)
            areaTriangle.show()

            def resultAreaTriangle():
                try:                # Проверка на наличие ошибок в полях 
                    a = float( ui.lineEdit.text() )
                    b = float( ui.lineEdit_2.text() )

                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )

                else:
                    c = 0.5 * a * b
                    ui.label.setText( str( c ) + " см³" )

            ui.pushButton.clicked.connect( resultAreaTriangle )
        
        def openAreaSquare():
            global areaSquare
            areaSquare = QtWidgets.QMainWindow()
            ui = Ui_areaSquare()
            ui.setupUi(areaSquare)
            areaSquare.show()

            def resultAreaSquare():
                try:
                    a = float( ui.lineEdit.text() )
                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )
                else:
                    b = a**2
                    ui.label.setText( str( b ) + " см³" )

            ui.pushButton.clicked.connect( resultAreaSquare )

        def openAreaTrapezia():
            global areaTrapezia
            areaTrapezia = QtWidgets.QMainWindow()
            ui = Ui_areaTrapezia()
            ui.setupUi(areaTrapezia)
            areaTrapezia.show()

            def resultAreaTrapezia():
                try:
                    a = float( ui.lineEdit.text() )
                    b = float( ui.lineEdit_2.text() )
                    c = float( ui.lineEdit_3.text() )
                except:
                    ui.label.setText( "Вы написали букву в одном из текстовых полей (っ´ω`)ﾉ(╥ω╥)" )
                else:
                    d = 0.5 * a * ( b + c )
                    ui.label.setText( str( d ) + " см³" )
                
                ui.pushButton.clicked.connect( resultAreaTrapezia )

            ui.pushButton.clicked.connect( resultAreaTrapezia )
        self.ui.pushButton.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "7") )
        self.ui.pushButton_2.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "4") )
        self.ui.pushButton_3.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "1") )
        self.ui.pushButton_4.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "8") )
        self.ui.pushButton_5.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "5") )
        self.ui.pushButton_6.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "2") )
        self.ui.pushButton_7.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "9") )
        self.ui.pushButton_8.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "6") )
        self.ui.pushButton_9.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "3") )
        self.ui.pushButton_10.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "0") )

        self.ui.pushButton_11.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "-") ) #вычитание
        self.ui.pushButton_12.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "+") ) #сложение
        self.ui.pushButton_13.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "*") ) #умножение

        self.ui.pushButton_14.clicked.connect( lambda: self.ui.label.setText("") )

        self.ui.pushButton_15.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "/") ) #деление
        self.ui.pushButton_16.clicked.connect( lambda: self.ui.label.setText( str( eval( self.ui.label.text() ) ) ) )

        self.ui.pushButton_17.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + ".") ) # эм..... точка?
        self.ui.pushButton_18.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "%") ) #деление по модулю
        self.ui.pushButton_19.clicked.connect( delete ) #удаление предыдущего элемента
        self.ui.pushButton_20.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "sqrt(" ) ) #квадратный корень
        self.ui.pushButton_21.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + "(" ) ) #скобка, которая открывает
        self.ui.pushButton_22.clicked.connect( lambda: self.ui.label.setText(self.ui.label.text() + ")" ) ) #скобка, которая закрывает

        self.ui.pushButton_23.clicked.connect( openSetMode ) #изменение режима

        self.show()

app = QtWidgets.QApplication([])
application = StupidCalc()
application.show()

sys.exit(app.exec())