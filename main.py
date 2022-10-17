

import sys ,os ,time ,ast
import win32api, win32con, pyWinhook
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pyautogui as pa
import threading as td

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


# 创建主窗口
class Main_Window(QWidget):

    def __init__(self):

        # 从文件中加载UI定义
        super(Main_Window, self).__init__()
        Main_ui = QFile(r'UI\MainWindow.ui')
        Main_ui.open(QFile.ReadOnly)
        Main_ui.close()
        # 读取UI文件
        self.ui = QUiLoader().load(Main_ui)

        # 设置文本编辑框为只读
        self.ui.plainTextEdit.setReadOnly(True)
        # 设置X按钮为隐藏
        self.ui.Button3.hide()
        self.ui.Button3.clicked.connect(self.B3_hide)
        # 设置标题标签为隐藏
        self.ui.label_5.hide()
        self.ui.label_9.hide()
        self.ui.lineEdit3.hide()
        # 设置提示标签为隐藏
        self.ui.label_11.hide()

        
        # 加载 启动停止快捷键(前台)
        self.ui.lineEdit1.setText('F1')
        self.ui.lineEdit2.setText('F2')
        self.ui.lineEdit1.setReadOnly(True)
        self.ui.lineEdit2.setReadOnly(True)
        self.ui.Button1.setShortcut('F1')
        self.ui.Button2.setShortcut('F2')


        # 启动和停止
        self.ui.Button1.clicked.connect(lambda:self.startAndStop(True))
        self.ui.Button2.clicked.connect(lambda:self.startAndStop(False))

        # 托盘部分
        self._restore_action = None
        self._quit_action = None
        self._tray_icon = None
        self._tray_icon_menu = None
        self.setup_ui()

        # 默认加载[键盘控制]菜单
        # t2 = td.Thread(target=self.key_file_name)
        # t2.start()
        # t2.join()
        # self.key_file_name_U()

        # 启动键盘监听
        self.KeyHook()

        #开启多选模式
        # self.ui.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # 双击事件
        self.ui.listWidget.doubleClicked.connect(self.RenameItem)  #双击事件

        # 右键菜单
        # 需要在编辑器中把 contextMenuPolicy 属性设置为 CustomContextMenu
        # self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listWidget.customContextMenuRequested.connect(self.myListWidgetContext)
        self.ui.plainTextEdit.customContextMenuRequested.connect(self.myPlainTextEditContext)

        # 主菜单事件
        self.ui.listWidget_2.itemClicked.connect(self.pos_Menu)


#   --------------------------------------------------控件功能-------------------------------------------------

    # 设置X按钮为隐藏
    def B3_hide(self):
        global save_path
        self.save_file()
        self.ui.Button3.hide()
        self.ui.label_5.hide()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.setReadOnly(True)
        save_path = 0


    # 提示标签功能
    def Qlabel_11(self,content):
        self.startAndStop(False)
        self.ui.label_11.show()
        self.ui.label_11.setText(content)
        time.sleep(3)
        self.ui.label_11.hide()

        # 加载 启动停止快捷键
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


#   --------------------------------------------------右键菜单-------------------------------------------------

    def myListWidgetContext(self,position):
        #弹出菜单
        popMenu = QMenu()
        open_file =QAction('打开项目', self)
        creAct =QAction("新建项目",self)
        delAct =QAction("删除项目",self)
        renameAct =QAction('重命名', self)
        #查看右键时是否在item上面,如果不在.就不显示打开、删除、修改.
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

    # 打开项目
    def open_file(self):
        global save_path
        # 设置文本编辑框为非只读
        self.ui.plainTextEdit.setReadOnly(False)
        # 设置X按钮为显示
        self.ui.Button3.show()
        # 设置标题标签为显示
        self.ui.label_5.show()
        name = self.ui.listWidget.currentItem().text()
        self.ui.label_5.setText(name)

        if selective_type == 'key' and name != '键盘控制使用说明':
            path = r'config\customize\Key_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'key' and name == '键盘控制使用说明':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)

        if selective_type == 'mouse' and name != '鼠标控制使用说明':
            path = r'config\customize\Mouse_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'mouse' and name == '鼠标控制使用说明':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)

        if selective_type == 'backstage' and name != '后台控制使用说明':
            path = r'config\customize\backstage_control'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
        if selective_type == 'backstage' and name == '后台控制使用说明':
            path = r'config\original'
            with open(path + '\\' + name + '.txt', 'r' , encoding='utf-8') as f :
                save_path = path + '\\' + name + '.txt'
                content = f.read()
                self.ui.plainTextEdit.clear()
                self.ui.plainTextEdit.appendPlainText(content)
                # 光标移动到文本开头
                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)
                self.ui.plainTextEdit.setTextCursor(cursor)
    

    # 新建项目
    def CreateNewItem(self):
        global n
    	#创建一个默认名字的item
        name = '新建项目'
        list_name = []
        try:
            for i in range(999):
                exist_name = self.ui.listWidget.item(i).text()
                list_name.append(exist_name)
        except Exception:
            while True:
                if name in list_name:
                    name = '新建项目'
                    n = n + 1
                    name = name + str(n)
                else:
                    break

        item = QListWidgetItem(name)
        item.setTextAlignment(Qt.AlignCenter)
        #使得item是可以编辑的.
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.listWidget.addItem(item)
        #创建后就可以编辑item,用户自己起名字.
        # self.ui.listWidget.editItem(item)

        if selective_type == 'key':
            with open(r'config\customize\Key_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '新建项目'
                n = 0
        if selective_type == 'mouse':
            with open(r'config\customize\Mouse_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '新建项目'
                n = 0
        if selective_type == 'backstage':
            with open(r'config\customize\backstage_control\%s.txt' % name,'w+',encoding='utf-8') as f:
                name = '新建项目'
                n = 0


    #删除项目
    def DeleteItem(self):
        global save_path
        if selective_type == 'key':
            # 获取选中项的名称
            name = self.ui.listWidget.currentItem().text()
            # 判断文件是否存在
            isfile = os.path.isfile(r'config\customize\Key_control\%s.txt' % name)
            if isfile == True:
                # 删除文件
                os.remove(r'config\customize\Key_control\%s.txt' % name)
                # 删除项目
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('找不到文件')

        if selective_type == 'mouse':
            name = self.ui.listWidget.currentItem().text()
            isfile = os.path.isfile(r'config\customize\Mouse_control\%s.txt' % name)
            if isfile == True:
                os.remove(r'config\customize\Mouse_control\%s.txt' % name)
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('找不到文件')

        if selective_type == 'backstage':
            name = self.ui.listWidget.currentItem().text()
            isfile = os.path.isfile(r'config\customize\backstage_control\%s.txt' % name)
            if isfile == True:
                os.remove(r'config\customize\backstage_control\%s.txt' % name)
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
                save_path = 0
            else:
                self.Qlabel_11('找不到文件')


    #重命名
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


    # 保存文件
    def myPlainTextEditContext(self,position):
        popMenu = QMenu()
        save_file =QAction('保存', self)
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


#   --------------------------------------------------托盘功能-------------------------------------------------


    def setup_ui(self):
        # 创建托盘
        self.create_actions()
        self.create_tray_icon()

    def create_actions(self):

        self._restore_action = QAction("显示主界面")
        self._restore_action.triggered.connect(self.ui.showNormal)

        self._quit_action = QAction("退出")
        self._quit_action.triggered.connect(app.quit)

    def create_tray_icon(self):
        self._tray_icon_menu = QMenu()
        self._tray_icon_menu.addAction(self._restore_action)
        # 添加分隔符
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)
        # 设置托盘图标
        self._tray_icon = QSystemTrayIcon()
        self._tray_icon.setIcon(QIcon(r'UI\logo.png'))
        self._tray_icon.setContextMenu(self._tray_icon_menu)
        # 在系统托盘显示此对象
        self._tray_icon.show()

        # 双击显示
        self._tray_icon.activated[QSystemTrayIcon.ActivationReason].connect(self.iconActivated)

    def iconActivated(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self._tray_icon.isVisible():
                self.ui.showNormal()
            else:
                self.hide()


#   --------------------------------------------------主菜单功能--加载默认文件----------------------------------

    # 菜单定位
    def pos_Menu(self,Index):
        global selective_type
        pos_name = self.ui.listWidget_2.item(self.ui.listWidget_2.row(Index)).text()
        if pos_name == '键盘控制':
            selective_type = 'key'
            self.key_file_name()
            self.key_file_name_U()
            self.B3_hide()
            # 按键名检测
            T8 = td.Thread(target=self.key_name)
            T8.setDaemon(True)
            T8.start()
        if pos_name == '鼠标控制':
            selective_type = 'mouse'
            self.mouse_file_name()
            self.mouse_file_name_U()
            self.B3_hide()
            # 实时检测鼠标位置
            T7 = td.Thread(target=self.mouse_position)
            T7.setDaemon(True)
            T7.start()
        if pos_name == '后台控制':
            selective_type = 'backstage'
            self.backstage_file_name()
            self.backstage_file_name_U()
            self.B3_hide()

    # 点击[键盘控制]按钮执行配置
    # 读取文件名
    def key_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '键盘控制使用说明.txt':
                i_split = i.split('.')
                self.key_defaultLoad(i_split[0])

    # 加载默认文件
    def key_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '键盘控制使用说明':
                    flag = 1
                    break
                if lise_name == '鼠标控制使用说明':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '后台控制使用说明':
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

    # 点击[鼠标控制]按钮执行配置
    # 读取文件名
    def mouse_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '鼠标控制使用说明.txt':
                i_split = i.split('.')
                self.mouse_defaultLoad(i_split[0])

    # 加载默认文件
    def mouse_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '鼠标控制使用说明':
                    flag = 1
                    break
                if lise_name == '键盘控制使用说明':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '后台控制使用说明':
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

    # 点击[后台控制]按钮执行配置
    # 读取文件名
    def backstage_file_name(self):
        self.ui.listWidget.clear()
        path = r"config\original"
        datanames = os.listdir(path)
        for i in datanames:
            if i == '后台控制使用说明.txt':
                i_split = i.split('.')
                self.backstage_defaultLoad(i_split[0])

    # 加载默认文件
    def backstage_defaultLoad(self,name):
        try:
            for i in range(100):
                lise_name = self.ui.listWidget.item(0).text()
                if lise_name == '后台控制使用说明':
                    flag = 1
                    break
                if lise_name == '键盘控制使用说明':
                    self.ui.listWidget.takeItem(i)
                    continue
                if lise_name == '鼠标控制使用说明':
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


#   --------------------------------------------------主菜单功能--加载用户文件----------------------------------

    # 点击[键盘控制]按钮执行配置
    # 读取文件名
    def key_file_name_U(self):
        path = r"config\customize\Key_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后创建时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_key(list_U_N)

    # 加载用户文件
    def load_user_file_key(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '键盘控制使用说明':
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

    # 点击[鼠标控制]按钮执行配置
    # 读取文件名
    def mouse_file_name_U(self):
        path = r"config\customize\Mouse_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后创建时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_mouse(list_U_N)

    # 加载用户文件
    def load_user_file_mouse(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '鼠标控制使用说明':
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

    # 点击[后台控制]按钮执行配置
    # 读取文件名
    def backstage_file_name_U(self):
        path = r"config\customize\\backstage_control"
        datanames = os.listdir(path)
        list_U_N = []
        if not datanames:
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后创建时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            datanames = sorted(datanames,key=lambda x: os.path.getctime(os.path.join(path, x)))
        for i in datanames:
            i_split = i.split('.')
            list_U_N.append(i_split[0])
        self.load_user_file_backstage(list_U_N)

    # 加载用户文件
    def load_user_file_backstage(self,itme_name):
        # print(itme_name)
        list_name = []
        try:
            for i in range(100):
                name = self.ui.listWidget.item(i).text()
                if name == '后台控制使用说明':
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


#   --------------------------------------------------检测--鼠标位置--按键名-----------------------------------

    # 检测鼠标位置
    def mouse_position(self):
        if selective_type == 'mouse' :
            self.ui.label_9.show()
            self.ui.lineEdit3.show()
            self.ui.lineEdit3.setReadOnly(True)
            self.ui.label_9.setText('鼠标位置:')
            try:
                while True:
                    ui_show = self.ui.isActiveWindow()
                    # 获取鼠标位置
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
    
    # 检测按键名
    def key_name(self):
        print(key_name)
        if selective_type == 'key' :
            self.ui.label_9.show()
            self.ui.lineEdit3.show()
            self.ui.lineEdit3.setReadOnly(False)
            self.ui.label_9.setText('按键名:')
            self.ui.lineEdit3.setText(key_name)
            try:
                while True:
                    ui_show = self.ui.isActiveWindow()
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


#   --------------------------------------------------键盘功能-------------------------------------------------
    
    # 快捷键
    def shortcut(self,key):
        global save_fast1 ,save_fast2
        # 检测窗口是否处于前台
        ui_show = self.ui.isActiveWindow()
        if ui_show == True :

            # 删除快捷键
            if key == 'Delete':
                self.DeleteItem()

            # 保存快捷键
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
    
    # 启动和停止
    def startAndStop(self,star_bool):
        global dict_text_key , switch_key
        title = self.ui.label_5.text()
        if title == '键盘控制使用说明' or title == '鼠标控制使用说明' or title == '后台控制使用说明' :
            dict_text_key = 0
            switch_key = 0
        else:
            switch_key = 1
            if star_bool == True :
                text = self.ui.plainTextEdit.toPlainText()
                text1 = text.replace('：' , ':')
                text2 = text1.replace('，' , ',')
                text3 = text2.replace("‘" , "'")
                text4 = text3.replace("’" , "'")
                text5 = text4.replace('延时','延迟')
                dict_text_key = ast.literal_eval(text5)
                print(dict_text_key)
            else:
                dict_text_key = 0
                switch_key = 0


    # -------------------------------------------------------------------------------------------------------

    # 多点点击
    def Multi_Click_mouse(self,data):
        try:
            coordinate = data['坐标'].split(',')
            for i in coordinate :
                print(i)
                if i[0:2] == '延迟' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                else:
                    coord = i.split(' ')
                    print(coord)
                    pa.click(int(coord[0]),int(coord[1]))

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    
    # 滑动
    def slide_mouse(self,data):
        try:
            coordinate = data['坐标'].split(',')
            coord1 = coordinate[0].split(' ')
            coord2 = coordinate[1].split(' ')
            pa.moveTo(int(coord1[0]),int(coord1[1]))
            # time.sleep(1)
            pa.dragTo(int(coord2[0]),int(coord2[1]),float(data['用时']))

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # -------------------------------------------------------------------------------------------------------
    
    # 连击
    def continuous_key(self,data):
        global key_bool
        try:
            while True:
                if key_bool == 1:
                    win32api.keybd_event(key_code[data['连击键']],0,0,0)
                    time.sleep(round(1/int(data['每秒次数']),3))
                    win32api.keybd_event(key_code[data['连击键']],0,win32con.KEYEVENTF_KEYUP,0)
                else:
                    break

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # 宏
    def magnificent_key(self,data):
        try:
            instruct = data['宏指令'].split(',')
            for i in instruct :
                if i[0:2] == '延迟' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                else:
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)
                    
        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # 高级宏
    def advanced_magnificent_key(self,data):
        try:
            instruct = data['宏指令'].split(',')
            for i in instruct :
                if i[0:2] == '延迟' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))
                if i[0:2] == '按下' :
                    press = i.split(' ') 
                    win32api.keybd_event(key_code[press[1]],0,0,0)
                if i[0:2] == '弹起' :
                    bounce = i.split(' ')
                    win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)
                if i[0:2] != '延迟' and i[0:2] != '按下' and i[0:2] != '弹起':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # 循环
    def circulate(self,data,circulates):
        global switch_key
        try:
            if circulates == 0 :
                pass
            else :
                instruct = data['宏指令'].split(',')
                for i in instruct :
                    if i[0:2] == '延迟' :
                        delay = i.split(' ')
                        time.sleep(float(delay[1]))
                    if i[0:2] == '按下' :
                        press = i.split(' ') 
                        win32api.keybd_event(key_code[press[1]],0,0,0)
                    if i[0:2] == '弹起' :
                        bounce = i.split(' ')
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)
                    if i[0:2] != '延迟' and i[0:2] != '按下' and i[0:2] != '弹起':
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
            self.Qlabel_11('数据错误，请检查')

    # 组合键
    def catapult(self,data,direction,Ndirection):
        try:
            instruct = data['宏指令'].split(',')
            for i in instruct :

                if i[0:2] == '延迟' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))

                if i[0:2] == '按下' :
                    press = i.split(' ') 
                    if press[1] == '方向' :
                        win32api.keybd_event(key_code[direction],0,0,0)
                    if press[1] == '反方向' :
                        win32api.keybd_event(key_code[Ndirection],0,0,0)
                    if press[1] != '方向' and press[1] != '反方向' :
                        win32api.keybd_event(key_code[press[1]],0,0,0)

                if i[0:2] == '弹起' :
                    bounce = i.split(' ')
                    if bounce[1] == '方向' :
                        win32api.keybd_event(key_code[direction],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] == '反方向' :
                        win32api.keybd_event(key_code[Ndirection],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] != '方向' and bounce[1] != '反方向' :
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)

                if i[0:2] != '延迟' and i[0:2] != '按下' and i[0:2] != '弹起':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # 映射键
    def mappings(self,data,direction,mapping,Ndirection,Nmapping):
        try:
            instruct = data['宏指令'].split(',')
            for i in instruct :

                if i[0:2] == '延迟' :
                    delay = i.split(' ')
                    time.sleep(float(delay[1]))

                if i[0:2] == '按下' :
                    press = i.split(' ') 
                    if press[1] == '方向' or press[1] == '映射' or press[1] == '反方向' or press[1] == '反映射' :
                        if press[1] == '方向' :
                            win32api.keybd_event(key_code[direction],0,0,0)
                        if press[1] == '反方向' :
                            win32api.keybd_event(key_code[Ndirection],0,0,0)
                        if press[1] == '映射' :
                            win32api.keybd_event(key_code[mapping],0,0,0)
                        if press[1] == '反映射' :
                            win32api.keybd_event(key_code[Nmapping],0,0,0)
                    if press[1] != '方向' and press[1] != '映射' and press[1] != '反方向' and press[1] != '反映射' : 
                        win32api.keybd_event(key_code[press[1]],0,0,0)

                if i[0:2] == '弹起' :
                    bounce = i.split(' ')
                    if bounce[1] == '方向' or bounce[1] == '映射' or bounce[1] == '反方向' or bounce[1] == '反映射' :
                        if bounce[1] == '方向' :
                            win32api.keybd_event(key_code[direction],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '反方向' :
                            win32api.keybd_event(key_code[Ndirection],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '映射' :
                            win32api.keybd_event(key_code[mapping],0,win32con.KEYEVENTF_KEYUP,0)
                        if bounce[1] == '反映射' :
                            win32api.keybd_event(key_code[Nmapping],0,win32con.KEYEVENTF_KEYUP,0)
                    if bounce[1] != '方向' and bounce[1] != '映射' and bounce[1] != '反方向' and bounce[1] != '反映射': 
                        win32api.keybd_event(key_code[bounce[1]],0,win32con.KEYEVENTF_KEYUP,0)

                if i[0:2] != '延迟' and i[0:2] != '按下' and i[0:2] != '弹起':
                    win32api.keybd_event(key_code[i],0,0,0)
                    time.sleep(0.07)
                    win32api.keybd_event(key_code[i],0,win32con.KEYEVENTF_KEYUP,0)

        except Exception:
            self.Qlabel_11('数据错误，请检查')

    # -------------------------------------------------------------------------------------------------------

    # 获得按下的键
    def KeyDown(self,event):
        global key_bool , trigger , left , right , circulates
        key = str(event.Key)

        if switch_key == 1 :
            for i in dict_text_key :
                if '按键类型' in i and selective_type == 'key':

                    if i['按键类型'] == '连击' :
                        if key == i['触发键'] :
                            key_bool = 1
                            T3 = td.Thread(target=self.continuous_key , args=(i,))
                            T3.start()

                    if i['按键类型'] == '宏' :
                        if key == i['触发键'] :
                            T4 = td.Thread(target=self.magnificent_key , args=(i,))
                            T4.start()

                    if i['按键类型'] == '高级宏' :
                        if key == i['触发键'] :
                            T9 = td.Thread(target=self.advanced_magnificent_key , args=(i,))
                            T9.start()

                    if i['按键类型'] == '循环' :
                        if key == i['触发键'] :
                            circulates = int(i['循环次数'])
                            if circulates != -1 and circulates != 0 and circulates != 1 :
                                circulates = circulates - 1
                            T12 = td.Thread(target=self.circulate , args=(i,circulates))
                            T12.start()

                    if i['按键类型'] == '组合键' :
                        if key == i['左方向'] :
                            left = 1
                            right = 0
                        if key == i['右方向'] :
                            right = 1
                            left = 0
                        if key == i['触发键'] :
                            trigger = 1
                            if trigger == 1 and left == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T10 = td.Thread(target=self.catapult , args=(i,i['左方向'],i['右方向']))
                                T10.start()
                            if trigger == 1 and right == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T11 = td.Thread(target=self.catapult , args=(i,i['右方向'],i['左方向']))
                                T11.start()

                    if i['按键类型'] == '映射键' :
                        if key == i['左方向'] :
                            left = 1
                            right = 0
                        if key == i['右方向'] :
                            right = 1
                            left = 0
                        if key == i['触发键'] :
                            trigger = 1
                            if trigger == 1 and left == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T10 = td.Thread(target=self.mappings , args=(i,i['左方向'],i['左映射'],i['右方向'],i['右映射']))
                                T10.start()
                            if trigger == 1 and right == 1 :
                                left = 0
                                right = 0
                                trigger = 0
                                T11 = td.Thread(target=self.mappings , args=(i,i['右方向'],i['右映射'],i['左方向'],i['左映射']))
                                T11.start()


                if '鼠标类型' in i and selective_type == 'mouse':

                    if i['鼠标类型'] == '多点点击' :
                        if key == i['触发键'] :
                            T5 = td.Thread(target=self.Multi_Click_mouse , args=(i,))
                            T5.start()

                    if i['鼠标类型'] == '滑动' :
                        if key == i['触发键'] :
                            T6 = td.Thread(target=self.slide_mouse , args=(i,))
                            T6.start()
        else:
            pass
        return True


    # 获得松开的键
    def KeyUp(self,event):
        global key_bool , key_name , key
        key = str(event.Key)
        key_name = key
        print(key)
        if switch_key == 1 :
            for i in dict_text_key :
                if '按键类型' in i and selective_type == 'key':
                    if i['按键类型'] == '连击' :
                        if key == i['触发键'] :
                            key_bool = 0
        
        # 调用快捷键函数
        if key == 'Delete' or key == 'Lcontrol' or key == 'S' or key == 'F1' or key == 'F2' :
            self.shortcut(key)
        return True


    # 键盘监听
    def KeyHook(self):
        # 实例化监听对象
        hm = pyWinhook.HookManager()
        # 监听按下的键
        hm.KeyDown = self.KeyDown
        # 监听松开的键
        hm.KeyUp = self.KeyUp
        # 设置键盘钩子
        hm.HookKeyboard()



if __name__=='__main__':
    # 每一个 PySide6 应用都必须创建一个应用对象
    app = QApplication([])
    ui = app.setWindowIcon(QIcon(r'UI\logo.png'))

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "系统托盘", "本系统检测不出系统托盘")
        sys.exit(1)
    QApplication.setQuitOnLastWindowClosed(False)  # 关闭最后一个窗口不退出程序

    Main_Window = Main_Window()
    Main_Window.ui.show()
    sys.exit(app.exec_())


