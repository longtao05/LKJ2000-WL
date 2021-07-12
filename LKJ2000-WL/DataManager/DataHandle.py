#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time

#模块导入
sys.path.append(r"..\Common")
sys.path.append(r"..\LogSys")

from SerDataHandle import SerDataHandle

class DataHandle():
    def __init__(self):
        self.serDataH = SerDataHandle()

    def OnDataHandle(self):
        self.serDataH.SerDataHandleProcess()

    def OnSendDataPre(self):
        self.serDataH.SerSendDataPreProcess()
