import sys
import binascii
from ctypes import *
from enum import Enum
import struct

#数据格式
 #信息长度：2 源通信地址：1 目的通信地址：1 业务类型：1 命令：1 数据：n CRC16:2
class _SN_DataType(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),
              ("PacketNum",c_ushort),
              ("Crc",c_ushort)]



#版本信息报
class _SN_VersionInfoPackage(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#90
              ("PacketNum",c_ushort),
              ("LKJVersion",c_uint),
              ("DMI1Ver",c_uint),
              ("DMI2Ver",c_uint),
              ("ParamVer",c_ubyte*16),#16 #V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("k2DataVer",c_ubyte*18),#18
              ("Resrve1",c_ushort),#预留
              ("DMI1xlbVer",c_uint),
              ("DMI1zmbVer",c_uint),
              ("DMI2xlbVer",c_uint),
              ("DMI2zmbVer",c_uint),
              ("BureauNum",c_ushort),#局号
              ("ALocoModel",c_ushort),#机车型号
              ("ATrainNum",c_uint),
              ("BLocoModel",c_ushort),#机车型号
              ("BTrainNum",c_uint),
              ("DeviceNum",c_ushort),#机车号
              ("LocoType",c_ubyte),#机车类型
              ("Resrve2",c_ubyte),#机车类型
              ("CommProVer",c_ushort),
              ("Crc",c_ushort)]


#版本信息报
class _SN_VersionInfoPackageReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("CommProVer",c_ushort),
              ("Crc",c_ushort)]


#活动性检测帧
class _SN_ActiDetectionInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("IdNum",c_ubyte),
              ("ChangeConInfo",c_ubyte),#换装条件信息
              ("ChangeStatusInfo",c_ubyte),#换装状态信息
              ("Model",c_ubyte),#模式
              ("LKJDeviceStatus",c_ubyte),#LKJ设备状态
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("Speed",c_ushort),
              ("LampPosition",c_ushort),#灯位
              ("TiuData",c_ubyte),#工况
              ("ParkingSta",c_ubyte),#停车状态
              ("DMIConfig",c_ubyte),#DMI配置
              ("TrainType",c_ubyte),#客货类型
              ("Primary",c_ubyte),#本补
              ("SideNum",c_ubyte),#
              ("BranchNum",c_ubyte),#
              ("LKJWUStatus",c_ubyte),#LKJ与无线扩展单元匹配状态
              ("OrgVoltage",c_ushort),#
              ("OrgCurrent",c_ushort),#
              ("DieSpeedAnoma",c_ushort),#
              ("LCGPressure",c_ushort),#
              ("ZDGPressure",c_ushort),#
              ("JHFG1Pressure",c_ushort),#
              ("JHFG2Pressure",c_ushort),#
              ("KIMData",c_uint),#里程信息
              ("CurTime",c_ubyte*6),
              ("Crc",c_ushort)]
#活动性检测应答
class _SN_ActiDetectionInfoReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("ManCode",c_ubyte),
              ("Resrve2",c_ubyte),#预留 字节对齐
              ("DeviceId",c_ubyte*6),
              ("WLRegiStatus",c_ubyte),#预留
              ("Resrve3",c_ubyte),#预留 字节对齐
              ("Crc",c_ushort)]


#升级信息请求
class _SN_UpgradeRequestInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("Crc",c_ushort)]

#升级信息发送
class _SN_UpgradeInfoSend(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("DataToolVersion",c_uint),
              ("UpgradePlanVer",c_uint64),#V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("OrderID",c_wchar_p), #32字节的命令ID
              ("FileName",c_wchar_p),#36字节长度
              ("FileLen",c_uint),
              ("Crc48",c_wchar_p),#6
              ("PlanStartTime",c_ubyte*6),#高到低 年月日时分秒 高字节在前
              ("PlanEffectiveTime",c_ubyte*6),
              ("UpdataModeType",c_ubyte),#更新方式
              ("DeviceType",c_ubyte),#设备类型
              ("VoucherCode",c_uint),#凭证码
              ("FileType",c_ubyte),#文件类型
              ("EjectCount",c_ubyte),#连续弹出次数
              ("FileWLFlag",c_ushort),#文件换装标识
              ("ShowTime",c_uint),#显示弹出时间间隔
              ("Resrve2",c_ushort),#预留 字节对齐
              ("Crc",c_ushort)]


#升级操作信息发送
class _SN_UpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#70
              ("PacketNum",c_ushort),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("OrderID",c_ubyte*32),#32字节
              ("LocoNum",c_uint),
              ("VoucherCode",c_uint),
              ("DriverNum",c_uint),
              ("OperationTime",c_ubyte*6),
              ("OperationType",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("WLFileFlag",c_ushort),
              ("Crc",c_ushort)
              ]
#升级操作信息应答
class _SN_UpgradeOperationInfoReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("OrderID",c_wchar_p),#32字节
              ("LocoNum",c_uint),
              ("WLFileFlag",c_ushort),
              ("DMIOperationTer",c_ubyte),
              ("IsCanUpgrade",c_ubyte),
              ("Resrve2",c_ushort),#预留 字节对齐
              ("Crc",c_ushort)]


#启动升级信息
class _SN_StartUpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#94
              ("PacketNum",c_ushort),
              ("UpdateResult",c_ushort),
              ("WLFileFlag",c_ushort),
              ("ParamVerInfo",c_wchar_p),#16
              ("K2dataVerInfo",c_wchar_p),#18
              ("Resrve1",c_ushort),
              ("ParamCRC",c_uint64),
              ("CrcCRC",c_uint64),
              ("K2dataCRC",c_uint64),
              ("K2dataXlbLenCRC",c_uint64),
              ("K2dataZmbLenCRC",c_uint64),
              ("Resrve2",c_ushort),
              ("Crc",c_ushort)]
#启动升级信息回复
class _SN_StartUpgradeOperationInfoReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("MessgaeRece",c_ushort),
              ("Crc",c_ushort)
             ]


#换装阶段活动性检测帧
class _SN_WLActiDetectionInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("IdNum",c_ubyte),
              ("LKJDeviceStatus",c_ubyte),#LKJ设备状态
              ("LKJWUStatus",c_ubyte),#LKJ与无线扩展单元匹配状态
              ("ChangeStatusInfo",c_ubyte),#换装状态信息
              ("ChangeSpeed",c_ushort),#换装进度
              ("DMIChangeSpeed",c_ushort),#DMI换装进度
              ("Crc",c_ushort)]
#换装阶段活动性检测应答
class _SN_WLActiDetectionInfoReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#14
              ("PacketNum",c_ushort),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("ManCode",c_ubyte),
              ("Resrve2",c_ubyte),#预留 字节对齐
              ("DeviceId",c_ubyte*6),
              ("WLRegiStatus",c_ubyte),#预留
              ("Resrve3",c_ubyte),#预留 字节对齐
              ("Crc",c_ushort)]

#版本确认信息发送
class _SN_VersionConfirmInfo(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#102
              ("PacketNum",c_ushort),
              ("UpgraddeDataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("ParamVer",c_ubyte*16),#16 #V1.2.0 2021-4-30 缺省0x00  [0x01,0x02,0x00,0x15,0x04,0x1e,0x00]
              ("k2DataVer",c_ubyte*18),#18
              ("FileWLFlag",c_ushort),
              ("DriverNum",c_uint),
              ("OperationTime",c_ubyte*6),
              ("DriverOperation",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("OrderID",c_ubyte*32),
              ("Resrve1",c_ushort),#预留 字节对齐
              ("Resrve2",c_ubyte*64),#预留 字节对齐

              ("Crc",c_ushort)
              ]
#版本确认信息应答
class _SN_VersionConfirmInfoReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#66
              ("PacketNum",c_ushort),
              ("UpgraddeDataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("FileWLFlag",c_ushort),
              ("DriverOperation",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("DriverNum",c_uint),
              ("CurVer",c_uint64),
              ("OrderID",c_wchar_p),
              ("Resrve2",c_ushort),#预留 字节对齐
              ("Resrve3",c_wchar_p),#预留 字节对齐

              ("Crc",c_ushort)
              ]

#升级计划取消包
class _SN_UpgradePlanCancelled(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#58
              ("PacketNum",c_ushort),
              ("DataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("TrainNum",c_uint),
              ("FileWLFlag",c_ushort),
              ("MessgaeInfo",c_ushort),#消息内容
              ("OrderID",c_wchar_p),#32
              ("Resrve2",c_ushort),
              ("Crc",c_ushort)
              ]
#升级计划取消包应答
class _SN_UpgradePlanCancelledReply(Structure):
  _pack_=1
  _fields_ = [("Resrve",c_ushort),#预留 字节对齐
              ("PacketType",c_ushort),
              ("TimeStamp",c_uint),
              ("InfoLen",c_ushort),#58
              ("PacketNum",c_ushort),
              ("CancelDataType",c_ubyte),
              ("IdNum",c_ubyte),
              ("IdNumReply",c_ubyte),
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("OrderID",c_ubyte*32),
              ("TrainNum",c_uint),
              ("FileWLFlag",c_ushort),
              ("CancelRelust",c_ushort),
              ("Crc",c_ushort)
              ]

