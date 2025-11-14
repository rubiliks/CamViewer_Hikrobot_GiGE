# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowSmir.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 785)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.videoWidget = QWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setGeometry(QRect(10, 20, 711, 761))
        self.groupBoxButton = QGroupBox(self.centralwidget)
        self.groupBoxButton.setObjectName(u"groupBoxButton")
        self.groupBoxButton.setGeometry(QRect(730, 10, 281, 81))
        self.gridLayoutWidget = QWidget(self.groupBoxButton)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 20, 281, 41))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonStartStopGrab = QPushButton(self.gridLayoutWidget)
        self.pushButtonStartStopGrab.setObjectName(u"pushButtonStartStopGrab")

        self.gridLayout.addWidget(self.pushButtonStartStopGrab, 0, 1, 1, 1)

        self.pushButtonConnectDisconect = QPushButton(self.gridLayoutWidget)
        self.pushButtonConnectDisconect.setObjectName(u"pushButtonConnectDisconect")

        self.gridLayout.addWidget(self.pushButtonConnectDisconect, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBoxButton.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0430\u043c\u0435\u0440\u043e\u0439", None))
        self.pushButtonStartStopGrab.setText(QCoreApplication.translate("MainWindow", u"StartStopGrab", None))
        self.pushButtonConnectDisconect.setText(QCoreApplication.translate("MainWindow", u"ConnectDisconectCam", None))
    # retranslateUi

