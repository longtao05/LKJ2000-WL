#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time
from CRC import *
from Comm import *
from WLTypeDef import _ActiDetectionInfoReply

#send_data = b'\x14\x00\x10\x11\x10\x02\x00\x01\x05\x00\x124\x03\x03D3"\x11fU\xc8\x82'

#
send_bytes=bytearray()

def send_data_package(send_data):
    global send_bytes
    global LOG
    data_len=len(send_data)
    if(1==LOG):
        f = open('./log/log.txt', 'ab') # 若是'wb'就表示写二进制文件
        #f.write(b'Senddata:'+str.encode(str(datetime.now()))+b':\n'+binascii.b2a_hex(send_data))
        f.write('发送数据:  时间戳:'.encode('utf-8')+str.encode(str(datetime.now()))+'  包类型:'.encode('utf-8')+binascii.b2a_hex(send_data[4:6])+b"\r\n"+binascii.b2a_hex(send_data))

        f.write(b'\r\n')
        f.close()

    i=0
    #添加头标识
    send_bytes= send_bytes+b'\x10'+b'\x02'# +b'\xa5'
    while(i<data_len):
        if(0x10 == send_data[i]):
            send_bytes =send_bytes + send_data[i].to_bytes(1,byteorder='little', signed=False) + b'\x00'
            #i+=1
        else:
            send_bytes =send_bytes + send_data[i].to_bytes(1,byteorder='little', signed=False)
        i+=1
    #添加尾标识
    send_bytes= send_bytes+b'\x10'+b'\x03'
    #print(type(send_data))
    #print(type(send_bytes))

    send_data = send_bytes
    send_data = bytes(send_data)
    send_bytes[0:]=b''
    return send_data

#send_data_package(send_data)
