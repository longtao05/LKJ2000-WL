#!/usr/bin/python
# -*-coding: utf-8 -*-

import os
import sys
import struct
from ctypes import *
import time
sys.path.append(r".\ZlgCanDriver")

import  ZLGCanControl

class _VCI_INIT_CONFIG(Structure):
    _fields_ = [('AccCode', c_ulong),
                ('AccMask', c_ulong),
                ('Reserved', c_ulong),
                ('Filter', c_ubyte),
                ('Timing0', c_ubyte),
                ('Timing1', c_ubyte),
                ('Mode', c_ubyte)]


class _VCI_CAN_OBJ(Structure):
    _fields_ = [('ID', c_uint),
                ('TimeStamp', c_uint),
                ('TimeFlag', c_byte),
                ('SendType', c_byte),
                ('RemoteFlag', c_byte),
                ('ExternFlag', c_byte),
                ('DataLen', c_byte),
                ('Data', c_byte*8),
                ('Reserved', c_byte*3)]


class _RX_CAN_OBJ(Structure):
    _fields_ = [('ID', c_uint),
                ('TimeStamp', c_uint),
                ('TimeFlag', c_byte),
                ('SendType', c_byte),
                ('RemoteFlag', c_byte),
                ('ExternFlag', c_byte),
                ('DataLen', c_byte),
                ('Data', c_byte*8),
                ('Reserved', c_byte*3)]

def ZLGtest():
    #新建对象
     c = Communication()
     #配置CAN卡, 型号：USB_CAN_2EU, CAN卡索引: 0, CAN卡通道：channel_0, 波特率: 500kbps
     c.set_can_board_configuration(can_type="usb_can_2eu",can_idx=0,chn=0,baud_rate=500)
     #打开CAN卡'
     c.open_new()

     # 注意发送函数默认发送数据长度为8个字节

     # 发送标准帧 id 为0x110
     data = [1,2,3,4,5,6,7,8]
     c.Transmit(0x110,data)

     # 发送拓展帧
     data = [1,2,3,4,5,6,7,8]
     c.Transmit(0x110,data,extern_flag = True)

     # 发送长度为6的帧 , 根据周立功官方手册，CAN帧最大发送数据长度为8，当然我对此表示怀疑，
     # 但既然周立功所提供驱动貌似只能发送最大长度为8 byte的帧，因此，请保证数据长度不大于8即可。
     data = [1,2,3,4,5,6]
     c.Transmit(0x110,data,data_len=6)

     # 新建线程，不断读取CAN卡上的报文并且打印出来
     cycle_read_thread = threading.Thread(target=c.PrintReceiveData)
     cycle_read_thread.start()

def Test():
    vic = _VCI_INIT_CONFIG()
    vic.AccCode = 0x00000000
    vic.AccMask = 0xffffffff
    vic.Filter = 0
    vic.Timing0 = 0x00
    vic.Timing1 = 0x1c
    vic.Mode = 0

    vco = _VCI_CAN_OBJ()
    vco.ID = 0x00000001
    vco.SendType = 0
    vco.RemoteFlag = 0
    vco.ExternFlag = 0
    vco.DataLen = 8
    vco.Data = (1, 2, 3, 4, 5, 6, 7, 8)

    rxdata=_RX_CAN_OBJ()

    canLib = windll.LoadLibrary('./ControlCAN.dll')
    print("下面执行操作返回“1”表示操作成功！")
    i=1
    while(i<28):
        print('打开设备: %d' % (canLib.VCI_OpenDevice(i, 0, 0)))
        time.sleep(1)
        i+=1

    print('打开设备: %d' % (canLib.VCI_OpenDevice(4, 0, 0)))
    print('设置波特率: %d' % (canLib.VCI_SetReference(4, 0, 0, 0, pointer(c_int(0x060003)))))#1000  0x060007 500k;0x060003 1000k
    print('初始化: %d' % (canLib.VCI_InitCAN(4, 0, 0, pointer(vic))))
    print('启动: %d' % (canLib.VCI_StartCAN(4, 0, 0)))
    print('清空缓冲区: %d' % (canLib.VCI_ClearBuffer(4, 0, 0)))
    print('发送: %d' % (canLib.VCI_Transmit(4, 0, 0, pointer(vco), 1)))

    #while canLib.VCI_GetReceiveNum(4,0,0)==0 :
        #continue
    print("接收缓存数量：",canLib.VCI_GetReceiveNum(4,0,0))
    if(canLib.VCI_Receive(4, 0, 0, pointer(rxdata),100,400)):
        print('从缓存读取一帧数据:', bytearray(rxdata.Data).hex())
    else:
        print("接收缓存区为空")
    print("接收缓存数量：",canLib.VCI_GetReceiveNum(4,0,0))

if __name__ == '__main__':
    ZLGtest()
