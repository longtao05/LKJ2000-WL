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

if __name__ == '__main__':

    #10 02 18 00 01 11 10 ff 01 00 01 05 00 12 34 05 00 12 34 03 03 01 00 01 01 01 0f A8 B6 10 03
#100200000620f90300001e00000000010000d800400004000102030405060100551003

    #print(hex(crc16("000006209fac00001e00000000010000d8004000040001020304050601")))

    #3e7f
    #print(hex(crc16("00000610d0030000140029000000070000000000")))


    #crc16Add("01 00 00 00 00 00 00 00")
    pass

