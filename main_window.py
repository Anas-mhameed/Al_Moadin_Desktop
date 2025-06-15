# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_adan_window_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCalendarWidget,
    QComboBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_file_rc

class Ui_central_widget(object):
    def setupUi(self, central_widget):
        if not central_widget.objectName():
            central_widget.setObjectName(u"central_widget")
        central_widget.resize(1397, 1199)
        central_widget.setStyleSheet(u"#central_widget{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(central_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.expandedMenu = QWidget(central_widget)
        self.expandedMenu.setObjectName(u"expandedMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expandedMenu.sizePolicy().hasHeightForWidth())
        self.expandedMenu.setSizePolicy(sizePolicy)
        self.expandedMenu.setMinimumSize(QSize(180, 0))
        self.expandedMenu.setMaximumSize(QSize(220, 16777215))
        self.expandedMenu.setStyleSheet(u"#expandedMenu{\n"
"border-right: 1px solid black;\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255,255,255);\n"
"}\n"
"	\n"
"#menuTitleLabel{\n"
"border-bottom: 5px solid rgb(255,255,255);\n"
"color: rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding: 12px 0 12px;\n"
"border:none;\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"\n"
"	background-color: rgb(53, 53, 53);\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(56, 56, 56);\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.expandedMenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 11, 0, 22)
        self.menuTitleLabel = QLabel(self.expandedMenu)
        self.menuTitleLabel.setObjectName(u"menuTitleLabel")
        self.menuTitleLabel.setMinimumSize(QSize(0, 49))
        self.menuTitleLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(19)
        font.setBold(True)
        self.menuTitleLabel.setFont(font)
        self.menuTitleLabel.setStyleSheet(u"")
        self.menuTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.menuTitleLabel)

        self.mainPageButton = QPushButton(self.expandedMenu)
        self.mainPageButton.setObjectName(u"mainPageButton")
        self.mainPageButton.setMinimumSize(QSize(0, 54))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(16)
        self.mainPageButton.setFont(font1)
        self.mainPageButton.setStyleSheet(u"")
        self.mainPageButton.setCheckable(True)
        self.mainPageButton.setChecked(True)
        self.mainPageButton.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.mainPageButton)

        self.notificationsPageButton = QPushButton(self.expandedMenu)
        self.notificationsPageButton.setObjectName(u"notificationsPageButton")
        self.notificationsPageButton.setMinimumSize(QSize(0, 54))
        self.notificationsPageButton.setFont(font1)
        self.notificationsPageButton.setCheckable(True)

        self.verticalLayout.addWidget(self.notificationsPageButton)

        self.quraanPageButton = QPushButton(self.expandedMenu)
        self.quraanPageButton.setObjectName(u"quraanPageButton")
        self.quraanPageButton.setMinimumSize(QSize(0, 54))
        self.quraanPageButton.setFont(font1)
        self.quraanPageButton.setCheckable(True)

        self.verticalLayout.addWidget(self.quraanPageButton)

        self.settingsPageButton = QPushButton(self.expandedMenu)
        self.settingsPageButton.setObjectName(u"settingsPageButton")
        self.settingsPageButton.setMinimumSize(QSize(0, 54))
        self.settingsPageButton.setFont(font1)
        self.settingsPageButton.setCheckable(True)

        self.verticalLayout.addWidget(self.settingsPageButton)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_20 = QFrame(self.expandedMenu)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(80, 80))
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.powerOffButton = QPushButton(self.frame_20)
        self.powerOffButton.setObjectName(u"powerOffButton")
        self.powerOffButton.setMinimumSize(QSize(50, 50))
        self.powerOffButton.setMaximumSize(QSize(50, 50))
        self.powerOffButton.setFont(font1)
        self.powerOffButton.setStyleSheet(u"QPushButton{\n"
"padding: 12px;\n"
"border:none;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius: 25px;\n"
"background-color: rgb(56,56,56);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.powerOffButton.setIcon(icon)
        self.powerOffButton.setIconSize(QSize(30, 30))
        self.powerOffButton.setCheckable(True)
        self.powerOffButton.setFlat(False)

        self.horizontalLayout_17.addWidget(self.powerOffButton)


        self.verticalLayout.addWidget(self.frame_20)


        self.horizontalLayout.addWidget(self.expandedMenu)

        self.frame_19 = QFrame(central_widget)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setMinimumSize(QSize(70, 0))
        self.frame_19.setMaximumSize(QSize(70, 16777215))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(15, -1, 0, -1)
        self.openMenuButton = QPushButton(self.frame_19)
        self.openMenuButton.setObjectName(u"openMenuButton")
        self.openMenuButton.setMinimumSize(QSize(50, 50))
        self.openMenuButton.setMaximumSize(QSize(50, 50))
        self.openMenuButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/menu_12237096.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openMenuButton.setIcon(icon1)
        self.openMenuButton.setIconSize(QSize(30, 30))
        self.openMenuButton.setCheckable(True)
        self.openMenuButton.setFlat(False)

        self.verticalLayout_19.addWidget(self.openMenuButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.frame_19)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.stackedWidget = QStackedWidget(central_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setStyleSheet(u"#stackedWidget{\n"
"background-color: rgb(0,0,0);\n"
"margin-right:30px;\n"
"}\n"
"\n"
"")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainPage.setStyleSheet(u"\n"
"\n"
"#mainPage{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.mainPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, -1, 25, 0)
        self.masgedNameWidget = QWidget(self.mainPage)
        self.masgedNameWidget.setObjectName(u"masgedNameWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.masgedNameWidget.sizePolicy().hasHeightForWidth())
        self.masgedNameWidget.setSizePolicy(sizePolicy2)
        self.masgedNameWidget.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setPointSize(8)
        self.masgedNameWidget.setFont(font2)
        self.horizontalLayout_2 = QHBoxLayout(self.masgedNameWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 11)
        self.horizontalSpacer_3 = QSpacerItem(216, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.masgedNameLabel = QLabel(self.masgedNameWidget)
        self.masgedNameLabel.setObjectName(u"masgedNameLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.masgedNameLabel.sizePolicy().hasHeightForWidth())
        self.masgedNameLabel.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Microsoft Uighur"])
        font3.setPointSize(35)
        font3.setBold(False)
        self.masgedNameLabel.setFont(font3)
        self.masgedNameLabel.setStyleSheet(u"color: black;")
        self.masgedNameLabel.setAlignment(Qt.AlignCenter)
        self.masgedNameLabel.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.masgedNameLabel)

        self.horizontalSpacer_4 = QSpacerItem(216, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.masgedNameWidget)

        self.widget_2 = QWidget(self.mainPage)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.widget_2)

        self.main_frame = QFrame(self.mainPage)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.timeDateWidget = QWidget(self.main_frame)
        self.timeDateWidget.setObjectName(u"timeDateWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.timeDateWidget.sizePolicy().hasHeightForWidth())
        self.timeDateWidget.setSizePolicy(sizePolicy4)
        self.timeDateWidget.setMinimumSize(QSize(0, 0))
        self.timeDateWidget.setMaximumSize(QSize(16777215, 380))
        self.timeDateWidget.setStyleSheet(u"#jomoaaWidget, #shorokWidget {\n"
"	border-radius: 25px;\n"
"	border: 4px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.timeDateWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.frame_12 = QFrame(self.timeDateWidget)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(202, 16777215))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.frame_21 = QFrame(self.frame_12)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.frame_21)

        self.jomoaaWidget = QWidget(self.frame_12)
        self.jomoaaWidget.setObjectName(u"jomoaaWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.jomoaaWidget.sizePolicy().hasHeightForWidth())
        self.jomoaaWidget.setSizePolicy(sizePolicy5)
        self.jomoaaWidget.setMinimumSize(QSize(150, 130))
        self.jomoaaWidget.setMaximumSize(QSize(200, 160))
        self.verticalLayout_11 = QVBoxLayout(self.jomoaaWidget)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(11, -1, 11, -1)
        self.jomoaa_label = QLabel(self.jomoaaWidget)
        self.jomoaa_label.setObjectName(u"jomoaa_label")
        sizePolicy1.setHeightForWidth(self.jomoaa_label.sizePolicy().hasHeightForWidth())
        self.jomoaa_label.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Microsoft Uighur"])
        font4.setPointSize(32)
        font4.setBold(True)
        self.jomoaa_label.setFont(font4)
        self.jomoaa_label.setStyleSheet(u"color:black;")
        self.jomoaa_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.jomoaa_label)

        self.jomoaa_adan_time = QLabel(self.jomoaaWidget)
        self.jomoaa_adan_time.setObjectName(u"jomoaa_adan_time")
        sizePolicy1.setHeightForWidth(self.jomoaa_adan_time.sizePolicy().hasHeightForWidth())
        self.jomoaa_adan_time.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(19)
        font5.setBold(False)
        self.jomoaa_adan_time.setFont(font5)
        self.jomoaa_adan_time.setStyleSheet(u"color:black;")
        self.jomoaa_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.jomoaa_adan_time)


        self.verticalLayout_29.addWidget(self.jomoaaWidget)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.timeWidget = QWidget(self.timeDateWidget)
        self.timeWidget.setObjectName(u"timeWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.timeWidget.sizePolicy().hasHeightForWidth())
        self.timeWidget.setSizePolicy(sizePolicy6)
        self.timeWidget.setMinimumSize(QSize(560, 200))
        self.timeWidget.setMaximumSize(QSize(16777215, 330))
        self.timeWidget.setStyleSheet(u"#timeWidget{\n"
"border: 4px solid rgb(0, 0, 0);\n"
"border-radius: 25px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.timeWidget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 5, -1, 0)
        self.time_upper_frame = QFrame(self.timeWidget)
        self.time_upper_frame.setObjectName(u"time_upper_frame")
        sizePolicy.setHeightForWidth(self.time_upper_frame.sizePolicy().hasHeightForWidth())
        self.time_upper_frame.setSizePolicy(sizePolicy)
        self.time_upper_frame.setMinimumSize(QSize(500, 0))
        self.time_upper_frame.setStyleSheet(u"QWidget{\n"
"	color: rgb(120, 208, 62);\n"
"}")
        self.time_upper_frame.setFrameShape(QFrame.NoFrame)
        self.time_upper_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.time_upper_frame)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 5, 0)
        self.frame_36 = QFrame(self.time_upper_frame)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_36)

        self.clockLabel = QLabel(self.time_upper_frame)
        self.clockLabel.setObjectName(u"clockLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.clockLabel.sizePolicy().hasHeightForWidth())
        self.clockLabel.setSizePolicy(sizePolicy7)
        self.clockLabel.setMinimumSize(QSize(0, 0))
        self.clockLabel.setMaximumSize(QSize(16777215, 16777215))
        self.clockLabel.setSizeIncrement(QSize(0, 0))
        self.clockLabel.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift"])
        font6.setPointSize(80)
        font6.setBold(True)
        self.clockLabel.setFont(font6)
        self.clockLabel.setStyleSheet(u"")
        self.clockLabel.setAlignment(Qt.AlignCenter)
        self.clockLabel.setWordWrap(False)

        self.horizontalLayout_34.addWidget(self.clockLabel)

        self.am_pm_frame = QFrame(self.time_upper_frame)
        self.am_pm_frame.setObjectName(u"am_pm_frame")
        self.am_pm_frame.setStyleSheet(u"")
        self.am_pm_frame.setFrameShape(QFrame.NoFrame)
        self.am_pm_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.am_pm_frame)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.am_pm_frame)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy3.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy3)
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.frame_35)

        self.seconds_label = QLabel(self.am_pm_frame)
        self.seconds_label.setObjectName(u"seconds_label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.seconds_label.sizePolicy().hasHeightForWidth())
        self.seconds_label.setSizePolicy(sizePolicy8)
        self.seconds_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.seconds_label)

        self.am_pm_label = QLabel(self.am_pm_frame)
        self.am_pm_label.setObjectName(u"am_pm_label")
        sizePolicy8.setHeightForWidth(self.am_pm_label.sizePolicy().hasHeightForWidth())
        self.am_pm_label.setSizePolicy(sizePolicy8)
        font7 = QFont()
        font7.setFamilies([u"Bahnschrift"])
        font7.setPointSize(36)
        font7.setBold(False)
        self.am_pm_label.setFont(font7)
        self.am_pm_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.am_pm_label)

        self.frame_34 = QFrame(self.am_pm_frame)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy3.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy3)
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.verticalLayout_36.addWidget(self.frame_34)


        self.horizontalLayout_34.addWidget(self.am_pm_frame)

        self.frame_37 = QFrame(self.time_upper_frame)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_37)


        self.verticalLayout_12.addWidget(self.time_upper_frame)

        self.timeLowerWidget = QWidget(self.timeWidget)
        self.timeLowerWidget.setObjectName(u"timeLowerWidget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.timeLowerWidget.sizePolicy().hasHeightForWidth())
        self.timeLowerWidget.setSizePolicy(sizePolicy9)
        self.horizontalLayout_7 = QHBoxLayout(self.timeLowerWidget)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_21 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_21)

        self.dateLabel = QLabel(self.timeLowerWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        sizePolicy1.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setFamilies([u"Sakkal Majalla"])
        font8.setPointSize(32)
        font8.setBold(True)
        self.dateLabel.setFont(font8)
        self.dateLabel.setStyleSheet(u"color:black;")
        self.dateLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.dateLabel, 0, Qt.AlignTop)

        self.horizontalSpacer_24 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_24)

        self.dayLabel = QLabel(self.timeLowerWidget)
        self.dayLabel.setObjectName(u"dayLabel")
        sizePolicy.setHeightForWidth(self.dayLabel.sizePolicy().hasHeightForWidth())
        self.dayLabel.setSizePolicy(sizePolicy)
        self.dayLabel.setFont(font8)
        self.dayLabel.setStyleSheet(u"color:black;")
        self.dayLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_7.addWidget(self.dayLabel, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.timeLowerWidget)


        self.horizontalLayout_6.addWidget(self.timeWidget, 0, Qt.AlignHCenter)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_16)

        self.frame_13 = QFrame(self.timeDateWidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(202, 16777215))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMaximumSize(QSize(16777215, 100))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_30.addWidget(self.frame_18)

        self.shorokWidget = QWidget(self.frame_13)
        self.shorokWidget.setObjectName(u"shorokWidget")
        sizePolicy5.setHeightForWidth(self.shorokWidget.sizePolicy().hasHeightForWidth())
        self.shorokWidget.setSizePolicy(sizePolicy5)
        self.shorokWidget.setMinimumSize(QSize(150, 130))
        self.shorokWidget.setMaximumSize(QSize(200, 160))
        self.verticalLayout_10 = QVBoxLayout(self.shorokWidget)
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(11, 11, 11, -1)
        self.shorok_label = QLabel(self.shorokWidget)
        self.shorok_label.setObjectName(u"shorok_label")
        sizePolicy1.setHeightForWidth(self.shorok_label.sizePolicy().hasHeightForWidth())
        self.shorok_label.setSizePolicy(sizePolicy1)
        self.shorok_label.setFont(font4)
        self.shorok_label.setStyleSheet(u"color:black;")
        self.shorok_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.shorok_label)

        self.shorok_adan_time = QLabel(self.shorokWidget)
        self.shorok_adan_time.setObjectName(u"shorok_adan_time")
        sizePolicy1.setHeightForWidth(self.shorok_adan_time.sizePolicy().hasHeightForWidth())
        self.shorok_adan_time.setSizePolicy(sizePolicy1)
        self.shorok_adan_time.setFont(font5)
        self.shorok_adan_time.setStyleSheet(u"color:black;")
        self.shorok_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.shorok_adan_time)


        self.verticalLayout_30.addWidget(self.shorokWidget)


        self.horizontalLayout_6.addWidget(self.frame_13)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addWidget(self.timeDateWidget)

        self.frame_30 = QFrame(self.main_frame)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy4.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy4)
        self.frame_30.setMaximumSize(QSize(16777215, 50))
        self.frame_30.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.frame_30)

        self.remainingTimeWidget = QWidget(self.main_frame)
        self.remainingTimeWidget.setObjectName(u"remainingTimeWidget")
        sizePolicy9.setHeightForWidth(self.remainingTimeWidget.sizePolicy().hasHeightForWidth())
        self.remainingTimeWidget.setSizePolicy(sizePolicy9)
        self.remainingTimeWidget.setMinimumSize(QSize(0, 0))
        self.remainingTimeWidget.setMaximumSize(QSize(16777215, 16777215))
        self.remainingTimeWidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.remainingTimeWidget)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.remainingTimeLabel = QLabel(self.remainingTimeWidget)
        self.remainingTimeLabel.setObjectName(u"remainingTimeLabel")
        sizePolicy9.setHeightForWidth(self.remainingTimeLabel.sizePolicy().hasHeightForWidth())
        self.remainingTimeLabel.setSizePolicy(sizePolicy9)
        self.remainingTimeLabel.setMinimumSize(QSize(0, 0))
        self.remainingTimeLabel.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Consolas"])
        font9.setPointSize(45)
        self.remainingTimeLabel.setFont(font9)
        self.remainingTimeLabel.setStyleSheet(u"QWidget{\n"
"color: rgb(193, 18, 51);\n"
"}")

        self.horizontalLayout_4.addWidget(self.remainingTimeLabel)

        self.nextAdanWidget = QWidget(self.remainingTimeWidget)
        self.nextAdanWidget.setObjectName(u"nextAdanWidget")
        sizePolicy9.setHeightForWidth(self.nextAdanWidget.sizePolicy().hasHeightForWidth())
        self.nextAdanWidget.setSizePolicy(sizePolicy9)
        self.nextAdanWidget.setMinimumSize(QSize(0, 0))
        self.nextAdanWidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.nextAdanWidget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(11, -1, 0, -1)
        self.remaining_text_label = QLabel(self.nextAdanWidget)
        self.remaining_text_label.setObjectName(u"remaining_text_label")
        sizePolicy9.setHeightForWidth(self.remaining_text_label.sizePolicy().hasHeightForWidth())
        self.remaining_text_label.setSizePolicy(sizePolicy9)
        self.remaining_text_label.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamilies([u"Calibri"])
        font10.setPointSize(28)
        font10.setBold(False)
        self.remaining_text_label.setFont(font10)
        self.remaining_text_label.setStyleSheet(u"QWidget{\n"
"color: rgb(193, 18, 51);\n"
"}")

        self.verticalLayout_13.addWidget(self.remaining_text_label, 0, Qt.AlignHCenter)

        self.nextAdanNameLabel = QLabel(self.nextAdanWidget)
        self.nextAdanNameLabel.setObjectName(u"nextAdanNameLabel")
        sizePolicy9.setHeightForWidth(self.nextAdanNameLabel.sizePolicy().hasHeightForWidth())
        self.nextAdanNameLabel.setSizePolicy(sizePolicy9)
        self.nextAdanNameLabel.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Calibri"])
        font11.setPointSize(30)
        font11.setBold(True)
        self.nextAdanNameLabel.setFont(font11)
        self.nextAdanNameLabel.setStyleSheet(u"QWidget{\n"
"color: rgb(8, 148, 108);}\n"
"")
        self.nextAdanNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.nextAdanNameLabel)


        self.horizontalLayout_4.addWidget(self.nextAdanWidget)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.remainingTimeWidget)

        self.emergency_stop_widget = QWidget(self.main_frame)
        self.emergency_stop_widget.setObjectName(u"emergency_stop_widget")
        sizePolicy1.setHeightForWidth(self.emergency_stop_widget.sizePolicy().hasHeightForWidth())
        self.emergency_stop_widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_27 = QHBoxLayout(self.emergency_stop_widget)
        self.horizontalLayout_27.setSpacing(15)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_25)

        self.emergency_stop_button = QPushButton(self.emergency_stop_widget)
        self.emergency_stop_button.setObjectName(u"emergency_stop_button")
        self.emergency_stop_button.setMinimumSize(QSize(46, 46))
        self.emergency_stop_button.setMaximumSize(QSize(46, 46))
        self.emergency_stop_button.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(213, 33, 10);\n"
"border-radius: 23px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(200, 28, 9);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(8, 185, 123);\n"
"	background-color: rgb(6, 235, 102);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/images/power_3039519.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emergency_stop_button.setIcon(icon2)
        self.emergency_stop_button.setIconSize(QSize(46, 46))
        self.emergency_stop_button.setCheckable(True)

        self.horizontalLayout_27.addWidget(self.emergency_stop_button)

        self.emergency_label = QLabel(self.emergency_stop_widget)
        self.emergency_label.setObjectName(u"emergency_label")
        sizePolicy1.setHeightForWidth(self.emergency_label.sizePolicy().hasHeightForWidth())
        self.emergency_label.setSizePolicy(sizePolicy1)
        font12 = QFont()
        font12.setFamilies([u"Calibri"])
        font12.setPointSize(22)
        self.emergency_label.setFont(font12)
        self.emergency_label.setStyleSheet(u"QWidget{\n"
"color: rgb(193, 18, 51);\n"
"}")

        self.horizontalLayout_27.addWidget(self.emergency_label)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_26)


        self.verticalLayout_3.addWidget(self.emergency_stop_widget)

        self.adansWidget = QWidget(self.main_frame)
        self.adansWidget.setObjectName(u"adansWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(1)
        sizePolicy10.setHeightForWidth(self.adansWidget.sizePolicy().hasHeightForWidth())
        self.adansWidget.setSizePolicy(sizePolicy10)
        self.adansWidget.setMinimumSize(QSize(0, 0))
        self.adansWidget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.adansWidget)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(11, 0, 11, 0)
        self.adans_frame = QFrame(self.adansWidget)
        self.adans_frame.setObjectName(u"adans_frame")
        sizePolicy3.setHeightForWidth(self.adans_frame.sizePolicy().hasHeightForWidth())
        self.adans_frame.setSizePolicy(sizePolicy3)
        self.adans_frame.setMaximumSize(QSize(16777215, 560))
        self.adans_frame.setStyleSheet(u"")
        self.adans_frame.setFrameShape(QFrame.NoFrame)
        self.adans_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.adans_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.adans_frame)
        self.widget.setObjectName(u"widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setMaximumSize(QSize(16777215, 480))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.widget)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setStyleSheet(u"\n"
"#aserWidget, #dohorWidget, #fajerWidget, #ishaaWidget, #magrebWidget{\n"
"border-radius: 14px;\n"
"border: 4px solid black;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-bottom-left-radius: 14px;\n"
"border-bottom-right-radius: 14px;\n"
"border: 4px solid black;\n"
"border-top: none;\n"
"padding: 5px 0;\n"
"background-color: rgb(167, 25, 35);\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(8, 185, 123);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(8, 148, 108);\n"
"}")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_14)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy5.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy5)
        self.frame_43.setMinimumSize(QSize(0, 0))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_43)
        self.verticalLayout_41.setSpacing(5)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.ishaaWidget = QWidget(self.frame_43)
        self.ishaaWidget.setObjectName(u"ishaaWidget")
        sizePolicy5.setHeightForWidth(self.ishaaWidget.sizePolicy().hasHeightForWidth())
        self.ishaaWidget.setSizePolicy(sizePolicy5)
        self.ishaaWidget.setMinimumSize(QSize(0, 0))
        self.ishaaWidget.setMaximumSize(QSize(250, 200))
        self.verticalLayout_9 = QVBoxLayout(self.ishaaWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.ishaa_label = QLabel(self.ishaaWidget)
        self.ishaa_label.setObjectName(u"ishaa_label")
        sizePolicy1.setHeightForWidth(self.ishaa_label.sizePolicy().hasHeightForWidth())
        self.ishaa_label.setSizePolicy(sizePolicy1)
        font13 = QFont()
        font13.setFamilies([u"Microsoft Uighur"])
        font13.setPointSize(39)
        font13.setBold(True)
        self.ishaa_label.setFont(font13)
        self.ishaa_label.setStyleSheet(u"color:black;")
        self.ishaa_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.ishaa_label)

        self.ishaa_adan_time = QLabel(self.ishaaWidget)
        self.ishaa_adan_time.setObjectName(u"ishaa_adan_time")
        sizePolicy1.setHeightForWidth(self.ishaa_adan_time.sizePolicy().hasHeightForWidth())
        self.ishaa_adan_time.setSizePolicy(sizePolicy1)
        font14 = QFont()
        font14.setFamilies([u"Bahnschrift"])
        font14.setPointSize(24)
        self.ishaa_adan_time.setFont(font14)
        self.ishaa_adan_time.setStyleSheet(u"color:black;")
        self.ishaa_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.ishaa_adan_time)

        self.ishaa_activate_button = QPushButton(self.ishaaWidget)
        self.ishaa_activate_button.setObjectName(u"ishaa_activate_button")
        font15 = QFont()
        font15.setFamilies([u"Calibri"])
        font15.setPointSize(15)
        font15.setBold(True)
        self.ishaa_activate_button.setFont(font15)
        self.ishaa_activate_button.setCheckable(True)

        self.verticalLayout_9.addWidget(self.ishaa_activate_button)


        self.verticalLayout_41.addWidget(self.ishaaWidget)

        self.ishaa_volume_slider = QSlider(self.frame_43)
        self.ishaa_volume_slider.setObjectName(u"ishaa_volume_slider")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.ishaa_volume_slider.sizePolicy().hasHeightForWidth())
        self.ishaa_volume_slider.setSizePolicy(sizePolicy11)
        self.ishaa_volume_slider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.ishaa_volume_slider.setMaximum(100)
        self.ishaa_volume_slider.setOrientation(Qt.Horizontal)
        self.ishaa_volume_slider.setInvertedAppearance(False)
        self.ishaa_volume_slider.setInvertedControls(False)
        self.ishaa_volume_slider.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_41.addWidget(self.ishaa_volume_slider)

        self.ishaaSoundButton = QPushButton(self.frame_43)
        self.ishaaSoundButton.setObjectName(u"ishaaSoundButton")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.ishaaSoundButton.sizePolicy().hasHeightForWidth())
        self.ishaaSoundButton.setSizePolicy(sizePolicy12)
        font16 = QFont()
        font16.setFamilies([u"Microsoft Uighur"])
        font16.setPointSize(22)
        font16.setBold(True)
        self.ishaaSoundButton.setFont(font16)
        self.ishaaSoundButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"color: black;\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 53);\n"
"color:white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_41.addWidget(self.ishaaSoundButton)


        self.horizontalLayout_28.addWidget(self.frame_43)

        self.frame_42 = QFrame(self.frame_14)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy5.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy5)
        self.frame_42.setMinimumSize(QSize(0, 0))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_42)
        self.verticalLayout_40.setSpacing(5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.magrebWidget = QWidget(self.frame_42)
        self.magrebWidget.setObjectName(u"magrebWidget")
        sizePolicy5.setHeightForWidth(self.magrebWidget.sizePolicy().hasHeightForWidth())
        self.magrebWidget.setSizePolicy(sizePolicy5)
        self.magrebWidget.setMinimumSize(QSize(0, 0))
        self.magrebWidget.setMaximumSize(QSize(250, 200))
        self.magrebWidget.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.magrebWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, 0)
        self.magreb_label = QLabel(self.magrebWidget)
        self.magreb_label.setObjectName(u"magreb_label")
        sizePolicy1.setHeightForWidth(self.magreb_label.sizePolicy().hasHeightForWidth())
        self.magreb_label.setSizePolicy(sizePolicy1)
        self.magreb_label.setFont(font13)
        self.magreb_label.setStyleSheet(u"color:black;")
        self.magreb_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.magreb_label)

        self.magreb_adan_time = QLabel(self.magrebWidget)
        self.magreb_adan_time.setObjectName(u"magreb_adan_time")
        self.magreb_adan_time.setFont(font14)
        self.magreb_adan_time.setStyleSheet(u"color:black;")
        self.magreb_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.magreb_adan_time)

        self.magreb_activate_button = QPushButton(self.magrebWidget)
        self.magreb_activate_button.setObjectName(u"magreb_activate_button")
        self.magreb_activate_button.setFont(font15)
        self.magreb_activate_button.setCheckable(True)

        self.verticalLayout_8.addWidget(self.magreb_activate_button)


        self.verticalLayout_40.addWidget(self.magrebWidget)

        self.magreb_volume_slider = QSlider(self.frame_42)
        self.magreb_volume_slider.setObjectName(u"magreb_volume_slider")
        sizePolicy11.setHeightForWidth(self.magreb_volume_slider.sizePolicy().hasHeightForWidth())
        self.magreb_volume_slider.setSizePolicy(sizePolicy11)
        self.magreb_volume_slider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.magreb_volume_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_40.addWidget(self.magreb_volume_slider)

        self.magrebSoundButton = QPushButton(self.frame_42)
        self.magrebSoundButton.setObjectName(u"magrebSoundButton")
        sizePolicy12.setHeightForWidth(self.magrebSoundButton.sizePolicy().hasHeightForWidth())
        self.magrebSoundButton.setSizePolicy(sizePolicy12)
        self.magrebSoundButton.setFont(font16)
        self.magrebSoundButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"color: black;\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 53);\n"
"color:white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_40.addWidget(self.magrebSoundButton)


        self.horizontalLayout_28.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.frame_14)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy5.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy5)
        self.frame_41.setMinimumSize(QSize(0, 0))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_41)
        self.verticalLayout_39.setSpacing(5)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.aserWidget = QWidget(self.frame_41)
        self.aserWidget.setObjectName(u"aserWidget")
        sizePolicy5.setHeightForWidth(self.aserWidget.sizePolicy().hasHeightForWidth())
        self.aserWidget.setSizePolicy(sizePolicy5)
        self.aserWidget.setMinimumSize(QSize(0, 0))
        self.aserWidget.setMaximumSize(QSize(250, 200))
        self.verticalLayout_7 = QVBoxLayout(self.aserWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.aser_label = QLabel(self.aserWidget)
        self.aser_label.setObjectName(u"aser_label")
        sizePolicy1.setHeightForWidth(self.aser_label.sizePolicy().hasHeightForWidth())
        self.aser_label.setSizePolicy(sizePolicy1)
        self.aser_label.setFont(font13)
        self.aser_label.setStyleSheet(u"color:black;")
        self.aser_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.aser_label)

        self.aser_adan_time = QLabel(self.aserWidget)
        self.aser_adan_time.setObjectName(u"aser_adan_time")
        sizePolicy1.setHeightForWidth(self.aser_adan_time.sizePolicy().hasHeightForWidth())
        self.aser_adan_time.setSizePolicy(sizePolicy1)
        self.aser_adan_time.setFont(font14)
        self.aser_adan_time.setStyleSheet(u"color:black;")
        self.aser_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.aser_adan_time)

        self.aser_activate_button = QPushButton(self.aserWidget)
        self.aser_activate_button.setObjectName(u"aser_activate_button")
        self.aser_activate_button.setFont(font15)
        self.aser_activate_button.setCheckable(True)

        self.verticalLayout_7.addWidget(self.aser_activate_button)


        self.verticalLayout_39.addWidget(self.aserWidget)

        self.aser_volume_slider = QSlider(self.frame_41)
        self.aser_volume_slider.setObjectName(u"aser_volume_slider")
        sizePolicy11.setHeightForWidth(self.aser_volume_slider.sizePolicy().hasHeightForWidth())
        self.aser_volume_slider.setSizePolicy(sizePolicy11)
        self.aser_volume_slider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.aser_volume_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_39.addWidget(self.aser_volume_slider)

        self.aserSoundButton = QPushButton(self.frame_41)
        self.aserSoundButton.setObjectName(u"aserSoundButton")
        sizePolicy12.setHeightForWidth(self.aserSoundButton.sizePolicy().hasHeightForWidth())
        self.aserSoundButton.setSizePolicy(sizePolicy12)
        self.aserSoundButton.setFont(font16)
        self.aserSoundButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"color: black;\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 53);\n"
"color:white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_39.addWidget(self.aserSoundButton)


        self.horizontalLayout_28.addWidget(self.frame_41)

        self.frame_29 = QFrame(self.frame_14)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy5.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy5)
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_29)
        self.verticalLayout_37.setSpacing(5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.dohorWidget = QWidget(self.frame_29)
        self.dohorWidget.setObjectName(u"dohorWidget")
        sizePolicy5.setHeightForWidth(self.dohorWidget.sizePolicy().hasHeightForWidth())
        self.dohorWidget.setSizePolicy(sizePolicy5)
        self.dohorWidget.setMinimumSize(QSize(0, 0))
        self.dohorWidget.setMaximumSize(QSize(250, 200))
        self.verticalLayout_6 = QVBoxLayout(self.dohorWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.dohor_label = QLabel(self.dohorWidget)
        self.dohor_label.setObjectName(u"dohor_label")
        sizePolicy1.setHeightForWidth(self.dohor_label.sizePolicy().hasHeightForWidth())
        self.dohor_label.setSizePolicy(sizePolicy1)
        self.dohor_label.setFont(font13)
        self.dohor_label.setStyleSheet(u"color:black;")
        self.dohor_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.dohor_label)

        self.dohor_adan_time = QLabel(self.dohorWidget)
        self.dohor_adan_time.setObjectName(u"dohor_adan_time")
        self.dohor_adan_time.setFont(font14)
        self.dohor_adan_time.setStyleSheet(u"color:black;")
        self.dohor_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.dohor_adan_time)

        self.dohor_activate_button = QPushButton(self.dohorWidget)
        self.dohor_activate_button.setObjectName(u"dohor_activate_button")
        sizePolicy9.setHeightForWidth(self.dohor_activate_button.sizePolicy().hasHeightForWidth())
        self.dohor_activate_button.setSizePolicy(sizePolicy9)
        self.dohor_activate_button.setFont(font15)
        self.dohor_activate_button.setStyleSheet(u"")
        self.dohor_activate_button.setCheckable(True)
        self.dohor_activate_button.setAutoDefault(False)
        self.dohor_activate_button.setFlat(False)

        self.verticalLayout_6.addWidget(self.dohor_activate_button)


        self.verticalLayout_37.addWidget(self.dohorWidget)

        self.dohor_volume_slider = QSlider(self.frame_29)
        self.dohor_volume_slider.setObjectName(u"dohor_volume_slider")
        sizePolicy11.setHeightForWidth(self.dohor_volume_slider.sizePolicy().hasHeightForWidth())
        self.dohor_volume_slider.setSizePolicy(sizePolicy11)
        self.dohor_volume_slider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.dohor_volume_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_37.addWidget(self.dohor_volume_slider)

        self.dohorSoundButton = QPushButton(self.frame_29)
        self.dohorSoundButton.setObjectName(u"dohorSoundButton")
        sizePolicy12.setHeightForWidth(self.dohorSoundButton.sizePolicy().hasHeightForWidth())
        self.dohorSoundButton.setSizePolicy(sizePolicy12)
        self.dohorSoundButton.setFont(font16)
        self.dohorSoundButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"color: black;\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 53);\n"
"color:white;\n"
"}\n"
"\n"
"")

        self.verticalLayout_37.addWidget(self.dohorSoundButton)


        self.horizontalLayout_28.addWidget(self.frame_29)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy5.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy5)
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.fajerWidget = QWidget(self.frame_15)
        self.fajerWidget.setObjectName(u"fajerWidget")
        sizePolicy5.setHeightForWidth(self.fajerWidget.sizePolicy().hasHeightForWidth())
        self.fajerWidget.setSizePolicy(sizePolicy5)
        self.fajerWidget.setMinimumSize(QSize(0, 0))
        self.fajerWidget.setMaximumSize(QSize(250, 200))
        self.verticalLayout_5 = QVBoxLayout(self.fajerWidget)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 11, 0, 0)
        self.fajer_label = QLabel(self.fajerWidget)
        self.fajer_label.setObjectName(u"fajer_label")
        sizePolicy1.setHeightForWidth(self.fajer_label.sizePolicy().hasHeightForWidth())
        self.fajer_label.setSizePolicy(sizePolicy1)
        font17 = QFont()
        font17.setFamilies([u"Microsoft Uighur"])
        font17.setPointSize(39)
        font17.setBold(True)
        font17.setKerning(True)
        self.fajer_label.setFont(font17)
        self.fajer_label.setStyleSheet(u"color:black;")
        self.fajer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.fajer_label)

        self.fajer_adan_time = QLabel(self.fajerWidget)
        self.fajer_adan_time.setObjectName(u"fajer_adan_time")
        sizePolicy1.setHeightForWidth(self.fajer_adan_time.sizePolicy().hasHeightForWidth())
        self.fajer_adan_time.setSizePolicy(sizePolicy1)
        self.fajer_adan_time.setFont(font14)
        self.fajer_adan_time.setStyleSheet(u"color:black;")
        self.fajer_adan_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.fajer_adan_time)

        self.fajer_activate_button = QPushButton(self.fajerWidget)
        self.fajer_activate_button.setObjectName(u"fajer_activate_button")
        self.fajer_activate_button.setFont(font15)
        self.fajer_activate_button.setCheckable(True)

        self.verticalLayout_5.addWidget(self.fajer_activate_button)


        self.verticalLayout_33.addWidget(self.fajerWidget)

        self.fajer_volume_slider = QSlider(self.frame_15)
        self.fajer_volume_slider.setObjectName(u"fajer_volume_slider")
        sizePolicy11.setHeightForWidth(self.fajer_volume_slider.sizePolicy().hasHeightForWidth())
        self.fajer_volume_slider.setSizePolicy(sizePolicy11)
        self.fajer_volume_slider.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.fajer_volume_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_33.addWidget(self.fajer_volume_slider)

        self.fajerSoundButton = QPushButton(self.frame_15)
        self.fajerSoundButton.setObjectName(u"fajerSoundButton")
        sizePolicy12.setHeightForWidth(self.fajerSoundButton.sizePolicy().hasHeightForWidth())
        self.fajerSoundButton.setSizePolicy(sizePolicy12)
        self.fajerSoundButton.setMinimumSize(QSize(0, 0))
        self.fajerSoundButton.setMaximumSize(QSize(16777215, 16777215))
        self.fajerSoundButton.setFont(font16)
        self.fajerSoundButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"color: black;\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 53);\n"
"color:white;\n"
"}\n"
"\n"
"")
        self.fajerSoundButton.setCheckable(True)

        self.verticalLayout_33.addWidget(self.fajerSoundButton)


        self.horizontalLayout_28.addWidget(self.frame_15)


        self.verticalLayout_21.addWidget(self.frame_14)


        self.verticalLayout_35.addWidget(self.widget)

        self.adanSoundWidget = QWidget(self.adans_frame)
        self.adanSoundWidget.setObjectName(u"adanSoundWidget")
        sizePolicy3.setHeightForWidth(self.adanSoundWidget.sizePolicy().hasHeightForWidth())
        self.adanSoundWidget.setSizePolicy(sizePolicy3)
        self.adanSoundWidget.setMinimumSize(QSize(0, 0))
        self.adanSoundWidget.setMaximumSize(QSize(16777215, 74))
        self.adanSoundWidget.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255,255,255);\n"
"border:none;\n"
"}\n"
"\n"
"#adanSoundWidget{\n"
"border: 3px solid black;\n"
"\n"
"}\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.adanSoundWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.adanSoundWidget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QPushButton{\n"
"qproperty-iconSize: 40px 40px;\n"
"}\n"
"QPushButton:hover {\n"
"    border-bottom: 2px solid rgb(53,53,53);\n"
"}\n"
"")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.instant_play_volume_controller = QSlider(self.frame_16)
        self.instant_play_volume_controller.setObjectName(u"instant_play_volume_controller")
        self.instant_play_volume_controller.setMinimumSize(QSize(0, 50))
        self.instant_play_volume_controller.setMaximumSize(QSize(500, 16777215))
        self.instant_play_volume_controller.setStyleSheet(u"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 2px; /* Set the line thickness */\n"
"    background: #d9d9d9;\n"
"    margin: 0px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: black;\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -7px 0; /* Adjusted to vertically center the handle on the thinner groove */\n"
"    border-radius: 8px; /* Circular handle */\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #d9d9d9;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: black;\n"
"}\n"
"")
        self.instant_play_volume_controller.setMaximum(100)
        self.instant_play_volume_controller.setPageStep(1)
        self.instant_play_volume_controller.setValue(0)
        self.instant_play_volume_controller.setSliderPosition(0)
        self.instant_play_volume_controller.setOrientation(Qt.Horizontal)
        self.instant_play_volume_controller.setTickPosition(QSlider.NoTicks)
        self.instant_play_volume_controller.setTickInterval(1)

        self.horizontalLayout_30.addWidget(self.instant_play_volume_controller)

        self.instant_player_play_button = QPushButton(self.frame_16)
        self.instant_player_play_button.setObjectName(u"instant_player_play_button")
        self.instant_player_play_button.setMinimumSize(QSize(50, 50))
        self.instant_player_play_button.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/images/play_14441317.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/newPrefix/images/play_14441317.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.instant_player_play_button.setIcon(icon3)
        self.instant_player_play_button.setIconSize(QSize(40, 40))
        self.instant_player_play_button.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.instant_player_play_button)

        self.instant_player_pause_button = QPushButton(self.frame_16)
        self.instant_player_pause_button.setObjectName(u"instant_player_pause_button")
        self.instant_player_pause_button.setMinimumSize(QSize(50, 50))
        self.instant_player_pause_button.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/images/square_13738097.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instant_player_pause_button.setIcon(icon4)
        self.instant_player_pause_button.setIconSize(QSize(40, 40))
        self.instant_player_pause_button.setCheckable(False)

        self.horizontalLayout_30.addWidget(self.instant_player_pause_button)

        self.instant_player_resume_button = QPushButton(self.frame_16)
        self.instant_player_resume_button.setObjectName(u"instant_player_resume_button")
        self.instant_player_resume_button.setMinimumSize(QSize(50, 50))
        self.instant_player_resume_button.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/images/pause_6415668.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instant_player_resume_button.setIcon(icon5)
        self.instant_player_resume_button.setIconSize(QSize(40, 40))
        self.instant_player_resume_button.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.instant_player_resume_button)

        self.instant_player_stop_button = QPushButton(self.frame_16)
        self.instant_player_stop_button.setObjectName(u"instant_player_stop_button")
        self.instant_player_stop_button.setMinimumSize(QSize(50, 50))
        self.instant_player_stop_button.setMaximumSize(QSize(50, 50))
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instant_player_stop_button.setIcon(icon6)
        self.instant_player_stop_button.setIconSize(QSize(40, 40))
        self.instant_player_stop_button.setCheckable(True)

        self.horizontalLayout_30.addWidget(self.instant_player_stop_button)


        self.horizontalLayout_3.addWidget(self.frame_16)

        self.widget_11 = QWidget(self.adanSoundWidget)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.widget_11.setFont(font2)
        self.widget_11.setStyleSheet(u"")
        self.verticalLayout_31 = QVBoxLayout(self.widget_11)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(10, 0, 0, 0)
        self.instant_player_choose_file_button = QPushButton(self.widget_11)
        self.instant_player_choose_file_button.setObjectName(u"instant_player_choose_file_button")
        sizePolicy1.setHeightForWidth(self.instant_player_choose_file_button.sizePolicy().hasHeightForWidth())
        self.instant_player_choose_file_button.setSizePolicy(sizePolicy1)
        self.instant_player_choose_file_button.setFont(font15)
        self.instant_player_choose_file_button.setStyleSheet(u"QPushButton{\n"
"border: 3px solid black;\n"
"border-bottom: 1px solid black;\n"
"padding: 0px 5px;\n"
"background-color: rgb(120, 208, 62);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(130, 225, 67);\n"
"}")
        self.instant_player_choose_file_button.setCheckable(True)

        self.verticalLayout_31.addWidget(self.instant_player_choose_file_button)

        self.instant_player_delete_file_button = QPushButton(self.widget_11)
        self.instant_player_delete_file_button.setObjectName(u"instant_player_delete_file_button")
        sizePolicy1.setHeightForWidth(self.instant_player_delete_file_button.sizePolicy().hasHeightForWidth())
        self.instant_player_delete_file_button.setSizePolicy(sizePolicy1)
        self.instant_player_delete_file_button.setFont(font15)
        self.instant_player_delete_file_button.setStyleSheet(u"QPushButton{\n"
"border: 3px solid black;\n"
"border-top: 1px solid black;\n"
"padding: 0px 5px;\n"
"background-color:rgb(213, 33, 10);\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(235, 33, 11);\n"
"}")
        self.instant_player_delete_file_button.setCheckable(True)

        self.verticalLayout_31.addWidget(self.instant_player_delete_file_button)


        self.horizontalLayout_3.addWidget(self.widget_11)


        self.verticalLayout_35.addWidget(self.adanSoundWidget)


        self.horizontalLayout_5.addWidget(self.adans_frame)


        self.verticalLayout_3.addWidget(self.adansWidget)

        self.verticalSpacer_7 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)


        self.verticalLayout_4.addWidget(self.main_frame)

        self.stackedWidget.addWidget(self.mainPage)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.notifications_page.setStyleSheet(u"#notifications_page{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.notifications_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(30, -1, 25, 30)
        self.frame = QFrame(self.notifications_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.notifications_frame = QFrame(self.frame)
        self.notifications_frame.setObjectName(u"notifications_frame")
        self.notifications_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.notifications_frame.setStyleSheet(u"")
        self.notifications_frame.setInputMethodHints(Qt.ImhHiddenText)
        self.notifications_frame.setFrameShape(QFrame.NoFrame)
        self.notifications_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.notifications_frame)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_28 = QFrame(self.notifications_frame)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy3.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy3)
        self.frame_28.setMaximumSize(QSize(16777215, 180))
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_28)

        self.total_noti_frame = QFrame(self.notifications_frame)
        self.total_noti_frame.setObjectName(u"total_noti_frame")
        sizePolicy9.setHeightForWidth(self.total_noti_frame.sizePolicy().hasHeightForWidth())
        self.total_noti_frame.setSizePolicy(sizePolicy9)
        self.total_noti_frame.setStyleSheet(u"color:black;")
        self.total_noti_frame.setFrameShape(QFrame.NoFrame)
        self.total_noti_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.total_noti_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.total_noti_label = QLabel(self.total_noti_frame)
        self.total_noti_label.setObjectName(u"total_noti_label")
        sizePolicy9.setHeightForWidth(self.total_noti_label.sizePolicy().hasHeightForWidth())
        self.total_noti_label.setSizePolicy(sizePolicy9)
        font18 = QFont()
        font18.setFamilies([u"Sakkal Majalla"])
        font18.setPointSize(30)
        font18.setBold(False)
        self.total_noti_label.setFont(font18)
        self.total_noti_label.setLayoutDirection(Qt.RightToLeft)
        self.total_noti_label.setFrameShape(QFrame.NoFrame)
        self.total_noti_label.setFrameShadow(QFrame.Plain)
        self.total_noti_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.total_noti_label)

        self.total_noti_text_label = QLabel(self.total_noti_frame)
        self.total_noti_text_label.setObjectName(u"total_noti_text_label")
        sizePolicy8.setHeightForWidth(self.total_noti_text_label.sizePolicy().hasHeightForWidth())
        self.total_noti_text_label.setSizePolicy(sizePolicy8)
        font19 = QFont()
        font19.setFamilies([u"Sakkal Majalla"])
        font19.setPointSize(34)
        font19.setBold(True)
        self.total_noti_text_label.setFont(font19)
        self.total_noti_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_14.addWidget(self.total_noti_text_label)


        self.verticalLayout_17.addWidget(self.total_noti_frame)

        self.frame_24 = QFrame(self.notifications_frame)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy3.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy3)
        self.frame_24.setMaximumSize(QSize(16777215, 150))
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_24)

        self.noti_sort_frame = QFrame(self.notifications_frame)
        self.noti_sort_frame.setObjectName(u"noti_sort_frame")
        sizePolicy9.setHeightForWidth(self.noti_sort_frame.sizePolicy().hasHeightForWidth())
        self.noti_sort_frame.setSizePolicy(sizePolicy9)
        self.noti_sort_frame.setFrameShape(QFrame.NoFrame)
        self.noti_sort_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.noti_sort_frame)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.new_notification_buttton = QPushButton(self.noti_sort_frame)
        self.new_notification_buttton.setObjectName(u"new_notification_buttton")
        self.new_notification_buttton.setMinimumSize(QSize(150, 50))
        self.new_notification_buttton.setMaximumSize(QSize(150, 50))
        font20 = QFont()
        font20.setFamilies([u"Sakkal Majalla"])
        font20.setPointSize(19)
        font20.setBold(False)
        self.new_notification_buttton.setFont(font20)
        self.new_notification_buttton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(38, 38, 38);\n"
"border-radius: 25px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border:2px solid black;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.new_notification_buttton)

        self.noti_sort_box = QComboBox(self.noti_sort_frame)
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.addItem("")
        self.noti_sort_box.setObjectName(u"noti_sort_box")
        sizePolicy13 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.noti_sort_box.sizePolicy().hasHeightForWidth())
        self.noti_sort_box.setSizePolicy(sizePolicy13)
        self.noti_sort_box.setMinimumSize(QSize(119, 0))
        self.noti_sort_box.setFont(font20)
        self.noti_sort_box.setLayoutDirection(Qt.LeftToRight)
        self.noti_sort_box.setStyleSheet(u"QComboBox {\n"
"                border: 3px solid rgb(38, 38, 38);\n"
"				border-radius: 3px;\n"
"                padding: 1px 10px 1px 7px;\n"
"                min-width: 6em;\n"
"            }\n"
"QComboBox::drop-down {\n"
"                color:white;\n"
"                width: 26px;\n"
"                border-left-width: 1px;\n"
"                border-left-color: rgb(38, 38, 38);\n"
"                border-left-style: solid;\n"
"\n"
"               background-color: rgb(38,38,38);\n"
"}\n"
"QComboBox::down-arrow {\n"
"\n"
"				width:20px;\n"
"				height: 20px;\n"
"				margin: 1px 3px 1px 3px;\n"
"                image: url(:/newPrefix/images/down-chevron.png); /* Use the resource path */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(53,53,53); \n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color:rgb(53,53,53);\n"
"\n"
"}\n"
"    \n"
"\n"
"           \n"
"\n"
"")
        self.noti_sort_box.setEditable(False)
        self.noti_sort_box.setDuplicatesEnabled(False)
        self.noti_sort_box.setFrame(False)

        self.horizontalLayout_15.addWidget(self.noti_sort_box)

        self.notis_text_label = QLabel(self.noti_sort_frame)
        self.notis_text_label.setObjectName(u"notis_text_label")
        font21 = QFont()
        font21.setFamilies([u"Sakkal Majalla"])
        font21.setPointSize(28)
        self.notis_text_label.setFont(font21)
        self.notis_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_15.addWidget(self.notis_text_label)


        self.verticalLayout_17.addWidget(self.noti_sort_frame)

        self.noti_show_frame = QFrame(self.notifications_frame)
        self.noti_show_frame.setObjectName(u"noti_show_frame")
        sizePolicy3.setHeightForWidth(self.noti_show_frame.sizePolicy().hasHeightForWidth())
        self.noti_show_frame.setSizePolicy(sizePolicy3)
        self.noti_show_frame.setMinimumSize(QSize(0, 420))
        self.noti_show_frame.setMaximumSize(QSize(16777215, 420))
        self.noti_show_frame.setStyleSheet(u"#noti_show_frame{\n"
"border: 2px solid rgb(53,53,53);\n"
"}")
        self.noti_show_frame.setFrameShape(QFrame.StyledPanel)
        self.noti_show_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.noti_show_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 20, 0, 0)
        self.display_noti_widget = QScrollArea(self.noti_show_frame)
        self.display_noti_widget.setObjectName(u"display_noti_widget")
        sizePolicy11.setHeightForWidth(self.display_noti_widget.sizePolicy().hasHeightForWidth())
        self.display_noti_widget.setSizePolicy(sizePolicy11)
        self.display_noti_widget.setMinimumSize(QSize(0, 0))
        self.display_noti_widget.setMaximumSize(QSize(16777215, 16777215))
        self.display_noti_widget.setSizeIncrement(QSize(0, 0))
        font22 = QFont()
        font22.setKerning(True)
        self.display_noti_widget.setFont(font22)
        self.display_noti_widget.setLayoutDirection(Qt.LeftToRight)
        self.display_noti_widget.setAutoFillBackground(False)
        self.display_noti_widget.setStyleSheet(u"QWidget {\n"
"                background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QScrollBar{\n"
"padding: 20px 15px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"                background-color: rgb(56, 56, 56);\n"
"                border: 1px solid rgb(56,56,56);\n"
"                height: 15px;\n"
"                margin: 0px ;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"                background-color: rgb(100, 100, 100);\n"
"				border: 1px solid rgb(100,100,100);\n"
"                min-width: 20px;\n"
"				min-height: 30px;\n"
"				margin: 0px 16px 0px 16px;\n"
"}\n"
"\n"
"            QScrollBar::handle:horizontal:hover {\n"
"                background-color: rgb(160,160, 160);\n"
"            }\n"
"\n"
"            QScrollBar::handle:horizontal:pressed {\n"
"                background-color: rgb(165, 165, 165);\n"
"            }\n"
"\n"
"            \n"
"\n"
"            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"                background: none;\n"
"            }")
        self.display_noti_widget.setFrameShape(QFrame.NoFrame)
        self.display_noti_widget.setFrameShadow(QFrame.Plain)
        self.display_noti_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.display_noti_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.display_noti_widget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.display_noti_widget.setWidgetResizable(True)
        self.display_noti_widget.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaContainer = QWidget()
        self.scrollAreaContainer.setObjectName(u"scrollAreaContainer")
        self.scrollAreaContainer.setGeometry(QRect(0, 0, 100, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.scrollAreaContainer)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 20, 20, -1)
        self.display_noti_widget.setWidget(self.scrollAreaContainer)

        self.verticalLayout_18.addWidget(self.display_noti_widget)


        self.verticalLayout_17.addWidget(self.noti_show_frame)

        self.stop_notification = QPushButton(self.notifications_frame)
        self.stop_notification.setObjectName(u"stop_notification")
        sizePolicy3.setHeightForWidth(self.stop_notification.sizePolicy().hasHeightForWidth())
        self.stop_notification.setSizePolicy(sizePolicy3)
        self.stop_notification.setMinimumSize(QSize(0, 40))
        self.stop_notification.setMaximumSize(QSize(16777215, 45))
        font23 = QFont()
        font23.setFamilies([u"Sakkal Majalla"])
        font23.setPointSize(18)
        font23.setBold(True)
        self.stop_notification.setFont(font23)
        self.stop_notification.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(213, 33, 10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(198, 35, 20);\n"
"}\n"
"\n"
"")

        self.verticalLayout_17.addWidget(self.stop_notification)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)


        self.horizontalLayout_18.addWidget(self.notifications_frame)


        self.verticalLayout_16.addWidget(self.frame)

        self.stackedWidget.addWidget(self.notifications_page)
        self.quran_page = QWidget()
        self.quran_page.setObjectName(u"quran_page")
        self.quran_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_34 = QVBoxLayout(self.quran_page)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.quran_main_frame = QFrame(self.quran_page)
        self.quran_main_frame.setObjectName(u"quran_main_frame")
        self.quran_main_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.quran_main_frame.setFrameShape(QFrame.NoFrame)
        self.quran_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.quran_main_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.quraan_coming_soon_label = QLabel(self.quran_main_frame)
        self.quraan_coming_soon_label.setObjectName(u"quraan_coming_soon_label")
        font24 = QFont()
        font24.setFamilies([u"Microsoft Uighur"])
        font24.setPointSize(30)
        self.quraan_coming_soon_label.setFont(font24)
        self.quraan_coming_soon_label.setStyleSheet(u"color:black;")
        self.quraan_coming_soon_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.quraan_coming_soon_label)


        self.verticalLayout_34.addWidget(self.quran_main_frame)

        self.stackedWidget.addWidget(self.quran_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"#settings_page{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.settings_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 25, 30)
        self.frame_10 = QFrame(self.settings_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.settings_frame = QFrame(self.frame_10)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setStyleSheet(u"")
        self.settings_frame.setFrameShape(QFrame.NoFrame)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.settings_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_27 = QFrame(self.settings_frame)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy3.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy3)
        self.frame_27.setMaximumSize(QSize(16777215, 110))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_27)

        self.frame_7 = QFrame(self.settings_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 50))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.masjed_time_settings_label = QLabel(self.frame_7)
        self.masjed_time_settings_label.setObjectName(u"masjed_time_settings_label")
        font25 = QFont()
        font25.setFamilies([u"MS Shell Dlg 2"])
        font25.setPointSize(39)
        font25.setBold(True)
        self.masjed_time_settings_label.setFont(font25)
        self.masjed_time_settings_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_8.addWidget(self.masjed_time_settings_label)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.masged_frame = QFrame(self.settings_frame)
        self.masged_frame.setObjectName(u"masged_frame")
        sizePolicy9.setHeightForWidth(self.masged_frame.sizePolicy().hasHeightForWidth())
        self.masged_frame.setSizePolicy(sizePolicy9)
        self.masged_frame.setMinimumSize(QSize(0, 0))
        self.masged_frame.setFrameShape(QFrame.NoFrame)
        self.masged_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.masged_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.masjedNameInput = QLineEdit(self.masged_frame)
        self.masjedNameInput.setObjectName(u"masjedNameInput")
        sizePolicy14 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.masjedNameInput.sizePolicy().hasHeightForWidth())
        self.masjedNameInput.setSizePolicy(sizePolicy14)
        self.masjedNameInput.setMinimumSize(QSize(400, 0))
        self.masjedNameInput.setMaximumSize(QSize(16777215, 50))
        font26 = QFont()
        font26.setFamilies([u"Sakkal Majalla"])
        font26.setPointSize(24)
        self.masjedNameInput.setFont(font26)
        self.masjedNameInput.setLayoutDirection(Qt.RightToLeft)
        self.masjedNameInput.setStyleSheet(u"QLineEdit{\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"background-color:white;\n"
"}")
        self.masjedNameInput.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.masjedNameInput.setFrame(False)
        self.masjedNameInput.setEchoMode(QLineEdit.Normal)
        self.masjedNameInput.setCursorPosition(0)
        self.masjedNameInput.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.masjedNameInput.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.masjedNameInput.setClearButtonEnabled(True)

        self.horizontalLayout_9.addWidget(self.masjedNameInput)

        self.masjed_name_text_label = QLabel(self.masged_frame)
        self.masjed_name_text_label.setObjectName(u"masjed_name_text_label")
        sizePolicy9.setHeightForWidth(self.masjed_name_text_label.sizePolicy().hasHeightForWidth())
        self.masjed_name_text_label.setSizePolicy(sizePolicy9)
        self.masjed_name_text_label.setFont(font8)
        self.masjed_name_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_9.addWidget(self.masjed_name_text_label)


        self.verticalLayout_14.addWidget(self.masged_frame)

        self.city_frame = QFrame(self.settings_frame)
        self.city_frame.setObjectName(u"city_frame")
        sizePolicy9.setHeightForWidth(self.city_frame.sizePolicy().hasHeightForWidth())
        self.city_frame.setSizePolicy(sizePolicy9)
        self.city_frame.setMinimumSize(QSize(0, 0))
        self.city_frame.setFrameShape(QFrame.NoFrame)
        self.city_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.city_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.cityInput = QLineEdit(self.city_frame)
        self.cityInput.setObjectName(u"cityInput")
        sizePolicy14.setHeightForWidth(self.cityInput.sizePolicy().hasHeightForWidth())
        self.cityInput.setSizePolicy(sizePolicy14)
        self.cityInput.setMinimumSize(QSize(300, 0))
        self.cityInput.setMaximumSize(QSize(16777215, 50))
        font27 = QFont()
        font27.setFamilies([u"Sakkal Majalla"])
        font27.setPointSize(24)
        font27.setBold(False)
        self.cityInput.setFont(font27)
        self.cityInput.setLayoutDirection(Qt.RightToLeft)
        self.cityInput.setAutoFillBackground(False)
        self.cityInput.setStyleSheet(u"QLineEdit{\n"
"border-bottom: 2px solid black;\n"
"color:black;\n"
"background-color:white;\n"
"}")
        self.cityInput.setLocale(QLocale(QLocale.Arabic, QLocale.Israel))
        self.cityInput.setFrame(False)
        self.cityInput.setCursorPosition(0)
        self.cityInput.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.cityInput.setDragEnabled(False)
        self.cityInput.setReadOnly(False)
        self.cityInput.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.cityInput.setClearButtonEnabled(True)

        self.horizontalLayout_10.addWidget(self.cityInput)

        self.city_text_label = QLabel(self.city_frame)
        self.city_text_label.setObjectName(u"city_text_label")
        sizePolicy9.setHeightForWidth(self.city_text_label.sizePolicy().hasHeightForWidth())
        self.city_text_label.setSizePolicy(sizePolicy9)
        self.city_text_label.setFont(font8)
        self.city_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_10.addWidget(self.city_text_label)


        self.verticalLayout_14.addWidget(self.city_frame)

        self.quds_diff_frame = QFrame(self.settings_frame)
        self.quds_diff_frame.setObjectName(u"quds_diff_frame")
        sizePolicy9.setHeightForWidth(self.quds_diff_frame.sizePolicy().hasHeightForWidth())
        self.quds_diff_frame.setSizePolicy(sizePolicy9)
        self.quds_diff_frame.setMinimumSize(QSize(0, 0))
        self.quds_diff_frame.setMaximumSize(QSize(16777215, 16777215))
        self.quds_diff_frame.setFrameShape(QFrame.NoFrame)
        self.quds_diff_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.quds_diff_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 11, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)

        self.qudsTimeDiff = QSpinBox(self.quds_diff_frame)
        self.qudsTimeDiff.setObjectName(u"qudsTimeDiff")
        sizePolicy15 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.qudsTimeDiff.sizePolicy().hasHeightForWidth())
        self.qudsTimeDiff.setSizePolicy(sizePolicy15)
        self.qudsTimeDiff.setMinimumSize(QSize(160, 60))
        self.qudsTimeDiff.setMaximumSize(QSize(160, 60))
        font28 = QFont()
        font28.setPointSize(17)
        self.qudsTimeDiff.setFont(font28)
        self.qudsTimeDiff.setMouseTracking(False)
        self.qudsTimeDiff.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    border: 3px solid black;\n"
"    border-radius: 7px;\n"
"color:black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/plus.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/minimize-sign.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    border: none;\n"
"	border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-bottom: 2px solid black; /* Add dividing line */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    border"
                        ": none;\n"
"border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-top: 2px solid black; /* Add dividing line */\n"
"}\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"\n"
"/* Hover effect for down button */\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"")
        self.qudsTimeDiff.setWrapping(False)
        self.qudsTimeDiff.setFrame(True)
        self.qudsTimeDiff.setAlignment(Qt.AlignCenter)
        self.qudsTimeDiff.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.qudsTimeDiff.setAccelerated(True)
        self.qudsTimeDiff.setKeyboardTracking(False)
        self.qudsTimeDiff.setProperty("showGroupSeparator", False)
        self.qudsTimeDiff.setMinimum(-300)
        self.qudsTimeDiff.setMaximum(200)

        self.horizontalLayout_11.addWidget(self.qudsTimeDiff)

        self.quds_diff_text_label = QLabel(self.quds_diff_frame)
        self.quds_diff_text_label.setObjectName(u"quds_diff_text_label")
        sizePolicy9.setHeightForWidth(self.quds_diff_text_label.sizePolicy().hasHeightForWidth())
        self.quds_diff_text_label.setSizePolicy(sizePolicy9)
        self.quds_diff_text_label.setMaximumSize(QSize(16777215, 16777215))
        self.quds_diff_text_label.setFont(font8)
        self.quds_diff_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_11.addWidget(self.quds_diff_text_label)


        self.verticalLayout_14.addWidget(self.quds_diff_frame)

        self.frame_26 = QFrame(self.settings_frame)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy3.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy3)
        self.frame_26.setMaximumSize(QSize(16777215, 50))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_26)

        self.time_buttons_frame = QFrame(self.settings_frame)
        self.time_buttons_frame.setObjectName(u"time_buttons_frame")
        sizePolicy3.setHeightForWidth(self.time_buttons_frame.sizePolicy().hasHeightForWidth())
        self.time_buttons_frame.setSizePolicy(sizePolicy3)
        self.time_buttons_frame.setMinimumSize(QSize(0, 150))
        self.time_buttons_frame.setFrameShape(QFrame.NoFrame)
        self.time_buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.time_buttons_frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sum_win_timing_label = QLabel(self.time_buttons_frame)
        self.sum_win_timing_label.setObjectName(u"sum_win_timing_label")
        sizePolicy9.setHeightForWidth(self.sum_win_timing_label.sizePolicy().hasHeightForWidth())
        self.sum_win_timing_label.setSizePolicy(sizePolicy9)
        self.sum_win_timing_label.setFont(font8)
        self.sum_win_timing_label.setStyleSheet(u"color:black;")
        self.sum_win_timing_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_15.addWidget(self.sum_win_timing_label)

        self.win_sum_frame = QFrame(self.time_buttons_frame)
        self.win_sum_frame.setObjectName(u"win_sum_frame")
        sizePolicy9.setHeightForWidth(self.win_sum_frame.sizePolicy().hasHeightForWidth())
        self.win_sum_frame.setSizePolicy(sizePolicy9)
        self.win_sum_frame.setFrameShape(QFrame.NoFrame)
        self.win_sum_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.win_sum_frame)
        self.horizontalLayout_12.setSpacing(4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, 30, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)

        self.summer_settings_label = QLabel(self.win_sum_frame)
        self.summer_settings_label.setObjectName(u"summer_settings_label")
        sizePolicy9.setHeightForWidth(self.summer_settings_label.sizePolicy().hasHeightForWidth())
        self.summer_settings_label.setSizePolicy(sizePolicy9)
        self.summer_settings_label.setMaximumSize(QSize(16777215, 16777215))
        font29 = QFont()
        font29.setFamilies([u"Microsoft Uighur"])
        font29.setPointSize(28)
        self.summer_settings_label.setFont(font29)
        self.summer_settings_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_12.addWidget(self.summer_settings_label)

        self.summerButton = QPushButton(self.win_sum_frame)
        self.summerButton.setObjectName(u"summerButton")
        self.summerButton.setMinimumSize(QSize(40, 40))
        self.summerButton.setMaximumSize(QSize(40, 40))
        self.summerButton.setStyleSheet(u"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius:20px;\n"
"	background-color: rgb(247, 255, 151);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 4px solid black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border: 4px solid black;\n"
"}")
        self.summerButton.setCheckable(True)
        self.summerButton.setChecked(True)

        self.horizontalLayout_12.addWidget(self.summerButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_8)

        self.winter_settings_label = QLabel(self.win_sum_frame)
        self.winter_settings_label.setObjectName(u"winter_settings_label")
        sizePolicy9.setHeightForWidth(self.winter_settings_label.sizePolicy().hasHeightForWidth())
        self.winter_settings_label.setSizePolicy(sizePolicy9)
        self.winter_settings_label.setMaximumSize(QSize(16777215, 16777215))
        self.winter_settings_label.setFont(font29)
        self.winter_settings_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_12.addWidget(self.winter_settings_label)

        self.winterButton = QPushButton(self.win_sum_frame)
        self.winterButton.setObjectName(u"winterButton")
        self.winterButton.setMinimumSize(QSize(40, 40))
        self.winterButton.setMaximumSize(QSize(40, 40))
        self.winterButton.setStyleSheet(u"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius:20px;\n"
"	background-color: rgb(92, 206, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 4px solid black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border: 4px solid black;\n"
"}")
        self.winterButton.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.winterButton)


        self.verticalLayout_15.addWidget(self.win_sum_frame)

        self.time_format_text_label = QLabel(self.time_buttons_frame)
        self.time_format_text_label.setObjectName(u"time_format_text_label")
        sizePolicy9.setHeightForWidth(self.time_format_text_label.sizePolicy().hasHeightForWidth())
        self.time_format_text_label.setSizePolicy(sizePolicy9)
        self.time_format_text_label.setFont(font8)
        self.time_format_text_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_15.addWidget(self.time_format_text_label)

        self.time_formate_frame = QFrame(self.time_buttons_frame)
        self.time_formate_frame.setObjectName(u"time_formate_frame")
        sizePolicy9.setHeightForWidth(self.time_formate_frame.sizePolicy().hasHeightForWidth())
        self.time_formate_frame.setSizePolicy(sizePolicy9)
        self.time_formate_frame.setFrameShape(QFrame.NoFrame)
        self.time_formate_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.time_formate_frame)
        self.horizontalLayout_13.setSpacing(4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, 30, -1)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)

        self.time_formate_12_label = QLabel(self.time_formate_frame)
        self.time_formate_12_label.setObjectName(u"time_formate_12_label")
        sizePolicy9.setHeightForWidth(self.time_formate_12_label.sizePolicy().hasHeightForWidth())
        self.time_formate_12_label.setSizePolicy(sizePolicy9)
        self.time_formate_12_label.setMaximumSize(QSize(16777215, 16777215))
        self.time_formate_12_label.setFont(font29)
        self.time_formate_12_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_13.addWidget(self.time_formate_12_label)

        self.hours_12_button = QPushButton(self.time_formate_frame)
        self.hours_12_button.setObjectName(u"hours_12_button")
        self.hours_12_button.setMinimumSize(QSize(40, 40))
        self.hours_12_button.setMaximumSize(QSize(40, 40))
        self.hours_12_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius:20px;\n"
"	background-color: rgb(138, 144, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 4px solid black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border: 4px solid black;\n"
"}")
        self.hours_12_button.setCheckable(True)
        self.hours_12_button.setChecked(True)

        self.horizontalLayout_13.addWidget(self.hours_12_button)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.time_formate_24_label = QLabel(self.time_formate_frame)
        self.time_formate_24_label.setObjectName(u"time_formate_24_label")
        sizePolicy9.setHeightForWidth(self.time_formate_24_label.sizePolicy().hasHeightForWidth())
        self.time_formate_24_label.setSizePolicy(sizePolicy9)
        self.time_formate_24_label.setMaximumSize(QSize(16777215, 16777215))
        self.time_formate_24_label.setFont(font29)
        self.time_formate_24_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_13.addWidget(self.time_formate_24_label)

        self.hours_24_button = QPushButton(self.time_formate_frame)
        self.hours_24_button.setObjectName(u"hours_24_button")
        self.hours_24_button.setMinimumSize(QSize(40, 40))
        self.hours_24_button.setMaximumSize(QSize(40, 40))
        self.hours_24_button.setStyleSheet(u"QPushButton{\n"
"border: 2px solid black;\n"
"border-radius:20px;\n"
"	background-color: rgb(138, 144, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 4px solid black;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"border: 4px solid black;\n"
"}")
        self.hours_24_button.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.hours_24_button)


        self.verticalLayout_15.addWidget(self.time_formate_frame)


        self.verticalLayout_14.addWidget(self.time_buttons_frame)

        self.frame_25 = QFrame(self.settings_frame)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy3.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy3)
        self.frame_25.setMaximumSize(QSize(16777215, 60))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_25)

        self.frame_39 = QFrame(self.settings_frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.advanced_settings_label = QLabel(self.frame_39)
        self.advanced_settings_label.setObjectName(u"advanced_settings_label")
        sizePolicy.setHeightForWidth(self.advanced_settings_label.sizePolicy().hasHeightForWidth())
        self.advanced_settings_label.setSizePolicy(sizePolicy)
        font30 = QFont()
        font30.setPointSize(39)
        font30.setBold(True)
        self.advanced_settings_label.setFont(font30)
        self.advanced_settings_label.setStyleSheet(u"color:black;")
        self.advanced_settings_label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_35.addWidget(self.advanced_settings_label)


        self.verticalLayout_14.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.settings_frame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_30)

        self.connect_to_zigbee_btn = QPushButton(self.frame_40)
        self.connect_to_zigbee_btn.setObjectName(u"connect_to_zigbee_btn")
        self.connect_to_zigbee_btn.setMinimumSize(QSize(150, 50))
        self.connect_to_zigbee_btn.setMaximumSize(QSize(150, 50))
        font31 = QFont()
        font31.setFamilies([u"Sakkal Majalla"])
        font31.setPointSize(19)
        self.connect_to_zigbee_btn.setFont(font31)
        self.connect_to_zigbee_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(38, 38, 38);\n"
"border-radius: 25px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border:2px solid black;\n"
"}\n"
"")
        self.connect_to_zigbee_btn.setCheckable(True)

        self.horizontalLayout_36.addWidget(self.connect_to_zigbee_btn)

        self.zigbee_connect_text_label = QLabel(self.frame_40)
        self.zigbee_connect_text_label.setObjectName(u"zigbee_connect_text_label")
        self.zigbee_connect_text_label.setFont(font29)
        self.zigbee_connect_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_36.addWidget(self.zigbee_connect_text_label)


        self.verticalLayout_14.addWidget(self.frame_40)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)


        self.horizontalLayout_31.addWidget(self.settings_frame)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.settings_page)
        self.new_notification_page = QWidget()
        self.new_notification_page.setObjectName(u"new_notification_page")
        self.new_notification_page.setStyleSheet(u"#new_notification_page{\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.new_notification_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_11 = QFrame(self.new_notification_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_2 = QFrame(self.frame_11)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_31 = QFrame(self.frame_2)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy3.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy3)
        self.frame_31.setMaximumSize(QSize(16777215, 180))
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_31)

        self.noti_kind_frame = QFrame(self.frame_2)
        self.noti_kind_frame.setObjectName(u"noti_kind_frame")
        sizePolicy9.setHeightForWidth(self.noti_kind_frame.sizePolicy().hasHeightForWidth())
        self.noti_kind_frame.setSizePolicy(sizePolicy9)
        self.noti_kind_frame.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 25, 35);;\n"
"border-radius: 19px;\n"
"border: 1px solid  rgb(97, 99, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 239, 255);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(8, 185, 123);\n"
"}")
        self.noti_kind_frame.setFrameShape(QFrame.NoFrame)
        self.noti_kind_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.noti_kind_frame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 20, 33, -1)
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_27)

        self.once_noti_label = QLabel(self.noti_kind_frame)
        self.once_noti_label.setObjectName(u"once_noti_label")
        font32 = QFont()
        font32.setFamilies([u"Microsoft Uighur"])
        font32.setPointSize(26)
        self.once_noti_label.setFont(font32)
        self.once_noti_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_19.addWidget(self.once_noti_label)

        self.once_noti = QPushButton(self.noti_kind_frame)
        self.once_noti.setObjectName(u"once_noti")
        self.once_noti.setMinimumSize(QSize(38, 38))
        self.once_noti.setMaximumSize(QSize(38, 38))
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/images/button_88647.png", QSize(), QIcon.Normal, QIcon.Off)
        self.once_noti.setIcon(icon7)
        self.once_noti.setIconSize(QSize(38, 38))
        self.once_noti.setCheckable(True)
        self.once_noti.setChecked(False)

        self.horizontalLayout_19.addWidget(self.once_noti)

        self.horizontalSpacer_28 = QSpacerItem(60, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_28)

        self.permenant_noti_label = QLabel(self.noti_kind_frame)
        self.permenant_noti_label.setObjectName(u"permenant_noti_label")
        self.permenant_noti_label.setFont(font32)
        self.permenant_noti_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_19.addWidget(self.permenant_noti_label)

        self.permenante_noti = QPushButton(self.noti_kind_frame)
        self.permenante_noti.setObjectName(u"permenante_noti")
        sizePolicy14.setHeightForWidth(self.permenante_noti.sizePolicy().hasHeightForWidth())
        self.permenante_noti.setSizePolicy(sizePolicy14)
        self.permenante_noti.setMinimumSize(QSize(38, 38))
        self.permenante_noti.setMaximumSize(QSize(38, 38))
        self.permenante_noti.setSizeIncrement(QSize(0, 0))
        self.permenante_noti.setStyleSheet(u"")
        self.permenante_noti.setIcon(icon7)
        self.permenante_noti.setIconSize(QSize(38, 38))
        self.permenante_noti.setCheckable(True)
        self.permenante_noti.setChecked(True)

        self.horizontalLayout_19.addWidget(self.permenante_noti)

        self.noti_type_text_label = QLabel(self.noti_kind_frame)
        self.noti_type_text_label.setObjectName(u"noti_type_text_label")
        self.noti_type_text_label.setFont(font4)
        self.noti_type_text_label.setStyleSheet(u"color:black;")

        self.horizontalLayout_19.addWidget(self.noti_type_text_label)


        self.verticalLayout_27.addWidget(self.noti_kind_frame)

        self.frame_33 = QFrame(self.frame_2)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy3.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy3)
        self.frame_33.setMaximumSize(QSize(16777215, 100))
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_33)

        self.noti_settings_frame = QFrame(self.frame_2)
        self.noti_settings_frame.setObjectName(u"noti_settings_frame")
        self.noti_settings_frame.setFrameShape(QFrame.NoFrame)
        self.noti_settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.noti_settings_frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.date_frame = QFrame(self.noti_settings_frame)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setMaximumSize(QSize(16777215, 16777215))
        self.date_frame.setFrameShape(QFrame.NoFrame)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.date_frame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)

        self.noti_date_frame = QFrame(self.date_frame)
        self.noti_date_frame.setObjectName(u"noti_date_frame")
        sizePolicy1.setHeightForWidth(self.noti_date_frame.sizePolicy().hasHeightForWidth())
        self.noti_date_frame.setSizePolicy(sizePolicy1)
        self.noti_date_frame.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(212, 212, 212);\n"
"border-radius: 16px;\n"
"border: 1px solid  rgb(97, 99, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 239, 255);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	\n"
"	background-color: rgb(143, 216, 255);\n"
"}")
        self.noti_date_frame.setFrameShape(QFrame.NoFrame)
        self.noti_date_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.noti_date_frame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.frame_9 = QFrame(self.noti_date_frame)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(380, 0))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_9)
        self.verticalLayout_38.setSpacing(22)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.date_noti_label = QLabel(self.frame_9)
        self.date_noti_label.setObjectName(u"date_noti_label")
        font33 = QFont()
        font33.setFamilies([u"Microsoft Uighur"])
        font33.setPointSize(28)
        font33.setBold(True)
        self.date_noti_label.setFont(font33)
        self.date_noti_label.setStyleSheet(u"color:black;")

        self.verticalLayout_38.addWidget(self.date_noti_label)

        self.noti_date = QCalendarWidget(self.frame_9)
        self.noti_date.setObjectName(u"noti_date")
        sizePolicy3.setHeightForWidth(self.noti_date.sizePolicy().hasHeightForWidth())
        self.noti_date.setSizePolicy(sizePolicy3)
        self.noti_date.setMinimumSize(QSize(0, 330))
        self.noti_date.setGridVisible(True)
        self.noti_date.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.noti_date.setNavigationBarVisible(True)
        self.noti_date.setDateEditEnabled(True)
        self.noti_date.setDateEditAcceptDelay(1500)

        self.verticalLayout_38.addWidget(self.noti_date)


        self.verticalLayout_26.addWidget(self.frame_9)


        self.horizontalLayout_23.addWidget(self.noti_date_frame)

        self.frame_32 = QFrame(self.date_frame)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setMaximumSize(QSize(100, 16777215))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_32)

        self.time_frame_2 = QFrame(self.date_frame)
        self.time_frame_2.setObjectName(u"time_frame_2")
        self.time_frame_2.setMinimumSize(QSize(0, 0))
        self.time_frame_2.setMaximumSize(QSize(600, 16777215))
        self.time_frame_2.setFrameShape(QFrame.NoFrame)
        self.time_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.time_frame_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.before_adan_frame = QFrame(self.time_frame_2)
        self.before_adan_frame.setObjectName(u"before_adan_frame")
        self.before_adan_frame.setFrameShape(QFrame.NoFrame)
        self.before_adan_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.before_adan_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 0, -1, 15)
        self.frame_6 = QFrame(self.before_adan_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(11, 0, 11, 0)
        self.before_adan_noti_label = QLabel(self.frame_6)
        self.before_adan_noti_label.setObjectName(u"before_adan_noti_label")
        sizePolicy9.setHeightForWidth(self.before_adan_noti_label.sizePolicy().hasHeightForWidth())
        self.before_adan_noti_label.setSizePolicy(sizePolicy9)
        self.before_adan_noti_label.setFont(font33)
        self.before_adan_noti_label.setStyleSheet(u"color:black;")
        self.before_adan_noti_label.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_24.addWidget(self.before_adan_noti_label)

        self.before_adan_type_button = QPushButton(self.frame_6)
        self.before_adan_type_button.setObjectName(u"before_adan_type_button")
        self.before_adan_type_button.setMinimumSize(QSize(32, 32))
        self.before_adan_type_button.setMaximumSize(QSize(32, 32))
        self.before_adan_type_button.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(227, 227, 227);\n"
"border: none;\n"
"border-radius:16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(225, 239, 240);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(8, 185, 123);\n"
"	background-color: rgb(190, 254, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/images/stop-button_73880.png", QSize(), QIcon.Normal, QIcon.Off)
        self.before_adan_type_button.setIcon(icon8)
        self.before_adan_type_button.setIconSize(QSize(32, 32))
        self.before_adan_type_button.setCheckable(True)
        self.before_adan_type_button.setChecked(True)

        self.horizontalLayout_24.addWidget(self.before_adan_type_button)


        self.verticalLayout_23.addWidget(self.frame_6)

        self.adan_min_frame = QFrame(self.before_adan_frame)
        self.adan_min_frame.setObjectName(u"adan_min_frame")
        sizePolicy9.setHeightForWidth(self.adan_min_frame.sizePolicy().hasHeightForWidth())
        self.adan_min_frame.setSizePolicy(sizePolicy9)
        self.adan_min_frame.setFrameShape(QFrame.NoFrame)
        self.adan_min_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.adan_min_frame)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.before_adan_minutes_spin = QSpinBox(self.adan_min_frame)
        self.before_adan_minutes_spin.setObjectName(u"before_adan_minutes_spin")
        self.before_adan_minutes_spin.setMinimumSize(QSize(200, 60))
        self.before_adan_minutes_spin.setMaximumSize(QSize(16777215, 60))
        font34 = QFont()
        font34.setFamilies([u"Microsoft Uighur"])
        font34.setPointSize(20)
        self.before_adan_minutes_spin.setFont(font34)
        self.before_adan_minutes_spin.setStyleSheet(u"QSpinBox {\n"
"	color:black;\n"
"    background-color: white;\n"
"    border: 3px solid black;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/plus.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/minimize-sign.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    border: none;\n"
"	border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-bottom: 2px solid black; /* Add dividing line */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    borde"
                        "r: none;\n"
"border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-top: 2px solid black; /* Add dividing line */\n"
"}\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"\n"
"/* Hover effect for down button */\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"")
        self.before_adan_minutes_spin.setFrame(False)
        self.before_adan_minutes_spin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.before_adan_minutes_spin.setAccelerated(True)
        self.before_adan_minutes_spin.setKeyboardTracking(True)
        self.before_adan_minutes_spin.setMinimum(1)
        self.before_adan_minutes_spin.setValue(1)

        self.horizontalLayout_21.addWidget(self.before_adan_minutes_spin)

        self.before_adan_box = QComboBox(self.adan_min_frame)
        self.before_adan_box.addItem("")
        self.before_adan_box.addItem("")
        self.before_adan_box.addItem("")
        self.before_adan_box.addItem("")
        self.before_adan_box.addItem("")
        self.before_adan_box.addItem("")
        self.before_adan_box.setObjectName(u"before_adan_box")
        self.before_adan_box.setMinimumSize(QSize(119, 60))
        self.before_adan_box.setMaximumSize(QSize(16777215, 60))
        font35 = QFont()
        font35.setFamilies([u"Sakkal Majalla"])
        font35.setPointSize(20)
        self.before_adan_box.setFont(font35)
        self.before_adan_box.setStyleSheet(u"QComboBox {\n"
"                border: 3px solid rgb(38, 38, 38);\n"
"				border-radius: 3px;\n"
"                padding: 1px 10px 1px 7px;\n"
"                min-width: 6em;\n"
"            }\n"
"QComboBox::drop-down {\n"
"                color:white;\n"
"                width: 26px;\n"
"                border-left-width: 1px;\n"
"                border-left-color: rgb(38, 38, 38);\n"
"                border-left-style: solid;\n"
"\n"
"               background-color: rgb(38,38,38);\n"
"}\n"
"QComboBox::down-arrow {\n"
"\n"
"				width:20px;\n"
"				height: 20px;\n"
"				margin: 1px 3px 1px 3px;\n"
"                image: url(:/newPrefix/images/down-chevron.png); /* Use the resource path */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(53,53,53); \n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color:rgb(53,53,53);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    text-decoration: none;  /* Prevent line-through text */\n"
"    background"
                        "-color: transparent;\n"
"}\n"
"\n"
"\n"
"           \n"
"\n"
"")
        self.before_adan_box.setFrame(True)

        self.horizontalLayout_21.addWidget(self.before_adan_box)


        self.verticalLayout_23.addWidget(self.adan_min_frame)


        self.verticalLayout_22.addWidget(self.before_adan_frame)

        self.after_adan_frame = QFrame(self.time_frame_2)
        self.after_adan_frame.setObjectName(u"after_adan_frame")
        sizePolicy1.setHeightForWidth(self.after_adan_frame.sizePolicy().hasHeightForWidth())
        self.after_adan_frame.setSizePolicy(sizePolicy1)
        self.after_adan_frame.setStyleSheet(u"")
        self.after_adan_frame.setFrameShape(QFrame.NoFrame)
        self.after_adan_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.after_adan_frame)
        self.verticalLayout_24.setSpacing(17)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 15)
        self.frame_8 = QFrame(self.after_adan_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.after_adan_noti_label = QLabel(self.frame_8)
        self.after_adan_noti_label.setObjectName(u"after_adan_noti_label")
        sizePolicy9.setHeightForWidth(self.after_adan_noti_label.sizePolicy().hasHeightForWidth())
        self.after_adan_noti_label.setSizePolicy(sizePolicy9)
        self.after_adan_noti_label.setFont(font33)
        self.after_adan_noti_label.setStyleSheet(u"color:black;")
        self.after_adan_noti_label.setFrameShape(QFrame.NoFrame)
        self.after_adan_noti_label.setWordWrap(False)

        self.horizontalLayout_25.addWidget(self.after_adan_noti_label)

        self.after_adan_type_button = QPushButton(self.frame_8)
        self.after_adan_type_button.setObjectName(u"after_adan_type_button")
        self.after_adan_type_button.setMinimumSize(QSize(32, 32))
        self.after_adan_type_button.setMaximumSize(QSize(32, 32))
        self.after_adan_type_button.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(227, 227, 227);\n"
"border: none;\n"
"border-radius:16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(225, 239, 240);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(190, 254, 255);\n"
"}")
        self.after_adan_type_button.setIcon(icon8)
        self.after_adan_type_button.setIconSize(QSize(32, 32))
        self.after_adan_type_button.setCheckable(True)

        self.horizontalLayout_25.addWidget(self.after_adan_type_button)


        self.verticalLayout_24.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.after_adan_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.after_adan_minutes_spin = QSpinBox(self.frame_4)
        self.after_adan_minutes_spin.setObjectName(u"after_adan_minutes_spin")
        self.after_adan_minutes_spin.setMinimumSize(QSize(200, 60))
        self.after_adan_minutes_spin.setMaximumSize(QSize(16777215, 60))
        self.after_adan_minutes_spin.setFont(font34)
        self.after_adan_minutes_spin.setStyleSheet(u"QSpinBox {\n"
"    background-color: white;\n"
"    border: 3px solid black;\n"
"    border-radius: 7px;\n"
"color:black;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/plus.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/minimize-sign.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    border: none;\n"
"	border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-bottom: 2px solid black; /* Add dividing line */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    border"
                        ": none;\n"
"border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-top: 2px solid black; /* Add dividing line */\n"
"}\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"\n"
"/* Hover effect for down button */\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"")
        self.after_adan_minutes_spin.setFrame(False)
        self.after_adan_minutes_spin.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.after_adan_minutes_spin.setAccelerated(True)
        self.after_adan_minutes_spin.setKeyboardTracking(False)
        self.after_adan_minutes_spin.setMinimum(10)
        self.after_adan_minutes_spin.setMaximum(60)
        self.after_adan_minutes_spin.setSingleStep(10)

        self.horizontalLayout_26.addWidget(self.after_adan_minutes_spin)

        self.after_adan_box = QComboBox(self.frame_4)
        self.after_adan_box.addItem("")
        self.after_adan_box.addItem("")
        self.after_adan_box.addItem("")
        self.after_adan_box.addItem("")
        self.after_adan_box.addItem("")
        self.after_adan_box.addItem("")
        self.after_adan_box.setObjectName(u"after_adan_box")
        self.after_adan_box.setMinimumSize(QSize(119, 60))
        self.after_adan_box.setMaximumSize(QSize(16777215, 60))
        self.after_adan_box.setFont(font35)
        self.after_adan_box.setStyleSheet(u"QComboBox {\n"
"                border: 3px solid rgb(38, 38, 38);\n"
"				border-radius: 3px;\n"
"                padding: 1px 10px 1px 7px;\n"
"                min-width: 6em;\n"
"            }\n"
"QComboBox::drop-down {\n"
"                color:white;\n"
"                width: 26px;\n"
"                border-left-width: 1px;\n"
"                border-left-color: rgb(38, 38, 38);\n"
"                border-left-style: solid;\n"
"\n"
"               background-color: rgb(38,38,38);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"				width:20px;\n"
"				height: 20px;\n"
"				margin: 1px 3px 1px 3px;\n"
"                image: url(:/newPrefix/images/down-chevron.png); \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(53,53,53); \n"
"}\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color:rgb(53,53,53);\n"
"\n"
"}\n"
"   \n"
"QComboBox QAbstractItemView::item {\n"
"    text-decoration: none;  \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_26.addWidget(self.after_adan_box)


        self.verticalLayout_24.addWidget(self.frame_4)


        self.verticalLayout_22.addWidget(self.after_adan_frame)

        self.frame_3 = QFrame(self.time_frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setSpacing(17)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.duration_label = QLabel(self.frame_3)
        self.duration_label.setObjectName(u"duration_label")
        sizePolicy9.setHeightForWidth(self.duration_label.sizePolicy().hasHeightForWidth())
        self.duration_label.setSizePolicy(sizePolicy9)
        self.duration_label.setFont(font33)
        self.duration_label.setStyleSheet(u"color:black;")

        self.verticalLayout_25.addWidget(self.duration_label)

        self.duration_spinbox = QSpinBox(self.frame_3)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        self.duration_spinbox.setMinimumSize(QSize(0, 60))
        self.duration_spinbox.setMaximumSize(QSize(16777215, 60))
        self.duration_spinbox.setFont(font35)
        self.duration_spinbox.setStyleSheet(u"QSpinBox {\n"
"color:black;\n"
"    background-color: white;\n"
"    border: 3px solid black;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/plus.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    background-color: transparent;\n"
"    image: url(:/newPrefix/images/minimize-sign.png);\n"
"    width: 25px; /* Adjust based on your image size */\n"
"    height: 25px;\n"
"    border: none; /* Remove extra borders */\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    border: none;\n"
"	border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-bottom: 2px solid black; /* Add dividing line */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    background-color: white;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    border"
                        ": none;\n"
"border-left: 3px solid Black;\n"
"    width: 28px;\n"
"    height: 28px;\n"
"    border-top: 2px solid black; /* Add dividing line */\n"
"}\n"
"QSpinBox::up-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"\n"
"/* Hover effect for down button */\n"
"QSpinBox::down-button:hover{\n"
"    background-color:rgb(243, 255, 255);\n"
"}\n"
"")
        self.duration_spinbox.setFrame(False)
        self.duration_spinbox.setAlignment(Qt.AlignCenter)
        self.duration_spinbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.duration_spinbox.setAccelerated(True)
        self.duration_spinbox.setMinimum(0)
        self.duration_spinbox.setMaximum(100)
        self.duration_spinbox.setSingleStep(1)
        self.duration_spinbox.setValue(0)

        self.verticalLayout_25.addWidget(self.duration_spinbox)


        self.verticalLayout_22.addWidget(self.frame_3)


        self.horizontalLayout_23.addWidget(self.time_frame_2)


        self.horizontalLayout_20.addWidget(self.date_frame)


        self.verticalLayout_27.addWidget(self.noti_settings_frame)

        self.frame_38 = QFrame(self.frame_2)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy3.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy3)
        self.frame_38.setMaximumSize(QSize(16777215, 170))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_38)

        self.save_sound_frame = QFrame(self.frame_2)
        self.save_sound_frame.setObjectName(u"save_sound_frame")
        sizePolicy9.setHeightForWidth(self.save_sound_frame.sizePolicy().hasHeightForWidth())
        self.save_sound_frame.setSizePolicy(sizePolicy9)
        self.save_sound_frame.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(53, 53, 53);\n"
"border-radius: 5px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border:2px solid black;\n"
"}\n"
"\n"
"")
        self.save_sound_frame.setFrameShape(QFrame.NoFrame)
        self.save_sound_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.save_sound_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.save_notification_button = QPushButton(self.save_sound_frame)
        self.save_notification_button.setObjectName(u"save_notification_button")
        self.save_notification_button.setMinimumSize(QSize(0, 50))
        self.save_notification_button.setMaximumSize(QSize(16777215, 50))
        font36 = QFont()
        font36.setFamilies([u"Microsoft Uighur"])
        font36.setPointSize(22)
        self.save_notification_button.setFont(font36)
        self.save_notification_button.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.save_notification_button)

        self.notification_sound_button = QPushButton(self.save_sound_frame)
        self.notification_sound_button.setObjectName(u"notification_sound_button")
        self.notification_sound_button.setMinimumSize(QSize(0, 50))
        self.notification_sound_button.setMaximumSize(QSize(16777215, 50))
        self.notification_sound_button.setSizeIncrement(QSize(0, 0))
        self.notification_sound_button.setBaseSize(QSize(0, 0))
        self.notification_sound_button.setFont(font36)
        self.notification_sound_button.setCheckable(True)
        self.notification_sound_button.setFlat(False)

        self.horizontalLayout_22.addWidget(self.notification_sound_button)


        self.verticalLayout_27.addWidget(self.save_sound_frame)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(213, 33, 10);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(198, 35, 20);\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 0, -1, -1)
        self.cancel_noti_create = QPushButton(self.frame_5)
        self.cancel_noti_create.setObjectName(u"cancel_noti_create")
        self.cancel_noti_create.setMinimumSize(QSize(0, 50))
        self.cancel_noti_create.setMaximumSize(QSize(16777215, 50))
        self.cancel_noti_create.setFont(font36)
        self.cancel_noti_create.setCheckable(True)

        self.verticalLayout_28.addWidget(self.cancel_noti_create)


        self.verticalLayout_27.addWidget(self.frame_5)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_8)


        self.horizontalLayout_32.addWidget(self.frame_2)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.new_notification_page)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(central_widget)
        self.openMenuButton.clicked.connect(self.expandedMenu.show)
        self.openMenuButton.clicked.connect(self.frame_19.hide)
        self.powerOffButton.clicked.connect(self.expandedMenu.hide)
        self.powerOffButton.clicked.connect(self.frame_19.show)

        self.openMenuButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.dohor_activate_button.setDefault(False)
        self.noti_sort_box.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(central_widget)
    # setupUi

    def retranslateUi(self, central_widget):
        central_widget.setWindowTitle(QCoreApplication.translate("central_widget", u"Form", None))
        self.menuTitleLabel.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0642\u0627\u0626\u0645\u0629", None))
        self.mainPageButton.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629", None))
        self.notificationsPageButton.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0627\u0634\u0639\u0627\u0631\u0627\u062a", None))
        self.quraanPageButton.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0642\u0631\u0621\u0627\u0646", None))
        self.settingsPageButton.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0627\u0639\u062f\u0627\u062f\u0627\u062a", None))
        self.powerOffButton.setText("")
        self.openMenuButton.setText("")
        self.masgedNameLabel.setText(QCoreApplication.translate("central_widget", u"\u0645\u0633\u062c\u062f \u0635\u0644\u0627\u062d \u0627\u0644\u062f\u064a\u0646 \u0627\u0644\u0627\u064a\u0648\u0628\u064a - \u0645\u0639\u0627\u0648\u064a\u0629", None))
        self.jomoaa_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u062c\u0645\u0639\u0629", None))
        self.jomoaa_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.clockLabel.setText(QCoreApplication.translate("central_widget", u"07:20:58", None))
        self.seconds_label.setText("")
        self.am_pm_label.setText(QCoreApplication.translate("central_widget", u"AM", None))
        self.dateLabel.setText(QCoreApplication.translate("central_widget", u"00/00/0000", None))
        self.dayLabel.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u062c\u0645\u0639\u0629", None))
        self.shorok_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0634\u0631\u0648\u0642", None))
        self.shorok_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.remainingTimeLabel.setText(QCoreApplication.translate("central_widget", u"00:00:00", None))
        self.remaining_text_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0648\u0642\u062a \u0627\u0644\u0645\u062a\u0628\u0642\u064a \u0644\u0623\u0630\u0627\u0646", None))
        self.nextAdanNameLabel.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0645\u063a\u0631\u0628", None))
        self.emergency_stop_button.setText("")
        self.emergency_label.setText(QCoreApplication.translate("central_widget", u"\u0644\u0625\u064a\u0642\u0627\u0641 \u0627\u0644\u0623\u0630\u0627\u0646 \u0625\u0636\u063a\u0637 \u0647\u0646\u0627", None))
        self.ishaa_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0639\u0634\u0627\u0621", None))
        self.ishaa_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.ishaa_activate_button.setText(QCoreApplication.translate("central_widget", u"\u062a\u0641\u0639\u064a\u0644 \u0627\u0644\u0627\u0630\u0627\u0646", None))
        self.ishaaSoundButton.setText(QCoreApplication.translate("central_widget", u"\u0635\u0648\u062a \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0634\u0627\u0621", None))
        self.magreb_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0645\u063a\u0631\u0628", None))
        self.magreb_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.magreb_activate_button.setText(QCoreApplication.translate("central_widget", u"\u062a\u0641\u0639\u064a\u0644 \u0627\u0644\u0627\u0630\u0627\u0646", None))
        self.magrebSoundButton.setText(QCoreApplication.translate("central_widget", u"\u0635\u0648\u062a \u0627\u0630\u0627\u0646 \u0627\u0644\u0645\u063a\u0631\u0628", None))
        self.aser_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0639\u0635\u0631", None))
        self.aser_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.aser_activate_button.setText(QCoreApplication.translate("central_widget", u"\u062a\u0641\u0639\u064a\u0644 \u0627\u0644\u0627\u0630\u0627\u0646", None))
        self.aserSoundButton.setText(QCoreApplication.translate("central_widget", u"\u0635\u0648\u062a \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0635\u0631", None))
        self.dohor_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0638\u0647\u0631", None))
        self.dohor_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.dohor_activate_button.setText(QCoreApplication.translate("central_widget", u"\u062a\u0641\u0639\u064a\u0644 \u0627\u0644\u0627\u0630\u0627\u0646", None))
        self.dohorSoundButton.setText(QCoreApplication.translate("central_widget", u"\u0635\u0648\u062a \u0627\u0630\u0627\u0646 \u0627\u0644\u0638\u0647\u0631", None))
        self.fajer_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0641\u062c\u0631", None))
        self.fajer_adan_time.setText(QCoreApplication.translate("central_widget", u"00:00 AM", None))
        self.fajer_activate_button.setText(QCoreApplication.translate("central_widget", u"\u062a\u0641\u0639\u064a\u0644 \u0627\u0644\u0627\u0630\u0627\u0646", None))
        self.fajerSoundButton.setText(QCoreApplication.translate("central_widget", u"\u0635\u0648\u062a \u0627\u0630\u0627\u0646 \u0627\u0644\u0641\u062c\u0631", None))
        self.instant_player_play_button.setText("")
        self.instant_player_pause_button.setText("")
        self.instant_player_resume_button.setText("")
        self.instant_player_stop_button.setText("")
        self.instant_player_choose_file_button.setText(QCoreApplication.translate("central_widget", u"\u0645\u0644\u0641 \u0635\u0648\u062a \u0644\u0644\u062a\u0634\u063a\u064a\u0644 \u0627\u0644\u0641\u0648\u0631\u064a", None))
        self.instant_player_delete_file_button.setText(QCoreApplication.translate("central_widget", u"\u062d\u0630\u0641 \u0627\u0644\u0645\u0644\u0641", None))
        self.total_noti_label.setText(QCoreApplication.translate("central_widget", u"0", None))
        self.total_noti_text_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u062c\u0645\u0627\u0644\u064a \u0639\u062f\u062f \u0627\u0644\u0627\u0634\u0639\u0627\u0631\u0627\u062a : ", None))
        self.new_notification_buttton.setText(QCoreApplication.translate("central_widget", u"\u0627\u0634\u0639\u0627\u0631 \u062c\u062f\u064a\u062f", None))
        self.noti_sort_box.setItemText(0, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u0641\u062c\u0631 ", None))
        self.noti_sort_box.setItemText(1, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u0638\u0647\u0631 ", None))
        self.noti_sort_box.setItemText(2, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u0639\u0635\u0631 ", None))
        self.noti_sort_box.setItemText(3, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u0645\u063a\u0631\u0628 ", None))
        self.noti_sort_box.setItemText(4, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u0639\u0634\u0627\u0621 ", None))
        self.noti_sort_box.setItemText(5, QCoreApplication.translate("central_widget", u"\u0635\u0644\u0627\u0629 \u0627\u0644\u062c\u0645\u0639\u0629", None))
        self.noti_sort_box.setItemText(6, QCoreApplication.translate("central_widget", u"\u0627\u0644\u0643\u0644 ", None))

        self.notis_text_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0627\u0634\u0639\u0627\u0631\u0627\u062a : ", None))
        self.stop_notification.setText(QCoreApplication.translate("central_widget", u"\u0627\u064a\u0642\u0627\u0641 \u0627\u0644\u0627\u0634\u0639\u0627\u0631 \u0627\u0644\u062d\u0627\u0644\u064a", None))
        self.quraan_coming_soon_label.setText(QCoreApplication.translate("central_widget", u"\u0642\u0631\u064a\u0628\u0627 ...", None))
        self.masjed_time_settings_label.setText(QCoreApplication.translate("central_widget", u"\u0625\u0639\u062f\u0627\u062f\u0627\u062a \u0627\u0644\u0645\u0633\u062c\u062f \u0648\u0627\u0644\u0648\u0642\u062a", None))
        self.masjedNameInput.setInputMask("")
        self.masjedNameInput.setPlaceholderText("")
        self.masjed_name_text_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062c\u062f:", None))
        self.cityInput.setPlaceholderText("")
        self.city_text_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u0628\u0644\u062f:", None))
        self.qudsTimeDiff.setSuffix(QCoreApplication.translate("central_widget", u" min", None))
        self.qudsTimeDiff.setPrefix("")
        self.quds_diff_text_label.setText(QCoreApplication.translate("central_widget", u"\u0641\u0627\u0631\u0642 \u0627\u0644\u062a\u0648\u0642\u064a\u062a \u0639\u0646 \u0645\u062f\u064a\u0646\u0629 \u0627\u0644\u0642\u062f\u0633 : ", None))
        self.sum_win_timing_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u062a\u0648\u0642\u064a\u062a:", None))
        self.summer_settings_label.setText(QCoreApplication.translate("central_widget", u"\u0635\u064a\u0641\u064a", None))
        self.summerButton.setText("")
        self.winter_settings_label.setText(QCoreApplication.translate("central_widget", u"\u0634\u062a\u0648\u064a", None))
        self.winterButton.setText("")
        self.time_format_text_label.setText(QCoreApplication.translate("central_widget", u"\u0639\u0631\u0636 \u0627\u0644\u0648\u0642\u062a:", None))
        self.time_formate_12_label.setText(QCoreApplication.translate("central_widget", u"12 \u0633\u0627\u0639\u0629", None))
        self.hours_12_button.setText("")
        self.time_formate_24_label.setText(QCoreApplication.translate("central_widget", u"24 \u0633\u0627\u0639\u0629", None))
        self.hours_24_button.setText("")
        self.advanced_settings_label.setText(QCoreApplication.translate("central_widget", u"\u0645\u062a\u0642\u062f\u0645", None))
        self.connect_to_zigbee_btn.setText(QCoreApplication.translate("central_widget", u"\u0627\u0631\u062a\u0628\u0637", None))
        self.zigbee_connect_text_label.setText(QCoreApplication.translate("central_widget", u"\u0644\u0644\u0627\u0631\u062a\u0628\u0627\u0637 \u0628\u062c\u0647\u0627\u0632 \u0627\u0644\u0635\u0648\u062a zigbee ", None))
        self.once_noti_label.setText(QCoreApplication.translate("central_widget", u"\u0645\u0631\u0629 \u0648\u0627\u062d\u062f\u0629", None))
        self.once_noti.setText("")
        self.permenant_noti_label.setText(QCoreApplication.translate("central_widget", u"\u062b\u0627\u0628\u062a", None))
        self.permenante_noti.setText("")
        self.noti_type_text_label.setText(QCoreApplication.translate("central_widget", u"\u0646\u0648\u0639 \u0627\u0644\u0627\u0634\u0639\u0627\u0631 :", None))
        self.date_noti_label.setText(QCoreApplication.translate("central_widget", u"\u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u062a\u0627\u0631\u064a\u062e :", None))
        self.before_adan_noti_label.setText(QCoreApplication.translate("central_widget", u"\u062a\u0639\u064a\u064a\u0646 \u0627\u0644\u0627\u0634\u0639\u0627\u0631 \u0642\u0628\u0644 \u0648\u0642\u062a \u0627\u0644\u0627\u0630\u0627\u0646 :", None))
        self.before_adan_type_button.setText("")
        self.before_adan_minutes_spin.setSuffix(QCoreApplication.translate("central_widget", u" \u062f\u0642\u0627\u0626\u0642", None))
        self.before_adan_minutes_spin.setPrefix(QCoreApplication.translate("central_widget", u"\u0628 ", None))
        self.before_adan_box.setItemText(0, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u0641\u062c\u0631 ", None))
        self.before_adan_box.setItemText(1, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u0638\u0647\u0631 ", None))
        self.before_adan_box.setItemText(2, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0635\u0631 ", None))
        self.before_adan_box.setItemText(3, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u0645\u063a\u0631\u0628 ", None))
        self.before_adan_box.setItemText(4, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0634\u0627\u0621 ", None))
        self.before_adan_box.setItemText(5, QCoreApplication.translate("central_widget", u"\u0642\u0628\u0644 \u0627\u0630\u0627\u0646 \u0627\u0644\u062c\u0645\u0639\u0629", None))

        self.after_adan_noti_label.setText(QCoreApplication.translate("central_widget", u"\u062a\u0639\u064a\u064a\u0646 \u0627\u0644\u0627\u0634\u0639\u0627\u0631 \u0628\u0639\u062f \u0648\u0642\u062a \u0627\u0644\u0627\u0630\u0627\u0646 :", None))
        self.after_adan_type_button.setText("")
        self.after_adan_minutes_spin.setSuffix(QCoreApplication.translate("central_widget", u" \u062b\u0648\u0627\u0646\u064a", None))
        self.after_adan_minutes_spin.setPrefix(QCoreApplication.translate("central_widget", u"\u0628 ", None))
        self.after_adan_box.setItemText(0, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u0641\u062c\u0631", None))
        self.after_adan_box.setItemText(1, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u0638\u0647\u0631", None))
        self.after_adan_box.setItemText(2, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0635\u0631", None))
        self.after_adan_box.setItemText(3, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u0645\u063a\u0631\u0628", None))
        self.after_adan_box.setItemText(4, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u0639\u0634\u0627\u0621", None))
        self.after_adan_box.setItemText(5, QCoreApplication.translate("central_widget", u"\u0628\u0639\u062f \u0627\u0630\u0627\u0646 \u0627\u0644\u062c\u0645\u0639\u0629", None))

        self.duration_label.setText(QCoreApplication.translate("central_widget", u"\u0645\u062f\u0629 \u0627\u0644\u062a\u0634\u063a\u064a\u0644 (\u0627\u062e\u062a\u064a\u0627\u0631\u064a) :", None))
        self.duration_spinbox.setSuffix(QCoreApplication.translate("central_widget", u"  \u062f\u0642\u0627\u0626\u0642", None))
        self.save_notification_button.setText(QCoreApplication.translate("central_widget", u"\u062d\u0641\u0638 \u0627\u0644\u0627\u0634\u0639\u0627\u0631", None))
        self.notification_sound_button.setText(QCoreApplication.translate("central_widget", u"\u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0635\u0648\u062a\u064a", None))
        self.cancel_noti_create.setText(QCoreApplication.translate("central_widget", u"\u0627\u0644\u063a\u0627\u0621", None))
    # retranslateUi

