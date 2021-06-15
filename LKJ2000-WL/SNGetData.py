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
from SNWLTypeDef import _SN_VersionInfoPackage ,_SN_ActiDetectionInfo ,_SN_UpgradeRequestInfo,_SN_UpgradeOperationInfo ,_SN_WLActiDetectionInfo,_SN_VersionConfirmInfo,_SN_UpgradePlanCancelledReply,_SN_HostEventInfo

'''
1002 1111 1111 0110  005a 0001 0000 0000
b0f0 2103 0121 0333 0300 2020 2020 0460
0120 0000 2000 0153 0546 9934 0547 0997
1000 0037 7300 2695 0000 0048 0000 0000
0000 0000 0048 0597 0002 0601 0044 9800
0122 1501 2239 2020 0108 2012 0700 0100 3322 1003
'''
def SN_VersionInfoPackage(data_Effbytes):

    item = _SN_VersionInfoPackage()
    byteOffset = 12
    byteNum = 4
    item.LKJVersion = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DMI1Ver = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DMI2Ver = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 16
    i=1
    for i in range(byteNum):
        item.ParamVer[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    #byteOffset = byteOffset + byteNum

    byteNum = 18
    i=1
    for i in range(byteNum):
        item.k2DataVer[i-1] =struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1

    byteNum = 2
    item.Resrve1 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum

    byteNum = 4
    item.DMI1xlbVer = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum

    byteNum = 4
    item.DMI1zmbVer = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DMI2xlbVer = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DMI2zmbVer = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.BureauNum = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.ALocoModel = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.ATrainNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.BLocoModel = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.BTrainNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.DeviceNum = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.LocoType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum +1  #预留
    byteNum = 2
    item.CommProVer = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.ManCode = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.DeviceType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item

'''
1002 11 1111 11 0210 005a 0001 00 0000 00
b0f0 2103 0121 0333 0300 2020 2020 0460

1000 0037

0122 1501 2239 2020 0108 2012 0700 0100 3322 1003
'''
def SN_ActiDetectionInfo(data_Effbytes):

    item = _SN_VersionInfoPackage()
    byteOffset = 12
    '''byteNum = 1
                item.IdNum = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum'''
    byteNum = 1
    item.ChangeConInfo = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.ChangeStatusInfo = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Model = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.LKJDeviceStatus = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum

    byteNum = 2
    item.Speed = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.LampPosition = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.TiuData = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.ParkingSta = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.DMIConfig = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.TrainType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Primary = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.SideNum = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.BranchNum = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.LKJWUStatus = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.OrgVoltage = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.OrgCurrent = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.DieSpeedAnoma = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.LCGPressure = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.ZDGPressure = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.JHFG1Pressure = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.JHFG2Pressure = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Resrve1 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.KIMData = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.CurTime = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item


'''
1002 0000 0310 0011 1111 110D 0001 0001
0200 0000 00 0000 0000 0000 3322 1003
'''
def SN_UpgradeRequestInfo(data_Effbytes):

    item = _SN_UpgradeRequestInfo()
    byteOffset = 12
    byteNum = 2
    item.MessgaeRece = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    '''
    byteNum = 1
    item.DataType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.IdNum = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Resrve1 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.TrainNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    '''
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item




'''
1002 0000 0410 0011 1111 1146 0001 00
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000
3322 1003
'''
def SN_UpgradeOperationInfo(data_Effbytes):

    item = _SN_UpgradeOperationInfo()
    byteOffset = 12
    byteNum = 1
    item.DataType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Resrve2 = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Resrve1 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 32
    i=1
    for i in range(byteNum):
        item.OrderID[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1

    byteNum = 4
    item.LocoNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.VoucherCode = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DriverNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 6
    i=1
    for i in range(byteNum):
        item.OperationTime[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1

    byteNum = 1
    item.OperationType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.DMIOperationTer = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.WLFileFlag = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item

'''
1002 0000 0510 0011 1111 1146 0001 00
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000 0000 0000
0102 0000 0000 0000 0000 0000
3322 1003
'''
def SN_StartUpgradeOperationInfoReply(data_Effbytes):

    item = _SN_StartUpgradeOperationInfoReply()
    byteOffset = 12
    byteNum = 2
    item.MessgaeRece = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item


'''
1002 00000610d00300001400290000000700000000003e7f 1003
'''
def SN_WLActiDetectionInfo(data_Effbytes):

    item = _SN_WLActiDetectionInfo()
    byteOffset = 12

    byteNum = 1
    item.LKJDeviceStatus = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.LKJWUStatus = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.ChangeStatusInfo = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Resrve1 = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.ChangeSpeed = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.DMIChangeSpeed = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2

    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item

'''
1002

0000 0710 6aea0000 1400 a20b 00 00 07 00 0000 0000 e11f
1003
'''
def SN_VersionConfirmInfo(data_Effbytes):

    item = _SN_VersionConfirmInfo()
    byteOffset = 12
    byteNum = 1
    item.UpgraddeDataType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Resrve11 = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Resrve1 = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.TrainNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 16
    i=1
    for i in range(byteNum):
        item.ParamVer[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    #byteOffset = byteOffset + byteNum
    byteNum = 18
    i=1
    for i in range(byteNum):
        item.k2DataVer[i-1] =struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    byteNum = 2
    item.FileWLFlag = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 4
    item.DriverNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 6
    i=1
    for i in range(byteNum):
        item.OperationTime[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    byteNum = 1
    item.DriverOperation = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.DMIOperationTer = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 32
    i=1
    for i in range(byteNum):
        item.OrderID[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    byteNum = 2
    item.Resrve2 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item

'''
1002
0000 0810 11110000 3a00 2200 01 22 33 00 4400450046004700480049004a004b004c004d004e004f005000510052005300
00000000 0000 0200 0000 128b
1003
'''
def SN_UpgradePlanCancelledReply(data_Effbytes):

    item = _SN_UpgradePlanCancelledReply()
    byteOffset = 12
    byteNum = 1
    item.CancelDataType = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    '''byteNum = 1
    item.IdNum = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.IdNumReply = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum'''
    byteNum = 2
    item.Resrve11 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 1
    item.Resrve1 = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+byteNum])[0]

    byteOffset = byteOffset + byteNum
    byteNum = 32
    i=1
    for i in range(byteNum):
        item.OrderID[i-1] = struct.unpack('<B',data_Effbytes[byteOffset:byteOffset+1])[0]
        i+=1
        byteOffset+=1
    byteNum = 4
    item.TrainNum = struct.unpack('<I',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.FileWLFlag = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.CancelRelust = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 8
    item.UpgrradeVer = struct.unpack('<Q',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Resrve2 = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum

    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item

def SN_HostEventInfo(data_Effbytes):

    item = _SN_HostEventInfo()
    byteOffset = 12
    byteNum = 2
    item.EventType = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    byteOffset = byteOffset + byteNum
    byteNum = 2
    item.Crc = struct.unpack('<H',data_Effbytes[byteOffset:byteOffset+byteNum])[0]
    return item
