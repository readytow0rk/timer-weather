import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from First import Ui_First
from Second import Ui_Timer
from third import Ui_TurnOff
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
        while True:
        
            i = 0 #hours
            ii = 0 #minutes
            timeUser = int(ui.lineEdit_2.text())
            comment = ui.lineEdit.text()
            for q in range(timeUser):
                time.sleep(3) #set to 60
                i += 1 
            showAlert()
            
            return

            
        


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

#heroku validation
def openTurnOff():
    global TurnOff
    TurnOff = QtWidgets.QDialog()
    ui = Ui_TurnOff()
    ui.setupUi(TurnOff)
    First.close()
    TurnOff.show()

# work of turnoffer ...
    def turnOff():
        # shutdown /s /t 60  it will turn off your pc )
        TurnOff.close()
        global alert2
        alert2 = QtWidgets.QDialog()
        ui = Ui_alert2()
        ui.setupUi(alert2)
        alert2.show()
    
    
    def closeAlertt():
        alert2.close()

        ui.pushButt.clicked.connct(closeAlertt)


    ui.push.clicked.connect(turnOff)
# work of turnoffer ...     fucking tabulation
    def returnToMainn():
        TurnOff.close()
        First.show()     
    ui.pushButton_2.clicked.connect(returnToMainn)    



ui.pb2.clicked.connect(openTurnOff)

ui.pb1.clicked.connect(openTimerWindow)   
    


def openWeather():
    global weather
    weather = QtWidgets.QDialog()
    ui = Ui_weather()
    ui.setupUi(weather)
    First.close()
    weather.show()

   
    
    def getWeather():
        # while place != observation :
        #     ui.weatherexport.setText('Write real city') 

        owm = OWM('4383a10a783aec00988fb6992379ab92')
        mgr = owm.weather_manager()
        place = ui.lineEdit.text()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        
        temp = w.temperature('celsius')['temp']

            

        if temp < 5 :
            ui.weatherexport.setText('In ' + place  + ' '+ w.detailed_status  + ' now.' +  ' \nIt about : ' + str(temp) + ' degree.' +' ' '\nPut on all your clothes )') 
        elif temp < 10 :
            ui.weatherexport.setText('In ' + place  + ' '+ w.detailed_status  + ' now.' +  ' \nIt about : ' + str(temp) + ' degree.' +' ' '\n50/50 but  cold.') 
        elif temp < 20 :
            ui.weatherexport.setText('In ' + place  + ' '+ w.detailed_status  + ' now.' +  ' \nIt about : ' + str(temp) + ' degree.' +' ' '\nput on everything you want.') 
        else : 
            ui.weatherexport.setText('In ' + place  + ' '+ w.detailed_status  + ' now.' +  ' \nIt about : ' + str(temp) + ' degree.' +' ' '\nhell on the Eart.')
        
    ui.but1.clicked.connect(getWeather)
      
        
    def returnToMainn():
        weather.close()
        First.show()     
    ui.but2.clicked.connect(returnToMainn) 
    

ui.pb2_2.clicked.connect(openWeather)
sys.exit(app.exec())







