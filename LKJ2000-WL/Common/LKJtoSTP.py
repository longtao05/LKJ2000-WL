#LKJ->STP 握手信息
class _LKJ_HandShackInfo_STP(Structure):
    _pack_=1
    _fields_ = [('Identify',c_byte), #标识
                ('HandShakeType1', c_byte),#握手类型
                ('HandShakeAttrCode1', c_ushort),#握手特征码
                ('HandShakeType2', c_byte),#握手类型
                ('HandShakeAttrCode2',c_ushort),#握手特征码
                (Crc8, c_byte)#CRC8
                ]

#LKJ->STP LKJ调车模式下的状态信息1
class _LKJ_LKJShuntStatInfo1_STP(Structure):
    _pack_=2
    _fields_ = [('TrainStateFlg',c_byte),  #机车状态标志
                ('SoftStateFlg', c_byte),  #软件状态标志
                ('LKJCurCtrldataNo', c_byte),  #LKJ当前执行的控制数据序号
                ('CtrlOperationPlanNo', c_byte),  #控制用作业计划钩号
                ('UnlckFlg',c_byte),  #解锁标志
                ('OperateKeyValue',c_byte),  #乘务员操作键值
                ('CurLiangShu', c_byte),  # 当前辆数
                (Crc8, c_byte)  #CRC8
                ]


#LKJ->STP LKJ调车模式下的状态信息2
class _LKJ_LKJShuntStatInfo2_STP(Structure):
    _pack_=3
    _fields_ = [('DisplayDistance',c_ushort),  #显示距离
                ('LenToNextSignal', c_ushort),  #距前方信号机距离
                ('ShuntMove', c_ushort),  #调车位移displacement
                ('Backup', c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP LKJ调车模式下的状态信息3
class _LKJ_LKJShuntStatInfo3_STP(Structure):
    _pack_=4
    _fields_ = [('FlatShuntSignal',c_byte),  #平调信号
                ('CurSpeed', c_byte),  #当前速度
                ('CurAllowSpeed', c_byte),  #当前限速
                ('CurSignalNo', c_ushort),  #当前信号机编号
                ('CurSignalState',c_byte),  #当前信号机状态
                ('Backup',c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 人工操作信息
class _LKJ_ManualOperateInfo_STP(Structure):
    _pack_=5
    _fields_ = [('AttrCode',c_byte),  #特征码
                ('ManualOperateFlg', c_ushort),  #人工操作标志
                ('Backup1', c_byte*3),  # 备用，协议未定义
                ('Backup2', c_ushort),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 越站调车申请信息
class _LKJ_PassStationShuntReqInfo_STP(Structure):
    _pack_=6
    _fields_ = [('AttrCode',c_byte),  #特征码
                ('PassStationListNo', c_ushort),  #越站单号
                ('Backup', c_uint),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 跟踪出站申请信息
class _LKJ_TrackOutboundReqInfo_STP(Structure):
    _pack_=7
    _fields_ = [('AttrCode',c_byte),  #特征码
                ('TrackListNo', c_ushort),  #跟踪单号
                ('Backup', c_uint),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 轨道区段定位信息
class _LKJ_TrackSectionPosInfo_STP(Structure):
    _pack_=8
    _fields_ = [(Crc16,c_ushort),  #CRC16
                ('Length', c_byte),  #长度
                ('TrackName', c_byte*12),  # 股道名称
                ('Backup', c_byte)  #备用
                ]

#LKJ->STP 站场定位信息
class _LKJ_StationYardPosInfo_STP(Structure):
    _pack_=9
    _fields_ = [('AttrCode', c_byte),  # 特征码
                ('StationNo', c_byte*3),  # 车站号
                ('YardNo', c_byte),  # 场号
                ('Backup', c_ushort),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP 辆数调整信息
class _LKJ_LiangShuAdjustInfo_STP(Structure):
    _pack_=10
    _fields_ = [('AttrCode', c_byte), # 特征码
                ('CurLiangShu', c_byte),  # 当前辆数
                ('Backup', c_byte*5),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP STP对话框回执信息
class _LKJ_STPDialogReceiptInfo_STP(Structure):
    _pack_=11
    _fields_ = [('AttrCode', c_byte),  # 特征码
                ('DataNo', c_byte),  # 数据序号
                ('OperateResult', c_byte),  # 乘务员操作结果
                ('Backup', c_uint),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP 机车信息
class _LKJ_TrainInfo_STP(Structure):
    _pack_=12
    _fields_ = [('TrainType', c_ushort), # 机车型号
                ('TrainNo', c_byte*3),  # 机车号/车次号
                ('Backup', c_ushort),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP 时间信息
class _LKJ_TimeInfo_STP(Structure):
    _pack_=13
    _fields_ = [('Year', c_byte), # 年
                ('Month', c_byte),  # 月
                ('Day', c_byte),  # 日
                ('Hour', c_byte), # 时
                ('Minute', c_byte),  # 分
                ('Second', c_byte),  # 秒
                ('Backup', c_byte),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP 请求信息
class _RequestInfo_STP(Structure):
    _pack_=14
    _fields_ = [('ReqInfo', c_byte), # 请求信息
                ('CurNo', c_byte),  # 当前钩号
                ('OperationPlanStartNo', c_byte),  # 作业计划开始钩号
                ('OperationPlanEndNo', c_byte), # 作业计划结束钩号
                ('Backup', c_byte*3),  # 备用
                (Crc8, c_byte)  # CRC8
                ]

#LKJ->STP LKJ列车模式下的强状态信息
class _LKJ_LKJTrainModeStrongInfo_STP(Structure):
    _pack_=15
    _fields_ = [('DisplayDistance',c_ushort),  #显示距离
                ('Speed', c_byte),  #速度
                ('TrainStateFlg', c_byte),  #机车状态标志
                ('SysReserve', c_ushort), #系统保留
                ('Backup', c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP LKJ列车模式下的弱状态信息
class _LKJ_LKJTrainModeWeakInfo_STP(Structure):
    _pack_=16
    _fields_ = [('TMISNo',c_byte*3),  #TMIS号
                ('SectionNo', c_byte),  #区段号
                ('SignalNo', c_ushort),  #信号机编号
                ('Backup', c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  设备信息1
class _LKJ_DeviceInfo1_STP(Structure):
    _pack_=17
    _fields_ = [('LKJHostProtocolVer',c_byte),  #LKJ主机协议版本
                ('LKJDMIProtocolVerI', c_byte),  #I 端LKJ显示器协议版本
                ('LKJDMIProtocolVerII', c_byte),  #II 端LKJ显示器协议版本
                ('Backup1', c_byte),  #备用，协议未定义
                ('Backup2', c_byte*3),  # 备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  设备信息2
class _LKJ_DeviceInfo2_STP(Structure):
    _pack_=18
    _fields_ = [('LKJBasicCtrlSoftVer',c_byte*3),  #LKJ基本控制软件版本
                ('Backup1', c_byte*3),  #备用，协议未定义
                ('Backup2', c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  设备信息3
class _LKJ_DeviceInfo3_STP(Structure):
    _pack_=19
    _fields_ = [('LKJDMISoftVerI', c_byte*3),  #I 端LKJ显示器软件版本
                ('LKJDMISoftVerII', c_byte*3),  #II 端LKJ显示器软件版本
                ('Backup', c_byte),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  I 端站场图数据版本信息
class _LKJ_StationYardMapVersionInfoI_STP(Structure):
    _pack_=20
    _fields_ = [('Year', c_byte), # 年
                ('Month', c_byte),  # 月
                ('Day', c_byte),  # 日
                ('ProtocolVer', c_byte),  # 协议版本
                ('Backup', c_byte*3),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  II 端站场图数据版本信息
class _LKJ_StationYardMapVersionInfoII_STP(Structure):
    _pack_=21
    _fields_ = [('Year', c_byte), # 年
                ('Month', c_byte),  # 月
                ('Day', c_byte),  # 日
                ('ProtocolVer', c_byte),  # 协议版本
                ('Backup', c_byte*3),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP  工况信息
class _LKJ_PowerStatIfo_STP(Structure):
    _pack_=22
    _fields_ = [('PipePressure',c_byte),  # 管压
                ('BrakePressure', c_byte),  # 闸压
                ('DieselRPM', c_byte),  # 柴转
                ('Backup', c_uint),  # 备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 司机操作按键信息
class _LKJ_DriverOperateKeyInfo_STP(Structure):
    _pack_=23
    _fields_ = [('AttrCode', c_byte),  # 特征码
                ('KeyInfo', c_byte*3),  #按键信息
                ('Backup', c_byte*3),  #备用
                (Crc8, c_byte)  #CRC8
                ]

#LKJ->STP 列车模式司机操作信息
class _LKJ_TrainModeDriverOperateInfo_STP(Structure):
    _pack_=24
    _fields_ = [('AttrCode', c_byte),  # 特征码
                ('InputCeXianNoJZ', c_ushort),  # 司机输入的列车进站侧线号
                ('GJDBKey', c_byte),  # 列车进站时司机操作的过机定标键
                ('Backup', c_byte*3),  #备用
                (Crc8, c_byte)  #CRC8
                ]
