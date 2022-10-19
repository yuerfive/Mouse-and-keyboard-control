# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowsTxHnN.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1243, 755)
        Form.setMinimumSize(QSize(1200, 700))
        Form.setMaximumSize(QSize(9999, 9999))
        Form.setStyleSheet(u"*{\n"
"	font-family:\u6977\u4f53;\n"
"	color:white;\n"
"}\n"
"\n"
"QRadioButton{\n"
"	background-color:#181D25;\n"
"}\n"
"\n"
"QLabel#label_6{\n"
"    background-color:#2d3445;\n"
"}\n"
"QLabel#label_7{\n"
"    background-color:#181D25;\n"
"}\n"
"QLabel#label_8{\n"
"    background-color:#181D25;\n"
"}\n"
"QLabel#label_11{\n"
"	font-size:24pt;\n"
"	color:red;\n"
"    background-color:#181D25,50%;\n"
"}\n"
"\n"
"QLabel#label_9\n"
"{\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"}\n"
"QLabel#label_10\n"
"{\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background-color:#181D25;\n"
"}\n"
"\n"
"QWidget { \n"
"background-color: #1F2430;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QLabel#label_4 { \n"
"background-color: qlineargradient(spread:pad, x1:0.114, y1:0.131, x2:0.869, y2:0.869318, stop:0 rgba(241, 151, 240, 255), stop:1 rgba(184, 247, 245, 255));\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_5 { \n"
"background-color: #181D25;\n"
""
                        "border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"QLabel { \n"
"background-color: #2f3648;\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"}\n"
"\n"
"QPushButton#Button1\n"
"{\n"
"	border-radius:3px;\n"
"}\n"
"QPushButton#Button2\n"
"{\n"
"	border-radius:3px;\n"
"}\n"
"QPushButton#Button3\n"
"{\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"\n"
"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton\n"
"{\n"
"    font-size:14pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#29303f;\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:5px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#363A45;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20"
                        "\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}\n"
"\n"
"\n"
"/*\u6ed1\u5757\u539f\u59cb\u72b6\u6001*/\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background:#404755;  \n"
"}\n"
"\n"
"/*\u6ed1\u5757\u5149\u6807\u7ecf\u8fc7\u72b6\u6001*/\n"
"QScrollBar::handle:vertical:hover \n"
"{\n"
"    background-color:#4F5767;\n"
"}\n"
"\n"
"\n"
"/*\u6ed1\u5757\u5df2\u7ecf\u7ecf\u8fc7\u7684\u6ed1\u8f68\u533a\u57df\u7684\u989c\u8272*/\n"
"QScrollBar::add-page:vertical\n"
"{\n"
"    background:#2F3648;\n"
"}\n"
"\n"
"/*\u6ed1\u5757\u8fd8\u6ca1\u7ecf\u8fc7\u7684\u6ed1\u8f68\u533a\u57df\u7684\u989c\u8272*/\n"
"QScrollBar::sub-page:vertical\n"
"{\n"
"    background:#2F3648; \n"
"}\n"
"\n"
"\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(25, 23, 181, 700))
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setScaledContents(False)
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(388, 60, 831, 621))
        self.plainTextEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit\n"
"{\n"
"    font-size:14pt;\n"
"	selection-background-color:#2A3546\n"
"}\n"
"")
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setReadOnly(False)
        self.plainTextEdit.setTabStopDistance(40.000000000000000)
        self.plainTextEdit.setCursorWidth(1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(205, 63, 171, 31))
        self.label_2.setStyleSheet(u"QLabel#label_2{\n"
"\n"
"    font-size:16pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(205, 153, 171, 571))
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.setStyleSheet(u"QListWidget#listWidget{\n"
"\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"	/*\u4e0d\u663e\u793a\u865a\u7ebf*/\n"
"	outline:0px;\n"
"}\n"
"\n"
"/*\u539f\u59cb\u72b6\u6001*/\n"
"QListWidget::item{\n"
"	/*\u4e0a\u4e0b\u5bbd\u5ea6*/\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	/*\u95f4\u9694*/\n"
"	margin-top:1px;\n"
"	margin-bottom:1px;\n"
"	background-color:#1e2537;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"/*\u60ac\u505c\u72b6\u6001*/\n"
"QListWidget::item:hover{\n"
"	background-color:#292e3a;\n"
"}\n"
"\n"
"/*\u9009\u4e2d\u72b6\u6001*/\n"
"QListWidget::item:selected\n"
"{\n"
"    background-color:#000000;\n"
"}\n"
"\n"
"/*\u5931\u53bb\u7126\u70b9\u72b6\u6001*/\n"
"QListWidget::item:selected:!active\n"
"{\n"
"border-width:0px; \n"
"background:#000000;\n"
"color:white;\n"
" }\n"
"\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(201, 23, 179, 701))
        self.label_3.setStyleSheet(u"QLabel#label_3{\n"
"\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"	border-radius:5px;\n"
"\n"
"}")
        self.lineEdit1 = QLineEdit(Form)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(690, 698, 70, 25))
        self.lineEdit1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit1.setAlignment(Qt.AlignCenter)
        self.lineEdit2 = QLineEdit(Form)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(960, 698, 70, 25))
        self.lineEdit2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit2.setAlignment(Qt.AlignCenter)
        self.Button1 = QPushButton(Form)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setGeometry(QRect(620, 698, 60, 25))
        self.Button2 = QPushButton(Form)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(890, 698, 60, 25))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(85, 53, 60, 60))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u"UI/logo_ui.png"))
        self.label_4.setScaledContents(True)
        self.listWidget_2 = QListWidget(Form)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(25, 143, 176, 581))
        self.listWidget_2.setStyleSheet(u"QListWidget#listWidget_2{\n"
"\n"
"    font-size:14pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#2F3648;\n"
"	/*\u4e0d\u663e\u793a\u865a\u7ebf*/\n"
"	outline:0px;\n"
"}\n"
"\n"
"/*\u539f\u59cb\u72b6\u6001*/\n"
"QListWidget::item{\n"
"	/*\u4e0a\u4e0b\u5bbd\u5ea6*/\n"
"	padding-top:10px;\n"
"	padding-bottom:10px;\n"
"	/*\u95f4\u9694*/\n"
"	margin-top:5px;\n"
"	margin-bottom:5px;\n"
"	margin-left:20px;\n"
"	margin-right:20px;\n"
"	background-color:#1e2537;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"/*\u60ac\u505c\u72b6\u6001*/\n"
"QListWidget::item:hover{\n"
"	background-color:#181D25;\n"
"}\n"
"\n"
"/*\u9009\u4e2d\u72b6\u6001*/\n"
"QListWidget::item:selected\n"
"{\n"
"    background-color:#000000;\n"
"}\n"
"\n"
"/*\u5931\u53bb\u7126\u70b9\u72b6\u6001*/\n"
"QListWidget::item:selected:!active\n"
"{\n"
"border-width:0px; \n"
"background:#000000;\n"
"color:white;\n"
" }\n"
"\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(389, 28, 180, 25))
        self.label_5.setStyleSheet(u"QLabel#label_5{\n"
"\n"
"    font-size:12pt;\n"
"    /*\u5b57\u4f53\u989c\u8272\u4e3a\u767d\u8272*/    \n"
"    color:white;\n"
"\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.Button3 = QPushButton(Form)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setGeometry(QRect(545, 28, 23, 23))
        self.Button3.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton#Button3\n"
"{\n"
"    font-size:14pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background: transparent;\n"
"    /*background-color:#181D25;*/\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:5px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton#Button3:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#363A45;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton#Button3:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(209, 129, 163, 2))
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(388, 698, 74, 25))
        self.label_9.setStyleSheet(u"QLabel#label_2{\n"
"\n"
"    font-size:16pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#181D25;\n"
"\n"
"}")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.lineEdit3 = QLineEdit(Form)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setGeometry(QRect(462, 698, 100, 25))
        self.lineEdit3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit3.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(65, 623, 90, 31))
        self.label_10.setStyleSheet(u"QLabel#label_10{\n"
"\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#2F3648;\n"
"\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(645, 283, 301, 111))
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 660, 110, 31))
        self.label_12.setStyleSheet(u"QLabel#label_12{\n"
"\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#2F3648;\n"
"\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(23, 13, 1210, 720))
        self.label_13.setMinimumSize(QSize(1210, 720))
        self.label_13.setStyleSheet(u"QLabel#label_13{\n"
"	border-radius:5px;\n"
"\n"
"}")
        self.Button5 = QPushButton(Form)
        self.Button5.setObjectName(u"Button5")
        self.Button5.setGeometry(QRect(1201, 20, 20, 20))
        self.Button5.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton#Button5\n"
"{\n"
"    font-size:14pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background: transparent;\n"
"    /*background-color:#181D25;*/\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton#Button5:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#1F2430;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton#Button5:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}")
        self.Button4 = QPushButton(Form)
        self.Button4.setObjectName(u"Button4")
        self.Button4.setGeometry(QRect(1168, 20, 25, 23))
        self.Button4.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton#Button4\n"
"{\n"
"    font-size:14pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background: transparent;\n"
"    /*background-color:#181D25;*/\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton#Button4:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#1F2430;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton#Button4:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(552, 260, 221, 131))
        self.label_7.setStyleSheet(u"QLabel#label_7{\n"
"	border-radius:5px;\n"
"\n"
"}")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.radioButton1 = QRadioButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton1)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setGeometry(QRect(580, 290, 50, 25))
        self.radioButton1.setStyleSheet(u"QRadioButton#radioButton1{\n"
"	background-color:#181D25;\n"
"}")
        self.radioButton2 = QRadioButton(Form)
        self.buttonGroup.addButton(self.radioButton2)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(652, 290, 97, 25))
        self.radioButton2.setStyleSheet(u"QRadioButton#radioButton2{\n"
"	background-color:#181D25;\n"
"}")
        self.radioButton3 = QRadioButton(Form)
        self.radioButton3.setObjectName(u"radioButton3")
        self.radioButton3.setGeometry(QRect(580, 321, 79, 25))
        self.radioButton3.setStyleSheet(u"QRadioButton#radioButton3{\n"
"	background-color:#181D25;\n"
"}")
        self.Button6 = QPushButton(Form)
        self.Button6.setObjectName(u"Button6")
        self.Button6.setGeometry(QRect(600, 355, 40, 25))
        self.Button6.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton#Button6\n"
"{\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background-color:#2F3648;\n"
"    /*background-color:#181D25;*/\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton#Button6:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#1F2430;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton#Button6:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}")
        self.Button7 = QPushButton(Form)
        self.Button7.setObjectName(u"Button7")
        self.Button7.setGeometry(QRect(690, 355, 40, 25))
        self.Button7.setStyleSheet(u"/*\u6309\u94ae\u666e\u901a\u6001*/\n"
"QPushButton#Button7\n"
"{\n"
"    font-size:12pt;\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"	background-color:#2F3648;\n"
"    /*background-color:#181D25;*/\n"
"    /*\u8fb9\u6846\u5706\u89d2\u534a\u5f84*/ \n"
"    border-radius:2px;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u505c\u7559\u6001*/\n"
"QPushButton#Button7:hover\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#1F2430;\n"
"}\n"
" \n"
"/*\u6309\u94ae\u6309\u4e0b\u6001*/\n"
"QPushButton#Button7:pressed\n"
"{\n"
"    /*\u80cc\u666f\u989c\u8272*/  \n"
"    background-color:#000000;\n"
"    /*\u5de6\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u53f3\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-left:1px;\n"
"    /*\u4e0a\u5185\u8fb9\u8ddd\u4e3a3\u50cf\u7d20\uff0c\u8ba9\u6309\u4e0b\u65f6\u5b57\u5411\u4e0b\u79fb\u52a83\u50cf\u7d20*/  \n"
"    padding-top:1px;\n"
"}")
        self.label_13.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.listWidget.raise_()
        self.lineEdit1.raise_()
        self.lineEdit2.raise_()
        self.Button1.raise_()
        self.Button2.raise_()
        self.label_4.raise_()
        self.listWidget_2.raise_()
        self.label_5.raise_()
        self.Button3.raise_()
        self.label_6.raise_()
        self.label_9.raise_()
        self.lineEdit3.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.Button5.raise_()
        self.Button4.raise_()
        self.label_7.raise_()
        self.radioButton1.raise_()
        self.radioButton2.raise_()
        self.radioButton3.raise_()
        self.Button6.raise_()
        self.Button7.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u542c\u96e8\u6309\u952e\u8f85\u52a9", None))
        self.label.setText("")
        self.plainTextEdit.setPlainText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u6587\u4ef6", None))
        self.label_3.setText("")
        self.lineEdit1.setText("")
        self.Button1.setText(QCoreApplication.translate("Form", u"\u542f\u52a8", None))
        self.Button2.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.label_4.setText("")

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u952e\u76d8\u63a7\u5236", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u63a7\u5236", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u540e\u53f0\u63a7\u5236", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_5.setText("")
        self.Button3.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.label_6.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u4f4d\u7f6e:", None))
        self.lineEdit3.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"v1.6.0", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Q\u7fa4\uff1a212769521", None))
        self.label_13.setText("")
        self.Button5.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.Button4.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_7.setText("")
        self.radioButton1.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.radioButton2.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316\u5230\u6258\u76d8", None))
        self.radioButton3.setText(QCoreApplication.translate("Form", u"\u4e0d\u518d\u663e\u793a", None))
        self.Button6.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.Button7.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
    # retranslateUi

