
#encoding:utf-8
#系统库导入
import sys
import os
import binascii
from datetime import datetime
import struct
import time

#模块导入

sys.path.append(r"..\LogSys")
sys.path.append(r"..\Common")
from MyCRC import *
from CommFun import *
import Mygol
import MyFilegol

from SerDataType import _SN_VersionInfoPackageReply ,_SN_ActiDetectionInfoReply ,\
_SN_UpgradeInfoSend,_SN_UpgradeOperationInfoReply,_SN_StartUpgradeOperationInfo ,\
_SN_WLActiDetectionInfoReply,_SN_VersionConfirmInfoReply,_SN_UpgradePlanCancelled,\
_SN_HostEventInfoReply,_SN_ChangeNotice_StartUpgrade,_SN_ChangeNotice_ControlInfo,\
_SN_ChangeNotice_UpgradeInfo


def SN_VersionInfoPackageReply(datatype,m_item):
    item = _SN_VersionInfoPackageReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2001
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 14
    item.PacketNum = datatype.PacketNum
    item.CommProVer = m_item.CommProVer #是否更改
    item.WUPSWCode = 0x177c9000 #是否更改

    item.Resrve1 = 0
    item.Resrve2 = 0
    item.Resrve3 = 0
    item.Resrve4 = 0
    item.Resrve5 = 0
    item.Resrve6[0] = 0
    item.Resrve6[1] = 0
    item.Resrve6[2] = 0
    item.Resrve6[3] = 0
    item.Resrve6[4] = 0
    item.Resrve6[5] = 0
    item.Resrve6[6] = 0
    item.Resrve6[7] = 0
    item.Resrve6[8] = 0
    item.Resrve6[9] = 0
    item.Resrve6[10] = 0
    item.Resrve6[11] = 0

    send_tempdata = struct.pack("<I4H5I14B", item.TimeStamp,item.PacketType,item.InfoLen,\
        item.PacketNum,item.Resrve,item.CommProVer,item.WUPSWCode,item.Resrve1,item.Resrve2,item.Resrve3,\
        item.Resrve4,item.Resrve5,item.Resrve6[0],item.Resrve6[1],item.Resrve6[2],item.Resrve6[3],\
        item.Resrve6[4],item.Resrve6[5],item.Resrve6[6],item.Resrve6[7],item.Resrve6[8],\
        item.Resrve6[9],item.Resrve6[10],item.Resrve6[11])

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4H5I14BH", item.TimeStamp,item.PacketType,item.InfoLen,\
        item.PacketNum,item.Resrve,item.CommProVer,item.WUPSWCode,item.Resrve1,item.Resrve2,item.Resrve3,\
        item.Resrve4,item.Resrve5,item.Resrve6[0],item.Resrve6[1],item.Resrve6[2],item.Resrve6[3],\
        item.Resrve6[4],item.Resrve6[5],item.Resrve6[6],item.Resrve6[7],item.Resrve6[8],\
        item.Resrve6[9],item.Resrve6[10],item.Resrve6[11],item.Crc)
    #数据组包加密

    return send_data


def SN_ActiDetectionInfoReply(datatype,m_item):
    item = _SN_ActiDetectionInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2002
    #item.TimeStamp = 0x11111011

    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 26
    item.PacketNum = datatype.PacketNum+1

    item.TrainNum = Mygol.get_value('TrainNum')
    item.ManCode = Mygol.get_value('ManCode')
    item.WUPInitStatus =1

    item.DeviceId[0] =0x01
    item.DeviceId[1] =0x02
    item.DeviceId[2] =0x03
    item.DeviceId[3] =0x04
    item.DeviceId[4] =0x05
    item.DeviceId[5] =0x06
    item.WLRegiStatus =1
    item.WLRegiConnStatus =1


    send_tempdata = struct.pack("<I4HI10B", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.ManCode,\
        item.WUPInitStatus,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],\
        item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.WLRegiConnStatus)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HI10BH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.ManCode,\
        item.WUPInitStatus,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],\
        item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.WLRegiConnStatus,item.Crc)
    #数据组包加密

    return send_data

def SN_UpgradeOperationInfoReply(datatype,m_item):
    item = _SN_UpgradeOperationInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2005
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 54
    item.PacketNum = datatype.PacketNum

    item.DataType =  Mygol.get_value('DataType')

    item.OrderID = Mygol.get_value('OrderID') #32
    item.TrainNum = Mygol.get_value('TrainNum')
    item.WLFileFlag = Mygol.get_value('WLFileFlag')

    item.DMIOperationTer = 1

    if(1 == m_item.OperationType):
        item.IsCanUpgrade =0 #升级
    elif(2 == m_item.OperationType):
        item.IsCanUpgrade =2#版本错误，提示未知
    elif(3 == m_item.OperationType):
        item.IsCanUpgrade =3 #退出
    else:
        item.IsCanUpgrade =4


    item.Resrve2 = 0

    send_tempdata = struct.pack("<I4H32sIH4B", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.OrderID.encode('utf-8'),\
        item.TrainNum,item.WLFileFlag,item.DMIOperationTer,item.IsCanUpgrade,item.DataType,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4H32sIH4BH", item.TimeStamp,item.PacketType,item.InfoLen,\
        item.PacketNum,item.Resrve,item.OrderID.encode('utf-8'),item.TrainNum,\
        item.WLFileFlag,item.DMIOperationTer,item.IsCanUpgrade,item.DataType,item.Resrve2,item.Crc)
    #数据组包加密


    return send_data




def SN_WLActiDetectionInfoReply(datatype,m_item):
    item = _SN_ActiDetectionInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2007
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 26
    item.PacketNum = datatype.PacketNum
    item.TrainNum = Mygol.get_value('TrainNum')
    item.ManCode =  Mygol.get_value('ManCode')
    item.WUPInitStatus =0

    item.DeviceId[0] =0x01
    item.DeviceId[1] =0x02
    item.DeviceId[2] =0x03
    item.DeviceId[3] =0x04
    item.DeviceId[4] =0x05
    item.DeviceId[5] =0x06
    item.WLRegiStatus =1
    item.WLRegiConnStatus =0


    send_tempdata = struct.pack("<I4HI2B8B", item.TimeStamp,item.PacketType,item.InfoLen,\
        item.PacketNum,item.Resrve,item.TrainNum,item.ManCode,item.WUPInitStatus,\
        item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],\
        item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.WLRegiConnStatus)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HI2B8BH", item.TimeStamp,item.PacketType,item.InfoLen,\
        item.PacketNum,item.Resrve,item.TrainNum,item.ManCode,item.WUPInitStatus,\
        item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],\
        item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.WLRegiConnStatus,item.Crc)

    #数据组包加密

    return send_data


def SN_VersionConfirmInfoReply(datatype,m_item):
    item = _SN_VersionConfirmInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2008
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 66
    item.PacketNum = m_item.TimeStamp

    item.UpgraddeDataType = m_item.UpgraddeDataType

    item.TrainNum = Mygol.get_value('TrainNum')
    item.WLFileFlag = Mygol.get_value('WLFileFlag')
    item.DriverOperation =1
    item.DMIOperationTer =1
    item.DriverNum =571
    item.CurVer =1
    item.OrderID = Mygol.get_value('OrderID')
    item.Resrve2 =0



    send_tempdata = struct.pack("<I4HIH2BIQ32sBB", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.WLFileFlag,\
        item.DriverOperation,item.DMIOperationTer,item.DriverNum,item.CurVer,\
        item.OrderID.encode('utf-8') ,item.UpgraddeDataType,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HIH2BIQ32sBBH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.WLFileFlag,\
        item.DriverOperation,item.DMIOperationTer,item.DriverNum,item.CurVer,\
        item.OrderID.encode('utf-8') ,item.UpgraddeDataType,item.Resrve2,item.Crc)
    #数据组包加密


    return send_data

def SN_UpgradePlanCancelled(datatype,m_item):
    item = _SN_UpgradePlanCancelled()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2009
    item.TimeStamp = 0x1111
    item.InfoLen = 62
    item.PacketNum = 0x22

    item.DataType = Mygol.get_value('DataType')

    item.TrainNum = Mygol.get_value('TrainNum')#0x51400 #
    item.WLFileFlag = Mygol.get_value('WLFileFlag')
    item.MessgaeInfo =3
    item.OrderID = Mygol.get_value('OrderID')
    item.Resrve2 =0
    item.UpgrradeVer = Mygol.get_value('UpgradePlanVer') #0x1506110200000000



    send_tempdata = struct.pack("<I4HI2H32sQ2B", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.WLFileFlag,\
        item.MessgaeInfo,item.OrderID.encode('utf-8'),item.UpgrradeVer,item.DataType,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HI2H32sQ2BH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.WLFileFlag,\
        item.MessgaeInfo,item.OrderID.encode('utf-8'),item.UpgrradeVer,item.DataType,item.Resrve2,item.Crc)
    #数据组包加密

    return send_data

def SN_ChangeNotice_UpgradeInfo(datatype,m_item):
    item = _SN_ChangeNotice_UpgradeInfo()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2003
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 78
    item.PacketNum = datatype.PacketNum


    item.TrainNum = Mygol.get_value('TrainNum')
    item.DataToolVersion = 1
    item.UpgradePlanVer = Mygol.get_value('UpgradePlanVer') #0x1506110200000000
    #item.OrderID = '1' #32
    item.FileName = 'param.dat'
    item.FileLen = 1111
    item.Crc48 = '0'
    item.WLFileFlag = Mygol.get_value('WLFileFlag')
    item.FileType= 1
    item.DataType = Mygol.get_value('DataType')

    send_tempdata = struct.pack("<I4H2IQ36sI6sH2B", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.DataToolVersion,\
        item.UpgradePlanVer,item.FileName.encode('utf-8'),item.FileLen,\
        item.Crc48.encode('utf-8'),item.WLFileFlag,item.FileType,item.DataType)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4H2IQ36sI6sH2BH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.DataToolVersion,\
        item.UpgradePlanVer,item.FileName.encode('utf-8'),item.FileLen,\
        item.Crc48.encode('utf-8'),item.WLFileFlag,item.FileType,item.DataType,item.Crc)
    #数据组包加密


    return send_data


def SN_ChangeNotice_ControlInfo(datatype,m_item):
    item = _SN_ChangeNotice_ControlInfo()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2004
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 106
    item.PacketNum = datatype.PacketNum


    item.TrainNum = Mygol.get_value('TrainNum')
    #item.DataToolVersion = 1
    #item.UpgradePlanVer = 1
    item.OrderID = Mygol.get_value('OrderID')#'1' #32
    PlanStartTime = Mygol.get_value('PlanStartTime')
    PlanEffectiveTime = Mygol.get_value('PlanEffectiveTime')
    item.PlanStartTime[0] = PlanStartTime.tm_sec
    item.PlanStartTime[1] = PlanStartTime.tm_min
    item.PlanStartTime[2] = PlanStartTime.tm_hour
    item.PlanStartTime[3] = PlanStartTime.tm_mday
    item.PlanStartTime[4] = PlanStartTime.tm_mon
    item.PlanStartTime[5] = PlanStartTime.tm_year-2000
    item.PlanEffectiveTime[0] = PlanEffectiveTime.tm_sec
    item.PlanEffectiveTime[1] = PlanEffectiveTime.tm_min
    item.PlanEffectiveTime[2] = PlanEffectiveTime.tm_hour
    item.PlanEffectiveTime[3] = PlanEffectiveTime.tm_mday
    item.PlanEffectiveTime[4] = PlanEffectiveTime.tm_mon
    item.PlanEffectiveTime[5] = PlanEffectiveTime.tm_year-2000
    item.VoucherCode = Mygol.get_value('VoucherCode')
    item.UpdataModeType = Mygol.get_value('UpdataModeType') #1:自动更新 2:确认更新 3:凭证码
    item.DeviceType = 1
    item.EjectCount = 0 #连续弹出次数
    #item.WLFileFlag = Mygol.get_value('WLFileFlag')
    item.ShowTime = 5 #显示弹出时间间隔
    item.Resrve1 = 0
    item.Resrve2 = 0
    item.ChangeNoticeReason = "snLKJ-2000(VV测试版本)"

    send_tempdata = struct.pack("<I4HI32s6B6BI4BI32sH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.OrderID.encode('utf-8'),\
        item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],\
        item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],\
        item.PlanEffectiveTime[1],item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],\
        item.PlanEffectiveTime[4],item.PlanEffectiveTime[5],item.VoucherCode,\
        item.UpdataModeType,item.DeviceType,item.EjectCount,item.Resrve1,item.ShowTime,\
        item.ChangeNoticeReason.encode('utf-8'),item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HI32s6B6BI4BI32sHH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.TrainNum,item.OrderID.encode('utf-8'),\
        item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],\
        item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],item.PlanEffectiveTime[1],\
        item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],item.PlanEffectiveTime[4],\
        item.PlanEffectiveTime[5],item.VoucherCode,item.UpdataModeType,item.DeviceType,\
        item.EjectCount,item.Resrve1,item.ShowTime,item.ChangeNoticeReason.encode('utf-8'),\
        item.Resrve2,item.Crc)
    #数据组包加密


    return send_data



def SN_ChangeNotice_StartUpgrade(datatype,m_item):
    item = _SN_ChangeNotice_StartUpgrade()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2006
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 98
    item.PacketNum = datatype.PacketNum

    item.UpdateResult = 1
    item.WLFileFlag = Mygol.get_value('WLFileFlag') #换装标志 1 线路数据 2 控制参数 换装标识

    #item.ParamVerInfo = '1'
    #由Index.dat获取
    #生成软件版本
    #Mygol.get_value()
    item.ParamVerInfo[0] = MyFilegol.get_value("ParamVerInfo[0]")
    item.ParamVerInfo[1] = MyFilegol.get_value("ParamVerInfo[1]")
    item.ParamVerInfo[2] = MyFilegol.get_value("ParamVerInfo[2]")
    item.ParamVerInfo[3] = MyFilegol.get_value("ParamVerInfo[3]")
    #item.ParamVerInfo[3] = 0x02
    #数据格式版本 1.0.0.8
    item.ParamVerInfo[4] = MyFilegol.get_value("ParamVerInfo[4]")
    item.ParamVerInfo[5] = MyFilegol.get_value("ParamVerInfo[5]")
    item.ParamVerInfo[6] = MyFilegol.get_value("ParamVerInfo[6]")
    item.ParamVerInfo[7] = MyFilegol.get_value("ParamVerInfo[7]")
    item.ParamVerInfo[8] = MyFilegol.get_value("ParamVerInfo[8]")
    item.ParamVerInfo[9] = MyFilegol.get_value("ParamVerInfo[9]")
    #生成日期
    item.ParamVerInfo[10] = MyFilegol.get_value("ParamVerInfo[10]")
    item.ParamVerInfo[11] = MyFilegol.get_value("ParamVerInfo[11]")
    item.ParamVerInfo[12] = MyFilegol.get_value("ParamVerInfo[12]")
    item.ParamVerInfo[13] = MyFilegol.get_value("ParamVerInfo[13]")
    item.ParamVerInfo[14] = MyFilegol.get_value("ParamVerInfo[14]")
    item.ParamVerInfo[15] = MyFilegol.get_value("ParamVerInfo[15]")

    #item.K2dataVerInfo = '1'

    #生成软件版本
    item.K2dataVerInfo[0] = MyFilegol.get_value("K2dataVerInfo[0]")
    item.K2dataVerInfo[1] = MyFilegol.get_value("K2dataVerInfo[1]")
    item.K2dataVerInfo[2] = MyFilegol.get_value("K2dataVerInfo[2]")
    item.K2dataVerInfo[3] = MyFilegol.get_value("K2dataVerInfo[3]")
    item.K2dataVerInfo[4] = MyFilegol.get_value("K2dataVerInfo[4]")
    item.K2dataVerInfo[5] = MyFilegol.get_value("K2dataVerInfo[5]")
    #数据格式版本 #无发获取
    item.K2dataVerInfo[6] = 51
    item.K2dataVerInfo[7] = 32
    item.K2dataVerInfo[8] = 16
    item.K2dataVerInfo[9] = 25
    item.K2dataVerInfo[10] = 4
    item.K2dataVerInfo[11] = 21
    #生成日期2kdata.bin  13~16
    item.K2dataVerInfo[12] = MyFilegol.get_value("K2dataVerInfo[12]")
    item.K2dataVerInfo[13] = MyFilegol.get_value("K2dataVerInfo[13]")
    item.K2dataVerInfo[14] = MyFilegol.get_value("K2dataVerInfo[14]")
    item.K2dataVerInfo[15] = MyFilegol.get_value("K2dataVerInfo[15]")
    item.K2dataVerInfo[16] = MyFilegol.get_value("K2dataVerInfo[16]")
    item.K2dataVerInfo[17] = MyFilegol.get_value("K2dataVerInfo[17]")



    item.K2dataSignaCode = 0
    item.BureauNum = MyFilegol.get_value('BureauNum')
    item.ManCode = Mygol.get_value('ManCode')

    item.ParamLen =MyFilegol.get_value('ParamLen')#44604 #从文件中获取
    #item.ParamLen = 0 #长度为0不换装
    item.ParamCRC = MyFilegol.get_value('ParamCRC')#0x077B88ED #从文件中获取
    item.CrcLen = MyFilegol.get_value('CrcLen')#11700
    item.CrcCRC = MyFilegol.get_value('CrcCRC')#0x33878e49
    item.K2dataLen =MyFilegol.get_value('K2dataLen')# 2994944
    item.K2dataCRC = MyFilegol.get_value('K2dataCRC')#0x1f280e08
    item.K2dataXlbLenLen = MyFilegol.get_value('K2dataXlbLenLen')#6720 #
    item.K2dataXlbLenCRC = MyFilegol.get_value('K2dataXlbLenCRC')#0xe572c5fc #需要自己计算CRC
    item.K2dataZmbLenLen = MyFilegol.get_value('K2dataZmbLenLen')#0x59568
    item.K2dataZmbLenCRC =MyFilegol.get_value('K2dataZmbLenCRC')#0x25b297fd
    item.Resrve2 = 0
    send_tempdata = struct.pack("<I4H2H16B18BI2B10IH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.UpdateResult,item.WLFileFlag,\
        item.ParamVerInfo[0],item.ParamVerInfo[1],item.ParamVerInfo[2],\
        item.ParamVerInfo[3],item.ParamVerInfo[4],item.ParamVerInfo[5],\
        item.ParamVerInfo[6],item.ParamVerInfo[7],item.ParamVerInfo[8],\
        item.ParamVerInfo[9],item.ParamVerInfo[10],item.ParamVerInfo[11],\
        item.ParamVerInfo[12],item.ParamVerInfo[13],item.ParamVerInfo[14],\
        item.ParamVerInfo[15],item.K2dataVerInfo[0],item.K2dataVerInfo[1],\
        item.K2dataVerInfo[2],item.K2dataVerInfo[3],item.K2dataVerInfo[4],\
        item.K2dataVerInfo[5],item.K2dataVerInfo[6],item.K2dataVerInfo[7],\
        item.K2dataVerInfo[8],item.K2dataVerInfo[9],item.K2dataVerInfo[10],\
        item.K2dataVerInfo[11],item.K2dataVerInfo[12],item.K2dataVerInfo[13],\
        item.K2dataVerInfo[14],item.K2dataVerInfo[15],item.K2dataVerInfo[16],\
        item.K2dataVerInfo[17],item.K2dataSignaCode,item.BureauNum,item.ManCode,\
        item.ParamLen,item.ParamCRC,item.CrcLen,item.CrcCRC,item.K2dataLen,\
        item.K2dataCRC,item.K2dataXlbLenLen,item.K2dataXlbLenCRC,item.K2dataZmbLenLen,\
        item.K2dataZmbLenCRC,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4H2H16B18BI2B10IHH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.UpdateResult,item.WLFileFlag,\
        item.ParamVerInfo[0],item.ParamVerInfo[1],item.ParamVerInfo[2],item.ParamVerInfo[3],\
        item.ParamVerInfo[4],item.ParamVerInfo[5],item.ParamVerInfo[6],item.ParamVerInfo[7],\
        item.ParamVerInfo[8],item.ParamVerInfo[9],item.ParamVerInfo[10],item.ParamVerInfo[11],\
        item.ParamVerInfo[12],item.ParamVerInfo[13],item.ParamVerInfo[14],item.ParamVerInfo[15],\
        item.K2dataVerInfo[0],item.K2dataVerInfo[1],item.K2dataVerInfo[2],item.K2dataVerInfo[3],\
        item.K2dataVerInfo[4],item.K2dataVerInfo[5],item.K2dataVerInfo[6],item.K2dataVerInfo[7],\
        item.K2dataVerInfo[8],item.K2dataVerInfo[9],item.K2dataVerInfo[10],item.K2dataVerInfo[11],\
        item.K2dataVerInfo[12],item.K2dataVerInfo[13],item.K2dataVerInfo[14],item.K2dataVerInfo[15],\
        item.K2dataVerInfo[16],item.K2dataVerInfo[17],item.K2dataSignaCode,item.BureauNum,item.ManCode,\
        item.ParamLen,item.ParamCRC,item.CrcLen,item.CrcCRC,item.K2dataLen,item.K2dataCRC,\
        item.K2dataXlbLenLen,item.K2dataXlbLenCRC,item.K2dataZmbLenLen,item.K2dataZmbLenCRC,\
        item.Resrve2,item.Crc)
    #数据组包加密


    return send_data

def SN_HostEventInfoReply(datatype,m_item):
    item = _SN_HostEventInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x200A
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 14
    item.PacketNum = datatype.PacketNum

    item.ReplyEventType = 1

    send_tempdata = struct.pack("<I4HH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.ReplyEventType)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<I4HHH", item.TimeStamp,item.PacketType,\
        item.InfoLen,item.PacketNum,item.Resrve,item.ReplyEventType,item.Crc)
    #数据组包加密


    return send_data
