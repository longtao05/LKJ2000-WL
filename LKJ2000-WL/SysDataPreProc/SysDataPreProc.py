#encoding:utf-8
#系统库导入
import sys
import os
import binascii

#模块导入
from SerDataParser import SerDataParser

class SysDataPreProc():
    def __init__(self):
        self.serDataPar = SerDataParser()

    def OnRecvSysDataPreProc(self):
        self.serDataPar.SerGetDataTran()

    def OnSendSysDataPreProc(self):
        self.serDataPar.SerSendDataTran()