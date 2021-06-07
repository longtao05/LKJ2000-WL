#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time
from SendData import *
from GetData import *
from WLTypeDef import _DataType,  _ActiDetectionInfo ,_UpgradeRequestInfo ,_UpgradeOperationInfo
#10 02 18 00 01 11 10 ff 01 00 01 05 00 12 34 05 00 12 34 03 03 01 00 01 01 01 0f A8 B6 10 03
send_data =bytearray()
def businesstype_handle(datatype,data_Effbytes):
    global send_data
    if(0x10 == datatype.BusinessType):
        #活动性检测
        print("业务类型：0x10")
        if(0x01 == datatype.Order):
            #收到活动性检测发送，准备发送应答
            item = _ActiDetectionInfo()
            #活动性检测帧解析
            item = ActiDetectionInfo(data_Effbytes)
            #回复活动性检测帧
            send_data = ActiDetectionInfoReply(datatype,item)
    elif(0x20 == datatype.BusinessType):
        print("业务类型：0x20")
        if(0x01 == datatype.Order):
            item = _UpgradeRequestInfo()
            item = UpgradeRequestInfo(data_Effbytes)
            send_data = UpgradeInfoSend(datatype,item)
        if(0x03 == datatype.Order):
            item = _UpgradeOperationInfo()
            item = UpgradeOperationInfo(data_Effbytes)
            send_data = UpgradeOperationInfoReply(datatype,item)


        #文件远程升级

    elif(0x30 == datatype.BusinessType):
        print("业务类型：0x30")

        #文件传输
        pass
    return send_data


def data_handle(data_Effbytes):
    print("有效数据处理：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
    data_len=len(data_Effbytes)
    i=0
    #帧格式解析
    #信息长度：2 源通信地址：1 目的通信地址：1 业务类型：1 命令：1 数据：n CRC16:2
    datatype = _DataType()
    datatype.InfoLen=struct.unpack('<H',data_Effbytes[i:i+2])[0]
    datatype.StartAddr=struct.unpack('<B',data_Effbytes[i+2:i+3])[0]
    datatype.EndAddr=struct.unpack('<B',data_Effbytes[i+3:i+4])[0]
    datatype.BusinessType=struct.unpack('<B',data_Effbytes[i+4:i+5])[0]
    datatype.Order=struct.unpack('<B',data_Effbytes[i+5:i+6])[0]
    datatype.Crc = struct.unpack('<H',data_Effbytes[-2:])[0]
    #loc_str = [InfoLen,StartAddr,EndAddr,BusinessType,Order,Crc]
    #业务类型处理
    send_data = businesstype_handle(datatype,data_Effbytes)

    return send_data


"""

    #struct 解析数据帧
    accelerated_x,accelerated_y,=struct.unpack('<hh',data_Effbytes[i+6:-2])
    print(accelerated_x,accelerated_y)"""


