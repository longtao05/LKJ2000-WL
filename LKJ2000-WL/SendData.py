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
from WLTypeDef import _ActiDetectionInfoReply,_UpgradeRequestInfo ,_UpgradeInfoSend


def ActiDetectionInfoReply(datatype,m_item):
    item = _ActiDetectionInfoReply()
    item.InfoLen = 87
    item.StartAddr = datatype.EndAddr
    item.EndAddr = datatype.StartAddr
    item.BusinessType = 0x10
    item.Order = 0x02
    item.IdNum =m_item.IdNum #struct.unpack('<H',data_Effbytes[i+6:i+8])[0]
    item.TrainNum =m_item.TrainNumA
    item.ManCode =m_item.ManCode
    item.RoadStationCode = m_item.RoadStationCode
    item.DeviceId[0] = 0x11#设备ID
    item.DeviceId[1] = 0x22#设备ID
    item.DeviceId[2] = 0x33#设备ID
    item.DeviceId[3] = 0x44#设备ID
    item.DeviceId[4] = 0x55#设备ID
    item.DeviceId[5] = 0x66#设备ID
    item.WLDataCacheComp = 0;#预留
    item.WLRegiStatus = 0;#预留

    send_tempdata = struct.pack("<H4BHI2B6B2B", item.InfoLen,item.StartAddr,item.EndAddr,item.BusinessType,item.Order,item.IdNum,item.TrainNum,item.ManCode,item.RoadStationCode,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLDataCacheComp,item.WLRegiStatus)

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("<H4BHI2B6B2BH", item.InfoLen,item.StartAddr,item.EndAddr,item.BusinessType,item.Order,item.IdNum,item.TrainNum,item.ManCode,item.RoadStationCode,item.DeviceId[0],item.DeviceId[1],item.DeviceId[2],item.DeviceId[3],item.DeviceId[4],item.DeviceId[5],item.WLDataCacheComp,item.WLRegiStatus,item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data


'''item = _UpgradeInfoSend()

item.WlrdReason = "hi,您好"

print(sizeof(item))
print(item.WlrdReason)'''

def UpgradeInfoSend(datatype,m_item):
    item = _UpgradeInfoSend()
    item.InfoLen = sizeof(item) + 6
    item.StartAddr = datatype.EndAddr
    item.EndAddr = datatype.StartAddr
    item.BusinessType = 0x10
    item.Order = 0x02
    item.DataType =m_item.DataType #1:LKJ2000 2：程序 3：LKJ15
    item.IdNum =m_item.IdNum #struct.unpack('<H',data_Effbytes[i+6:i+8])[0]
    item.BoolTask =1
    item.UpgradePlanVer[0] =0x01
    item.UpgradePlanVer[1] =0x02
    item.UpgradePlanVer[2] =0x00
    item.UpgradePlanVer[3] =0x15
    item.UpgradePlanVer[4] =0x04
    item.UpgradePlanVer[5] =0x0e
    item.UpgradePlanVer[6] =0x00
    item.FileNameLen = 2
    item.FileName[0] = 8
    item.FileName[1] = 8
    item.FileLen = 2
    item.Crc48[0] = 0
    item.Crc48[1] = 0
    item.Crc48[2] = 0
    item.Crc48[3] = 0
    item.Crc48[4] = 0
    item.Crc48[5] = 0

    item.PlanStartTime[0] =0x01
    item.PlanStartTime[1] =0x02
    item.PlanStartTime[2] =0x00
    item.PlanStartTime[3] =0x15
    item.PlanStartTime[4] =0x04
    item.PlanStartTime[5] =0x01

    item.PlanEffectiveTime[0] =0x15
    item.PlanEffectiveTime[1] =0x04
    item.PlanEffectiveTime[2] =0x01
    item.PlanEffectiveTime[3] =0x01
    item.PlanEffectiveTime[4] =0x02
    item.PlanEffectiveTime[5] =0x03

    item.FileCompilationDate[0] =0x15
    item.FileCompilationDate[1] =0x04
    item.FileCompilationDate[2] =0x01
    item.FileCompilationDate[3] =0x01

    item.DataToolVersion[0] =0x01
    item.DataToolVersion[1] =0x03
    item.DataToolVersion[2] =0x00
    item.DataToolVersion[3] =0x15
    item.DataToolVersion[4] =0x04
    item.DataToolVersion[5] =0x01

    item.VoucherCode = 0x5555
    item.UpdataModeType = 3
    item.WlrdReason = '数据升级,更新版本'



    send_tempdata = struct.pack("<H7B7B3BI29BIB32s", item.InfoLen,item.StartAddr,item.EndAddr,item.BusinessType,item.Order,item.DataType,item.IdNum,item.BoolTask,item.UpgradePlanVer[0],item.UpgradePlanVer[1],item.UpgradePlanVer[2],item.UpgradePlanVer[3],item.UpgradePlanVer[4],item.UpgradePlanVer[5],item.UpgradePlanVer[6],item.FileNameLen,item.FileName[0],item.FileName[1],item.FileLen ,item.Crc48[0],item.Crc48[1],item.Crc48[2],item.Crc48[3],item.Crc48[4],item.Crc48[5],item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],item.PlanEffectiveTime[1],item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],item.PlanEffectiveTime[4],item.PlanEffectiveTime[5],item.FileCompilationDate[0],item.FileCompilationDate[1],item.FileCompilationDate[2],item.FileCompilationDate[3],item.DataToolVersion[0],item.DataToolVersion[1],item.DataToolVersion[2],item.DataToolVersion[3],item.DataToolVersion[4],item.DataToolVersion[5],item.DataToolVersion[6], item.VoucherCode,item.UpdataModeType,item.WlrdReason.encode('utf-8'))

    send_tempdata = bytesToHexString(send_tempdata)
    item.Crc = crc16(send_tempdata)

    send_data = struct.pack("H7B7B3BI29BIB32sH", item.InfoLen,item.StartAddr,item.EndAddr,item.BusinessType,item.Order,item.DataType,item.IdNum,item.BoolTask,item.UpgradePlanVer[0],item.UpgradePlanVer[1],item.UpgradePlanVer[2],item.UpgradePlanVer[3],item.UpgradePlanVer[4],item.UpgradePlanVer[5],item.UpgradePlanVer[6],item.FileNameLen,item.FileName[0],item.FileName[1],item.FileLen ,item.Crc48[0],item.Crc48[1],item.Crc48[2],item.Crc48[3],item.Crc48[4],item.Crc48[5],item.PlanStartTime[0],item.PlanStartTime[1],item.PlanStartTime[2],item.PlanStartTime[3],item.PlanStartTime[4],item.PlanStartTime[5],item.PlanEffectiveTime[0],item.PlanEffectiveTime[1],item.PlanEffectiveTime[2],item.PlanEffectiveTime[3],item.PlanEffectiveTime[4],item.PlanEffectiveTime[5],item.FileCompilationDate[0],item.FileCompilationDate[1],item.FileCompilationDate[2],item.FileCompilationDate[3],item.DataToolVersion[0],item.DataToolVersion[1],item.DataToolVersion[2],item.DataToolVersion[3],item.DataToolVersion[4],item.DataToolVersion[5],item.DataToolVersion[6], item.VoucherCode,item.UpdataModeType,item.WlrdReason.encode('utf-8'),item.Crc)
    #数据组包加密
    send_data = send_data_package(send_data)
    return send_data
