# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import src.design.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/icons/src/icons/summarize_black.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #222, stop:0.42 #333, stop:1 #444);\n"
"	font-family: Noto Sans SC;\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgba(255,255,255,30);\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-weight: bold;\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255,255,255,30);\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius: 7px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255,255,255,80);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgba(0,0,0,30);\n"
"	border-radius: 7px;\n"
"	border: none;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: rgba(0,0,0,30);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Prompt_frame = QFrame(self.centralwidget)
        self.Prompt_frame.setObjectName(u"Prompt_frame")
        self.Prompt_frame.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.Prompt_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_prompts = QLabel(self.Prompt_frame)
        self.lbl_prompts.setObjectName(u"lbl_prompts")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_prompts.sizePolicy().hasHeightForWidth())
        self.lbl_prompts.setSizePolicy(sizePolicy)
        self.lbl_prompts.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.lbl_prompts)

        self.lbl_prompt_1 = QLabel(self.Prompt_frame)
        self.lbl_prompt_1.setObjectName(u"lbl_prompt_1")
        sizePolicy.setHeightForWidth(self.lbl_prompt_1.sizePolicy().hasHeightForWidth())
        self.lbl_prompt_1.setSizePolicy(sizePolicy)
        self.lbl_prompt_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.lbl_prompt_1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.btn_summarize = QPushButton(self.Prompt_frame)
        self.btn_summarize.setObjectName(u"btn_summarize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_summarize.sizePolicy().hasHeightForWidth())
        self.btn_summarize.setSizePolicy(sizePolicy1)
        self.btn_summarize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_summarize.setStyleSheet(u"font-weight: bold;\n"
"font-size: 14pt;\n"
"padding: 0 1em;")

        self.horizontalLayout_2.addWidget(self.btn_summarize)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.te_prompt_1 = QTextEdit(self.Prompt_frame)
        self.te_prompt_1.setObjectName(u"te_prompt_1")
        self.te_prompt_1.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_5.addWidget(self.te_prompt_1)

        self.lbl_prompt_2 = QLabel(self.Prompt_frame)
        self.lbl_prompt_2.setObjectName(u"lbl_prompt_2")
        self.lbl_prompt_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.lbl_prompt_2)

        self.te_prompt_2 = QTextEdit(self.Prompt_frame)
        self.te_prompt_2.setObjectName(u"te_prompt_2")
        self.te_prompt_2.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_5.addWidget(self.te_prompt_2)

        self.lbl_prompt_3 = QLabel(self.Prompt_frame)
        self.lbl_prompt_3.setObjectName(u"lbl_prompt_3")
        self.lbl_prompt_3.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.lbl_prompt_3)

        self.te_prompt_3 = QTextEdit(self.Prompt_frame)
        self.te_prompt_3.setObjectName(u"te_prompt_3")
        self.te_prompt_3.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_5.addWidget(self.te_prompt_3)

        self.lbl_prompt_4 = QLabel(self.Prompt_frame)
        self.lbl_prompt_4.setObjectName(u"lbl_prompt_4")
        self.lbl_prompt_4.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 12pt;")

        self.verticalLayout_5.addWidget(self.lbl_prompt_4)

        self.te_prompt_4 = QTextEdit(self.Prompt_frame)
        self.te_prompt_4.setObjectName(u"te_prompt_4")
        self.te_prompt_4.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.verticalLayout_5.addWidget(self.te_prompt_4)


        self.verticalLayout_3.addWidget(self.Prompt_frame)

        self.Open_file_frame = QFrame(self.centralwidget)
        self.Open_file_frame.setObjectName(u"Open_file_frame")
        self.Open_file_frame.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.Open_file_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_path = QLabel(self.Open_file_frame)
        self.lbl_path.setObjectName(u"lbl_path")
        self.lbl_path.setStyleSheet(u"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_path)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.le_path = QLineEdit(self.Open_file_frame)
        self.le_path.setObjectName(u"le_path")
        self.le_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_path)

        self.btn_open_file = QPushButton(self.Open_file_frame)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_file.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/src/icons/file_open_white.svg", QSize(), QIcon.Disabled, QIcon.On)
        self.btn_open_file.setIcon(icon1)
        self.btn_open_file.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_open_file)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.Open_file_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0431\u0438\u0432\u0430\u0442\u0438 \u043f\u0456\u0434\u0441\u0443\u043c\u043a\u0438 \u0437\u0430 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u043e\u044e chatGPT", None))
        self.lbl_prompts.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043c\u043f\u0442\u0438:", None))
        self.lbl_prompt_1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443", None))
        self.btn_summarize.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0441\u0443\u043c\u0443\u0432\u0430\u0442\u0438", None))
        self.lbl_prompt_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u0430 \u0430\u043d\u0430\u043b\u0456\u0437\u0443", None))
        self.lbl_prompt_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0456 \u0432\u0456\u0434 chatGPT", None))
        self.lbl_prompt_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u0432\u0438\u043c\u043e\u0433\u0438", None))
        self.lbl_path.setText(QCoreApplication.translate("MainWindow", u"\u0428\u043b\u044f\u0445 \u0444\u0430\u0439\u043b\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443", None))
        self.btn_open_file.setText("")
    # retranslateUi

