from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QFontDatabase, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,)

import resources_rc as resources_rc
from ResourceFile import resource_path

class Ui_notification_widget(object):
    def __init__(self, widget):

        self.widget = widget
        
        Readex_Pro_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Readex_Pro/static/ReadexPro-Regular.ttf"))
        self.ReadexPro_font_family = QFontDatabase.applicationFontFamilies(Readex_Pro_font_id)[0]

        font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Noto_Kufi_Arabic/static/NotoKufiArabic-Regular.ttf"))
        self.kufi_ont_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        tajawal_bold_font_id = QFontDatabase.addApplicationFont(resource_path("resources/fonts/Tajawal/Tajawal-Bold.ttf"))
        self.tajawal_bold_font_family = QFontDatabase.applicationFontFamilies(tajawal_bold_font_id)[0]


        self.setupUi(self.widget)

    def setupUi(self, notification_widget):
        if not notification_widget.objectName():
            notification_widget.setObjectName(u"notification_widget")
        notification_widget.resize(310, 370)
        notification_widget.setMinimumSize(QSize(310, 0))
        notification_widget.setMaximumSize(QSize(315, 16777215))
        notification_widget.setStyleSheet(u"#notification_widget{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(notification_widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.notification_frame = QFrame(notification_widget)
        self.notification_frame.setObjectName(u"notification_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notification_frame.sizePolicy().hasHeightForWidth())
        self.notification_frame.setSizePolicy(sizePolicy)
        self.notification_frame.setMinimumSize(QSize(300, 350))
        self.notification_frame.setMaximumSize(QSize(16777215, 16777215))
        self.notification_frame.setStyleSheet(u"#notification_frame{\n"
"background-color: rgb(255,255,255);\n"
"border: 3px solid rgb(13, 13, 13);\n"
"border-radius: 5px;\n"
"}\n"
"")
        self.notification_frame.setFrameShape(QFrame.NoFrame)
        self.notification_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.notification_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.notification_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.noti_date_label = QLabel(self.frame)
        self.noti_date_label.setObjectName(u"noti_date_label")
        
        font = QFont(self.kufi_ont_family, 16)
        font.setBold(True)

        self.noti_date_label.setFont(font)
        self.noti_date_label.setStyleSheet(u"color:black;")
        self.noti_date_label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_2.addWidget(self.noti_date_label)

        self.noti_time_label = QLabel(self.frame)
        self.noti_time_label.setObjectName(u"noti_time_label")
        
        font = QFont(self.kufi_ont_family, 28)
        font.setBold(True)
        
        self.noti_time_label.setFont(font)
        self.noti_time_label.setStyleSheet(u"color:black;")
        self.noti_time_label.setFrameShape(QFrame.NoFrame)
        self.noti_time_label.setFrameShadow(QFrame.Plain)
        self.noti_time_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.noti_time_label)

        self.noti_adan_label = QLabel(self.frame)
        self.noti_adan_label.setObjectName(u"noti_adan_label")

        font = QFont(self.ReadexPro_font_family, 20)
        self.noti_adan_label.setFont(font)

        self.noti_adan_label.setStyleSheet(u"color:black;")
        self.noti_adan_label.setScaledContents(False)
        self.noti_adan_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.noti_adan_label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.is_noti_active_label = QLabel(self.frame_2)
        self.is_noti_active_label.setObjectName(u"is_noti_active_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.is_noti_active_label.sizePolicy().hasHeightForWidth())
        
        font = QFont(self.tajawal_bold_font_family, 20)
        font.setBold(True)

        self.is_noti_active_label.setFont(font)
        self.is_noti_active_label.setStyleSheet(u"color:black;")
        self.is_noti_active_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.is_noti_active_label)

        self.activate_noti_button = QPushButton(self.frame_2)
        self.activate_noti_button.setObjectName(u"activate_noti_button")
        self.activate_noti_button.setMinimumSize(QSize(34, 34))
        self.activate_noti_button.setMaximumSize(QSize(34, 34))
        self.activate_noti_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(193, 18, 51);\n"
"border:none;\n"
"border-radius: 17px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(180, 239, 255);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(8, 185, 123);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/power_3039519.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/newPrefix/images/button_88647.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.activate_noti_button.setIcon(icon)
        self.activate_noti_button.setIconSize(QSize(34, 34))
        self.activate_noti_button.setCheckable(True)
        self.activate_noti_button.setChecked(True)

        self.horizontalLayout_2.addWidget(self.activate_noti_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.notification_frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.show_noti_button = QPushButton(self.frame_3)
        self.show_noti_button.setObjectName(u"show_noti_button")
        self.show_noti_button.setMinimumSize(QSize(0, 60))

        font = QFont(self.tajawal_bold_font_family, 22)
        font.setBold(True)

        self.show_noti_button.setFont(font)
        self.show_noti_button.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(13, 13, 13);\n"
"color: rgb(255,255,255);\n"
"border-bottom-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(236, 236, 236);\n"
"	color:black;\n"
"border-top: 2px solid rgb(13, 13, 13);\n"
"}")
        self.show_noti_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.show_noti_button)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.notification_frame)


        self.retranslateUi(notification_widget)

        QMetaObject.connectSlotsByName(notification_widget)
    # setupUi

    def retranslateUi(self, notification_widget):
        notification_widget.setWindowTitle(QCoreApplication.translate("notification_widget", u"\u0627\u0634\u0639\u0627\u0631", None))
        self.noti_date_label.setText(QCoreApplication.translate("notification_widget", u"04/08/2024", None))
        self.noti_time_label.setText(QCoreApplication.translate("notification_widget", u"09:48 AM", None))
        self.noti_adan_label.setText(QCoreApplication.translate("notification_widget", u"<html><head/><body><p>\u0642\u0628\u0644 \u0635\u0644\u0627\u0629 \u0627\u0644\u0638\u0647\u0631 <br/>\u0628 5 \u062f\u0642\u0627\u0626\u0642</p></body></html>", None))
        self.is_noti_active_label.setText(QCoreApplication.translate("notification_widget", u"\u0645\u0641\u0639\u0644", None))
        self.activate_noti_button.setText("")
        self.show_noti_button.setText(QCoreApplication.translate("notification_widget", u"\u0639\u0631\u0636 \u0627\u0644\u0627\u0634\u0639\u0627\u0631", None))
    # retranslateUi

