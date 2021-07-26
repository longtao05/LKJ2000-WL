#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
import struct
import threading
from datetime import datetime

#模块导入
sys.path.append(r"..\Common")

from SerStructParserData import *
from SerStructSendData import *
from CommFun import *

from SerDataType import _SN_DataType,_SN_VersionInfoPackage ,_SN_ActiDetectionInfo ,_SN_UpgradeRequestInfo,_SN_UpgradeOperationInfo ,_SN_WLActiDetectionInfo,_SN_VersionConfirmInfo,_SN_UpgradePlanCancelledReply,_SN_HostEventInfo


import DataQueue

import Mygol

dataParserlock = threading.Lock()
#异常测试用例
global begintestcount
begintestcount = 0
class SerDataHandle():
    def __init__(self):
        #self.serDataH = DataFileProcess()
        self.serDataH = DataQueue.DataQueue()
        #有效数据
        self.effdata = bytearray()
        #数据头信息
        self.dataHead = _SN_DataType()
        self.dataParser= bytearray()
        self.senddata= _SN_DataType()
        self.state = ''

    def SerDataHandleProcess(self):
        self.effdata = bytearray(self.serDataH.get_get_Hdata())
        if(len(self.effdata)>10):
            self.datahandle()

    def SerSendDataPreProcess(self):
        self.senddatapackage()
        #self.serDataH.set_send_data(self.senddata)


    def senddatapackage(self):
        with dataParserlock:
            if(0x1001 == self.dataHead.PacketType):
                #回复版本信息包
                self.senddata = SN_VersionInfoPackageReply(self.dataHead,self.dataParser)
                if(2 == Mygol.get_value('CaseNum')):
                    time.sleep(0.9)
                    self.serDataH.set_send_data(self.senddata)
                    Mygol.set_value('CaseNum',0)
                if(3 == Mygol.get_value('CaseNum')):
                    self.serDataH.set_send_data(self.dataParser)
                    Mygol.set_value('CaseNum',0)
                else:
                    self.serDataH.set_send_data(self.senddata)

                #self.serDataH.set_send_data(self.senddata)

                if(0 != Mygol.get_value('UpgradeCount')):
                    #延时10毫秒后，发送换装通知--升级信息
                    time.sleep(0.01)
                    #换装通知--升级信息
                    self.senddata = SN_ChangeNotice_UpgradeInfo(self.dataHead,self.dataParser)
                    self.serDataH.set_send_data(self.senddata)

                    if(1==Mygol.get_value('LOG')):
                        f = open('./log/test.txt', 'ab') # 若是'wb'就表示写二进制文件
                        #f.write(b'Senddata:'+str.encode(str(datetime.now()))+b':\n'+binascii.b2a_hex(send_data))
                        f.write('换装通知--升级信息:'.encode('utf-8')+str.encode(str(datetime.now())))

                        f.write(b'\r\n')
                        f.close()
                    Mygol.set_value('UpgradeCount',0)

            elif(0x1002 == self.dataHead.PacketType):
                #回复活动性检测帧
                self.senddata = SN_ActiDetectionInfoReply(self.dataHead,self.dataParser)
                if(1 == Mygol.get_value('CaseNum') and begintestcount>10 and begintestcount<20):
                    pass
                elif(5 == Mygol.get_value('CaseNum')):
                    time.sleep(2)
                    Mygol.set_value('CaseNum',0)
                    self.serDataH.set_send_data(self.senddata)
                else:
                    self.serDataH.set_send_data(self.senddata)

                #if(1 == Mygol.get_value('DelayPerPack')):
                    #sleep(10)
                    #Mygol.set_value('DelayPerPack',0)


            elif(0x1003 == self.dataHead.PacketType):
                if(2==Mygol.get_value('MessgaeRece')):
                    #换装通知--换装控制信息
                    self.senddata = SN_ChangeNotice_ControlInfo(self.dataHead,self.dataParser)
                    self.serDataH.set_send_data(self.senddata)

                elif(3==Mygol.get_value('MessgaeRece')):
                    pass
                    #换装通知--启动升级
                    #self.senddata = SN_ChangeNotice_StartUpgrade(self.dataHead,self.dataParser)
                    #mSerial.self.senddata(self.senddata)
                elif(4==Mygol.get_value('MessgaeRece')):
                    #换装通知--升级信息
                    print("已正确接收启动信息内容")

            elif(0x1005 == self.dataHead.PacketType):
                #升级操作信息应答
                self.senddata = SN_UpgradeOperationInfoReply(self.dataHead,self.dataParser)
                self.serDataH.set_send_data(self.senddata)

            elif(0x1007 == self.dataHead.PacketType):
                #回复活动性检测帧
                self.senddata = SN_WLActiDetectionInfoReply(self.dataHead,self.dataParser)
                #self.serDataH.set_send_data(self.senddata)

                if(4 == Mygol.get_value('CaseNum') and begintestcount>0 and begintestcount<=10):
                    pass
                else:
                    self.serDataH.set_send_data(self.senddata)

                #取消换装测试
                if(0 != Mygol.get_value('PlanCancelled')):
                    #目前换装阶段周期包不检测超时
                    time.sleep(Mygol.get_value('PlanCancelled'))
                    self.senddata = SN_UpgradePlanCancelled(self.dataHead,self.dataParser)
                    self.serDataH.set_send_data(self.senddata)

            elif(0x1008 == self.dataHead.PacketType):
                self.senddata = SN_VersionConfirmInfoReply(self.dataHead,self.dataParser)
                self.serDataH.set_send_data(self.senddata)
                if(1==Mygol.get_value('LOG')):
                    f = open('./log/test.txt', 'ab') # 若是'wb'就表示写二进制文件
                    #f.write(b'Senddata:'+str.encode(str(datetime.now()))+b':\n'+binascii.b2a_hex(send_data))
                    f.write('版本确认--换装完成:'.encode('utf-8')+str.encode(str(datetime.now())))
                    f.write(b'\r\n')
                    f.close()


                #拷机测试
                if(1 == Mygol.get_value("CopeMacTest")):
                    Mygol.set_value("DelayPerPack",1)
                    Mygol.set_value('UpgradeCount',1)
                    time.sleep(10)
                    self.serDataH.get_get_Hdata()


                else:
                    Mygol.set_value("DelayPerPack",0)
                    Mygol.set_value('UpgradeCount',0)

            elif(0x1009 == self.dataHead.PacketType):
                print("收到升级计划取消应答包")
            elif(0x100A == self.dataHead.PacketType):
                self.senddata = SN_HostEventInfoReply(self.dataHead,self.dataParser)
                self.serDataH.set_send_data(self.senddata)


                #换装通知--启动升级
                time.sleep(0.1)
                self.senddata = SN_ChangeNotice_StartUpgrade(self.dataHead,self.dataParser)
                self.serDataH.set_send_data(self.senddata)

            elif(0x100C == self.dataHead.PacketType):
                #print("包类型：",'%#x'%self.dataHead.PacketType)
                Mygol.set_value('UpgradeCount',0)

            else:
                pass
                #print("未识别的包类型：",'%#x'%self.dataHead.PacketType)
            self.dataHead.PacketType = 0

        self.senddata = b''

    def datahandle(self):
        data_len=len(self.effdata)
        i=0
        #帧格式解析
        #先不考虑两包情况，但肯定存在，后续必须优化
        with dataParserlock:
            if(data_len>=12):
                byteOffset = 0
                byteNum = 4
                self.dataHead.TimeStamp = struct.unpack('<I',self.effdata[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum
                byteNum = 2
                self.dataHead.PacketType = struct.unpack('<H',self.effdata[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum
                byteNum = 2
                self.dataHead.InfoLen = struct.unpack('<H',self.effdata[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum
                byteNum = 2
                self.dataHead.PacketNum = struct.unpack('<H',self.effdata[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum
                byteNum = 2
                self.dataHead.Resrve = struct.unpack('<H',self.effdata[byteOffset:byteOffset+byteNum])[0]
                byteOffset = byteOffset + byteNum
                byteNum = 2

                #self.dataHead.Crc = struct.unpack('<H',self.effdata[-2:])[0]
                #print(self.dataHead.PacketType)
                #print(self.dataHead.InfoLen)
                self.packagehandle()
            else:
                pass

    def packagehandle(self):
        global begintestcount
        if(1 == Mygol.get_value('LOG')):
            f = open('./log/log.txt', 'ab') # 若是'wb'就表示写二进制文件
            f.write('接收数据:  时间戳:'.encode('utf-8')+str.encode(str(datetime.now()))+'  包类型:'.encode('utf-8')+binascii.b2a_hex(self.dataHead.PacketType.to_bytes(2,byteorder='little', signed=False))+b"\r\n"+binascii.b2a_hex(self.effdata))
            f.write(b'\r\n')
            f.close()

        self.dataParserlock = False
        if(0x1001 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
            self.dataParser = _SN_VersionInfoPackage()
            #版本信息包帧解析
            self.dataParser = SN_VersionInfoPackage(self.effdata)

        elif(0x1002 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
             #收到活动性检测发送，准备发送应答
            self.dataParser = _SN_ActiDetectionInfo()
            #活动性检测帧解析
            self.dataParser = SN_ActiDetectionInfo(self.effdata)
            if (1 == Mygol.get_value('CaseNum')):
                begintestcount +=1
                #Mygol.set_value('case1',1)
        elif(0x1003 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
             #换装通知应答包
            self.dataParser = _SN_UpgradeRequestInfo()
            self.dataParser = SN_UpgradeRequestInfo(self.effdata)
            print("换装应答内容：",'%#x'%self.dataParser.MessgaeRece)
            Mygol.set_value('MessgaeRece',self.dataParser.MessgaeRece)
            if(2==self.dataParser.MessgaeRece):
                #换装通知--换装控制信息
                pass
            elif(3==self.dataParser.MessgaeRece):
                pass
                #换装通知--启动升级
            elif(4==self.dataParser.MessgaeRece):
                #换装通知--升级信息
                print("已正确接收启动信息内容")

        elif(0x1005 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
            self.dataParser = _SN_UpgradeOperationInfo()
            #升级操作信息请求
            self.dataParser = SN_UpgradeOperationInfo(self.effdata)

        elif(0x1007 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
             #
            self.dataParser = _SN_WLActiDetectionInfo()
            #活动性检测帧解析
            self.dataParser = SN_WLActiDetectionInfo(self.effdata)
            if (4 == Mygol.get_value('CaseNum')):
                begintestcount +=1
        elif(0x1008 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
            self.dataParser = _SN_VersionConfirmInfo()
            self.dataParser = SN_VersionConfirmInfo(self.effdata)

        elif(0x1009 == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
            self.dataParser = _SN_UpgradePlanCancelledReply()
            self.dataParser = SN_UpgradePlanCancelledReply(self.effdata)
            print("收到升级计划取消应答包")
        elif(0x100A == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
            self.dataParser = _SN_HostEventInfo()
            self.dataParser = SN_HostEventInfo(self.effdata)

        elif(0x100C == self.dataHead.PacketType):
            print("包类型：",'%#x'%self.dataHead.PacketType)
        else:
            pass
            #print("未识别的包类型：",'%#x'%self.dataHead.PacketType)

