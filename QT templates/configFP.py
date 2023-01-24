# -*- coding: utf-8 -*-
# First Window
################################################################################
## Form generated from reading UI file 'timerWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QLineEdit,
    QPushButton, QSizePolicy, QTimeEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(213, 137)
        Dialog.setStyleSheet(u"QDialog {\n"
"background-color:black;\n"
"}")
        self.timeEdit = QTimeEdit(Dialog)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(50, 40, 118, 22))
        self.dateEdit = QDateEdit(Dialog)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(60, 70, 101, 22))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 100, 93, 28))
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 100, 93, 28))
        self.pushButton_2.setStyleSheet(u"QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 191, 22))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Done", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"    What u want to see here ?", None))
    # retranslateUi

