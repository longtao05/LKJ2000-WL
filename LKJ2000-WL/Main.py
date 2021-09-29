
#encoding:utf-8
#系统库导入
import sys
import os
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
import binascii
import time
import threading
import os,inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
#模块导入
sys.path.append(r".\Graphic")
sys.path.append(r".\BusinessManager")
sys.path.append(r".\Comm")
sys.path.append(r".\DataManager")
sys.path.append(r".\LogSys")
sys.path.append(r".\Common")
sys.path.append(r".\SysDataPreProc")

import Mygol
import MyFilegol
import FileHandle
import ConfigHandle
from DataBase import DataBase
from SockCanData import SockCanData
from SerialPortData import SerialPortData
from CanData import CanData
import Login
import STPMain

from BusinessProcess import BusinessProcess
from DataProcessMgr import DataProcess

global commType
commType = DataBase()

class ReadThread(QThread): # 建立一个任务线程类

    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(ReadThread, self).__init__()

    def run(self): # 在启动线程后任务从这个函数里面开始执行
        print("ReadThread") # 调用传递过来的数据
        while(True):
            DataProcess.OnreadData(self,commType)

  
        #Mygol.set_value('FuncType','STP')
        # datarecvtask = threading.Thread(target=self.DataRecvProcessTask)
        # datarecvtask.setDaemon(True)
        # datarecvtask.start()

        # #数据发送线程
        # datasendtask = threading.Thread(target=self.DataSendProcessTask)
        # datasendtask.setDaemon(True)
        # datasendtask.start()


        # #任务管理线程
        # businessTask = threading.Thread(target=self.businessTask.OnBusinessProcess)
        # businessTask.setDaemon(True)
        # businessTask.start()
class SendThread(QThread): # 建立一个任务线程类
    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(SendThread, self).__init__()

    def run(self): # 在启动线程后任务从这个函数里面开始执行
        print("SendThread") # 调用传递过来的数据
        while(True):
            DataProcess.OnsendData(self,commType)
class BusinessThread(QThread): # 建立一个任务线程类
    signal = pyqtSignal(str) #设置触发信号传递的参数数据类型,这里是字符串
    def __init__(self):
        super(BusinessThread, self).__init__()

    def run(self): # 在启动线程后任务从这个函数里面开始执行
        print("BusinessThread") # 调用传递过来的数据
        bustask = BusinessProcess()
        while(True):
            bustask.OnBusinessProcess()
        
class Main(Login.Login):
    def __init__(self,parent=None,name = "调试工具"):
        #构造函数
        super().__init__(parent)
        #全局变量字典定义
        Mygol._init()
        # Mygol.set_value('FuncType','STP')
        MyFilegol._init()
        #读取配置信息至全局变量

        FileHandle.readMyfile()
        ConfigHandle.readConfig()
        self.businessTask = BusinessProcess()
        self.dataTask = DataProcess()
        

        ###############读数据################
        self.myreadthread = ReadThread() # 实例化自己建立的任务线程类
        self.myreadthread.signal.connect(self.callback) #设置任务线程发射信号触发的函数
        ###############################
        ################发数据###############
        self.mysendthread = SendThread() # 实例化自己建立的任务线程类
        self.mysendthread.signal.connect(self.callback) #设置任务线程发射信号触发的函数
        ###############################

        #################主任务##############
        self.mybusnthread = BusinessThread() # 实例化自己建立的任务线程类
        self.mybusnthread.signal.connect(self.callback) #设置任务线程发射信号触发的函数
        ###############################

    def callback(self,i): # 这里的 i 就是任务线程传回的数据
        # self.wl_pushButton.setText(i)
        print(i)
        

    #数据接收线程
    def DataRecvProcessTask(self):
        global is_exit
        while not is_exit:
            self.dataTask.OnRecvDataProcess()

    #数据发送线程 
    def DataSendProcessTask(self):
        global is_exit
        while not is_exit:
            self.dataTask.OnSendDataProcess()



    def WL_slot(self):#这里WL_slot就是槽函数, 当点击按钮时执行 WL_slot 函数中的内容, 注意有一个参数为 self
        #pushButton的槽函数
        print("wl")
        #Mygol.set_value('FuncType','WL')
        self.mysendthread.terminate() # 结束任务线程
        self.myreadthread.terminate() # 结束任务线程

        self.mybusnthread.terminate() # 结束任务线程

        global commType
        commType = SerialPortData()
        self.mysendthread.start() # 启动任务线程
        self.myreadthread.start() # 启动任务线程

        self.mybusnthread.start() # 启动任务线程
        

    def STP_slot(self):#这里STP_slot就是槽函数, 当点击按钮时执行 STP_slot 函数中的内容, 注意有一个参数为 self
        #pushButton的槽函数
        print("stp")
        self.mysendthread.terminate() # 结束任务线程
        self.myreadthread.terminate() # 结束任务线程
        self.mybusnthread.terminate() # 结束任务线程
        global commType
        commType = SockCanData()
        self.mysendthread.start() # 启动任务线程
        time.sleep(0.3)#需要建联，确认端口号，所以需等待延迟
        self.myreadthread.start() # 启动任务线程

        self.mybusnthread.start() # 启动任务线程

        
        #self.m_uiSTPMain.show()
        # tmp = STPMain.STPMain(self)
        # tmp.exec_()


##################################################################################################################################
is_exit=False


def delfile():
    if os.path.isdir('log'):
        pass
    else:
        os.mkdir('log') #创建目录
    path = './log/log.txt'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
        os.remove(path)
    path = './log/test.txt'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
        time.sleep(1)
        os.remove(path)

if __name__ == '__main__':
    if('WL' == Mygol.get_value('FuncType')):
        print("版本:1.0.1")
        time.sleep(3)
        delfile()
    elif('STP' == Mygol.get_value('FuncType')):
        print('STP调试版本：1.0.0-1')

    app = QApplication(sys.argv)
    myMain = Main()
    myMain.show()

    # if('WL'==Mygol.get_value('FuncType') or 'STP'==Mygol.get_value('FuncType')):
    #     #数据接收线程
    #     datarecvtask = threading.Thread(target=myMain.DataRecvProcessTask)
    #     datarecvtask.setDaemon(True)
    #     datarecvtask.start()

    #     #数据发送线程
    #     datasendtask = threading.Thread(target=myMain.DataSendProcessTask)
    #     datasendtask.setDaemon(True)
    #     datasendtask.start()


    #     while not is_exit:
    #         #任务管理线程
    #         myMain.businessTask.OnBusinessProcess()

    app.exec_()

