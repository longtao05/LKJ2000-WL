#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
#模块导入
sys.path.append(r"../Common")
sys.path.append(r"../BusinessManager")
import Mygol
from SerialPortData import SerialPortData
from SerBusiness import SerBusiness
from DataQueue import *

class BusinessProcess():
    def __init__(self):
        self.serBus = SerBusiness()

    def OnBusinessProcess(self):
        self.serBus.OnSerProcess()



