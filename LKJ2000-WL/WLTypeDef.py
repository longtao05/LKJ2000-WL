import sys
import binascii
from ctypes import *
from enum import Enum
import struct


#数据格式
 #信息长度：2 源通信地址：1 目的通信地址：1 业务类型：1 命令：1 数据：n CRC16:2
class _DataType(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("Crc",c_ushort)]
#活动性检测帧
class _ActiDetectionInfo(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("IdNum",c_ushort),
              ("TrainNumA",c_uint),
              ("TrainNumB",c_uint),
              ("RoadStationCode",c_ubyte),
              ("ManCode",c_ubyte),
              ("ProtocolVer",c_ushort),
              ("DeviceType",c_ubyte),
              ("LocoModelA",c_ubyte),
              ("LocoModelB",c_ubyte),
              ("LKJDeviceStatus",c_ubyte),
              ("ReloadingStatus",c_ubyte),
              ("Crc",c_ushort)]
#活动性检测应答
class _ActiDetectionInfoReply(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("IdNum",c_ushort),
              ("TrainNum",c_uint),
              ("ManCode",c_ubyte),
              ("RoadStationCode",c_ubyte),
              ("DeviceId",c_ubyte*6),
              ("DataReady",c_ubyte),
              ("WLDataCacheComp",c_ubyte),#预留
              ("WLRegiStatus",c_ubyte),#预留
              ("Crc",c_ushort)]

#升级信息请求
class _UpgradeRequestInfo(Structure):
  _pack_=1
  _fields_ = [("DataType",c_ubyte),
              ("IdNum",c_ubyte),
               ("Crc",c_ushort)]

#升级信息发送
class _UpgradeInfoSend(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("BoolTask",c_ubyte),
              ("UpgradePlanVer",c_ubyte*7),#V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("FileNameLen",c_ubyte),
              ("FileName",c_ubyte*2),#长度预留
              ("FileLen",c_uint),
              ("Crc48",c_ubyte*6),
              ("PlanStartTime",c_ubyte*6),#高到低 年月日时分秒 高字节在前
              ("PlanEffectiveTime",c_ubyte*6),
              ("FileCompilationDate",c_ubyte*4),#年月日 子版本
              ("DataToolVersion",c_ubyte*7),
              ("VoucherCode",c_uint),
              ("UpdataModeType",c_ubyte),
              ("WlrdReason",c_wchar_p), #32字节的ASCII码字符串
               ("Crc",c_ushort)]

#升级信息应答
class _UpgradeInfoReply(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("DataType",c_ubyte),
              ("FileCompilationDate",c_ubyte*4),#年月日 子版本
              ("DataToolVersion",c_ubyte*7),
              ("VoucherCode",c_uint),
              ("UpdataModeType",c_ubyte),
              ("IdNum",c_ubyte),
              ("Crc",c_ushort)
              ]

#升级操作信息发送
class _UpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              #("TrainNum",c_ubyte*5),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("OrderID",c_wchar_p),#32字节
              ("LocoNum",c_uint),
              ("VoucherCode",c_uint),
              ("DriverNum",c_uint),
              ("OperationTime",c_ubyte*6),
              ("OperationType",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("Crc",c_ushort)
              ]
#升级操作信息应答
class _UpgradeOperationInfoReply(Structure):
  _pack_=1
  _fields_ = [("InfoLen",c_ushort),#2bitys
              ("StartAddr",c_ubyte),#1bitys
              ("EndAddr",c_ubyte),
              ("BusinessType",c_ubyte),
              ("Order",c_ubyte),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("OrderID",c_wchar_p),#32字节
              ("LocoNum",c_uint),
              ("IsCanUpgrade",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("Crc",c_ushort)
              ]
#启动升级信息
class _StartUpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("DataReady",c_ubyte),
              ("Reserve",c_ubyte*5),
              ("ParamLen",c_uint),
              ("ParamCRC",c_uint),
              ("2KdataLen",c_uint),
              ("2KdataCRC",c_uint),
              ("CrcLen",c_uint),
              ("CrcCRC",c_uint),
              ("2KdataXlbLen",c_uint),
              ("2KdataXlbLenCRC",c_uint),
              ("2KdataZmbLen",c_uint),
              ("2KdataZmbLenCRC",c_uint)]
#启动升级信息
class _StartUpgradeOperationInfoReply(Structure):
  _pack_=1
  _fields_ = [("DataType",c_ubyte),
              ("IdNum",c_ubyte)
             ]

#版本确认信息发送
class _VersionConfirmInfo(Structure):
  _pack_=1
  _fields_ = [("TrainNum",c_ubyte*5),
              ("UpgraddeDataType",c_ubyte),
              ("UpgradePlanVer",c_ubyte*7),#V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("VoucherCode",c_uint),
              ("DriverOperation",c_ubyte),
              ("DriverNum",c_uint),
              ("OperationTime",c_ubyte*6),
              ("DMIOperationTer",c_ubyte),
              ("IdNum",c_ubyte)
              ]
#升级计划取消包
class _UpgradePlanCancelled(Structure):
  _pack_=1
  _fields_ = [("TrainNum",c_uint),
              ("CancelDataType",c_ubyte),
              ("CancelPlanVer",c_ubyte*7),#V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("VoucherCode",c_uint),
              ("IdNum",c_ubyte)
              ]
#升级计划取消包应答
class _UpgradePlanCancelledReply(Structure):
  _pack_=1
  _fields_ = [("TrainNum",c_uint),
              ("CancelDataType",c_ubyte),
              ("CancelPlanVer",c_ubyte*7),#V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("VoucherCode",c_uint),
              ("IdNum",c_ubyte)
              ]


'''
item = DataType(259,44,33)

itsci = TSciParseInfo()

itsci.szTempData[0] = item.InfoLen&0xff
itsci.szTempData[1] = (item.InfoLen&0xff)<<8

print(item.InfoLen)
print(itsci.szTempData[0])
print(itsci.szTempData[1])
'''


