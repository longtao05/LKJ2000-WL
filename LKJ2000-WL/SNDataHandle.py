#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import Comm
import csv
import WLrdBusiness
import time
from SNSendData import *
from SNGetData import *
from SNWLTypeDef import _SN_DataType,  _SN_VersionInfoPackage , _SN_ActiDetectionInfo,_SN_UpgradeRequestInfo ,_SN_UpgradeOperationInfo,_SN_WLActiDetectionInfo,_SN_VersionConfirmInfo,_SN_UpgradePlanCancelledReply,_SN_HostEventInfo

import Mygol


send_data =bytearray()


global Count
Count = 0
global Count1
Count1 = 0
def SN_businesstype_handle(mSerial,datatype,data_Effbytes):
    global send_data
    global PlanCancelled
    global Count
    global Count1
    if(1==Mygol.get_value("LOG")):
        f = open('./log/log.txt', 'ab') # 若是'wb'就表示写二进制文件
        f.write('接收数据:  时间戳:'.encode('utf-8')+str.encode(str(datetime.now()))+'  包类型:'.encode('utf-8')+binascii.b2a_hex(datatype.PacketType.to_bytes(2,byteorder='little', signed=False))+b"\r\n"+binascii.b2a_hex(data_Effbytes))
        f.write(b'\r\n')
        f.close()

    if(0x1001 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        item = _SN_VersionInfoPackage()
        #版本信息包帧解析
        item = SN_VersionInfoPackage(data_Effbytes)
        #回复版本信息包
        send_data = SN_VersionInfoPackageReply(datatype,item)
        mSerial.send_data(send_data)
        Count1+=1
        if(1==Mygol.get_value("LOG")):
            f = open('./log/count.txt', 'ab') # 若是'wb'就表示写二进制文件
            f.write('换装时间:'.encode('utf-8')+str.encode(str(datetime.now()))+b"\r\n"+binascii.b2a_hex(Count1.to_bytes(2,byteorder='little', signed=False))+b"\r\n")
            f.write(b'\r\n')
            f.close()

        if(0 == Mygol.get_value("StopFlag")):
            #延时10毫秒后，发送换装通知--升级信息
            time.sleep(0.2)
            #换装通知--升级信息
            send_data = SN_ChangeNotice_UpgradeInfo(datatype,item)
            mSerial.send_data(send_data)
            #pass

    elif(0x1002 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
         #收到活动性检测发送，准备发送应答
        item = _SN_ActiDetectionInfo()
        #活动性检测帧解析
        item = SN_ActiDetectionInfo(data_Effbytes)
        #回复活动性检测帧
        send_data = SN_ActiDetectionInfoReply(datatype,item)
        mSerial.send_data(send_data)


        if(1 == Mygol.get_value("StopFlag")):
            Count+=1
            if(Count > 3):
                exit(0)



    elif(0x1003 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
         #换装通知应答包
        item = _SN_UpgradeRequestInfo()
        item = SN_UpgradeRequestInfo(data_Effbytes)
        print("换装应答内容：",'%#x'%item.MessgaeRece)
        if(2==item.MessgaeRece):
            #换装通知--换装控制信息
            send_data = SN_ChangeNotice_ControlInfo(datatype,item)
            mSerial.send_data(send_data)
        elif(3==item.MessgaeRece):
            pass
            #换装通知--启动升级
            #send_data = SN_ChangeNotice_StartUpgrade(datatype,item)
            #mSerial.send_data(send_data)
        elif(4==item.MessgaeRece):
            #换装通知--升级信息
            print("已正确接收启动信息内容")


    elif(0x1005 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        item = _SN_UpgradeOperationInfo()
        #升级操作信息请求
        item = SN_UpgradeOperationInfo(data_Effbytes)

        if(1!=item.OperationType):
            Mygol.set_value("StopFlag",1)

        #升级操作信息应答
        send_data = SN_UpgradeOperationInfoReply(datatype,item)
        mSerial.send_data(send_data)

        #延时1秒后，发送启动升级信息
        #time.sleep(0.01)
        #send_data = SN_StartUpgradeOperationInfo(datatype,item)
        #mSerial.send_data(send_data)
        #换装通知--启动升级
        #send_data = SN_ChangeNotice_StartUpgrade(datatype,item)
        #mSerial.send_data(send_data)
    elif(0x1007 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
         #
        item = _SN_WLActiDetectionInfo()
        #活动性检测帧解析
        item = SN_WLActiDetectionInfo(data_Effbytes)
        #回复活动性检测帧
        send_data = SN_WLActiDetectionInfoReply(datatype,item)
        mSerial.send_data(send_data)
        Mygol.set_value("StopFlag",1)
        #可以处理换装取消
        if(0!=Mygol.get_value("PlanCancelled")):
            Mygol.set_value('PlanCancelledFlag',1)

    elif(0x1008 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        item = _SN_VersionConfirmInfo()
        item = SN_VersionConfirmInfo(data_Effbytes)
        send_data = SN_VersionConfirmInfoReply(datatype,item)
        mSerial.send_data(send_data)
        #延时3秒后，正常退出程序
        #time.sleep(3)
        #exit(0)
        #send_data = SN_StartUpgradeOperationInfo(datatype,item)
        #mSerial.send_data(send_data)
        #Flag = 1
    elif(0x1009 == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        item = _SN_UpgradePlanCancelledReply()
        item = SN_UpgradePlanCancelledReply(data_Effbytes)
        print("收到升级计划取消应答包")
    elif(0x100A == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        item = _SN_HostEventInfo()
        item = SN_HostEventInfo(data_Effbytes)

        send_data = SN_HostEventInfoReply(datatype,item)
        mSerial.send_data(send_data)

        #换装通知--启动升级
        time.sleep(0.1)
        send_data = SN_ChangeNotice_StartUpgrade(datatype,item)
        mSerial.send_data(send_data)

        Mygol.set_value('StopSendActReply',1)

    elif(0x100C == datatype.PacketType):
        print("包类型：",'%#x'%datatype.PacketType)
        Mygol.set_value("StopFlag",1)

        if(1 == Mygol.get_value("StopFlag")):
            Count+=1
            if(Count > 3):
                exit(0)

    else:
        print("未识别的包类型：",'%#x'%datatype.PacketType)

    return send_data


def SN_data_handle(mSerial,data_Effbytes):
    #print("有效数据处理：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
    data_len=len(data_Effbytes)
    i=0
    #帧格式解析
    if(data_len>=12):

        datatype = _SN_DataType()

        byteOffset = 0
        byteNum = 4
        datatype.TimeStamp = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
        byteOffset = byteOffset + byteNum
        byteNum = 2
        datatype.PacketType = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
        byteOffset = byteOffset + byteNum
        byteNum = 2
        datatype.InfoLen = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
        byteOffset = byteOffset + byteNum
        byteNum = 2
        datatype.PacketNum = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
        byteOffset = byteOffset + byteNum
        byteNum = 2
        datatype.Resrve = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
        byteOffset = byteOffset + byteNum
        byteNum = 2

        datatype.Crc = struct.unpack('<H',data_Effbytes[-2:])[0]
        #loc_str = [InfoLen,StartAddr,EndAddr,BusinessType,Order,Crc]
        #业务类型处理
        send_data = SN_businesstype_handle(mSerial,datatype,data_Effbytes)
    else:
        print("数据不正确")

    return send_data
