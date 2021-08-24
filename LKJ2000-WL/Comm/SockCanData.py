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
from CanDataType import _VCI_CAN_OBJ,_RX_CAN_OBJ

bufsize = 1024

#02000000 6ea0ef00 01 00 00 00 08 0001020304050607 000077
#调试使用
vco = _VCI_CAN_OBJ()
vco.ID = 0x000007ff
vco.SendType = 0
vco.RemoteFlag = 0
vco.ExternFlag = 0
vco.DataLen = 8
vco.Data = (1, 2, 3, 4, 5, 6, 7, 8)

class SockCanData():
    def __init__(self):
        self.Dataqueue = DataQueue.DataQueue()
        serialPort = Mygol.get_value('serialPort')
        baudRate = Mygol.get_value('baudRate')

        #self.recvhost = '192.168.208.211' #监听所有的ip
        self.recvhost = '127.0.0.1' #监听所有的ip
        self.recvport = 10002 #接口必须一致
        self.recvaddr=(self.recvhost,self.recvport)
        self.udpServer = socket(AF_INET,SOCK_DGRAM)
        self.udpServer.bind(self.recvaddr) #开始监听

        #self.sendhost = '192.168.208.211' # 这是客户端的电脑的ip
        self.sendhost = '127.0.0.1' # 这是客户端的电脑的ip
        self.sendport = 10001 #接口必须一致
        self.sendaddr=(self.sendhost,self.sendport)

        self.udpClient = socket(AF_INET,SOCK_DGRAM)#创建数据发送端

        self.rxdataA=_RX_CAN_OBJ()
        self.rxdataA_put_flag = True #写标志
        #暂未使用，PC调试，只考虑单系
        #self.rxdataB=_RX_CAN_OBJ()
        #self.rxdataB_put_flag = True #写标志

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        #02000000 6ea0ef00 01 00 00 00 08 0001020304050607 000077
        #data = vco
        #data = data.encode(encoding="utf-8")
        time.sleep(1)
        retval = self.Dataqueue.get_canA_recv_data()
        if(retval[0]):
            self.udpClient.sendto(retval[1],self.sendaddr) # 发送数据
            print('发送数据:', bytearray(retval[1]).hex())
            print('发送数据:', retval[1])
            #print("缓存队发送成功！")
        else:
            print("缓存队列为空！")

    def read_data(self):
        print('Waiting for connection...')
        #处理数据
        #data = data.decode(encoding='utf-8').upper()
        #data = "at %s :%s"%(ctime(),data)
        #020000006ea0ef0001000000080001020304050607000077

        #缓存队列未满,从缓冲区读取数据，负责存储上次未存储数据
        if(self.rxdataA_put_flag):
            #self.canLib.VCI_Receive(self.devType, self.devIndex, self.can0Index, pointer(self.rxdataA),1,400)
            data,self.recvaddr = self.udpServer.recvfrom(bufsize) #接收数据和返回地址
            print('接收数据:', bytearray(data).hex())

            tupdata = struct.unpack('<II5B8s3s',data)
            self.rxdataA.ID = tupdata[0]
            self.rxdataA.TimeStamp = tupdata[1]
            self.rxdataA.TimeFlag = tupdata[2]
            self.rxdataA.SendType = tupdata[3]
            self.rxdataA.RemoteFlag = tupdata[4]
            self.rxdataA.ExternFlag = tupdata[5]
            self.rxdataA.DataLen = tupdata[6]
            #必须将数据转换成一个整数列表，并为构造函数解压。一定有更简单的方法！目前使用此办法
            self.rxdataA.Data = (ctypes.c_ubyte*8)(*list(bytearray(tupdata[7])))
            self.rxdataA.Reserved = (ctypes.c_ubyte*3)(*list(bytearray(tupdata[8])))
            print("A系",hex(self.rxdataA.ID))
            print(bytearray(self.rxdataA).hex())
        else:
            print("缓存A队列已满！")
        self.rxdataA_put_flag = self.Dataqueue.put_canA_recv_data(self.rxdataA)

        #udpServer.sendto(data.encode(encoding='utf-8'),addr)
        #发送数据
        #print('...recevied from and return to :',addr)
