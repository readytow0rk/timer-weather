# Form implementation generated from reading ui file 'alert.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_reminder(object):
    def setupUi(self, reminder):
        reminder.setObjectName("reminder")
        reminder.resize(212, 129)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clock.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        reminder.setWindowIcon(icon)
        reminder.setStyleSheet("QDialog {\n"
"background-color:black;\n"
"}")
        self.buttonBox = QtWidgets.QDialogButtonBox(reminder)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(reminder)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 191, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(0, 244, 138);\n"
"font-size: 20px;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(reminder)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(reminder)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(reminder)
        self.buttonBox.accepted.connect(reminder.accept) # type: ignore
        self.buttonBox.rejected.connect(reminder.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(reminder)

    def retranslateUi(self, reminder):
        _translate = QtCore.QCoreApplication.translate
        reminder.setWindowTitle(_translate("reminder", "Alert"))
        self.pushButton.setText(_translate("reminder", "Repeat"))
        self.pushButton_2.setText(_translate("reminder", "Close"))
        self.lineEdit.setText(_translate("reminder", "    What u want to see here ?"))


