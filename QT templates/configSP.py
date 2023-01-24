# -*- coding: utf-8 -*-
# Second window
################################################################################
## Form generated from reading UI file 'firstWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(153, 78)
        Dialog.setStyleSheet(u"QDialog {\n"
"background-color:black;\n"
"}")
        self.pb1 = QPushButton(Dialog)
        self.pb1.setObjectName(u"pb1")
        self.pb1.setGeometry(QRect(20, 10, 111, 28))
        self.pb1.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300&display=swap');\n"
"QPushButton {\n"
"font-family: 'Oswald', sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: green;\n"
"font-size: 20px;\n"
"}\n"
"")
        self.pb2 = QPushButton(Dialog)
        self.pb2.setObjectName(u"pb2")
        self.pb2.setGeometry(QRect(20, 40, 111, 28))
        self.pb2.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300&display=swap');\n"
"QPushButton {\n"
"font-family: 'Oswald', sans-serif;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: red;\n"
"font-size: 20px;\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pb1.setText(QCoreApplication.translate("Dialog", u"Timer", None))
        self.pb2.setText(QCoreApplication.translate("Dialog", u"Turn off", None))
    # retranslateUi

