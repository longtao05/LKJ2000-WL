#encoding:utf-8
#系统库导入
import os
import sys
import struct
from ctypes import *
import time
import platform
import can
import random
import binascii
from datetime import datetime

#模块导入
sys.path.append(r"..\Common")
import Mygol
from DataQueue import *

import DataQueue
from CanDataType import _VCI_CAN_OBJ,_RX_CAN_OBJ,_VCI_INIT_CONFIG

#02000000 6ea0ef00 01 00 00 00 08 0001020304050607 000077


class CanData():
    def __init__(self):
        self.rxdataA=_RX_CAN_OBJ()
        self.rxdataA_put_flag = True #写标志
        self.rxdataB=_RX_CAN_OBJ()
        self.rxdataB_put_flag = True #写标志
        self.Dataqueue = DataQueue.DataQueue()
        self.canLib = windll.LoadLibrary('./Comm/ControlCAN.dll')

        #can相关参数信息
        self.devType = 3
        self.devIndex = 0
        self.can0Index = 0
        self.can1Index = 1

        self.Device_open()

    def Device_open(self):
        vic = _VCI_INIT_CONFIG()
        vic.AccCode = 0x00000000
        vic.AccMask = 0xffffffff
        vic.Filter = 0
        vic.Timing0 = 0x00
        vic.Timing1 = 0x1c
        vic.Mode = 0

        #一个设备只能打开一次
        print('打开设备: %d' % (self.canLib.VCI_OpenDevice(self.devType, self.devIndex, 0)))

        #Can0
        print('设置波特率: %d' % (self.canLib.VCI_SetReference(self.devType, self.devIndex, self.can0Index, 0, pointer(c_int(0x060007)))))#500  0x060007 500k;0x060003 1000k
        print('初始化: %d' % (self.canLib.VCI_InitCAN(self.devType, self.devIndex, self.can0Index, pointer(vic))))
        print('启动: %d' % (self.canLib.VCI_StartCAN(self.devType, self.devIndex, self.can0Index)))
        print('清空缓冲区: %d' % (self.canLib.VCI_ClearBuffer(self.devType, self.devIndex, self.can0Index)))
        #Can1
        print('设置波特率: %d' % (self.canLib.VCI_SetReference(self.devType, self.devIndex, self.can1Index, 0, pointer(c_int(0x060007)))))#500  0x060007 500k;0x060003 1000k
        print('初始化: %d' % (self.canLib.VCI_InitCAN(self.devType, self.devIndex, self.can1Index, pointer(vic))))
        print('启动: %d' % (self.canLib.VCI_StartCAN(self.devType, self.devIndex, self.can1Index)))
        print('清空缓冲区: %d' % (self.canLib.VCI_ClearBuffer(self.devType, self.devIndex, self.can1Index)))

    def Device_close(self):
        print('关闭设备: %d' % (self.canLib.VCI_CloseDevice(self.devType, self.devIndex, 0)))


    def send_data(self):
        retval = self.Dataqueue.get_canA_recv_data()
        retvalB = self.Dataqueue.get_canB_recv_data()
        if(retval[0]):
            self.canLib.VCI_Transmit(self.devType, self.devIndex, self.can0Index, pointer(retval[1]), 1)
            self.canLib.VCI_Transmit(self.devType, self.devIndex, self.can1Index, pointer(retval[1]), 1)
            #print("缓存队发送成功！")
        else:
            print("缓存队列为空！")


    def read_data(self):
        #缓存队列未满,从缓冲区读取数据，负责存储上次未存储数据
        if(self.rxdataA_put_flag):
            self.canLib.VCI_Receive(self.devType, self.devIndex, self.can0Index, pointer(self.rxdataA),1,400)
            print("A系",hex(self.rxdataA.ID))
            print(bytearray(self.rxdataA).hex())
            #print(type(self.rxdataA.Data))
        else:
            print("缓存A队列已满！")
        self.rxdataA_put_flag = self.Dataqueue.put_canA_recv_data(self.rxdataA)

        #缓存队列未满,从缓冲区读取数据，负责存储上次未存储数据
        if(self.rxdataB_put_flag):
            self.canLib.VCI_Receive(self.devType, self.devIndex, self.can1Index, pointer(self.rxdataB),1,400)
            print("B系",hex(self.rxdataB.ID))
        else:
            print("缓存B队列已满！")
        self.rxdataB_put_flag = self.Dataqueue.put_canB_recv_data(self.rxdataB)

