import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from First import Ui_First
from Second import Ui_Timer
from third import Ui_TurnOff

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


ui.pb1.clicked.connect(openTimerWindow)    



sys.exit(app.exec())




