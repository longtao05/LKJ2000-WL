#encoding:utf-8
#系统库导入
from binascii import *
from crcmod import *

# CRC16-MODBUS
def crc16Add(read):
    #initCrc:0xc33c
    crc16 =crcmod.mkCrcFun(0x18005,rev=True,initCrc=0xc33c,xorOut=0x0000)
    data = read.replace(" ","")
    readcrcout=hex(crc16(unhexlify(data))).upper()
    str_list = list(readcrcout)
    if len(str_list) < 6:
        str_list.insert(2, '0'*(6-len(str_list)))  # 位数不足补0
    crc_data = "".join(str_list)
    print(crc_data)
    read = read.strip()+' '+crc_data[4:]+' '+crc_data[2:4]
    print('CRC16校验:',crc_data[4:]+' '+crc_data[2:4])
    print('增加Modbus CRC16校验：>>>',read)
    #print(type(crc_data))
    return read

# CRC16-MODBUS
def crc16(read):
    #initCrc:0xc33c
    crc16 =crcmod.mkCrcFun(0x18005,rev=True,initCrc=0xc33c,xorOut=0x0000)
    data = read.replace(" ","")
    readcrcout=hex(crc16(unhexlify(data))).upper()
    str_list = list(readcrcout)
    if len(str_list) < 6:
        str_list.insert(2, '0'*(6-len(str_list)))  # 位数不足补0
    crc_data = "".join(str_list)
    crc_data=int(crc_data,16)
    return crc_data


# CRC32-MODBUS
def crc32(read):
    #initCrc:0xc33c3c3c
    crc32 =crcmod.mkCrcFun(0xedb88320,rev=True,initCrc=0xc3c33c3c,xorOut=0x00000000)
    data = read.replace(" ","")
    readcrcout=hex(crc32(unhexlify(data))).upper()
    str_list = list(readcrcout)
    if len(str_list) < 6:
        str_list.insert(2, '0'*(6-len(str_list)))  # 位数不足补0
    crc_data = "".join(str_list)
    crc_data=int(crc_data,16)
    return crc_data


