import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from First import Ui_First
from Second import Ui_Timer
from weather import Ui_weather
from alert import Ui_reminder
from pyowm import OWM
from alert2 import Ui_alert2


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

    # work of timer...

    def timerStart():
        # while int(timeUser) < 1 or int(timeUser) > 10000:
        #     ui.lineEdit.setText('error')
            # name = input('Enter your name:')

            # while name == '':
            #     print('write something')
            #     name = input('Enter your name:')
            # print('ok') i understand how working validation but i have not enough time to find rules for this lirary to do it


                          
            i = 0  # hours
            ii = 0  # minutes
            timeUser = int(ui.lineEdit_2.text())
            comment = ui.lineEdit.text()
            for q in range(timeUser):
                time.sleep(3)  # set to 60
                i += 1
            showAlert()
            # ui.lineEdit.setText(ui.lineEdit.text())
            return
    
        
# and i not understanding how to share text from timer to reminder as well
    def timerClose():
        Timer.close()

    def showAlert():
        global reminder
        reminder = QtWidgets.QDialog()
        ui = Ui_reminder()
        ui.setupUi(reminder)
        reminder.show()

        def alertRep():
            reminder.close()
            Timer.show()

        def alertOff():
            reminder.close()

        ui.pushButton.clicked.connect(alertRep)
        ui.pushButton_2.clicked.connect(alertOff)

    ui.pushButton.clicked.connect(timerClose)
    ui.pushButton.clicked.connect(timerStart)
    # work of timer...
    def returnToMain():
        Timer.close()
        First.show()

    ui.pushButton_2.clicked.connect(returnToMain)


ui.pb1.clicked.connect(openTimerWindow)


def openWeather():
    global weather
    weather = QtWidgets.QDialog()
    ui = Ui_weather()
    ui.setupUi(weather)
    First.close()
    weather.show()

    def getWeather():
      # while name == '':
    #       print('write something')
    #       name = input('Enter your name:')
      # print('ok') i understand how working validation but i have not enough time to find rules for this lirary to do it
        owm = OWM("4383a10a783aec00988fb6992379ab92")
        mgr = owm.weather_manager()
        place = ui.lineEdit.text()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        temp = w.temperature("celsius")["temp"]

        # while ui.lineEdit.text() == observation :
        #   ui.weatherexport.setText('Write a COUNTRY OR CITY')
        if temp < 5:
            ui.weatherexport.setText(
                "In "
                + place
                + " "
                + w.detailed_status
                + " now."
                + " \nIt about : "
                + str(temp)
                + " degree."
                + " "
                "\nPut on all your clothes )"
            )
        elif temp < 10:
            ui.weatherexport.setText(
                "In "
                + place
                + " "
                + w.detailed_status
                + " now."
                + " \nIt about : "
                + str(temp)
                + " degree."
                + " "
                "\n50/50 but  cold."
            )
        elif temp < 20:
            ui.weatherexport.setText(
                "In "
                + place
                + " "
                + w.detailed_status
                + " now."
                + " \nIt about : "
                + str(temp)
                + " degree."
                + " "
                "\nput on everything you want."
            )
        else:
            ui.weatherexport.setText(
                "In "
                + place
                + " "
                + w.detailed_status
                + " now."
                + " \nIt about : "
                + str(temp)
                + " degree."
                + " "
                "\nhell on the Eart."
            )

    ui.but1.clicked.connect(getWeather)

    def returnToMainn():
        weather.close()
        First.show()

    ui.but2.clicked.connect(returnToMainn)


ui.pb2_2.clicked.connect(openWeather)
sys.exit(app.exec())
