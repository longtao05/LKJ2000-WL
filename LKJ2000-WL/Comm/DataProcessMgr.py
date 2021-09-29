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
from CanData import CanData
from SockCanData import SockCanData
from SysDataPreProc import SysDataPreProc
from DataQueue import *

class DataProcess():
    def __init__(self):
        if('WL' == Mygol.get_value('FuncType')):
            self.SerialTask = SerialPortData()
            self.SysDataPre = SysDataPreProc()
        elif('STP' == Mygol.get_value('FuncType')):
            #self.CanTask = CanData()
            self.CanTask = SockCanData()

    def OnRecvDataProcess(self):
        if('WL' == Mygol.get_value('FuncType')):
            self.OnRecvSerData()
        elif('STP' == Mygol.get_value('FuncType')):
            self.OnRecvCanData()

    def OnSendDataProcess(self):
        if('WL' == Mygol.get_value('FuncType')):
            self.OnSendSerData()
        elif('STP' == Mygol.get_value('FuncType')):
            self.OnSendCanData()

    #串口相关函数
    def OnRecvSerData(self):
        self.SerialTask.read_data()
        self.SysDataPre.OnRecvSysDataPreProc()

    def OnSendSerData(self):
        self.SysDataPre.OnSendSysDataPreProc()
        self.SerialTask.send_data()

    #串口相关函数
    def OnRecvCanData(self):
        self.CanTask.read_data()
        #self.SysDataPre.OnRecvSysDataPreProc()

    def OnSendCanData(self):
        #self.SysDataPre.OnSendSysDataPreProc()
        self.CanTask.send_data()

    def OnsendData(self,dataTy):
        dataTy.send_data()

    def OnreadData(self,dataTy):
        dataTy.read_data()

