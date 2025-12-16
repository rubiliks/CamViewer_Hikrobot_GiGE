# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowSmir_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 704)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.videoWidget = QWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        self.videoWidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.videoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.videoWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout_5 = QVBoxLayout(self.mainTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.CameraLabel = QLabel(self.mainTab)
        self.CameraLabel.setObjectName(u"CameraLabel")
        self.CameraLabel.setEnabled(True)
        self.CameraLabel.setMinimumSize(QSize(720, 540))
        self.CameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.CameraLabel)

        self.tabWidget.addTab(self.mainTab, "")
        self.MaterialTab = QWidget()
        self.MaterialTab.setObjectName(u"MaterialTab")
        self.verticalLayout_19 = QVBoxLayout(self.MaterialTab)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")

        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.MaterialTab, "")
        self.SettingTab = QWidget()
        self.SettingTab.setObjectName(u"SettingTab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SettingTab.sizePolicy().hasHeightForWidth())
        self.SettingTab.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.SettingTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea = QScrollArea(self.SettingTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.AascrollAreaWidgetContents = QWidget()
        self.AascrollAreaWidgetContents.setObjectName(u"AascrollAreaWidgetContents")
        self.AascrollAreaWidgetContents.setGeometry(QRect(0, 0, 377, 502))
        self.verticalLayout_14 = QVBoxLayout(self.AascrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cameraSettinglabel = QLabel(self.AascrollAreaWidgetContents)
        self.cameraSettinglabel.setObjectName(u"cameraSettinglabel")
        self.cameraSettinglabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.cameraSettinglabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exposureTime_lable = QLabel(self.AascrollAreaWidgetContents)
        self.exposureTime_lable.setObjectName(u"exposureTime_lable")

        self.horizontalLayout_2.addWidget(self.exposureTime_lable)

        self.exposureTime_spinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.exposureTime_spinBox.setObjectName(u"exposureTime_spinBox")

        self.horizontalLayout_2.addWidget(self.exposureTime_spinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gainLable = QLabel(self.AascrollAreaWidgetContents)
        self.gainLable.setObjectName(u"gainLable")

        self.horizontalLayout_8.addWidget(self.gainLable)

        self.gainDoubleSpinBox = QDoubleSpinBox(self.AascrollAreaWidgetContents)
        self.gainDoubleSpinBox.setObjectName(u"gainDoubleSpinBox")

        self.horizontalLayout_8.addWidget(self.gainDoubleSpinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.BalanceRedlabel = QLabel(self.AascrollAreaWidgetContents)
        self.BalanceRedlabel.setObjectName(u"BalanceRedlabel")

        self.horizontalLayout_9.addWidget(self.BalanceRedlabel)

        self.BalanceRedSpinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.BalanceRedSpinBox.setObjectName(u"BalanceRedSpinBox")

        self.horizontalLayout_9.addWidget(self.BalanceRedSpinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.BalanceGreenlabel = QLabel(self.AascrollAreaWidgetContents)
        self.BalanceGreenlabel.setObjectName(u"BalanceGreenlabel")

        self.horizontalLayout_10.addWidget(self.BalanceGreenlabel)

        self.BalanceGreenspinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.BalanceGreenspinBox.setObjectName(u"BalanceGreenspinBox")

        self.horizontalLayout_10.addWidget(self.BalanceGreenspinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.BalanceBuelabel = QLabel(self.AascrollAreaWidgetContents)
        self.BalanceBuelabel.setObjectName(u"BalanceBuelabel")

        self.horizontalLayout_11.addWidget(self.BalanceBuelabel)

        self.BalanceBuespinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.BalanceBuespinBox.setObjectName(u"BalanceBuespinBox")

        self.horizontalLayout_11.addWidget(self.BalanceBuespinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Widthlabel = QLabel(self.AascrollAreaWidgetContents)
        self.Widthlabel.setObjectName(u"Widthlabel")

        self.horizontalLayout_12.addWidget(self.Widthlabel)

        self.WidthspinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.WidthspinBox.setObjectName(u"WidthspinBox")

        self.horizontalLayout_12.addWidget(self.WidthspinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Heightlabel = QLabel(self.AascrollAreaWidgetContents)
        self.Heightlabel.setObjectName(u"Heightlabel")

        self.horizontalLayout_13.addWidget(self.Heightlabel)

        self.HeightspinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.HeightspinBox.setObjectName(u"HeightspinBox")

        self.horizontalLayout_13.addWidget(self.HeightspinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.OffsetXlabel = QLabel(self.AascrollAreaWidgetContents)
        self.OffsetXlabel.setObjectName(u"OffsetXlabel")

        self.horizontalLayout_14.addWidget(self.OffsetXlabel)

        self.OffsetXspinBox = QSpinBox(self.AascrollAreaWidgetContents)
        self.OffsetXspinBox.setObjectName(u"OffsetXspinBox")

        self.horizontalLayout_14.addWidget(self.OffsetXspinBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.reverseXlabel = QLabel(self.AascrollAreaWidgetContents)
        self.reverseXlabel.setObjectName(u"reverseXlabel")

        self.horizontalLayout_27.addWidget(self.reverseXlabel)

        self.reverseXcheckBox = QCheckBox(self.AascrollAreaWidgetContents)
        self.reverseXcheckBox.setObjectName(u"reverseXcheckBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reverseXcheckBox.sizePolicy().hasHeightForWidth())
        self.reverseXcheckBox.setSizePolicy(sizePolicy2)
        self.reverseXcheckBox.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_27.addWidget(self.reverseXcheckBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_4)

        self.scrollArea.setWidget(self.AascrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.scrollArea)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_2 = QScrollArea(self.SettingTab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.AscrollAreaWidgetContents = QWidget()
        self.AscrollAreaWidgetContents.setObjectName(u"AscrollAreaWidgetContents")
        self.AscrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 500))
        self.verticalLayout_16 = QVBoxLayout(self.AscrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.cnnSettinglabel = QLabel(self.AscrollAreaWidgetContents)
        self.cnnSettinglabel.setObjectName(u"cnnSettinglabel")
        self.cnnSettinglabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.cnnSettinglabel)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Cnn_path_lable = QLabel(self.AscrollAreaWidgetContents)
        self.Cnn_path_lable.setObjectName(u"Cnn_path_lable")
        self.Cnn_path_lable.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.Cnn_path_lable)

        self.cnnPathQlineEdit = QLineEdit(self.AscrollAreaWidgetContents)
        self.cnnPathQlineEdit.setObjectName(u"cnnPathQlineEdit")
        self.cnnPathQlineEdit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cnnPathQlineEdit.sizePolicy().hasHeightForWidth())
        self.cnnPathQlineEdit.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.cnnPathQlineEdit)


        self.verticalLayout_16.addLayout(self.horizontalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.modbuslabel = QLabel(self.AscrollAreaWidgetContents)
        self.modbuslabel.setObjectName(u"modbuslabel")
        self.modbuslabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.modbuslabel)


        self.verticalLayout_16.addLayout(self.verticalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.AscrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.AscrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_16.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.AscrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_15)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.settingPathlabel = QLabel(self.SettingTab)
        self.settingPathlabel.setObjectName(u"settingPathlabel")

        self.horizontalLayout_7.addWidget(self.settingPathlabel)

        self.settingPathlineEdit = QLineEdit(self.SettingTab)
        self.settingPathlineEdit.setObjectName(u"settingPathlineEdit")
        self.settingPathlineEdit.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.settingPathlineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.SettingTab, "")
        self.ValvesTab = QWidget()
        self.ValvesTab.setObjectName(u"ValvesTab")
        self.verticalLayout_12 = QVBoxLayout(self.ValvesTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_3 = QScrollArea(self.ValvesTab)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 768, 540))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lengthToValvesBlockLabel = QLabel(self.scrollAreaWidgetContents)
        self.lengthToValvesBlockLabel.setObjectName(u"lengthToValvesBlockLabel")

        self.horizontalLayout_24.addWidget(self.lengthToValvesBlockLabel)

        self.lengthToValvesBlockSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.lengthToValvesBlockSpinBox.setObjectName(u"lengthToValvesBlockSpinBox")

        self.horizontalLayout_24.addWidget(self.lengthToValvesBlockSpinBox)


        self.verticalLayout_29.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.numbersOfValvesLabel = QLabel(self.scrollAreaWidgetContents)
        self.numbersOfValvesLabel.setObjectName(u"numbersOfValvesLabel")

        self.horizontalLayout_23.addWidget(self.numbersOfValvesLabel)

        self.numbersOfValvesSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.numbersOfValvesSpinBox.setObjectName(u"numbersOfValvesSpinBox")

        self.horizontalLayout_23.addWidget(self.numbersOfValvesSpinBox)


        self.verticalLayout_29.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.conveyorSpeedlabel = QLabel(self.scrollAreaWidgetContents)
        self.conveyorSpeedlabel.setObjectName(u"conveyorSpeedlabel")

        self.horizontalLayout_25.addWidget(self.conveyorSpeedlabel)

        self.conveyorSpeeddoubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.conveyorSpeeddoubleSpinBox.setObjectName(u"conveyorSpeeddoubleSpinBox")

        self.horizontalLayout_25.addWidget(self.conveyorSpeeddoubleSpinBox)


        self.verticalLayout_29.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.timeOfShotValvelabel = QLabel(self.scrollAreaWidgetContents)
        self.timeOfShotValvelabel.setObjectName(u"timeOfShotValvelabel")

        self.horizontalLayout_22.addWidget(self.timeOfShotValvelabel)

        self.timeOfShotValvedoubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.timeOfShotValvedoubleSpinBox.setObjectName(u"timeOfShotValvedoubleSpinBox")

        self.horizontalLayout_22.addWidget(self.timeOfShotValvedoubleSpinBox)


        self.verticalLayout_29.addLayout(self.horizontalLayout_22)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer)


        self.horizontalLayout_19.addLayout(self.verticalLayout_29)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.horizontalLayout_19.addLayout(self.verticalLayout_28)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.ValvesTab, "")
        self.SignalsTab = QWidget()
        self.SignalsTab.setObjectName(u"SignalsTab")
        self.verticalLayout_23 = QVBoxLayout(self.SignalsTab)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.verticalLayout_23.addLayout(self.verticalLayout_22)

        self.tabWidget.addTab(self.SignalsTab, "")
        self.StatisticTab = QWidget()
        self.StatisticTab.setObjectName(u"StatisticTab")
        self.verticalLayout_21 = QVBoxLayout(self.StatisticTab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")

        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.tabWidget.addTab(self.StatisticTab, "")
        self.AlarsTab = QWidget()
        self.AlarsTab.setObjectName(u"AlarsTab")
        self.verticalLayout_13 = QVBoxLayout(self.AlarsTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.tabWidget.addTab(self.AlarsTab, "")
        self.ControlTab = QWidget()
        self.ControlTab.setObjectName(u"ControlTab")
        self.verticalLayout_26 = QVBoxLayout(self.ControlTab)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.resultingLineRateLabel = QLabel(self.ControlTab)
        self.resultingLineRateLabel.setObjectName(u"resultingLineRateLabel")

        self.horizontalLayout_17.addWidget(self.resultingLineRateLabel)

        self.resultingLineRatespinBox = QSpinBox(self.ControlTab)
        self.resultingLineRatespinBox.setObjectName(u"resultingLineRatespinBox")
        self.resultingLineRatespinBox.setEnabled(False)

        self.horizontalLayout_17.addWidget(self.resultingLineRatespinBox)


        self.verticalLayout_27.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.resultingFrameRatelabel = QLabel(self.ControlTab)
        self.resultingFrameRatelabel.setObjectName(u"resultingFrameRatelabel")

        self.horizontalLayout_18.addWidget(self.resultingFrameRatelabel)

        self.resultingFrameRatedoubleSpinBox = QDoubleSpinBox(self.ControlTab)
        self.resultingFrameRatedoubleSpinBox.setObjectName(u"resultingFrameRatedoubleSpinBox")
        self.resultingFrameRatedoubleSpinBox.setEnabled(False)

        self.horizontalLayout_18.addWidget(self.resultingFrameRatedoubleSpinBox)


        self.verticalLayout_27.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.cycleTimeCycleCnnlabel = QLabel(self.ControlTab)
        self.cycleTimeCycleCnnlabel.setObjectName(u"cycleTimeCycleCnnlabel")

        self.horizontalLayout_26.addWidget(self.cycleTimeCycleCnnlabel)

        self.cycleTimeCycleCnndoubleSpinBox = QDoubleSpinBox(self.ControlTab)
        self.cycleTimeCycleCnndoubleSpinBox.setObjectName(u"cycleTimeCycleCnndoubleSpinBox")
        self.cycleTimeCycleCnndoubleSpinBox.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.cycleTimeCycleCnndoubleSpinBox)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.cycleTimeCycleValve = QLabel(self.ControlTab)
        self.cycleTimeCycleValve.setObjectName(u"cycleTimeCycleValve")

        self.horizontalLayout_21.addWidget(self.cycleTimeCycleValve)

        self.cycleTimeCycleValvedoubleSpinBox = QDoubleSpinBox(self.ControlTab)
        self.cycleTimeCycleValvedoubleSpinBox.setObjectName(u"cycleTimeCycleValvedoubleSpinBox")
        self.cycleTimeCycleValvedoubleSpinBox.setEnabled(False)

        self.horizontalLayout_21.addWidget(self.cycleTimeCycleValvedoubleSpinBox)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_4)


        self.horizontalLayout_16.addLayout(self.verticalLayout_27)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.horizontalLayout_16.addLayout(self.verticalLayout_9)


        self.verticalLayout_25.addLayout(self.horizontalLayout_16)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.tabWidget.addTab(self.ControlTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statusBarLable = QLabel(self.videoWidget)
        self.statusBarLable.setObjectName(u"statusBarLable")

        self.horizontalLayout_6.addWidget(self.statusBarLable)

        self.statusBarlineEdit = QLineEdit(self.videoWidget)
        self.statusBarlineEdit.setObjectName(u"statusBarlineEdit")

        self.horizontalLayout_6.addWidget(self.statusBarlineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.valve_widget = QWidget(self.videoWidget)
        self.valve_widget.setObjectName(u"valve_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.valve_widget.sizePolicy().hasHeightForWidth())
        self.valve_widget.setSizePolicy(sizePolicy4)
        self.verticalLayout_10 = QVBoxLayout(self.valve_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.valveImagelabel = QLabel(self.valve_widget)
        self.valveImagelabel.setObjectName(u"valveImagelabel")

        self.verticalLayout_10.addWidget(self.valveImagelabel)


        self.verticalLayout.addWidget(self.valve_widget)


        self.gridLayout_2.addWidget(self.videoWidget, 0, 0, 1, 1)

        self.groupBoxButton = QGroupBox(self.centralwidget)
        self.groupBoxButton.setObjectName(u"groupBoxButton")
        self.groupBoxButton.setMinimumSize(QSize(200, 0))
        self.groupBoxButton.setMaximumSize(QSize(210, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxButton)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.remoteControlCheckBox = QCheckBox(self.groupBoxButton)
        self.remoteControlCheckBox.setObjectName(u"remoteControlCheckBox")

        self.verticalLayout_2.addWidget(self.remoteControlCheckBox)

        self.camFindLabel = QLabel(self.groupBoxButton)
        self.camFindLabel.setObjectName(u"camFindLabel")

        self.verticalLayout_2.addWidget(self.camFindLabel)

        self.pushButtonsearchCam = QPushButton(self.groupBoxButton)
        self.pushButtonsearchCam.setObjectName(u"pushButtonsearchCam")

        self.verticalLayout_2.addWidget(self.pushButtonsearchCam)

        self.line = QFrame(self.groupBoxButton)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label = QLabel(self.groupBoxButton)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

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

        self.line_2 = QFrame(self.groupBoxButton)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.CnnLayout = QVBoxLayout()
        self.CnnLayout.setObjectName(u"CnnLayout")
        self.cnn_control_label = QLabel(self.groupBoxButton)
        self.cnn_control_label.setObjectName(u"cnn_control_label")

        self.CnnLayout.addWidget(self.cnn_control_label)

        self.cnnStatusProgressBar = QProgressBar(self.groupBoxButton)
        self.cnnStatusProgressBar.setObjectName(u"cnnStatusProgressBar")
        self.cnnStatusProgressBar.setEnabled(True)
        self.cnnStatusProgressBar.setValue(100)
        self.cnnStatusProgressBar.setTextVisible(False)

        self.CnnLayout.addWidget(self.cnnStatusProgressBar)

        self.pushButtonStartObjDetectCnn = QPushButton(self.groupBoxButton)
        self.pushButtonStartObjDetectCnn.setObjectName(u"pushButtonStartObjDetectCnn")

        self.CnnLayout.addWidget(self.pushButtonStartObjDetectCnn)

        self.pushButtonStopObjDetectCnn = QPushButton(self.groupBoxButton)
        self.pushButtonStopObjDetectCnn.setObjectName(u"pushButtonStopObjDetectCnn")

        self.CnnLayout.addWidget(self.pushButtonStopObjDetectCnn)


        self.verticalLayout_2.addLayout(self.CnnLayout)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_2 = QLabel(self.groupBoxButton)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_24.addWidget(self.label_2)

        self.lightControlprogressBar = QProgressBar(self.groupBoxButton)
        self.lightControlprogressBar.setObjectName(u"lightControlprogressBar")
        self.lightControlprogressBar.setValue(100)
        self.lightControlprogressBar.setTextVisible(False)

        self.verticalLayout_24.addWidget(self.lightControlprogressBar)

        self.pushButton = QPushButton(self.groupBoxButton)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_24.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBoxButton)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_24.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_24)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.gridLayout_2.addWidget(self.groupBoxButton, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CameraLabel.setText(QCoreApplication.translate("MainWindow", u"Camera view", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), QCoreApplication.translate("MainWindow", u"Main View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MaterialTab), QCoreApplication.translate("MainWindow", u"Materials", None))
        self.cameraSettinglabel.setText(QCoreApplication.translate("MainWindow", u"Camera setting", None))
        self.exposureTime_lable.setText(QCoreApplication.translate("MainWindow", u"Exposure Time", None))
        self.gainLable.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.BalanceRedlabel.setText(QCoreApplication.translate("MainWindow", u"Balance Red", None))
        self.BalanceGreenlabel.setText(QCoreApplication.translate("MainWindow", u"Balance Green", None))
        self.BalanceBuelabel.setText(QCoreApplication.translate("MainWindow", u"Balance Blue", None))
        self.Widthlabel.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.Heightlabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.OffsetXlabel.setText(QCoreApplication.translate("MainWindow", u"Offset X", None))
        self.reverseXlabel.setText(QCoreApplication.translate("MainWindow", u"ReverseX", None))
        self.reverseXcheckBox.setText("")
        self.cnnSettinglabel.setText(QCoreApplication.translate("MainWindow", u"CNN Setting", None))
        self.Cnn_path_lable.setText(QCoreApplication.translate("MainWindow", u"CNN Path:", None))
        self.cnnPathQlineEdit.setText(QCoreApplication.translate("MainWindow", u"./resources/EMG_2025_24_06_v1.engine", None))
        self.modbuslabel.setText(QCoreApplication.translate("MainWindow", u"Modbus TCP In/Out Setting", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Modbus IP ", None))
        self.settingPathlabel.setText(QCoreApplication.translate("MainWindow", u"Setting path:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SettingTab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lengthToValvesBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Length to valves block", None))
        self.numbersOfValvesLabel.setText(QCoreApplication.translate("MainWindow", u"Numbers of valves", None))
        self.conveyorSpeedlabel.setText(QCoreApplication.translate("MainWindow", u"Conveyor speed", None))
        self.timeOfShotValvelabel.setText(QCoreApplication.translate("MainWindow", u"Time of shot valve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ValvesTab), QCoreApplication.translate("MainWindow", u"Valves", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SignalsTab), QCoreApplication.translate("MainWindow", u"Signals", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StatisticTab), QCoreApplication.translate("MainWindow", u"Statistic", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AlarsTab), QCoreApplication.translate("MainWindow", u"Alarms", None))
        self.resultingLineRateLabel.setText(QCoreApplication.translate("MainWindow", u"Resulting Line Rate(Hz)", None))
        self.resultingFrameRatelabel.setText(QCoreApplication.translate("MainWindow", u"Resulting Frame Rate(Fps)", None))
        self.cycleTimeCycleCnnlabel.setText(QCoreApplication.translate("MainWindow", u"Cycle time cycle CNN", None))
        self.cycleTimeCycleValve.setText(QCoreApplication.translate("MainWindow", u"Cycle time cycle valve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ControlTab), QCoreApplication.translate("MainWindow", u"Control", None))
        self.statusBarLable.setText(QCoreApplication.translate("MainWindow", u"Status bar", None))
        self.valveImagelabel.setText(QCoreApplication.translate("MainWindow", u"ValveImage", None))
        self.groupBoxButton.setTitle(QCoreApplication.translate("MainWindow", u"Control board", None))
        self.remoteControlCheckBox.setText(QCoreApplication.translate("MainWindow", u"Remote control", None))
        self.camFindLabel.setText(QCoreApplication.translate("MainWindow", u"No find cam", None))
        self.pushButtonsearchCam.setText(QCoreApplication.translate("MainWindow", u"Search Cam", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera control", None))
        self.cameraStatusProgressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pushButtonConnectCam.setText(QCoreApplication.translate("MainWindow", u"Connect Cam", None))
        self.pushButtonDisconectCam.setText(QCoreApplication.translate("MainWindow", u"Disconect Cam", None))
        self.cnn_control_label.setText(QCoreApplication.translate("MainWindow", u"CNN control", None))
        self.cnnStatusProgressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pushButtonStartObjDetectCnn.setText(QCoreApplication.translate("MainWindow", u"Start Obj Detection", None))
        self.pushButtonStopObjDetectCnn.setText(QCoreApplication.translate("MainWindow", u"Stop Obj Detection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Light control", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"On light", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Off light", None))
    # retranslateUi

