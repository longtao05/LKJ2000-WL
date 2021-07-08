#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import Comm
from pathlib import Path

#模块导入
sys.path.append(r"..\\")
import MyFilegol

MyFilegol._init()
#读取配置项到全局变量

#反转16进制数据
def hextoint(fread,start,bytenum):
    num = 0
    for i in range(bytenum):
        num += fread[start+bytenum-i-1]*16**((bytenum-i-1)*2)
        i+=1
    return num

def isfile(path):
    my_file = Path(path)
    return my_file.is_file()


#print(isfile('./data/param.dat'))
def readMyfile():

    if(isfile('./data/param.dat')):
        with open('./data/param.dat', 'rb') as paramdat:
            param = paramdat.read()

        MyFilegol.set_value('ParamVerInfo[0]',int(binascii.b2a_hex(param[28:29]),16))
        MyFilegol.set_value('ParamVerInfo[1]',int(binascii.b2a_hex(param[29:30]),16))
        MyFilegol.set_value('ParamVerInfo[2]',int(binascii.b2a_hex(param[30:31]),16))
        MyFilegol.set_value('ParamVerInfo[3]',int(binascii.b2a_hex(param[31:32]),16))

        MyFilegol.set_value('ParamVerInfo[4]',int(binascii.b2a_hex(param[32:33]),16))
        MyFilegol.set_value('ParamVerInfo[5]',int(binascii.b2a_hex(param[33:34]),16))
        MyFilegol.set_value('ParamVerInfo[6]',int(binascii.b2a_hex(param[34:35]),16))
        MyFilegol.set_value('ParamVerInfo[7]',int(binascii.b2a_hex(param[35:36]),16))
        MyFilegol.set_value('ParamVerInfo[8]',0)
        MyFilegol.set_value('ParamVerInfo[9]',0)

        x =int(binascii.b2a_hex(param[8:9]),16)
        y =int(binascii.b2a_hex(param[9:10]),16)
        z = int(binascii.b2a_hex(param[10:11]),16)
        b = int(binascii.b2a_hex(param[11:12]),16)
        num = x+y*16**2+z*16**4+b*16**6
        data_js = Comm.TimestampToData(num)
        MyFilegol.set_value('ParamVerInfo[10]',data_js.tm_sec)
        MyFilegol.set_value('ParamVerInfo[11]',data_js.tm_min)
        MyFilegol.set_value('ParamVerInfo[12]',data_js.tm_hour)
        MyFilegol.set_value('ParamVerInfo[13]',data_js.tm_mday)
        MyFilegol.set_value('ParamVerInfo[14]',data_js.tm_mon)
        MyFilegol.set_value('ParamVerInfo[15]',data_js.tm_year-2000)
    else:
        for i in range(16):
            strtmp = 'ParamVerInfo'+'['+str(i)+']'
            MyFilegol.set_value(strtmp,0)


    if(isfile('./data/2kdata.bin')):
        with open('./data/2kdata.bin', 'rb') as k2databin:
            k2datab = k2databin.read()

        x = int(binascii.b2a_hex(k2datab[8:9]),16)
        y = int(binascii.b2a_hex(k2datab[9:10]),16)
        z = int(binascii.b2a_hex(k2datab[10:11]),16)
        b = int(binascii.b2a_hex(k2datab[11:12]),16)
        num = x+y*16**2+z*16**4+b*16**6

        MyFilegol.set_value('K2dataVerInfo[0]',0)
        MyFilegol.set_value('K2dataVerInfo[1]',0)
        MyFilegol.set_value('K2dataVerInfo[2]',0)
        MyFilegol.set_value('K2dataVerInfo[3]',num%100)
        MyFilegol.set_value('K2dataVerInfo[4]',num//100%100)
        MyFilegol.set_value('K2dataVerInfo[5]',(num//10000%10000)-2000)

        x =int(binascii.b2a_hex(k2datab[12:13]),16)
        y =int(binascii.b2a_hex(k2datab[13:14]),16)
        z = int(binascii.b2a_hex(k2datab[14:15]),16)
        b = int(binascii.b2a_hex(k2datab[15:16]),16)
        num = x+y*16**2+z*16**4+b*16**6
        data_js = Comm.TimestampToData(num)
        MyFilegol.set_value('K2dataVerInfo[12]',data_js.tm_sec)
        MyFilegol.set_value('K2dataVerInfo[13]',data_js.tm_min)
        MyFilegol.set_value('K2dataVerInfo[14]',data_js.tm_hour)
        MyFilegol.set_value('K2dataVerInfo[15]',data_js.tm_mday)
        MyFilegol.set_value('K2dataVerInfo[16]',data_js.tm_mon)
        MyFilegol.set_value('K2dataVerInfo[17]',data_js.tm_year-2000)
    else:
        for i in range(18):
            strtmp = 'K2dataVerInfo'+'['+str(i)+']'
            MyFilegol.set_value(strtmp,0)
    if(isfile('./data/2kdata.bin')):

        with open('./data/index.dat', 'rb') as indexdat:
            index = indexdat.read()
        MyFilegol.set_value('BureauNum',hextoint(index,4,1))
        MyFilegol.set_value('ParamLen',hextoint(index,56,4))
        MyFilegol.set_value('ParamCRC',hextoint(index,68,4))
        MyFilegol.set_value('CrcLen',hextoint(index,44,4))
        MyFilegol.set_value('CrcCRC',hextoint(index,64,4))
        MyFilegol.set_value('K2dataLen',hextoint(index,40,4))
        MyFilegol.set_value('K2dataCRC',hextoint(index,60,4))
        MyFilegol.set_value('K2dataXlbLenLen',hextoint(index,96,4))
        MyFilegol.set_value('K2dataXlbLenCRC',hextoint(index,100,4))
        MyFilegol.set_value('K2dataZmbLenLen',hextoint(index,104,4))
        MyFilegol.set_value('K2dataZmbLenCRC',hextoint(index,108,4))
    else:
        MyFilegol.set_value('BureauNum',0)
        MyFilegol.set_value('ParamLen',0)
        MyFilegol.set_value('ParamCRC',0)
        MyFilegol.set_value('CrcLen',0)
        MyFilegol.set_value('CrcCRC',0)
        MyFilegol.set_value('K2dataLen',0)
        MyFilegol.set_value('K2dataCRC',0)
        MyFilegol.set_value('K2dataXlbLenLen',0)
        MyFilegol.set_value('K2dataXlbLenCRC',0)
        MyFilegol.set_value('K2dataZmbLenLen',0)
        MyFilegol.set_value('K2dataZmbLenCRC',0)
    #print(MyFilegol.get_value('BureauNum'))
    '''print(binascii.b2a_hex(index[40:44]))#车载数据长度
    print(binascii.b2a_hex(x[44:48]))#CRC长度
    print(binascii.b2a_hex(x[56:60]))#参数长度
    print(binascii.b2a_hex(x[60:64]))#车载数据CRC
    print(binascii.b2a_hex(x[64:68]))#车载CRC的crc
    print(binascii.b2a_hex(x[68:72]))#参数的crc
    print(binascii.b2a_hex(x[96:100]))#xlb 长度
    print(binascii.b2a_hex(x[100:104]))#xlb的crc
    print(binascii.b2a_hex(x[104:108]))#zmb的
    print(binascii.b2a_hex(x[108:112]))#zmb的crc'''

#readMyfile()






