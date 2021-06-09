import sys
import binascii
from ctypes import *
from enum import Enum
import struct

#数据格式
 #信息长度：2 源通信地址：1 目的通信地址：1 业务类型：1 命令：1 数据：n CRC16:2
class _SN_DataType(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("Crc",c_ushort)]



#版本信息包
class _SN_VersionInfoPackage(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
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
              ("DeviceNum",c_ushort),#装置号
              ("LocoType",c_ubyte),#机车类型
              ("Resrve2",c_ubyte),#
              ("CommProVer",c_ushort),#版本协议
              ("ManCode",c_ubyte),#厂家编号
              ("DeviceType",c_ubyte),#设备类型
              ("Crc",c_ushort)]


#版本信息包应答
class _SN_VersionInfoPackageReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("CommProVer",c_ushort),
              ("Crc",c_ushort)]


#活动性检测帧
class _SN_ActiDetectionInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              #("IdNum",c_ubyte),
              ("ChangeConInfo",c_ubyte),#换装条件信息
              ("ChangeStatusInfo",c_ubyte),#换装状态信息
              ("Model",c_ubyte),#模式
              ("LKJDeviceStatus",c_ubyte),#LKJ设备状态
              ("Speed",c_ushort),#速度
              ("LampPosition",c_ushort),#灯位
              ("TiuData",c_ubyte),#工况
              ("ParkingSta",c_ubyte),#停车状态
              ("DMIConfig",c_ubyte),#DMI配置
              ("TrainType",c_ubyte),#客货类型
              ("Primary",c_ubyte),#本补
              ("SideNum",c_ubyte),#侧线号
              ("BranchNum",c_ubyte),#支线号
              ("LKJWUStatus",c_ubyte),#LKJ与无线扩展单元匹配状态
              ("OrgVoltage",c_ushort),#原边电压
              ("OrgCurrent",c_ushort),#原边电流
              ("DieSpeedAnoma",c_ushort),#柴油机转速
              ("LCGPressure",c_ushort),#列车管压力
              ("ZDGPressure",c_ushort),#制动缸压力
              ("JHFG1Pressure",c_ushort),#均衡风缸1压力
              ("JHFG2Pressure",c_ushort),#均衡风缸2压力
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("KIMData",c_uint),#里程信息
              ("CurTime",c_ubyte*6),
              ("Crc",c_ushort)]
#活动性检测应答
class _SN_ActiDetectionInfoReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              #("IdNum",c_ubyte),
              #("IdNumReply",c_ubyte),
              #("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("ManCode",c_ubyte),#厂家编号
              ("WUPInitStatus",c_ubyte),#WUP自检状态
              ("DeviceId",c_ubyte*6),#无线扩展单元设备ID
              ("WLRegiStatus",c_ubyte),#预留
              ("WLRegiConnStatus",c_ubyte),#无线扩展单元连接状态
              ("Crc",c_ushort)]


#升级信息请求 换装通知应答
class _SN_UpgradeRequestInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("DataType",c_ubyte),
              #("IdNum",c_ubyte),
              #("Resrve1",c_ushort),#预留 字节对齐
              #("TrainNum",c_uint),
              ("MessgaeRece",c_ushort),#消息回执
              ("Crc",c_ushort)]

#升级信息发送
class _SN_UpgradeInfoSend(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
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





#换装通知--升级信息
class _SN_ChangeNotice_UpgradeInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("DataToolVersion",c_uint),#数据工具软件版本
              ("UpgradePlanVer",c_uint64),#升级计划版本
              ("FileName",c_wchar_p),#36 文件名
              ("FileLen",c_uint),#文件长度
              ("Crc48",c_wchar_p),#6 文件校验码
              ("WLFileFlag",c_ushort),#换装文件标识
              ("FileType",c_ubyte),#文件类型
              ("DataType",c_ubyte),
              ("Crc",c_ushort)
              ]

#换装通知--换装控制信息
class _SN_ChangeNotice_ControlInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("OrderID",c_wchar_p), #32字节的命令ID
              ("PlanStartTime",c_ubyte*6),#高到低 年月日时分秒 高字节在前
              ("PlanEffectiveTime",c_ubyte*6),
              ("VoucherCode",c_uint),#凭证码
              ("UpdataModeType",c_ubyte),#更新方式
              ("DeviceType",c_ubyte),#设备类型
              ("EjectCount",c_ubyte),#连续弹出次数
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("ShowTime",c_uint),#显示弹出时间间隔
              ("ChangeNoticeReason",c_wchar_p),#32 换装缘由
              ("Resrve2",c_ushort),#预留 字节对齐
              ("Crc",c_ushort)
              ]
#换装通知--启动升级
class _SN_ChangeNotice_StartUpgrade(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("UpdateResult",c_ushort),
              ("WLFileFlag",c_ushort),
              ("ParamVerInfo",c_wchar_p),#16
              ("K2dataVerInfo",c_wchar_p),#18

              ("K2dataSignaCode",c_uint),#基础数据特征码
              ("BureauNum",c_ubyte),#局号
              ("ManCode",c_ubyte),#厂家编号

              ("ParamCRC",c_uint64),
              ("CrcCRC",c_uint64),
              ("K2dataCRC",c_uint64),
              ("K2dataXlbLenCRC",c_uint64),
              ("K2dataZmbLenCRC",c_uint64),
              ("Resrve2",c_ushort),
              ("Crc",c_ushort)]

#升级操作信息发送
class _SN_UpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("DataType",c_ubyte),
              #("IdNum",c_ubyte),
              ("Resrve2",c_ubyte),
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
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              #("IdNum",c_ubyte),
              #("IdNumReply",c_ubyte),
              #("Resrve1",c_ushort),#预留 字节对齐
              ("OrderID",c_wchar_p),#32字节
              ("LocoNum",c_uint),
              ("WLFileFlag",c_ushort),
              ("DMIOperationTer",c_ubyte),
              ("IsCanUpgrade",c_ubyte),
              ("DataType",c_ubyte),
              ("Resrve2",c_ubyte),#预留 字节对齐
              ("Crc",c_ushort)]


#启动升级信息
class _SN_StartUpgradeOperationInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
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
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("MessgaeRece",c_ushort),
              ("Crc",c_ushort)
             ]


#换装阶段活动性检测帧
class _SN_WLActiDetectionInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("LKJDeviceStatus",c_ubyte),#LKJ设备状态
              ("LKJWUStatus",c_ubyte),#LKJ与无线扩展单元匹配状态
              ("ChangeStatusInfo",c_ubyte),#换装状态信息
              ("Resrve1",c_ubyte),
              ("ChangeSpeed",c_ushort),#换装进度
              ("DMIChangeSpeed",c_ushort),#DMI换装进度
              ("Crc",c_ushort)]
#换装阶段活动性检测应答
class _SN_WLActiDetectionInfoReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              #("IdNum",c_ubyte),
              #("IdNumReply",c_ubyte),
              #("Resrve1",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("ManCode",c_ubyte),
              ("WUPInitStatus",c_ubyte),#WUP自检状态
              ("DeviceId",c_ubyte*6),
              ("WLRegiStatus",c_ubyte),#
              ("WLRegiConnStatus",c_ubyte),#
              ("Crc",c_ushort)]

#版本确认信息发送
class _SN_VersionConfirmInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("UpgraddeDataType",c_ubyte),
              ("Resrve11",c_ubyte),
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
              ("Resrve3",c_ushort),#预留 字节对齐
              ("Crc",c_ushort)
              ]
#版本确认信息应答
class _SN_VersionConfirmInfoReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              #("IdNum",c_ubyte),
              #("IdNumReply",c_ubyte),
              #("Resrve1",c_ubyte),#预留 字节对齐
              ("TrainNum",c_uint),#机车号
              ("FileWLFlag",c_ushort),
              ("DriverOperation",c_ubyte),
              ("DMIOperationTer",c_ubyte),
              ("DriverNum",c_uint),
              ("CurVer",c_uint64),
              ("OrderID",c_wchar_p),
              ("UpgraddeDataType",c_ubyte),
              ("Resrve2",c_ubyte),#预留 字节对齐
              ("Crc",c_ushort)
              ]

#升级计划取消包
class _SN_UpgradePlanCancelled(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("TrainNum",c_uint),
              ("FileWLFlag",c_ushort),
              ("MessgaeInfo",c_ushort),#消息内容
              ("OrderID",c_wchar_p),#32
              ("DataType",c_ubyte),
              ("Resrve2",c_ubyte),
              ("Crc",c_ushort)
              ]
#升级计划取消包应答
class _SN_UpgradePlanCancelledReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("CancelDataType",c_ubyte),
              #("IdNum",c_ubyte),
              #("IdNumReply",c_ubyte),
              ("Resrve11",c_ushort),#预留 字节对齐
              ("Resrve1",c_ubyte),#预留 字节对齐
              ("OrderID",c_ubyte*32),
              ("TrainNum",c_uint),
              ("FileWLFlag",c_ushort),
              ("CancelRelust",c_ushort),
              ("Crc",c_ushort)
              ]

#主机事件信息包
class _SN_HostEventInfo(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("EventType",c_ushort),
              ("Crc",c_ushort)
              ]
#主机事件信息应答包
class _SN_HostEventInfoReply(Structure):
  _pack_=1
  _fields_ = [("TimeStamp",c_uint),#时间戳
              ("PacketType",c_ushort),#包类型
              ("InfoLen",c_ushort),#数据域长度
              ("PacketNum",c_ushort),#包序号
              ("Resrve",c_ushort),#预留 字节对齐
              ("ReplyEventType",c_ushort),
              ("Crc",c_ushort)
              ]
