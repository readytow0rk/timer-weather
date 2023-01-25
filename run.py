import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from First import Ui_First
from Second import Ui_Timer
from Third import Ui_TurnOff
from weather import Ui_weather
from pyowm import OWM



app = QtWidgets.QApplication(sys.argv)

First = QtWidgets.QDialog()
ui = Ui_First()
ui.setupUi(First)
First.show()

   
def openTimerWindow():
    global Timer
    Timer = QtWidgets.QDialog()
    ui = Ui_Timer()
    ui.setupUi(Timer)
    First.close()
    Timer.show()

    def returnToMain():
        Timer.close()
        First.show()

    ui.pushButton_2.clicked.connect(returnToMain)


def openTurnOff():
    global TurnOff
    TurnOff = QtWidgets.QDialog()
    ui = Ui_TurnOff()
    ui.setupUi(TurnOff)
    First.close()
    TurnOff.show()

    def returnToMainn():
        TurnOff.close()
        First.show()     
    ui.pushButton_2.clicked.connect(returnToMainn)    


def openWeather():
    global weather
    weather = QtWidgets.QDialog()
    ui = Ui_weather()
    ui.setupUi(weather)
    First.close()
    weather.show()
    
    # owm = OWM('4383a10a783aec00988fb6992379ab92')
    # mgr = owm.weather_manager()
    # place = input('Where u live?')
    # observation = mgr.weather_at_place(place)
    # w = observation.weather
    # temp = w.temperature('celsius')['temp']
    # print('In' + place + w.detailed_status + 'now' )

    # print( 'it about : ' + str(temp) + ' degree')

    # if temp < 5 :
    #     print('Put on all your clothes )') 
    # elif temp < 10 :
    #     print('50/50 but  cold.') 
    # elif temp < 20 :
    #     print('put on everything you want.') 
    # else : 
    #     print('hell on the Eart.')
    
    def returnToMainn():
        weather.close()
        First.show()     
    ui.but2.clicked.connect(returnToMainn) 
    

ui.pb2_2.clicked.connect(openWeather)
ui.pb2.clicked.connect(openTurnOff)
ui.pb1.clicked.connect(openTimerWindow)   
    

sys.exit(app.exec())







