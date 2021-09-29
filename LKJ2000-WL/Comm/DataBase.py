#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
from abc import ABCMeta, abstractmethod
#模块导入
sys.path.append(r"../Common")
sys.path.append(r"../SysDataPreProc")
import Mygol

from SysDataPreProc import SysDataPreProc
from DataQueue import *

class DataBase():
    def __init__(self):
        pass

    @abstractmethod
    def send_data(self):
        pass

    @abstractmethod
    def read_data(self):
        pass 

