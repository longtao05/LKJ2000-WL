#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
#模块导入
sys.path.append(r"../Common")
import Mygol
from SerialPortData import SerialPortData
from SysDataPreProc import SysDataPreProc
from DataQueue import *

class DataProcess():
    def __init__(self):
        self.SerialTask = SerialPortData()
        self.SysDataPre = SysDataPreProc()

    def OnRecvDataProcess(self):
        self.OnRecvSerData()

    def OnSendDataProcess(self):
        self.OnSendSerData()

    #串口相关函数
    def OnRecvSerData(self):
        self.SerialTask.read_data()
        self.SysDataPre.OnRecvSysDataPreProc()

    def OnSendSerData(self):
        self.SysDataPre.OnSendSysDataPreProc()
        self.SerialTask.send_data()


