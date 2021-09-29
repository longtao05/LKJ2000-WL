#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
from datetime import datetime
from socket import *
from time import ctime
import struct
import ctypes
from ctypes import *
#模块导入
sys.path.append(r"..\Common")
import Mygol
from DataQueue import *

import DataQueue
from CanDataType import _UDP_CAN_OBJ
import DataBase

bufsize = 1024

#02000000 6ea0ef00 01 00 00 00 08 0001020304050607 000077
#调试使用
vco = _UDP_CAN_OBJ()
vco.ID = 0x00000300
vco.DataLen = 8
vco.Data = (1, 2, 3, 4, 5, 6, 7, 8)
initdata = _UDP_CAN_OBJ()
initdata.ID = 0x00000400
initdata.DataLen = 8
initdata.Data = (9, 8, 7, 6, 5, 4, 3, 2)

lkjID = [0x300,0x308,0x309,0x30a,0x390,0x391,0x392,0x388,0x389,0x38a,0x38b,0x38c,0x38d,0x38e,0x38f,0x393,0x398,0x39b]
dmiID = [0x400,0x403,0x408,0x409,0x40a,0x410,0x411,0x412,0x413,0x414,0x415,0x416,0x417,0x418,0x41a,0x41b,0x41c]

def singleton(cls, *args, **kwargs):
    instances = {}
    
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class SockCanData(DataBase.DataBase):
    def __init__(self):
        self.Dataqueue = DataQueue.DataQueue()
        serialPort = Mygol.get_value('serialPort')
        baudRate = Mygol.get_value('baudRate')

        #self.recvhost = '192.168.208.211' #监听所有的ip
        '''self.recvhost = '127.0.0.1' #监听所有的ip
        self.recvport = 10002 #接口必须一致
        self.recvaddr=(self.recvhost,self.recvport)
        self.udpServer = socket(AF_INET,SOCK_DGRAM)
        self.udpServer.bind(self.recvaddr) #开始监听'''

        #self.lkjhost = '192.168.208.131' # 这是客户端的电脑的ip
        
        self.lkjhost = '127.0.0.1'# 这是客户端的电脑的ip
        self.lkjport = 10001 #接口必须一致
        self.lkjaddr=(self.lkjhost,self.lkjport)
        #setdefaulttimeout(500)
        self.lkjsocket= socket(AF_INET,SOCK_DGRAM)#创建数据发送端
        #self.lkjsocket.bind(self.lkjaddr) #开始监听'''


        self.dmihost = '127.0.0.1' # 这是客户端的电脑的ip
        self.dmiport = 10002 #接口必须一致
        self.dmiaddr=(self.dmihost,self.dmiport)

        self.dmisocket= socket(AF_INET,SOCK_DGRAM)#创建数据发送端
        #self.dmisocket.bind(self.dmiaddr) #开始监听'''
        self.rxdataA=_UDP_CAN_OBJ()
        self.rxdataA_put_flag = True #写标志
        #暂未使用，PC调试，只考虑单系
        #self.rxdataB=_RX_CAN_OBJ()
        # #self.rxdataB_put_flag = True #写标志
        # self.lkjsocket.sendto(initdata,self.lkjaddr) # 发送数据
        # self.dmisocket.sendto(initdata,self.dmiaddr) # 发送数据


    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    #发送数据考虑发送对象，LKJ or DMI
    def data_divide(self):
        ret = 0
        self.Dataqueue.put_can_send_data(vco)  
        time.sleep(1)
        retval = self.Dataqueue.get_can_send_data()
        if(retval[0]):
            if(retval[1].ID in lkjID):
                ret = 1
            elif(retval[1].ID in dmiID):
                ret = 2 
        else:
            print("缓存队列为空！")  
        return [ret,retval[1]]

    def send_data(self):
        retval = self.data_divide()
        if(1==retval[0]):
            self.lkjsocket.sendto(retval[1],self.lkjaddr) # 发送数据
            print('发送LKJ数据:', bytearray(retval[1]).hex())
        elif(2==retval[0]):
            self.dmisocket.sendto(retval[1],self.dmiaddr) # 发送数据
            print('发送DMI数据:', bytearray(retval[1]).hex())

    def read_data(self):
        #缓存队列未满,从缓冲区读取数据，负责存储上次未存储数据
        time.sleep(1)
        if(self.rxdataA_put_flag):
            data,recvaddr = self.lkjsocket.recvfrom(1024) #接收数据和返回地址
            tupdata = struct.unpack('<II8s',data)
            self.rxdataA.ID = tupdata[0]
            self.rxdataA.DataLen = tupdata[1]
            #必须将数据转换成一个整数列表，并为构造函数解压。一定有更简单的方法！目前使用此办法
            self.rxdataA.Data = (ctypes.c_ubyte*8)(*list(bytearray(tupdata[2])))
            print('接收数据:',bytearray(self.rxdataA).hex())
            print('测试')
        else:
            print("缓存A队列已满！")
        #self.rxdataA_put_flag = self.Dataqueue.put_canA_recv_data(self.rxdataA)