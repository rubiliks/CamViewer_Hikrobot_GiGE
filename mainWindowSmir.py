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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(962, 576)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.videoWidget = QWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.videoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.videoWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(720, 540))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.videoWidget, 0, 0, 1, 1)

        self.groupBoxButton = QGroupBox(self.centralwidget)
        self.groupBoxButton.setObjectName(u"groupBoxButton")
        self.groupBoxButton.setMinimumSize(QSize(200, 0))
        self.groupBoxButton.setMaximumSize(QSize(210, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxButton)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cameraStatusProgressBar = QProgressBar(self.groupBoxButton)
        self.cameraStatusProgressBar.setObjectName(u"cameraStatusProgressBar")
        self.cameraStatusProgressBar.setValue(100)
        self.cameraStatusProgressBar.setTextVisible(False)
        self.cameraStatusProgressBar.setOrientation(Qt.Orientation.Horizontal)
        self.cameraStatusProgressBar.setInvertedAppearance(False)
        self.cameraStatusProgressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_2.addWidget(self.cameraStatusProgressBar)

        self.pushButtonConnectCam = QPushButton(self.groupBoxButton)
        self.pushButtonConnectCam.setObjectName(u"pushButtonConnectCam")

        self.verticalLayout_2.addWidget(self.pushButtonConnectCam)

        self.pushButtonDisconectCam = QPushButton(self.groupBoxButton)
        self.pushButtonDisconectCam.setObjectName(u"pushButtonDisconectCam")

        self.verticalLayout_2.addWidget(self.pushButtonDisconectCam)

        self.CnnLayout = QVBoxLayout()
        self.CnnLayout.setObjectName(u"CnnLayout")
        self.cnn_control_label = QLabel(self.groupBoxButton)
        self.cnn_control_label.setObjectName(u"cnn_control_label")

        self.CnnLayout.addWidget(self.cnn_control_label)

        self.pushButtonStartObjDetectCnn = QPushButton(self.groupBoxButton)
        self.pushButtonStartObjDetectCnn.setObjectName(u"pushButtonStartObjDetectCnn")

        self.CnnLayout.addWidget(self.pushButtonStartObjDetectCnn)

        self.pushButtonStopObjDetectCnn = QPushButton(self.groupBoxButton)
        self.pushButtonStopObjDetectCnn.setObjectName(u"pushButtonStopObjDetectCnn")

        self.CnnLayout.addWidget(self.pushButtonStopObjDetectCnn)


        self.verticalLayout_2.addLayout(self.CnnLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.camera_setting_label = QLabel(self.groupBoxButton)
        self.camera_setting_label.setObjectName(u"camera_setting_label")

        self.verticalLayout_2.addWidget(self.camera_setting_label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gain_lable = QLabel(self.groupBoxButton)
        self.gain_lable.setObjectName(u"gain_lable")

        self.gridLayout.addWidget(self.gain_lable, 1, 0, 1, 1)

        self.exposureTime_spinBox = QSpinBox(self.groupBoxButton)
        self.exposureTime_spinBox.setObjectName(u"exposureTime_spinBox")

        self.gridLayout.addWidget(self.exposureTime_spinBox, 0, 1, 1, 1)

        self.exposureTime_lable = QLabel(self.groupBoxButton)
        self.exposureTime_lable.setObjectName(u"exposureTime_lable")

        self.gridLayout.addWidget(self.exposureTime_lable, 0, 0, 1, 1)

        self.gain_doubleSpinBox = QDoubleSpinBox(self.groupBoxButton)
        self.gain_doubleSpinBox.setObjectName(u"gain_doubleSpinBox")

        self.gridLayout.addWidget(self.gain_doubleSpinBox, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.groupBoxButton, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera view", None))
        self.groupBoxButton.setTitle(QCoreApplication.translate("MainWindow", u"Camera control", None))
        self.cameraStatusProgressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pushButtonConnectCam.setText(QCoreApplication.translate("MainWindow", u"Connect Cam", None))
        self.pushButtonDisconectCam.setText(QCoreApplication.translate("MainWindow", u"Disconect Cam", None))
        self.cnn_control_label.setText(QCoreApplication.translate("MainWindow", u"CNN control", None))
        self.pushButtonStartObjDetectCnn.setText(QCoreApplication.translate("MainWindow", u"Start Obj Detection", None))
        self.pushButtonStopObjDetectCnn.setText(QCoreApplication.translate("MainWindow", u"Stop Obj Detection", None))
        self.camera_setting_label.setText(QCoreApplication.translate("MainWindow", u"Camera setting", None))
        self.gain_lable.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.exposureTime_lable.setText(QCoreApplication.translate("MainWindow", u"ExposureTime", None))
    # retranslateUi

