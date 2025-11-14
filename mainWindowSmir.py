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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 874)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.videoWidget = QWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.verticalLayout = QVBoxLayout(self.videoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.videoWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(720, 540))

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.videoWidget, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.groupBoxButton = QGroupBox(self.centralwidget)
        self.groupBoxButton.setObjectName(u"groupBoxButton")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxButton)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonStartStopGrab = QPushButton(self.groupBoxButton)
        self.pushButtonStartStopGrab.setObjectName(u"pushButtonStartStopGrab")

        self.verticalLayout_2.addWidget(self.pushButtonStartStopGrab)

        self.pushButtonConnectDisconect = QPushButton(self.groupBoxButton)
        self.pushButtonConnectDisconect.setObjectName(u"pushButtonConnectDisconect")

        self.verticalLayout_2.addWidget(self.pushButtonConnectDisconect)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addWidget(self.groupBoxButton, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBoxButton.setTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u0430\u043c\u0435\u0440\u043e\u0439", None))
        self.pushButtonStartStopGrab.setText(QCoreApplication.translate("MainWindow", u"StartStopGrab", None))
        self.pushButtonConnectDisconect.setText(QCoreApplication.translate("MainWindow", u"ConnectDisconectCam", None))
    # retranslateUi

