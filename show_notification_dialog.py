# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_notification_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resource_file_rc

class Ui_NotificationInfo_dialog(object):
    def setupUi(self, NotificationInfo_dialog):
        if not NotificationInfo_dialog.objectName():
            NotificationInfo_dialog.setObjectName(u"NotificationInfo_dialog")
        NotificationInfo_dialog.resize(400, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NotificationInfo_dialog.sizePolicy().hasHeightForWidth())
        NotificationInfo_dialog.setSizePolicy(sizePolicy)
        NotificationInfo_dialog.setMinimumSize(QSize(400, 0))
        NotificationInfo_dialog.setMaximumSize(QSize(400, 350))
        NotificationInfo_dialog.setSizeIncrement(QSize(0, 0))
        NotificationInfo_dialog.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/mosque.png", QSize(), QIcon.Normal, QIcon.Off)
        NotificationInfo_dialog.setWindowIcon(icon)
        NotificationInfo_dialog.setStyleSheet(u"\n"
"QDialog{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(NotificationInfo_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 11, -1, 15)
        self.noti_date_label = QLabel(NotificationInfo_dialog)
        self.noti_date_label.setObjectName(u"noti_date_label")
        font = QFont()
        font.setFamilies([u"Monotype Hadassah"])
        font.setPointSize(10)
        font.setBold(True)
        self.noti_date_label.setFont(font)
        self.noti_date_label.setStyleSheet(u"color:black;")
        self.noti_date_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.noti_date_label)

        self.info_frame = QFrame(NotificationInfo_dialog)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.info_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.noti_time_label = QLabel(self.info_frame)
        self.noti_time_label.setObjectName(u"noti_time_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.noti_time_label.sizePolicy().hasHeightForWidth())
        self.noti_time_label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Traditional Arabic"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.noti_time_label.setFont(font1)
        self.noti_time_label.setStyleSheet(u"color:black;")
        self.noti_time_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.noti_time_label)

        self.noti_info_label = QLabel(self.info_frame)
        self.noti_info_label.setObjectName(u"noti_info_label")
        font2 = QFont()
        font2.setFamilies([u"Traditional Arabic"])
        font2.setPointSize(26)
        font2.setBold(True)
        self.noti_info_label.setFont(font2)
        self.noti_info_label.setStyleSheet(u"color:black;")
        self.noti_info_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.noti_info_label)


        self.verticalLayout.addWidget(self.info_frame)

        self.edit_frame = QFrame(NotificationInfo_dialog)
        self.edit_frame.setObjectName(u"edit_frame")
        sizePolicy1.setHeightForWidth(self.edit_frame.sizePolicy().hasHeightForWidth())
        self.edit_frame.setSizePolicy(sizePolicy1)
        self.edit_frame.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(13, 13, 13);\n"
"color: rgb(255,255,255);\n"
"border: none;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 3px solid black;\n"
"background-color: rgb(255,255,255);\n"
"color: black;\n"
"}\n"
"")
        self.edit_frame.setFrameShape(QFrame.NoFrame)
        self.edit_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.edit_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 11, -1, 0)
        self.edit_sound_noti_button = QPushButton(self.edit_frame)
        self.edit_sound_noti_button.setObjectName(u"edit_sound_noti_button")
        self.edit_sound_noti_button.setMinimumSize(QSize(0, 40))
        self.edit_sound_noti_button.setMaximumSize(QSize(16777215, 40))
        self.edit_sound_noti_button.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Traditional Arabic"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.edit_sound_noti_button.setFont(font3)

        self.horizontalLayout_2.addWidget(self.edit_sound_noti_button)


        self.verticalLayout.addWidget(self.edit_frame)

        self.save_del_frame = QFrame(NotificationInfo_dialog)
        self.save_del_frame.setObjectName(u"save_del_frame")
        sizePolicy1.setHeightForWidth(self.save_del_frame.sizePolicy().hasHeightForWidth())
        self.save_del_frame.setSizePolicy(sizePolicy1)
        self.save_del_frame.setStyleSheet(u"QPushButton{\n"
"color: rgb(255,255,255);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#delete_noti_button{\n"
"background-color: rgb(167, 25, 35);\n"
"}\n"
"#delete_noti_button:hover{\n"
"background-color: rgb(190, 28, 41);\n"
"}\n"
"\n"
"#save_noti_button{\n"
"background-color: rgb(8, 148, 108);\n"
"}\n"
"\n"
"#save_noti_button:hover{\n"
"background-color: rgb(8, 185, 123);\n"
"}")
        self.save_del_frame.setFrameShape(QFrame.NoFrame)
        self.save_del_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.save_del_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 11)
        self.save_noti_button = QPushButton(self.save_del_frame)
        self.save_noti_button.setObjectName(u"save_noti_button")
        self.save_noti_button.setMinimumSize(QSize(0, 40))
        self.save_noti_button.setMaximumSize(QSize(16777215, 40))
        self.save_noti_button.setFont(font3)

        self.horizontalLayout_3.addWidget(self.save_noti_button)

        self.delete_noti_button = QPushButton(self.save_del_frame)
        self.delete_noti_button.setObjectName(u"delete_noti_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.delete_noti_button.sizePolicy().hasHeightForWidth())
        self.delete_noti_button.setSizePolicy(sizePolicy2)
        self.delete_noti_button.setMinimumSize(QSize(0, 40))
        self.delete_noti_button.setMaximumSize(QSize(16777215, 40))
        self.delete_noti_button.setFont(font3)

        self.horizontalLayout_3.addWidget(self.delete_noti_button)


        self.verticalLayout.addWidget(self.save_del_frame)


        self.retranslateUi(NotificationInfo_dialog)

        QMetaObject.connectSlotsByName(NotificationInfo_dialog)
    # setupUi

    def retranslateUi(self, NotificationInfo_dialog):
        NotificationInfo_dialog.setWindowTitle(QCoreApplication.translate("NotificationInfo_dialog", u"\u0645\u0639\u0644\u0648\u0645\u0627\u062a \u0627\u0644\u0627\u0634\u0639\u0627\u0631", None))
        self.noti_date_label.setText(QCoreApplication.translate("NotificationInfo_dialog", u"04/08/2024", None))
        self.noti_time_label.setText(QCoreApplication.translate("NotificationInfo_dialog", u"00:00:00", None))
        self.noti_info_label.setText(QCoreApplication.translate("NotificationInfo_dialog", u"\u0642\u0628\u0644 \u0635\u0644\u0627\u0629 \u0627\u0644\u0638\u0647\u0631 \u0628 ", None))
        self.edit_sound_noti_button.setText(QCoreApplication.translate("NotificationInfo_dialog", u"\u062a\u0639\u062f\u064a\u0644 \u0627\u0644\u0635\u0648\u062a", None))
        self.save_noti_button.setText(QCoreApplication.translate("NotificationInfo_dialog", u"\u062d\u0641\u0638", None))
        self.delete_noti_button.setText(QCoreApplication.translate("NotificationInfo_dialog", u"\u062d\u0630\u0641 \u0627\u0644\u0627\u0634\u0639\u0627\u0631", None))
    # retranslateUi

