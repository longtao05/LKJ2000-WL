
#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time
from CRC import *
from Comm import *
from Package import *
from SNWLTypeDef import _SN_VersionInfoPackageReply ,_SN_ActiDetectionInfoReply ,_SN_UpgradeInfoSend,_SN_UpgradeOperationInfoReply,_SN_StartUpgradeOperationInfo ,_SN_WLActiDetectionInfoReply,_SN_VersionConfirmInfoReply,_SN_UpgradePlanCancelled




def SN_VersionInfoPackageReply(datatype,m_item):
    item = _SN_VersionInfoPackageReply()
    item.Resrve = 0x0000 # 预留字节
    item.PacketType = 0x2001
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 14
    item.PacketNum = datatype.PacketNum
    item.CommProVer = m_item.CommProVer #是否更改

    send_tempdata = struct.pack("<2HI3H", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.CommProVer)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI3HH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.CommProVer,item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data


def SN_ActiDetectionInfoReply(datatype,m_item):
    item = _SN_ActiDetectionInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2002
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 30
    item.PacketNum = m_item.TimeStamp

    item.IdNum = m_item.IdNum
    item.IdNumReply = m_item.IdNum +1
    item.Resrve1 =0
    item.TrainNum = 0x4000D8
    item.ManCode = 0x04
    item.Resrve2 =0

    item.DeviceId[0] =0x01
    item.DeviceId[1] =0x02
    item.DeviceId[2] =0x03
    item.DeviceId[3] =0x04
    item.DeviceId[4] =0x05
    item.DeviceId[5] =0x06
    item.WLRegiStatus =1
    item.Resrve3 =0


    send_tempdata = struct.pack("<2HI2H2BHI10B", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.ManCode,item.Resrve2,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.Resrve3)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H2BHI10BH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.ManCode,item.Resrve2,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.Resrve3,item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data

'''item = _SN_UpgradeInfoSend()
print(sizeof(item))
print(struct.calcsize('2HI2H3BHIIQ32B36BI6B6B6B2BI2B3H'))
print(struct.calcsize('Q'))'''

def SN_UpgradeInfoSend(datatype,m_item):
    item = _SN_UpgradeInfoSend()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2003
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 138
    item.PacketNum = datatype.PacketNum

    item.DataType = 1
    item.IdNum = m_item.IdNum
    item.IdNumReply = item.IdNum +1
    item.Resrve1 = 0
    item.TrainNum = 1
    item.DataToolVersion = 1
    item.UpgradePlanVer = 1
    item.OrderID = '1' #32
    item.FileName = '2kdata.bin'
    item.FileLen = 1111
    item.Crc48 = '0'
    item.PlanStartTime[0] = 1
    item.PlanStartTime[1] = 2
    item.PlanStartTime[2] = 3
    item.PlanStartTime[3] = 4
    item.PlanStartTime[4] = 5
    item.PlanStartTime[5] = 6
    item.PlanEffectiveTime[0] = 1
    item.PlanEffectiveTime[1] = 2
    item.PlanEffectiveTime[2] = 3
    item.PlanEffectiveTime[3] = 4
    item.PlanEffectiveTime[4] = 5
    item.PlanEffectiveTime[5] = 6
    item.UpdataModeType = 1
    item.VoucherCode = 1
    item.FileType = 1
    item.EjectCount = 1
    item.FileWLFlag = 1
    item.ShowTime = 1
    item.Resrve2 = 0

    send_tempdata = struct.pack("<2HI2H3BHIIQ32s36sI6s6B6B2BI2BHIH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.DataToolVersion,item.UpgradePlanVer,item.OrderID.encode('utf-8'),item.FileName.encode('utf-8'),item.FileLen,item.Crc48.encode('utf-8'),item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],item.PlanEffectiveTime[1],item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],item.PlanEffectiveTime[4],item.PlanEffectiveTime[5],item.UpdataModeType,item.DeviceType,item.VoucherCode,item.FileType,item.EjectCount,item.FileWLFlag,item.ShowTime,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H3BHIIQ32s36sI6s6B6B2BI2BHIHH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.DataToolVersion,item.UpgradePlanVer,item.OrderID.encode('utf-8'),item.FileName.encode('utf-8'),item.FileLen,item.Crc48.encode('utf-8'),item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],item.PlanEffectiveTime[1],item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],item.PlanEffectiveTime[4],item.PlanEffectiveTime[5],item.UpdataModeType,item.DeviceType,item.VoucherCode,item.FileType,item.EjectCount,item.FileWLFlag,item.ShowTime,item.Resrve2,item.Crc)
    #数据组包加密

    send_data = send_data_package(send_data)
    return send_data

def SN_UpgradeOperationInfoReply(datatype,m_item):
    item = _SN_UpgradeOperationInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2004
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 58
    item.PacketNum = datatype.PacketNum

    item.DataType = 1
    item.IdNum = m_item.IdNum
    item.IdNumReply = item.IdNum +1
    item.Resrve1 = 0
    item.OrderID = '1' #32
    item.LocoNum = 216
    item.WLFileFlag = 1

    item.DMIOperationTer = 1
    item.IsCanUpgrade = 0
    item.Resrve2 = 0

    send_tempdata = struct.pack("<2HI2H3BH32sIH2BH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.OrderID.encode('utf-8'),item.LocoNum,item.WLFileFlag,item.DMIOperationTer,item.IsCanUpgrade,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H3BH32sIH2BHH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.OrderID.encode('utf-8'),item.LocoNum,item.WLFileFlag,item.DMIOperationTer,item.IsCanUpgrade,item.Resrve2,item.Crc)
    #数据组包加密

    send_data = send_data_package(send_data)
    return send_data


def SN_StartUpgradeOperationInfo(datatype,m_item):
    item = _SN_StartUpgradeOperationInfo()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2005
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 94
    item.PacketNum = datatype.PacketNum

    item.UpdateResult = 1
    item.WLFileFlag = 1

    item.ParamVerInfo = '1'
    item.K2dataVerInfo = '1'
    item.Resrve1 = 0
    item.ParamCRC = 2
    item.CrcCRC = 2
    item.K2dataCRC = 2
    item.K2dataXlbLenCRC = 2
    item.K2dataZmbLenCRC = 2
    item.Resrve2 = 0
    send_tempdata = struct.pack("<2HI2H2H16s18sH5QH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.UpdateResult,item.WLFileFlag,item.ParamVerInfo.encode('utf-8'),item.K2dataVerInfo.encode('utf-8'),item.Resrve1,item.ParamCRC,item.CrcCRC,item.K2dataCRC,item.K2dataXlbLenCRC,item.K2dataZmbLenCRC,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H2H16s18sH5QHH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.UpdateResult,item.WLFileFlag,item.ParamVerInfo.encode('utf-8'),item.K2dataVerInfo.encode('utf-8'),item.Resrve1,item.ParamCRC,item.CrcCRC,item.K2dataCRC,item.K2dataXlbLenCRC,item.K2dataZmbLenCRC,item.Resrve2,item.Crc)
    #数据组包加密

    send_data = send_data_package(send_data)
    return send_data

def SN_WLActiDetectionInfoReply(datatype,m_item):
    item = _SN_ActiDetectionInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2006
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 30
    item.PacketNum = m_item.TimeStamp

    item.IdNum = m_item.IdNum
    item.IdNumReply = m_item.IdNum +1
    item.Resrve1 =0
    item.TrainNum = 0x4000D8
    item.ManCode = 0x04
    item.Resrve2 =0

    item.DeviceId[0] =0x01
    item.DeviceId[1] =0x02
    item.DeviceId[2] =0x03
    item.DeviceId[3] =0x04
    item.DeviceId[4] =0x05
    item.DeviceId[5] =0x06
    item.WLRegiStatus =1
    item.Resrve3 =0


    send_tempdata = struct.pack("<2HI2H2BHI10B", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.ManCode,item.Resrve2,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.Resrve3)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H2BHI10BH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.ManCode,item.Resrve2,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLRegiStatus,item.Resrve3,item.Crc)

    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data


def SN_VersionConfirmInfoReply(datatype,m_item):
    item = _SN_VersionConfirmInfoReply()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2007
    item.TimeStamp = datatype.TimeStamp
    item.InfoLen = 66 +64
    item.PacketNum = m_item.TimeStamp

    item.UpgraddeDataType = m_item.UpgraddeDataType
    item.IdNum = m_item.IdNum
    item.IdNumReply = m_item.IdNum +1
    item.Resrve1 =0
    item.TrainNum = 0x4000D8
    item.FileWLFlag = 1
    item.DriverOperation =1
    item.DMIOperationTer =1
    item.DriverNum =571
    item.CurVer =1
    item.OrderID = '1'
    item.Resrve2 =0
    #测试
    item.Resrve3 ='1'


    send_tempdata = struct.pack("<2HI2H4BIH2BIQ32sH128s", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.UpgraddeDataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.FileWLFlag,item.DriverOperation,item.DMIOperationTer,item.DriverNum,item.CurVer,item.OrderID.encode('utf-8') ,item.Resrve2,item.Resrve3.encode('utf-8'))

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H4BIH2BIQ32sH128sH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.UpgraddeDataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.FileWLFlag,item.DriverOperation,item.DMIOperationTer,item.DriverNum,item.CurVer,item.OrderID.encode("utf-8") ,item.Resrve2,item.Resrve3.encode('utf-8'),item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)

    return send_data

def SN_UpgradePlanCancelled():
    item = _SN_UpgradePlanCancelled()
    item.Resrve = 0 # 预留字节
    item.PacketType = 0x2008
    item.TimeStamp = 0x1111
    item.InfoLen = 58
    item.PacketNum = 0x22

    item.DataType = 1
    item.IdNum = 2
    item.IdNumReply = 3
    item.Resrve1 =0
    item.TrainNum = 0x4000D8
    item.FileWLFlag = 1
    item.MessgaeInfo =3
    item.OrderID = '1'
    item.Resrve2 =0



    send_tempdata = struct.pack("<2HI2H4BI2H32sH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.FileWLFlag,item.MessgaeInfo,item.OrderID.encode('utf-8') ,item.Resrve2)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<2HI2H4BI2H32sHH", item.Resrve,item.PacketType,item.TimeStamp,item.InfoLen,item.PacketNum,item.DataType,item.IdNum,item.IdNumReply,item.Resrve1,item.TrainNum,item.FileWLFlag,item.MessgaeInfo,item.OrderID.encode('utf-8') ,item.Resrve2,item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data
