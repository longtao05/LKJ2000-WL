import struct
import ctypes
from ctypes import *
class _VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_uint),  # 验收码。SJA1000的帧过滤验收码。对经过屏蔽码过滤为“有关位”进行匹配，全部匹配成功后，此帧可以被接收。
                ("AccMask", c_uint),
                # 屏蔽码。SJA1000的帧过滤屏蔽码。对接收的CAN帧ID进行过滤，对应位为0的是“有关位”，对应位为1的是“无关位”。屏蔽码推荐设置为0xFFFFFFFF，即全部接收。
                ("Reserved", c_uint),  # 保留
                ("Filter", c_ubyte),   # 滤波方式
                ("Timing0", c_ubyte),  # 波特率定时器 0
                ("Timing1", c_ubyte),  # 波特率定时器 1
                ("Mode", c_ubyte)  # 模式。=0表示正常模式（相当于正常节点），=1表示只听模式（只接收，不影响总线），=2表示自发自收模式（环回模式）。
                ]


class _VCI_CAN_OBJ(Structure):  # _VCI_CAN_OBJ结构体是CAN帧结构体，即1个结构体表示一个帧的数据结构。在发送函数VCI_Transmit和接收函数VCI_Receive中，被用来传送CAN信息帧。
    _fields_ = [("ID", c_uint),  # 帧ID。32位变量，数据格式为靠右对齐
                ("TimeStamp", c_uint),  # 设备接收到某一帧的时间标识。时间标示从CAN卡上电开始计时，计时单位为0.1ms。
                ("TimeFlag", c_ubyte),  # 是否使用时间标识，为1时TimeStamp有效，TimeFlag和TimeStamp只在此帧为接收帧时有意义。
                ("SendType", c_ubyte),
                # 发送帧类型。=0时为正常发送（发送失败会自动重发，重发时间为4秒，4秒内没有发出则取消）；=1时为单次发送（只发送一次，发送失败不会自动重发，总线只产生一帧数据）；其它值无效。
                ("RemoteFlag", c_ubyte),  # 是否是远程帧。=0时为为数据帧，=1时为远程帧（数据段空）。
                ("ExternFlag", c_ubyte),  # 是否是扩展帧。=0时为标准帧（11位ID），=1时为扩展帧（29位ID）。
                ("DataLen", c_ubyte),  # 数据长度 DLC (<=8)，即CAN帧Data有几个字节。约束了后面Data[8]中的有效字节
                ("Data", c_ubyte * 8),
                # CAN帧的数据。由于CAN规定了最大是8个字节，所以这里预留了8个字节的空间，受DataLen约束。如DataLen定义为3，即Data[0]、Data[1]、Data[2]是有效的
                ("Reserved", c_ubyte * 3)  # 系统保留
                ]


class _RX_CAN_OBJ(Structure):
    _pack_=1
    _fields_ = [('ID', c_uint),
                ('TimeStamp', c_uint),
                ('TimeFlag', c_ubyte),
                ('SendType', c_ubyte),
                ('RemoteFlag', c_ubyte),
                ('ExternFlag', c_ubyte),
                ('DataLen', c_ubyte),
                ('Data', c_ubyte*8),
                #('Data',_LKJ_HandShackInfo_STP),
                ('Reserved', c_ubyte*3)]

#LKJ->STP 握手信息
class _LKJ_HandShackInfo_STP(Structure):
    _pack_=1
    _fields_ = [('Identify',c_ubyte), #标识
                ('HandShakeType1', c_ubyte),#握手类型
                ('HandShakeAttrCode1', c_ushort),#握手特征码
                ('HandShakeType2', c_ubyte),#握手类型
                ('HandShakeAttrCode2',c_ushort),#握手特征码
                ('Crc8', c_ubyte)#CRC8
                ]

#LKJ->STP LKJ调车模式下的状态信息1
class _LKJ_LKJShuntStatInfo1_STP(Structure):
    _pack_=1
    _fields_ = [('TrainStateFlg',c_ubyte),  #机车状态标志
                ('SoftStateFlg', c_ubyte),  #软件状态标志
                ('LKJCurCtrldataNo', c_ubyte),  #LKJ当前执行的控制数据序号
                ('CtrlOperationPlanNo', c_ubyte),  #控制用作业计划钩号
                ('UnlckFlg',c_ubyte),  #解锁标志
                ('OperateKeyValue',c_ubyte),  #乘务员操作键值
                ('CurLiangShu', c_ubyte),  # 当前辆数
                ('Crc8', c_ubyte)  #CRC8
                ]


#LKJ->STP LKJ调车模式下的状态信息2
class _LKJ_LKJShuntStatInfo2_STP(Structure):
    _pack_=1
    _fields_ = [('DisplayDistance',c_ushort),  #显示距离
                ('LenToNextSignal', c_ushort),  #距前方信号机距离
                ('ShuntMove', c_ushort),  #调车位移displacement
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP LKJ调车模式下的状态信息3
class _LKJ_LKJShuntStatInfo3_STP(Structure):
    _pack_=1
    _fields_ = [('FlatShuntSignal',c_ubyte),  #平调信号
                ('CurSpeed', c_ubyte),  #当前速度
                ('CurAllowSpeed', c_ubyte),  #当前限速
                ('CurSignalNo', c_ushort),  #当前信号机编号
                ('CurSignalState',c_ubyte),  #当前信号机状态
                ('Backup',c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 人工操作信息
class _LKJ_ManualOperateInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode',c_ubyte),  #特征码
                ('ManualOperateFlg', c_ushort),  #人工操作标志
                ('Backup1', c_ubyte*3),  # 备用，协议未定义
                ('Backup2', c_ushort),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 越站调车申请信息
class _LKJ_PassStationShuntReqInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode',c_ubyte),  #特征码
                ('PassStationListNo', c_ushort),  #越站单号
                ('Backup', c_uint),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 跟踪出站申请信息
class _LKJ_TrackOutboundReqInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode',c_ubyte),  #特征码
                ('TrackListNo', c_ushort),  #跟踪单号
                ('Backup', c_uint),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 轨道区段定位信息
class _LKJ_TrackSectionPosInfo_STP(Structure):
    _pack_=1
    _fields_ = [('Crc16',c_ushort),  #CRC16
                ('Length', c_ubyte),  #长度
                ('TrackName', c_ubyte*12),  # 股道名称
                ('Backup', c_ubyte)  #备用
                ]

#LKJ->STP 站场定位信息
class _LKJ_StationYardPosInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode', c_ubyte),  # 特征码
                ('StationNo', c_ubyte*3),  # 车站号
                ('YardNo', c_ubyte),  # 场号
                ('Backup', c_ushort),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP 辆数调整信息
class _LKJ_LiangShuAdjustInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode', c_ubyte), # 特征码
                ('CurLiangShu', c_ubyte),  # 当前辆数
                ('Backup', c_ubyte*5),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP STP对话框回执信息
class _LKJ_STPDialogReceiptInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode', c_ubyte),  # 特征码
                ('DataNo', c_ubyte),  # 数据序号
                ('OperateResult', c_ubyte),  # 乘务员操作结果
                ('Backup', c_uint),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP 机车信息
class _LKJ_TrainInfo_STP(Structure):
    _pack_=1
    _fields_ = [('TrainType', c_ushort), # 机车型号
                ('TrainNo', c_ubyte*3),  # 机车号/车次号
                ('Backup', c_ushort),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP 时间信息
class _LKJ_TimeInfo_STP(Structure):
    _pack_=1
    _fields_ = [('Year', c_ubyte), # 年
                ('Month', c_ubyte),  # 月
                ('Day', c_ubyte),  # 日
                ('Hour', c_ubyte), # 时
                ('Minute', c_ubyte),  # 分
                ('Second', c_ubyte),  # 秒
                ('Backup', c_ubyte),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP 请求信息
class _RequestInfo_STP(Structure):
    _pack_=1
    _fields_ = [('ReqInfo', c_ubyte), # 请求信息
                ('CurNo', c_ubyte),  # 当前钩号
                ('OperationPlanStartNo', c_ubyte),  # 作业计划开始钩号
                ('OperationPlanEndNo', c_ubyte), # 作业计划结束钩号
                ('Backup', c_ubyte*3),  # 备用
                ('Crc8', c_ubyte)  # CRC8
                ]

#LKJ->STP LKJ列车模式下的强状态信息
class _LKJ_LKJTrainModeStrongInfo_STP(Structure):
    _pack_=1
    _fields_ = [('DisplayDistance',c_ushort),  #显示距离
                ('Speed', c_ubyte),  #速度
                ('TrainStateFlg', c_ubyte),  #机车状态标志
                ('SysReserve', c_ushort), #系统保留
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP LKJ列车模式下的弱状态信息
class _LKJ_LKJTrainModeWeakInfo_STP(Structure):
    _pack_=1
    _fields_ = [('TMISNo',c_ubyte*3),  #TMIS号
                ('SectionNo', c_ubyte),  #区段号
                ('SignalNo', c_ushort),  #信号机编号
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  设备信息1
class _LKJ_DeviceInfo1_STP(Structure):
    _pack_=1
    _fields_ = [('LKJHostProtocolVer',c_ubyte),  #LKJ主机协议版本
                ('LKJDMIProtocolVerI', c_ubyte),  #I 端LKJ显示器协议版本
                ('LKJDMIProtocolVerII', c_ubyte),  #II 端LKJ显示器协议版本
                ('Backup1', c_ubyte),  #备用，协议未定义
                ('Backup2', c_ubyte*3),  # 备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  设备信息2
class _LKJ_DeviceInfo2_STP(Structure):
    _pack_=1
    _fields_ = [('LKJBasicCtrlSoftVer',c_ubyte*3),  #LKJ基本控制软件版本
                ('Backup1', c_ubyte*3),  #备用，协议未定义
                ('Backup2', c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  设备信息3
class _LKJ_DeviceInfo3_STP(Structure):
    _pack_=1
    _fields_ = [('LKJDMISoftVerI', c_ubyte*3),  #I 端LKJ显示器软件版本
                ('LKJDMISoftVerII', c_ubyte*3),  #II 端LKJ显示器软件版本
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  I 端站场图数据版本信息
class _LKJ_StationYardMapVersionInfoI_STP(Structure):
    _pack_=1
    _fields_ = [('Year', c_ubyte), # 年
                ('Month', c_ubyte),  # 月
                ('Day', c_ubyte),  # 日
                ('ProtocolVer', c_ubyte),  # 协议版本
                ('Backup', c_ubyte*3),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  II 端站场图数据版本信息
class _LKJ_StationYardMapVersionInfoII_STP(Structure):
    _pack_=1
    _fields_ = [('Year', c_ubyte), # 年
                ('Month', c_ubyte),  # 月
                ('Day', c_ubyte),  # 日
                ('ProtocolVer', c_ubyte),  # 协议版本
                ('Backup', c_ubyte*3),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP  工况信息
class _LKJ_PowerStatIfo_STP(Structure):
    _pack_=1
    _fields_ = [('PipePressure',c_ubyte),  # 管压
                ('BrakePressure', c_ubyte),  # 闸压
                ('DieselRPM', c_ubyte),  # 柴转
                ('Backup', c_uint),  # 备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 司机操作按键信息
class _LKJ_DriverOperateKeyInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode', c_ubyte),  # 特征码
                ('KeyInfo', c_ubyte*3),  #按键信息
                ('Backup', c_ubyte*3),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#LKJ->STP 列车模式司机操作信息
class _LKJ_TrainModeDriverOperateInfo_STP(Structure):
    _pack_=1
    _fields_ = [('AttrCode', c_ubyte),  # 特征码
                ('InputCeXianNoJZ', c_ushort),  # 司机输入的列车进站侧线号
                ('GJDBKey', c_ubyte),  # 列车进站时司机操作的过机定标键
                ('Backup', c_ubyte*3),  #备用
                ('Crc8', c_ubyte)  #CRC8
                ]

#径路数据包头定义
class _STP_PathPacketHeader_LKJ(Structure):
    _pack_=1
    _fields_ = [('Crc16', c_ushort),#CRC16
                ('Length', c_ubyte),#长度
                ('DataSerialNum', c_ubyte),#数据序号
                ('ValidRouteDataNum', c_ubyte),#有效进路数据数量
                ('ValidSpdLmtPntDataNum',c_ubyte),#有效限速点数据数量
                ('SiteNum', c_ubyte),#场号
                ]

#STP->LKJ进路数据
class _STP_RouteDataNum_LKJ(Structure):
    _pack_=1
    _fields_ = [('RouteEndSignal', c_ubyte),#进路末端信号表示
                ('DelayTime', c_ubyte),#延迟时间
                ('RouteEndDataFeature', c_ubyte),#进路末端数据特征
                ('RouteEndUnlockCtrl', c_ubyte),#进路末端解锁控制
                ('RouteStartSignalCode',c_ushort),#进路始端信号机代号
                ('OverDistance', c_ushort),#越过距离
                ]

#STP->LKJ 限速数据
class _STP_SpdLmtData_LKJ(Structure):
    _pack_=1
    _fields_ = [('BasicRoadNum', c_ubyte),#基本进路号#STP->LKJ径路数据包头文件定义
                ('SpdLmt', c_ubyte),  #限速
                ('Backup', c_ubyte),  #备用
                ('SpdLmtType',c_ubyte),  #限速类型
                ('SpdLmtID', c_ushort),  #限速ID
                ('SpdLmt_StartSignD', c_ushort),  # 限速点距端点信号机的距离
                ]

#STP->LKJ 存车数据
class _STP_SaveTrain_LKJ(Structure):
    _pack_=1
    _fields_ = [('BasicRoadNum', c_ubyte),#基本进路号
                ('SaveTrain_StartSignD', c_ushort),#存车至始端信号机的距离
                ('Backup', c_ubyte*5),#备用
                ]

#STP->LKJ 状态迁移命令
class _STP_StatusTrstcmd_LKJ(Structure):
    _pack_=1
    _fields_ = [('CmdByte', c_ubyte),#命令字节
                ('Backup', c_ubyte*6),#备用
                ('Crc8', c_ubyte),  #CRC8
               ]


#STP->LKJ限速解除命令
class _STP_UnSpdLmtData_LKJ(Structure):
    _pack_=1
    _fields_ = [('SpdLmtPntType_1', c_ubyte),#限速点1的类型
                ('SpdLmtPntID_1', c_ushort),  #限速点1的ID
                ('SpdLmtPntType_2', c_ubyte),  #限速点2的类型
                ('SpdLmtPntID_2', c_ushort),  # 限速点2的ID
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->LKJ STP强状态信息
class _STP_StrStusInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('DevSelfCheckStus', c_ubyte),#设备自检状态
                ('CtrlStusFlag', c_ubyte),  #控制状态标志
                ('STPCurtRunCtrlDataNum', c_ubyte), #STP当前执行的控制数据序号
                ('CurtNum', c_ubyte),  #当前辆数
                ('JFNum', c_ubyte),  #接风辆数
                ('STPOutCtrlSpdLmt', c_ubyte), #STP输出控制限速值
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte),  #CRC8
                ]


#STP->LKJ STP弱状态信息
class _STP_WeakStusInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('StationNum', c_ubyte*3),#车站编号
                ('SiteNum', c_ubyte),  #场编号
                ('TracksectionNum', c_ushort), #轨道区段代号
                ('SysReserve', c_ubyte),  #系统保留
                ('Crc8', c_ubyte),  #CRC8
                ]

#STP->LKJ 控制调车作业计划
class _STP_CtrlShuntingtPlan_LKJ(Structure):
    _pack_=1
    _fields_ = [('ShuntingPlanNum', c_ushort),#调车作业计划编号
                ('GNum', c_ubyte),  #钩序号
                ('JGNum', c_ubyte),  #解挂辆数
                ('WorkMethod', c_ubyte),  #作业方法&特征
                ('TracksectNumSpdLmt', c_ubyte),  #轨道区段代号&特殊车辆限速
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->LKJ 越站/跟踪调车回执信息
class _STP_CrossStaton_trackShuntRecptInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('Signature', c_ubyte),#特征码
                ('ListNum', c_ushort),  #单号
                ('Recpt', c_ubyte),  #回执
                ('WorkDistance', c_ubyte),  #作业距离
                ('Backup', c_ubyte),  #备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->LKJ 应答定位器信息
class _STP_TelLocatorInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('TelLocatorNum', c_ubyte*3),#应答定位器编号
                ('Backup', c_uint),  #备用
                ('Crc8', c_ubyte),  # CRC8
                ]


#STP->LKJ 设备信息
class _STP_DevInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('ProtocolVer', c_ubyte),#协议版本
                ('HostSoftwareVer_A', c_ubyte),    # 车载主机软件版本 字段A
                ('HostSoftwareVer_B', c_ubyte),    # 车载主机软件版本 字段B
                ('HostSoftwareVer_C', c_ushort),  # 车载主机软件版本 字段C
                ('HostSoftwareVer_D', c_ushort),  # 车载主机软件版本 字段D
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->LKJ 握手信息
class _STP_HandShackInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('HandShakeType', c_ubyte),  # 握手类型
                ('HandShakeAttrCode1', c_ushort),  # 握手特征码
                ('Backup', c_uint),  # 备用
                ('Crc8', c_ubyte),  # CRC8
                ]


#STP->LKJ 语音信息
class _STP_VoiceInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('VoiceCmd', c_ubyte),  # 语音指令
                ('VoiceCode', c_ubyte),  # 语音代码
                ('Backup', c_ubyte*5),  # 备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->LKJ 厂家信息
class _STP_FactoryInfo_LKJ(Structure):
    _pack_=1
    _fields_ = [('FactoryInfoID', c_ubyte),  # 厂家标识
                ('Backup', c_ubyte*6),  # 备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP向DMI发送信息
#STP->DMI STP回执信息
class _STP_RecptInfo_DMI(Structure):
    _pack_=1
    _fields_ = [('ManOperateRecpt', c_ubyte),  # 人工操作回执
                ('PrintRecptInfo', c_ubyte),  #打印回执信息
                ('Backup', c_ubyte * 5),  # 备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->DMI 定位请求信息
class _STP_LocalReqstInfo_DMI(Structure):
    _pack_=1
    _fields_ = [('LocalRestInfo', c_ubyte),  #定位请求信息
                ('Backup', c_ubyte * 6),  # 备用
                ('Crc8', c_ubyte),  # CRC8
                ]

#STP->DMI 站场广播信息
class _STP_StationBroadcastInfo_DMI(Structure):
    _pack_=1
    _fields_ = [('TrackCircuitInfoNum', c_ubyte),  #轨道电路信息组号
                ('TrackCircuitInfoData', c_ubyte * 7),  # 轨道电路信息数据
                ('SignalInfoNum', c_ubyte),  # 信号机信号组号
                ('SignalInfoData', c_ubyte * 7),  # 信号机信息数据
                ('TurnoutInfoNum', c_ubyte),  # 道岔信息组号
                ('TurnoutInfoData', c_ubyte * 7),  #道岔信息数据
                ]

#STP->DMI 作业计划包头定义
class _STP_WorkPlanPacketDef_DMI(Structure):
    _pack_=19
    _fields_ = [('Crc16', c_ushort),     # CRC16
                ('Length', c_ushort),    # 长度
                ('WorkPlanNum', c_ubyte), # 作业计划序号
                ('Backup',c_ubyte*3),     #备用
                ]

#STP->DMI 头文件定义
class _STP_HeaderFileDef_DMI(Structure):
    _pack_=1
    _fields_ = [('ShuntingPlanNum', c_uint),     # 调车作业计划编号
                ('PlanStartHour', c_ubyte),    # 计划开始时
                ('PlanStartMin', c_ubyte),  # 计划开始分
                ('PlanStopHour', c_ubyte),  # 计划终止时
                ('PlanStopMin', c_ubyte), # 计划终止分
                ]

#STP->DMI 作业计划数据定义
class _STP_WorkPlanDataDef_DMI(Structure):
    _pack_=1
    _fields_ = [('GNum', c_ubyte),     # 钩序号
                ('StockRoadName', c_ubyte*8),    # 股道名称
                ('WorkMethod', c_ubyte),  # 作业方法
                ('LNum', c_ubyte),  # 辆数
                ('RecordThsLength', c_ubyte),  # 接风与记事长度
                ('RecordThsInfo', c_ubyte*12),  # 记事栏信息
                ]

#STP->DMI 显示状态标志
class _STP_DisplayStatusFlag_DMI(Structure):
    _pack_=1
    _fields_ = [('DisplayStatusFlag', c_ubyte),     # 显示状态标志
                ('WirelessSignalFlag', c_ubyte),    # 无线信号状态
                ('STPCurtRunWorkNum', c_ubyte),  # STP当前执行的作业计划序号
                ('AllWorkPlanGNum', c_ubyte),  # 整个作业计划的整钩数
                ('CurtGNum', c_ubyte),  # 当前钩编号
                ('GFlagAndGenterID', c_ushort),  # 钩状态及钩确认显示标志
                ('Crc8', c_ubyte),  # 'Crc8'
                ]

#STP->DMI STP对话框内容信息
class _STP_DialogContentInfo_DMI(Structure):
    _pack_=1
    _fields_ = [('Crc16', c_ushort),     # CRC16
                ('Length', c_ubyte),      # 长度
                ('DataNum', c_ubyte),     # 数据序号
                ('DialogContent', c_ubyte*20),  # 对话框内容
                ]
