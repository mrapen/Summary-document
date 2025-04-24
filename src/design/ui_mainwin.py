# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import src.design.resources
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/icons/src/icons/summarize_black.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 #222, stop:0.42 #333, stop:1 #444);\n"
"	font-family: Noto Sans SC;\n"
"	color: white;\n"
"	font-size: 10pt;\n"
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
"	background-color: none;\n"
"	border: none;\n"
"	margin-left: 2px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgba(255,255,255,30);\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius: 7px;\n"
"	font-weight: bold;\n"
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
"	border: 1px solid rgba(255,255,255,40);\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: rgba(0,0,0,30"
                        ");\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgba(0,0,0,30);\n"
"	border-radius: 7px;\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: #444;\n"
"	border: #333;\n"
"	font-family: Noto Sans SC;\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_5)

        self.btn_open_file = QPushButton(self.centralwidget)
        self.btn_open_file.setObjectName(u"btn_open_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_open_file.sizePolicy().hasHeightForWidth())
        self.btn_open_file.setSizePolicy(sizePolicy1)
        self.btn_open_file.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_open_file.setStyleSheet(u"padding: 0 0.5em;\n"
"margin-right: 1px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/src/icons/file_open_white.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_open_file.setIcon(icon1)
        self.btn_open_file.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_open_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.le_path = QLineEdit(self.centralwidget)
        self.le_path.setObjectName(u"le_path")
        self.le_path.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_path.sizePolicy().hasHeightForWidth())
        self.le_path.setSizePolicy(sizePolicy2)
        self.le_path.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_path)


        self.horizontalLayout_1.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.label_7)

        self.cb_prompt_lang = QComboBox(self.centralwidget)
        self.cb_prompt_lang.addItem("")
        self.cb_prompt_lang.addItem("")
        self.cb_prompt_lang.setObjectName(u"cb_prompt_lang")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cb_prompt_lang.sizePolicy().hasHeightForWidth())
        self.cb_prompt_lang.setSizePolicy(sizePolicy4)
        self.cb_prompt_lang.setMinimumSize(QSize(0, 0))
        self.cb_prompt_lang.setStyleSheet(u"")
        self.cb_prompt_lang.setEditable(False)
        self.cb_prompt_lang.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.cb_prompt_lang.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.cb_prompt_lang.setIconSize(QSize(16, 16))
        self.cb_prompt_lang.setDuplicatesEnabled(False)
        self.cb_prompt_lang.setFrame(False)

        self.verticalLayout_2.addWidget(self.cb_prompt_lang)


        self.horizontalLayout_1.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_save_summary = QPushButton(self.centralwidget)
        self.btn_save_summary.setObjectName(u"btn_save_summary")
        self.btn_save_summary.setCheckable(False)

        self.verticalLayout_6.addWidget(self.btn_save_summary)

        self.btn_summarize = QPushButton(self.centralwidget)
        self.btn_summarize.setObjectName(u"btn_summarize")
        sizePolicy4.setHeightForWidth(self.btn_summarize.sizePolicy().hasHeightForWidth())
        self.btn_summarize.setSizePolicy(sizePolicy4)
        self.btn_summarize.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_summarize)


        self.horizontalLayout_1.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setStyleSheet(u"font-size: 12pt;\n"
"margin-left: 0.2em;")

        self.verticalLayout_5.addWidget(self.label)

        self.te_prompt_1 = QTextEdit(self.centralwidget)
        self.te_prompt_1.setObjectName(u"te_prompt_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.te_prompt_1.sizePolicy().hasHeightForWidth())
        self.te_prompt_1.setSizePolicy(sizePolicy6)

        self.verticalLayout_5.addWidget(self.te_prompt_1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.label_6)

        self.te_response = QTextEdit(self.centralwidget)
        self.te_response.setObjectName(u"te_response")
        self.te_response.setEnabled(True)
        self.te_response.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.te_response)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0432\u043e\u0440\u0438\u0442\u0438 \u0441\u0430\u043c\u0430\u0440\u0456 \u0437 AI", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0428\u043b\u044f\u0445 \u0444\u0430\u0439\u043b\u043e\u0432\u043e\u0433\u043e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443", None))
#if QT_CONFIG(tooltip)
        self.btn_open_file.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u0444\u0430\u0439\u043b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_open_file.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_open_file.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u043e\u0432\u0430 \u043f\u0440\u043e\u043c\u043f\u0442\u0456\u0432</p></body></html>", None))
        self.cb_prompt_lang.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430", None))
        self.cb_prompt_lang.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

        self.cb_prompt_lang.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.btn_save_summary.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0438\u0432\u043a\u043b\u044e\u0447\u0438\u0442\u0438 \u043e\u0441\u0442\u0430\u043d\u0454 \u0441\u0430\u043c\u0430\u0440\u0456</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save_summary.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0431\u0435\u0440\u0435\u0433\u0442\u0438 \u0441\u0430\u043c\u0430\u0440\u0456", None))
        self.btn_summarize.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0441\u0443\u043c\u0443\u0432\u0430\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0438\u0439 \u043f\u0440\u043e\u043c\u043f\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u044c \u0432\u0456\u0434 AI", None))
    # retranslateUi

