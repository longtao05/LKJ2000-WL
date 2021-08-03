
#encoding:utf-8
#系统库导入
import sys
import os
#from PyQt5.Qt import *
#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import *
import binascii
import time
import threading
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


from BusinessProcess import BusinessProcess
from DataProcess import DataProcess

class Main():
    def __init__(self):
        #super(Main,self).__init__()
        #全局变量字典定义
        Mygol._init()
        MyFilegol._init()
        #读取配置信息至全局变量

        FileHandle.readMyfile()
        ConfigHandle.readConfig()
        self.businessTask = BusinessProcess()
        self.dataTask = DataProcess()
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
        os.remove(path)

if __name__ == '__main__':
    print("版本:1.0.0")

    delfile()
    myMain = Main()

    #数据接收线程
    datarecvtask = threading.Thread(target=myMain.DataRecvProcessTask)
    datarecvtask.setDaemon(True)
    datarecvtask.start()

    #数据发送线程
    datasendtask = threading.Thread(target=myMain.DataSendProcessTask)
    datasendtask.setDaemon(True)
    datasendtask.start()


    while not is_exit:
        #任务管理线程
        myMain.businessTask.OnBusinessProcess()

