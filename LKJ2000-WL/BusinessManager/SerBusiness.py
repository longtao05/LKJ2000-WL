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
from DataHandle import DataHandle
from DataQueue import *

class SerBusiness():
    def __init__(self):
        self.dataH = DataHandle()

    def OnSerProcess(self):
        #print("enter OnSerProcess ")
        self.dataH.OnDataHandle()

        self.dataH.OnSendDataPre()
        #print("exit OnSerProcess ")



    def OnBusinessDatasendTask(self):
        pass


