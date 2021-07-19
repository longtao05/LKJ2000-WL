#!/usr/bin/python
# -*-coding: utf-8 -*-

import binascii
import os
import struct
import time



from ctypes import *
import CRC



def DataToTimestamp(time_sj):
    # 转换成时间数组
    timeArray = time.strptime(time_sj, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))-946656000
    return timestamp
#print(hex(DataToTimestamp('2020-01-01 00:01:01')))

#数据格式

class _SN_Data(Structure):
  _pack_=1
  _fields_ = [("FileFlag",c_wchar_p),#文件标识16字节
              ("FileLen",c_uint),#文件长度 包括CRC
              ("BureauNum",c_uint),#局编号
              ("MatchCode",c_uint),#匹配码
              ("ChangeTime",c_uint),#换装时间
              ("DWDName",c_wchar_p),#电务段名称 64
              #("DataVer1",c_uint),#数据版本 64
              ("DataVer",c_wchar_p),#数据版本 64
              #("MonitorVer1",c_uint),#监控版本 64
              ("MonitorVer",c_wchar_p),#监控版本 64
              #("OperSection1",c_uint),#运用区段 128
              ("OperSection",c_wchar_p),#运用区段 128
              ("Crc",c_uint)]


def SN_Data(IsCRC,crcnum=0):
    data = _SN_Data()
    data.FileFlag = "SNDATA.TAG"
    data.FileLen = 356
    data.BureauNum = 3
    data.MatchCode = 0x2878918b
    #data.ChangeTime = 0x259e9dbd #需要转换
    data.ChangeTime = DataToTimestamp('2021-07-11 16:37:23') #需要转换
    data.DWDName = '候马电务段'

    #data.DataVer1 = 0x287b39f5
    data.DataVer = 'HM20210716  1008'

    #data.MonitorVer1 = 0x3e
    data.MonitorVer = 'HM20210718 1300'
    #data.OperSection1 = 0x22
    data.OperSection = '侯马,北京,南宁'

    #Write_tempdata = struct.pack("<16s4I64sI60sI60sI124s",data.FileFlag.encode('utf-8'),data.FileLen,data.BureauNum,data.MatchCode,data.ChangeTime,data.DWDName.encode('utf-8'),data.DataVer1,data.DataVer.encode('utf-8'),data.MonitorVer1,data.MonitorVer.encode('utf-8'),data.OperSection1,data.OperSection.encode('utf-8'))
    Write_tempdata = struct.pack("<16s4I64s64s64s128s",data.FileFlag.encode('utf-8'),data.FileLen,data.BureauNum,data.MatchCode,data.ChangeTime,data.DWDName.encode('utf-8'),data.DataVer.encode('utf-8'),data.MonitorVer.encode('utf-8'),data.OperSection.encode('utf-8'))


    if(IsCRC):
        data.CRC = crcnum
        print(hex(data.CRC))
        #Write_tempdata = struct.pack("<16s4I64sI60sI60sI124sI",data.FileFlag.encode('utf-8'),data.FileLen,data.BureauNum,data.MatchCode,data.ChangeTime,data.DWDName.encode('utf-8'),data.DataVer1,data.DataVer.encode('utf-8'),data.MonitorVer1,data.MonitorVer.encode('utf-8'),data.OperSection1,data.OperSection.encode('utf-8'),data.CRC)
        Write_tempdata = struct.pack("<16s4I64s64s64s128sI",data.FileFlag.encode('utf-8'),data.FileLen,data.BureauNum,data.MatchCode,data.ChangeTime,data.DWDName.encode('utf-8'),data.DataVer.encode('utf-8'),data.MonitorVer.encode('utf-8'),data.OperSection.encode('utf-8'),data.CRC)


    return Write_tempdata





def CreatSNDATAFile():
    filename = "SNDATA.TAG"
    with open(filename,"wb+") as f:
        f.write(SN_Data(False))

    crc = CRC.File_Cal_crc32(filename)

    with open(filename,"wb+") as f:
        f.write(SN_Data(True,crc))





if __name__ == '__main__':
    CreatSNDATAFile()


