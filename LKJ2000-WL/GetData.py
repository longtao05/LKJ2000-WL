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
from WLTypeDef import  _ActiDetectionInfo ,_UpgradeRequestInfo ,_UpgradeOperationInfo


#10 02 A5 18 00 01 11 10 00 01 0f 00 05 00 12 34 05 00 12 34 03 03 01 00 01 0B 0C 05 01 A8 B6 5A 10 03
def ActiDetectionInfo(data_Effbytes):
    i = 0
    item = _ActiDetectionInfo()

    item.IdNum = struct.unpack('<H',data_Effbytes[i+6:i+8])[0]
    item.TrainNumA = struct.unpack('<I',data_Effbytes[i+8:i+12])[0]
    item.TrainNumB = struct.unpack('<I',data_Effbytes[i+12:i+16])[0]
    item.ManCode = struct.unpack('<B',data_Effbytes[i+16:i+17])[0]
    item.RoadStationCode = struct.unpack('<B',data_Effbytes[i+17:i+18])[0]
    item.ProtocolVer = struct.unpack('<H',data_Effbytes[i+18:i+20])[0]
    item.DeviceType = struct.unpack('<B',data_Effbytes[i+20:i+21])[0]
    item.LocoModelA = struct.unpack('<B',data_Effbytes[i+21:i+22])[0]
    item.LocoModelB = struct.unpack('<B',data_Effbytes[i+22:i+23])[0]
    item.LKJDeviceStatus = struct.unpack('<B',data_Effbytes[i+23:i+24])[0]
    item.ReloadingStatus = struct.unpack('<B',data_Effbytes[i+24:i+25])[0]

    return item

#10 02 A5 08 00 01 01 20 01 01 01 A8 B6 5A 10 03
def UpgradeRequestInfo(data_Effbytes):
    i = 0
    item = _UpgradeRequestInfo()
    item.DataType = struct.unpack('<B',data_Effbytes[i+6:i+7])[0]
    item.IdNum = struct.unpack('<B',data_Effbytes[i+7:i+8])[0]


    return item

#10 02 08 00 01 03 20 01 01 01 A8 B6 10 03
def UpgradeOperationInfo(data_Effbytes):
    i = 0
    item = _UpgradeOperationInfo()
    item.DataType = struct.unpack('<B',data_Effbytes[i+6:i+7])[0]
    item.IdNum = struct.unpack('<B',data_Effbytes[i+7:i+8])[0]


    return item


