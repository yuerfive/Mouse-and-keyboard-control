

import sys ,os ,time ,ast
import win32api, win32con, pyWinhook
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pyautogui as pa
import threading as td
from UI import MainWindow

selective_type = 'key'
# selective_type = 'mouse'
# selective_type = 'backstage'
save_path = 0
n = 0

save_fast1 = 0
save_fast2 = 0

dict_text_key = 0
switch_key = 0

start_key = 0
Stop_key = 0

key = '0'

key_bool = 0

key_name = '0'

trigger = 0
left = 0
right = 0

key_code = {
    'A' : 65,
    'B' : 66,
    'C' : 67,
    'D' : 68,
    'E' : 69,
    'F' : 70,
    'G' : 71,
    'H' : 72,
    'I' : 73,
    'J' : 74,
    'K' : 75,
    'L' : 76,
    'M' : 77,
    'N' : 78,
    'O' : 79,
    'P' : 80,
    'Q' : 81,
    'R' : 82,
    'S' : 83,
    'T' : 84,
    'U' : 85,
    'V' : 86,
    'W' : 87,
    'X' : 88,
    'Y' : 89,
    'Z' : 90,
    'Space' : 32,
    'Oem_4' : 219,
    'Oem_6' : 221,
    'Oem_1' : 186,
    'Oem_7' : 222,
    'Oem_Comma' : 188,
    'Oem_Period' : 190,
    'Oem_2' : 191,
    'Oem_5' : 220,

    'Oem_3' : 192,
    '0' : 48,
    '1' : 49,
    '2' : 50,
    '3' : 51,
    '4' : 52,
    '5' : 53,
    '6' : 54,
    '7' : 55,
    '8' : 56,
    '9' : 57,
    'Oem_Minus' : 189,
    'Oem_Plus' : 187,

    'Numpad0' : 96,
    'Numpad1' : 97,
    'Numpad2' : 98,
    'Numpad3' : 99,
    'Numpad4' : 100,
    'Numpad5' : 101,
    'Numpad6' : 102,
    'Numpad7' : 103,
    'Numpad8' : 104,
    'Numpad9' : 105,
    'Decimal' : 110,
    'Add' : 107,
    'Subtract' : 109,
    'Multiply' : 106,
    'Divide' : 111,
    'Return' : 13,

    'F1' : 112,
    'F2' : 113,
    'F3' : 114,
    'F4' : 115,
    'F5' : 116,
    'F6' : 117,
    'F7' : 118,
    'F8' : 119,
    'F9' : 120,
    'F10' : 121,
    'F11' : 122,
    'F12' : 123,

    'Back' : 8,
    'Tab' : 9,
    'Lshift' : 16,
    'Rshift' : 16,
    'Lcontrol' : 17,
    'Rcontrol' : 17,
    'Capital' : 20,
    'Lmenu' : 18,
    'Rmenu' : 18,
    'Lwin' : 91,

    'Escape' : 27,

    'Insert' : 45,
    'Delete' : 46,
    'Home' : 36,
    'End' : 35,
    'Prior' : 33,
    'Next' : 34,

    'Left' : 37,
    'Up' : 38,
    'Right' : 39,
    'Down' : 40,
}


# ???????????????
class Main_Window(QWidget):

    def __init__(self,parent = None):

        # ??????????????????UI??????
        super(Main_Window, self).__init__(parent)
        self.ui = MainWindow.Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)		#????????????????????????
        self.setAttribute(Qt.WA_TranslucentBackground)	#?????????????????????????????????
        self.shadow = QGraphicsDropShadowEffect()		#??????????????????,?????????10,?????????#444444,?????????0,0
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#444444"))
        self.shadow.setOffset(0, 0)
        self.ui.label_13.setGraphicsEffect(self.shadow)	#???frame??????????????????

        self.ui.Button4.clicked.connect(self.showMinimized)
        self.ui.Button5.clicked.connect(self.close)

        # ??????????????????????????????
        self.ui.plainTextEdit.setReadOnly(True)
        # ??????X???????????????
        self.ui.Button3.hide()
        self.ui.Button3.clicked.connect(self.B3_hide)
        # ???????????????????????????
        self.ui.label_5.hide()
        self.ui.label_9.hide()
        self.ui.lineEdit3.hide()
        # ???????????????????????????
        self.ui.label_11.hide()
        # ??????????????????????????????????????????
        self.ui.label_7.hide()
        self.ui.radioButton1.hide()
        self.ui.radioButton2.hide()
        self.ui.radioButton3.hide()
        self.ui.Button6.hide()
        self.ui.Button7.hide()

        
        # ?????? ?????????????????????(??????)
        self.ui.lineEdit1.setText('F1')
        self.ui.lineEdit2.setText('F2')
        self.ui.lineEdit1.setReadOnly(True)
        self.ui.lineEdit2.setReadOnly(True)
        self.ui.Button1.setShortcut('F1')
        self.ui.Button2.setShortcut('F2')


        # ???????????????
        self.ui.Button1.clicked.connect(lambda:self.startAndStop(True))
        self.ui.Button2.clicked.connect(lambda:self.startAndStop(False))

        # ????????????
        self._restore_action = None
        self._quit_action = None
        self._tray_icon = None
        self._tray_icon_menu = None
        self.setup_ui()


        # ??????????????????
        self.KeyHook()

        #??????????????????
        # self.ui.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # ????????????
        self.ui.listWidget.doubleClicked.connect(self.RenameItem)  #????????????

        # ????????????
        # ???????????????????????? contextMenuPolicy ??????????????? CustomContextMenu
        # self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget.customContextMenuRequested.connect(self.myListWidgetContext)
        self.ui.plainTextEdit.customContextMenuRequested.connect(self.myPlainTextEditContext)

        # ???????????????
        self.ui.listWidget_2.itemClicked.connect(self.pos_Menu)

    def mousePressEvent(self, event):		#???????????????????????????????????????,??????????????????
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
        elif event.button() == Qt.RightButton:
            self.m_flag = False
    
    def mouseMoveEvent(self, QMouseEvent):	#??????????????????????????????????????????,????????????????????????
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    
    def mouseReleaseEvent(self, QMouseEvent):	#?????????????????????,????????????
        self.m_flag = False


#   --------------------------------------------------????????????-------------------------------------------------

    # ??????X???????????????
    def B3_hide(self):
        global save_path
        self.save_file()
        self.ui.Button3.hide()
        self.ui.label_5.hide()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setReadOnly(True)
        save_path = 0


    # ??????????????????
    def Qlabel_11(self,content):
        self.startAndStop(False)
        self.ui.label_11.show()
        self.ui.label_11.setText(content)
        time.sleep(3)
        self.ui.label_11.hide()

        # ?????? ?????????????????????
        # def Shortcut_key(self):
        #     global start_key ,Stop_key
        #     with open(r'config\original\Shortcut_key.txt') as f:
        #         data_key = f.read()
        #         dict_key = ast.literal_eval(data_key)
        #         start_key = dict_key['start']
        #         Stop_key = dict_key['Stop']
        #         self.set_startandStop_shortcut()

        # def set_startandStop_shortcut(self):
        #     global start_key ,Stop_key
        #     if start_key != 0 :
        #         self.ui.Button1.setShortcut(start_key)
        #         self.ui.lineEdit1.setText(start_key)
        #         self.ui.lineEdit1.setReadOnly(True)

        #     if Stop_key != 0 :
        #         self.ui.Button2.setShortcut(Stop_key)
        #         self.ui.lineEdit2.setText(Stop_key)
        #         self.ui.lineEdit2.setReadOnly(True)


#   --------------------------------------------------????????????-------------------------------------------------

    def myListWidgetContext(self,position):
        #????????????
        popMenu = QMenu()
        open_file =QAction('????????????', self)
        creAct =QAction("????????????",self)
        delAct =QAction("????????????",self)
        renameAct =QAction('?????????', self)
        #????????????????????????item??????,????????????.????????????????????????????????????.
        if self.ui.listWidget.itemAt(position):
            popMenu.addAction(open_file)
            popMenu.addAction(creAct)
            popMenu.addAction(delAct)
            popMenu.addAction(renameAct)
        else:
            popMenu.addAction(creAct)

        open_file.triggered.connect(self.open_file)
        creAct.triggered.connect(self.CreateNewItem)
        renameAct.triggered.connect(self.RenameItem)
        delAct.triggered.connect(self.DeleteItem)
        popMenu.exec_(self.ui.listWidget.mapToGlobal(position))

    # ????????????
    def open_file(self):
        global save_path
        # ?????????????????????????????????
        self.ui.plainTextEdit.setReadOnly(False)
        # ??????X???????????????
        self.ui.Button3.show()
        # ???????????????????????????
        self.ui.label_5.show()
        name = self.ui.listWidget.currentItem().text()
        self.ui.label_5.setText(name)

        if selective_type == 'key' and name != '????????????????????????':
            path = r'config\customize\Key_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'key' and name == '????????????????????????':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)

        if selective_type == 'mouse' and name != '????????????????????????':
            path = r'config\customize\Mouse_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'mouse' and name == '????????????????????????':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)

        if selective_type == 'backstage' and name != '????????????????????????':
            path = r'config\customize\backstage_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'backstage' and name == '????????????????????????':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # ???????????????????????????
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
    

    # ????????????
    def CreateNewItem(self):
        global n
    	#???????????????????????????item
        name = '????????????'
        list_name = []
        try:
            for i in range(999):
                exist_name = self.ui.listWidget.item(i).text()
                list_name.append(exist_name)
        except Exception:
            while True:
                if name in list_name:
                    name = '????????????'
                    n = n + 1
                    name = name + str(n)
                else:
                    break

        item = QListWidgetItem(name)
        item.setTextAlignment(Qt.AlignCenter)
        #??????item??????????????????.
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.listWidget.addItem(item)
        #????????????????????????item,?????????????????????.
        # self.ui.listWidget.editItem(item)

        if selective_type == 'key':
            with open(r'config\customize\Key_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '????????????'
                n = 0
        if selective_type == 'mouse':
            with open(r'config\customize\Mouse_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '????????????'
                n = 0
        if selective_type == 'backstage':
            with open(r'config\customize\backstage_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '????????????'
                n = 0


    #????????????
    def DeleteItem(self):
        global save_path
        if selective_type == 'key':
            # ????????????????????????
            name = self.ui.listWidget.currentItem().text()
            # ????????????????????????
            isfile = os.path.isfile(r'config\customize\Key_control\%s.txt' % name)
            if isfile == True:
                # ????????????
                os.remove(r'config\customize\Key_control\%s.txt' % name)
                # ????????????
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('???????????????')

        if selective_type == 'mouse':
            name = self.ui.listWidget.currentItem().text()
            isfile = os.path.isfile(r'config\customize\Mouse_control\%s.txt' % name)
            if isfile == True:
                os.remove(r'config\customize\Mouse_control\%s.txt' % name)
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('???????????????')

        if selective_type == 'backstage':
            name = self.ui.listWidget.currentItem().text()
            isfile = os.path.isfile(r'config\customize\backstage_control\%s.txt' % name)
            if isfile == True:
                os.remove(r'config\customize\backstage_control\%s.txt' % name)
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('???????????????')


    #?????????
    def RenameItem(self):
        name = self.ui.listWidget.currentItem().text()
        curRow =self.ui.listWidget.currentRow()
        item=self.ui.listWidget.item(curRow)
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.listWidget.editItem(item)

        self.ui.listWidget.itemChanged.connect(lambda :self.ChangeItem(name))

    def ChangeItem(self,name):
        global save_path
        new_name = self.ui.listWidget.currentItem().text()
        if new_name == name:
            pass
        if new_name != name and selective_type == 'key':
            path = r'config\customize\Key_control'
            os.rename(path + '\\' + name + '.txt' , path + '\\' + new_name + '.txt')
            save_path = path + '\\' + new_name + '.txt'
            name = self.ui.listWidget.currentItem().text()
            self.ui.label_5.setText(name)
        if new_name != name and selective_type == 'mouse':
            path = r'config\customize\Mouse_control'
            os.rename(path + '\\' + name + '.txt' , path + '\\' + new_name + '.txt')
            save_path = path + '\\' + new_name + '.txt'
            name = self.ui.listWidget.currentItem().text()
            self.ui.label_5.setText(name)
        if new_name != name and selective_type == 'backstage':
            path = r'config\customize\backstage_control'
            os.rename(path + '\\' + name + '.txt' , path + '\\' + new_name + '.txt')
            save_path = path + '\\' + new_name + '.txt'
            name = self.ui.listWidget.currentItem().text()
            self.ui.label_5.setText(name)


    # ????????????
    def myPlainTextEditContext(self,position):
        popMenu = QMenu()
        save_file =QAction('??????', self)
        if self.ui.listWidget.itemAt(position):
            popMenu.addAction(save_file)
        else:
            popMenu.addAction(save_file)
        save_file.setShortcut('Ctrl+S')
        save_file.triggered.connect(self.save_file)
        popMenu.exec_(self.ui.plainTextEdit.mapToGlobal(position))

    def save_file(self):
        global save_path
        try:
            with open(save_path,'w',encoding='utf-8') as f :
                f.seek(0)
                f.truncate()
                content = self.ui.plainTextEdit.toPlainText()
                f.write(content)
        except Exception:
            pass


#   --------------------------------------------------????????????-------------------------------------------------


    def setup_ui(self):
        # ????????????
        self.create_actions()
        self.create_tray_icon()

    def create_actions(self):

        self._restore_action = QAction("???????????????")
        self._restore_action.triggered.connect(self.showNormal)

        self._quit_action = QAction("??????")
        self._quit_action.triggered.connect(app.quit)

    def create_tray_icon(self):
        self._tray_icon_menu = QMenu()
        self._tray_icon_menu.addAction(self._restore_action)
        # ???????????????
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)
        # ??????????????????
        self._tray_icon = QSystemTrayIcon()
        self._tray_icon.setIcon(QIcon(r'UI\logo.png'))
        self._tray_icon.setContextMenu(self._tray_icon_menu)
        # ??????????????????????????????
        self._tray_icon.show()

        # ????????????
        self._tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)

    def iconActivated(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self._tray_icon.isVisible():
                self.showNormal()
            else:
                self.hide()


#   --------------------------------------------------???????????????--??????????????????----------------------------------

    # ????????????
    def pos_Menu(self,Index):
        global selective_type
        pos_name = self.ui.listWidget_2.item(self.ui.listWidget_2.row(Index)).text()
        if pos_name == '????????????':
            selective_type = 'key'
            self.key_file_name()
            self.key_file_name_U()
            self.B3_hide()
            # ???????????????
            T8 = td.Thread(target=self.key_name)
            T8.setDaemon(True)
            T8.start()
        if pos_name == '????????????':
            selective_type = 'mouse'
            self.mouse_file_name()
            self.mouse_file_name_U()
            self.B3_hide()
            # ????????????????????????
            T7 = td.Thread(target=self.mouse_position)
            T7.setDaemon(True)
            T7.start()
        if pos_name == '????????????':
            selective_type = 'backstage'
            self.backstage_file_name()
            self.backstage_file_name_U()
            self.B3_hide()

    # ??????[????????????]??????????????????
    # ???????????????
    def key_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '????????????????????????.txt':
                i_split = i.split('.')
                self.key_defaultLoad(i_split[0])

    # ??????????????????
    def key_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '????????????????????????':
                    flag = 1
                    break
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                else:
                    flag = 0
        except Exception:
            flag = 0

        if flag != 1 :
            item = QListWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.listWidget.addItem(item)

    # ----------------------------------------------------------------------------------------------------------

    # ??????[????????????]??????????????????
    # ???????????????
    def mouse_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '????????????????????????.txt':
                i_split = i.split('.')
                self.mouse_defaultLoad(i_split[0])

    # ??????????????????
    def mouse_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '????????????????????????':
                    flag = 1
                    break
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                else:
                    flag = 0
        except Exception:
            flag = 0

        if flag != 1 :
            item = QListWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.listWidget.addItem(item)

    # ----------------------------------------------------------------------------------------------------------

    # ??????[????????????]??????????????????
    # ???????????????
    def backstage_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '????????????????????????.txt':
                i_split = i.split('.')
                self.backstage_defaultLoad(i_split[0])

    # ??????????????????
    def backstage_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '????????????????????????':
                    flag = 1
                    break
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '????????????????????????':
                    self.ui.listWidget.takeItem(i)
                    continue
                else:
                    flag = 0
        except Exception:
            flag = 0

        if flag != 1 :
            item = QListWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.ui.listWidget.addItem(item)


#   --------------------------------------------------???????????????--??????????????????----------------------------------

    # ??????[????????????]??????????????????
    # ???????????????
    def key_file_name_U(self):
        path = r"config\customize\Key_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # ?????????????????????lambda???????????????????????????????????????????????????????????????
            # os.path.getmtime() ???????????????????????????????????????
            # os.path.getctime() ???????????????????????????????????????
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_key(list_U_N)

    # ??????????????????
    def load_user_file_key(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '????????????????????????':
                    pass
                else:
                    list_name.append(name)
        except Exception:
            pass
        for i in itme_name :
            if not i in list_name:
                item = QListWidgetItem(i)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.ui.listWidget.addItem(item)
        

    # ----------------------------------------------------------------------------------------------------------

    # ??????[????????????]??????????????????
    # ???????????????
    def mouse_file_name_U(self):
        path = r"config\customize\Mouse_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # ?????????????????????lambda???????????????????????????????????????????????????????????????
            # os.path.getmtime() ???????????????????????????????????????
            # os.path.getctime() ???????????????????????????????????????
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_mouse(list_U_N)

    # ??????????????????
    def load_user_file_mouse(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '????????????????????????':
                    pass
                else:
                    list_name.append(name)
        except Exception:
            pass
        for i in itme_name :
            if not i in list_name:
                item = QListWidgetItem(i)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.ui.listWidget.addItem(item)

    # ----------------------------------------------------------------------------------------------------------

    # ??????[????????????]??????????????????
    # ???????????????
    def backstage_file_name_U(self):
        path = r"config\customize\\backstage_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # ?????????????????????lambda???????????????????????????????????????????????????????????????
            # os.path.getmtime() ???????????????????????????????????????
            # os.path.getctime() ???????????????????????????????????????
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_backstage(list_U_N)

    # ??????????????????
    def load_user_file_backstage(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '????????????????????????':
                    pass
                else:
                    list_name.append(name)
        except Exception:
            pass
        for i in itme_name :
            if not i in list_name:
                item = QListWidgetItem(i)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.ui.listWidget.addItem(item)


#   --------------------------------------------------??????--????????????--?????????-----------------------------------

    # ??????????????????
    def mouse_position(self):
        if selective_type == 'mouse' :
            self.ui.label_9.show()
            self.ui.lineEdit3.show()
            self.ui.lineEdit3.setReadOnly(True)
            self.ui.label_9.setText('????????????:')
            try:
                while True:
                    ui_show = self.isActiveWindow()
                    # ??????????????????
                    x, y = pa.position()  
                    self.ui.lineEdit3.setText(str(x)+','+str(y))
                    time.sleep(0.1)  
                    if selective_type == 'backstage' :
                        self.ui.label_9.hide()
                        self.ui.lineEdit3.hide()
                        break
                    if selective_type != 'mouse' or ui_show != True :
                        break
            except Exception:
                pass
    
    # ???????????????
    def key_name(self):
        print(key_name)
        if selective_type == 'key' :
            self.ui.label_9.show()
            self.ui.lineEdit3.show()
            self.ui.lineEdit3.setReadOnly(False)
            self.ui.label_9.setText('?????????:')
            self.ui.lineEdit3.setText(key_name)
            try:
                while True:
                    ui_show = self.isActiveWindow()
                    text = self.ui.lineEdit3.text()
                    if text == key_name :
                        pass
                    if text != key_name :
                        self.ui.lineEdit3.clear()
                        self.ui.lineEdit3.setText(key_name)
                    time.sleep(0.1)  
                    if selective_type == 'backstage' :
                        self.ui.label_9.hide()
                        self.ui.lineEdit3.hide()
                        break
                    if selective_type != 'key' or ui_show != True :
                        break
            except Exception:
                pass


#   --------------------------------------------------????????????-------------------------------------------------
    
    # ?????????
    def shortcut(self,key):
        global save_fast1 ,save_fast2
        # ??????????????????????????????
        ui_show = self.isActiveWindow()
        if ui_show == True :

            # ???????????????
            if key == 'Delete':
                self.DeleteItem()

            # ???????????????
            if key == 'Lcontrol':
                save_fast1 = 1
            if key == 'S':
                save_fast2 = 1
            if save_fast1 == 1 and save_fast2 == 1 :
                self.save_file()
                save_fast1 = 0
                save_fast2 = 0
        else:
            if key == 'F1':
                self.startAndStop(True)
            if key == 'F2':
                self.startAndStop(False)
    
    # ???????????????
    def startAndStop(self,star_bool):
        global dict_text_key , switch_key
        title = self.ui.label_5.text()
        if title == '????????????????????????' or title == '????????????????????????' or title == '????????????????????????' :
            dict_text_key = 0
            switch_key = 0
        else:
            switch_key = 1
            if star_bool == True :
                text = self.ui.plainTextEdit.toPlainText()
                text1 = text.replace('???' , ':')
                text2 = text1.replace('???' , ',')
                text3 = text2.replace("???" , "'")
                text4 = text3.replace("???" , "'")
                text5 = text4.replace('??????','??????')
                dict_text_key = ast.literal_eval(text5)
                print(dict_text_key)
            else:
                dict_text_key = 0
                switch_key = 0


    # -------------------------------------------------------------------------------------------------------

    # ????????????
    def Multi_Click_mouse(self,data):
        try:
            coordinate = data['??????'].split(',')
            for i in coordinate :
                print(i)
                if i[0:2] == '??????' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                else:
                    coord = i.split(' ')
                    print(coord)
                    pa.click(int(coord[0]),int(coord[1]))

        except Exception:
            self.Qlabel_11('????????????????????????')

    
    # ??????
    def slide_mouse(self,data):
        try:
            coordinate = data['??????'].split(',')
            coord1 = coordinate[0].split(' ')
            coord2 = coordinate[1].split(' ')
            pa.moveTo(int(coord1[0]),int(coord1[1]))
            # time.sleep(1)
            pa.dragTo(int(coord2[0]),int(coord2[1]),float(data['??????']))

        except Exception:
            self.Qlabel_11('????????????????????????')

    # -------------------------------------------------------------------------------------------------------
    
    # ??????
    def continuous_key(self,data):
        global key_bool
        try:
            while True:
                if key_bool == 1:
                    win32api.keybd_event(key_code[data['?????????']],0,0,0)
                    time.sleep(round(1/int(data['????????????']),3))
                    win32api.keybd_event(key_code[data['?????????']],0,win32con.KEYEVENTF_KEYUP,0)
                else:
                    break

        except Exception:
            self.Qlabel_11('????????????????????????')

    # ???
    def magnificent_key(self,data):
        try:
            instruct = data['?????????'].split(',')
            for i in instruct :
                if i[0:2] == '??????' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                else:
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)
                    
        except Exception:
            self.Qlabel_11('????????????????????????')

    # ?????????
    def advanced_magnificent_key(self,data):
        try:
            instruct = data['?????????'].split(',')
            for i in instruct :
                if i[0:2] == '??????' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                if i[0:2] == '??????' :
                    press = i.split(' ') 
                    win32api.keybd_event(key_code[press[1]],0,0,0)
                if i[0:2] == '??????' :
                    bounce = i.split(' ')
                    win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)
                if i[0:2] != '??????' and i[0:2] != '??????' and i[0:2] != '??????':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('????????????????????????')

    # ??????
    def circulate(self,data,circulates):
        global switch_key
        try:
            if circulates == 0 :
                pass
            else :
                instruct = data['?????????'].split(',')
                for i in instruct :
                    if i[0:2] == '??????' :
                        delay = i.split(' ')
                        time.sleep(float(delay[1]))
                    if i[0:2] == '??????' :
                        press = i.split(' ') 
                        win32api.keybd_event(key_code[press[1]],0,0,0)
                    if i[0:2] == '??????' :
                        bounce = i.split(' ')
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)
                    if i[0:2] != '??????' and i[0:2] != '??????' and i[0:2] != '??????':
                        win32api.keybd_event(key_code[i],0,0,0)
                        time.sleep(0.07)
                        win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)
            
            if circulates != -1 and circulates != 0 :
                if switch_key == 0:
                    circulates = 0
                circulates = circulates - 1
                self.circulate(data,circulates)
            if circulates == -1 :
                if switch_key == 0:
                    circulates = 0
                self.circulate(data,circulates)

        except Exception:
            self.Qlabel_11('????????????????????????')

    # ?????????
    def catapult(self,data,direction,Ndirection):
        try:
            instruct = data['?????????'].split(',')
            for i in instruct :

                if i[0:2] == '??????' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))

                if i[0:2] == '??????' :
                    press = i.split(' ') 
                    if press[1] == '??????' :
                        win32api.keybd_event(key_code[direction],0,0,0)
                    if press[1] == '?????????' :
                        win32api.keybd_event(key_code[Ndirection],0,0,0)
                    if press[1] != '??????' and press[1] != '?????????' :
                        win32api.keybd_event(key_code[press[1]],0,0,0)

                if i[0:2] == '??????' :
                    bounce = i.split(' ')
                    if bounce[1] == '??????' :
                        win32api.keybd_event(key_code[direction],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] == '?????????' :
                        win32api.keybd_event(key_code[Ndirection],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] != '??????' and bounce[1] != '?????????' :
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)

                if i[0:2] != '??????' and i[0:2] != '??????' and i[0:2] != '??????':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('????????????????????????')

    # ?????????
    def mappings(self,data,direction,mapping,Ndirection,Nmapping):
        try:
            instruct = data['?????????'].split(',')
            for i in instruct :

                if i[0:2] == '??????' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))

                if i[0:2] == '??????' :
                    press = i.split(' ') 
                    if press[1] == '??????' or press[1] == '??????' or press[1] == '?????????' or press[1] == '?????????' :
                        if press[1] == '??????' :
                            win32api.keybd_event(key_code[direction],0,0,0)
                        if press[1] == '?????????' :
                            win32api.keybd_event(key_code[Ndirection],0,0,0)
                        if press[1] == '??????' :
                            win32api.keybd_event(key_code[mapping],0,0,0)
                        if press[1] == '?????????' :
                            win32api.keybd_event(key_code[Nmapping],0,0,0)
                    if press[1] != '??????' and press[1] != '??????' and press[1] != '?????????' and press[1] != '?????????' : 
                        win32api.keybd_event(key_code[press[1]],0,0,0)

                if i[0:2] == '??????' :
                    bounce = i.split(' ')
                    if bounce[1] == '??????' or bounce[1] == '??????' or bounce[1] == '?????????' or bounce[1] == '?????????' :
                        if bounce[1] == '??????' :
                            win32api.keybd_event(key_code[direction],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '?????????' :
                            win32api.keybd_event(key_code[Ndirection],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '??????' :
                            win32api.keybd_event(key_code[mapping],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '?????????' :
                            win32api.keybd_event(key_code[Nmapping],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] != '??????' and bounce[1] != '??????' and bounce[1] != '?????????' and bounce[1] != '?????????': 
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)

                if i[0:2] != '??????' and i[0:2] != '??????' and i[0:2] != '??????':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('????????????????????????')

    # -------------------------------------------------------------------------------------------------------

    # ??????????????????
    def KeyDown(self,event):
        global key_bool , trigger , left , right , circulates
        key = str(event.Key)

        if switch_key == 1 :
            for i in dict_text_key :
                if '????????????' in i and selective_type == 'key':

                    if i['????????????'] == '??????' :
                        if key == i['?????????'] :
                            key_bool = 1
                            T3 = td.Thread(target=self.continuous_key , args=(i,))
                            T3.start()

                    if i['????????????'] == '???' :
                        if key == i['?????????'] :
                            T4 = td.Thread(target=self.magnificent_key , args=(i,))
                            T4.start()

                    if i['????????????'] == '?????????' :
                        if key == i['?????????'] :
                            T9 = td.Thread(target=self.advanced_magnificent_key , args=(i,))
                            T9.start()

                    if i['????????????'] == '??????' :
                        if key == i['?????????'] :
                            circulates = int(i['????????????'])
                            if circulates != -1 and circulates != 0 and circulates != 1 :
                                circulates = circulates - 1
                            T12 = td.Thread(target=self.circulate , args=(i,circulates))
                            T12.start()

                    if i['????????????'] == '?????????' :
                        if key == i['?????????'] :
                            left = 1
                            right = 0
                        if key == i['?????????'] :
                            right = 1
                            left = 0
                        if key == i['?????????'] :
                            trigger = 1
                            if trigger == 1 and left == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T10 = td.Thread(target=self.catapult , args=(i,i['?????????'],i['?????????']))
                                T10.start()
                            if trigger == 1 and right == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T11 = td.Thread(target=self.catapult , args=(i,i['?????????'],i['?????????']))
                                T11.start()

                    if i['????????????'] == '?????????' :
                        if key == i['?????????'] :
                            left = 1
                            right = 0
                        if key == i['?????????'] :
                            right = 1
                            left = 0
                        if key == i['?????????'] :
                            trigger = 1
                            if trigger == 1 and left == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T10 = td.Thread(target=self.mappings , args=(i,i['?????????'],i['?????????'],i['?????????'],i['?????????']))
                                T10.start()
                            if trigger == 1 and right == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T11 = td.Thread(target=self.mappings , args=(i,i['?????????'],i['?????????'],i['?????????'],i['?????????']))
                                T11.start()


                if '????????????' in i and selective_type == 'mouse':

                    if i['????????????'] == '????????????' :
                        if key == i['?????????'] :
                            T5 = td.Thread(target=self.Multi_Click_mouse , args=(i,))
                            T5.start()

                    if i['????????????'] == '??????' :
                        if key == i['?????????'] :
                            T6 = td.Thread(target=self.slide_mouse , args=(i,))
                            T6.start()
        else:
            pass
        return True


    # ??????????????????
    def KeyUp(self,event):
        global key_bool , key_name , key
        key = str(event.Key)
        key_name = key
        print(key)
        if switch_key == 1 :
            for i in dict_text_key :
                if '????????????' in i and selective_type == 'key':
                    if i['????????????'] == '??????' :
                        if key == i['?????????'] :
                            key_bool = 0
        
        # ?????????????????????
        if key == 'Delete' or key == 'Lcontrol' or key == 'S' or key == 'F1' or key == 'F2' :
            self.shortcut(key)
        return True


    # ????????????
    def KeyHook(self):
        # ?????????????????????
        hm = pyWinhook.HookManager()
        # ??????????????????
        hm.KeyDown = self.KeyDown
        # ??????????????????
        hm.KeyUp = self.KeyUp
        # ??????????????????
        hm.HookKeyboard()



if __name__=='__main__':
    # ????????? PySide6 ???????????????????????????????????????
    app = QApplication([])
    ui = app.setWindowIcon(QIcon(r'UI\logo.png'))

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "????????????", "?????????????????????????????????")
        sys.exit(1)
    QApplication.setQuitOnLastWindowClosed(False)  # ???????????????????????????????????????

    Main_Window = Main_Window()
    Main_Window.show()
    sys.exit(app.exec_())


