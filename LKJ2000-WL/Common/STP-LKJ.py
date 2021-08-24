#径路数据包头定义
class _STP_PathPacketHeader_LKJ(Structure):
    _pack_=1
    _fields_ = [(Crc16, c_ushort),#CRC16
                ('Length', c_byte),#长度
                ('DataSerialNum', c_byte),#数据序号
                ('ValidRouteDataNum', c_byte),#有效进路数据数量
                ('ValidSpdLmtPntDataNum',c_byte),#有效限速点数据数量
                ('SiteNum', c_byte),#场号
                ]

#STP->LKJ进路数据
class _STP_RouteDataNum_LKJ(Structure):
    _pack_=2
    _fields_ = [('RouteEndSignal', c_byte),#进路末端信号表示
                ('DelayTime', c_byte),#延迟时间
                ('RouteEndDataFeature', c_byte),#进路末端数据特征
                ('RouteEndUnlockCtrl', c_byte),#进路末端解锁控制
                ('RouteStartSignalCode',c_ushort),#进路始端信号机代号
                ('OverDistance', c_ushort),#越过距离
                ]

#STP->LKJ 限速数据
class _STP_SpdLmtData_LKJ(Structure):
    _pack_=3
    _fields_ = [('BasicRoadNum', c_byte),#基本进路号#STP->LKJ径路数据包头文件定义
                ('SpdLmt', c_byte),  #限速
                ('Backup', c_byte),  #备用
                ('SpdLmtType',c_byte),  #限速类型
                ('SpdLmtID', c_ushort),  #限速ID
                ('SpdLmt_StartSignD', c_ushort),  # 限速点距端点信号机的距离
                ]

#STP->LKJ 存车数据
class _STP_SaveTrain_LKJ(Structure):
    _pack_=4
    _fields_ = [('BasicRoadNum', c_byte),#基本进路号
                ('SaveTrain_StartSignD', c_ushort),#存车至始端信号机的距离
                ('Backup', c_byte*5),#备用


#STP->LKJ 状态迁移命令
class _STP_StatusTrstcmd_LKJ(Structure):
    _pack_=5
    _fields_ = [('CmdByte', c_byte),#命令字节
                ('Backup', c_byte*6),#备用
                (Crc8, c_byte),  #CRC8
               ]


#STP->LKJ限速解除命令
class _STP_UnSpdLmtData_LKJ(Structure):
    _pack_=6
    _fields_ = [('SpdLmtPntType_1', c_byte),#限速点1的类型
                ('SpdLmtPntID_1', c_ushort),  #限速点1的ID
                ('SpdLmtPntType_2', c_byte),  #限速点2的类型
                ('SpdLmtPntID_2', c_ushort),  # 限速点2的ID
                ('Backup', c_byte),  #备用
                (Crc8, c_byte),  # CRC8
                ]

#STP->LKJ STP强状态信息
class _STP_StrStusInfo_LKJ(Structure):
    _pack_=7
    _fields_ = [('DevSelfCheckStus', c_byte),#设备自检状态
                ('CtrlStusFlag', c_byte),  #控制状态标志
                ('STPCurtRunCtrlDataNum', c_byte), #STP当前执行的控制数据序号
                ('CurtNum', c_byte),  #当前辆数
                ('JFNum', c_byte),  #接风辆数
                ('STPOutCtrlSpdLmt', c_byte), #STP输出控制限速值
                ('Backup', c_byte),  #备用
                (Crc8, c_byte),  #CRC8
                ]


#STP->LKJ STP弱状态信息
class _STP_WeakStusInfo_LKJ(Structure):
    _pack_=8
    _fields_ = [('StationNum', c_byte*3),#车站编号
                ('SiteNum', c_byte),  #场编号
                ('TracksectionNum', c_ushort), #轨道区段代号
                ('SysReserve', c_byte),  #系统保留
                (Crc8, c_byte),  #CRC8
                ]

#STP->LKJ 控制调车作业计划
class _STP_CtrlShuntingtPlan_LKJ(Structure):
    _pack_=9
    _fields_ = [('ShuntingPlanNum', c_ushort),#调车作业计划编号
                ('GNum', c_byte),  #钩序号
                ('JGNum', c_byte),  #解挂辆数
                ('WorkMethod', c_byte),  #作业方法&特征
                ('TracksectNumSpdLmt', c_byte),  #轨道区段代号&特殊车辆限速
                (Crc8, c_byte),  # CRC8
                ]

#STP->LKJ 越站/跟踪调车回执信息
class _STP_CrossStaton/trackShuntRecptInfo_LKJ(Structure):
    _pack_=10
    _fields_ = [('Signature', c_byte),#特征码
                ('ListNum', c_ushort),  #单号
                ('Recpt', c_byte),  #回执
                ('WorkDistance', c_byte),  #作业距离
                ('Backup', c_byte),  #备用
                (Crc8, c_byte),  # CRC8
                ]

#STP->LKJ 应答定位器信息
class _STP_TelLocatorInfo_LKJ(Structure):
    _pack_=11
    _fields_ = [('TelLocatorNum', c_byte*3),#应答定位器编号
                ('Backup', c_uint),  #备用
                (Crc8, c_byte),  # CRC8
                ]


#STP->LKJ 设备信息
class _STP_DevInfo_LKJ(Structure):
    _pack_=12
    _fields_ = [('ProtocolVer', c_byte),#协议版本
                ('HostSoftwareVer_A', c_byte),    # 车载主机软件版本 字段A
                ('HostSoftwareVer_B', c_byte),    # 车载主机软件版本 字段B
                ('HostSoftwareVer_C', c_ushort),  # 车载主机软件版本 字段C
                ('HostSoftwareVer_D', c_ushort),  # 车载主机软件版本 字段D
                (Crc8, c_byte),  # CRC8
                ]

#STP->LKJ 握手信息
class _STP_HandShackInfo_LKJ(Structure):
    _pack_=13
    _fields_ = [('HandShakeType', c_byte),  # 握手类型
                ('HandShakeAttrCode1', c_ushort),  # 握手特征码
                ('Backup', c_uint),  # 备用
                (Crc8, c_byte),  # CRC8
                ]


#STP->LKJ 语音信息
class _STP_VoiceInfo_LKJ(Structure):
    _pack_=14
    _fields_ = [('VoiceCmd', c_byte),  # 语音指令
                ('VoiceCode', c_byte),  # 语音代码
                ('Backup', c_byte*5),  # 备用
                (Crc8, c_byte),  # CRC8
                ]

#STP->LKJ 厂家信息
class _STP_FactoryInfo_LKJ(Structure):
    _pack_=15
    _fields_ = [('FactoryInfoID', c_byte),  # 厂家标识
                ('Backup', c_byte*6),  # 备用
                (Crc8, c_byte),  # CRC8
                ]

#STP向DMI发送信息
#STP->DMI STP回执信息
class _STP_RecptInfo_DMI(Structure):
    _pack_=16
    _fields_ = [('ManOperateRecpt', c_byte),  # 人工操作回执
                ('PrintRecptInfo', c_byte),  #打印回执信息
                ('Backup', c_byte * 5),  # 备用
                (Crc8, c_byte),  # CRC8
                ]

#STP->DMI 定位请求信息
class _STP_LocalReqstInfo_DMI(Structure):
    _pack_=17
    _fields_ = [('LocalRestInfo', c_byte),  #定位请求信息
                ('Backup', c_byte * 6),  # 备用
                (Crc8, c_byte),  # CRC8
                ]

#STP->DMI 站场广播信息
class _STP_StationBroadcastInfo_DMI(Structure):
    _pack_=18
    _fields_ = [('TrackCircuitInfoNum', c_byte),  #轨道电路信息组号
                ('TrackCircuitInfoData', c_byte * 7),  # 轨道电路信息数据
                ('SignalInfoNum', c_byte),  # 信号机信号组号
                ('SignalInfoData', c_byte * 7),  # 信号机信息数据
                ('TurnoutInfoNum', c_byte),  # 道岔信息组号
                ('TurnoutInfoData', c_byte * 7),  #道岔信息数据
                ]

#STP->DMI 作业计划包头定义
class _STP_WorkPlanPacketDef_DMI(Structure):
    _pack_=19
    _fields_ = [('Crc16', c_ushort),     # CRC16
                ('Length', c_ushort),    # 长度
                ('WorkPlanNum', c_byte), # 作业计划序号
                ('Backup',c_byte*3),     #备用
                ]

#STP->DMI 头文件定义
class _STP_HeaderFileDef_DMI(Structure):
    _pack_=20
    _fields_ = [('ShuntingPlanNum', c_uint),     # 调车作业计划编号
                ('PlanStartHour', c_byte),    # 计划开始时
                ('PlanStartMin', c_byte),  # 计划开始分
                ('PlanStopHour', c_byte),  # 计划终止时
                ('PlanStopMin', c_byte), # 计划终止分
                ]

#STP->DMI 作业计划数据定义
class _STP_WorkPlanDataDef_DMI(Structure):
    _pack_=21
    _fields_ = [('GNum', c_byte),     # 钩序号
                ('StockRoadName', c_byte*8),    # 股道名称
                ('WorkMethod', c_byte),  # 作业方法
                ('LNum', c_byte),  # 辆数
                ('RecordThsLength', c_byte),  # 接风与记事长度
                ('RecordThsInfo', c_byte*12),  # 记事栏信息
                ]

#STP->DMI 显示状态标志
class _STP_DisplayStatusFlag_DMI(Structure):
    _pack_=22
    _fields_ = [('DisplayStatusFlag', c_byte),     # 显示状态标志
                ('WirelessSignalFlag', c_byte),    # 无线信号状态
                ('STPCurtRunWorkNum', c_byte),  # STP当前执行的作业计划序号
                ('AllWorkPlanGNum', c_byte),  # 整个作业计划的整钩数
                ('CurtGNum', c_byte),  # 当前钩编号
                ('GFlagAndGenterID', c_ushort),  # 钩状态及钩确认显示标志
                (Crc8, c_byte),  # CRC8
                ]

#STP->DMI STP对话框内容信息
class _STP_DialogContentInfo_DMI(Structure):
    _pack_=23
    _fields_ = [('Crc16', c_ushort),     # CRC16
                ('Length', c_byte),      # 长度
                ('DataNum', c_byte),     # 数据序号
                ('DialogContent', c_byte*20),  # 对话框内容
                ]