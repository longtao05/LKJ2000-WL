#!/usr/bin/python
# -*-coding: utf-8 -*-

import binascii
import os
import struct
#import CRC


def Test():

    FileFlag=u"SNDATA.TAG"
    print(type(FileFlag),FileFlag)
    FileFlag=FileFlag.encode("utf-8")#写入的文件编码格式为utf-8

    FileFlag = ''.join(['%02X ' % b for b in FileFlag])
    print(type(FileFlag),FileFlag)

    with open("SNDATA.TAG","wb+") as f:
        for x in FileFlag:
            s = struct.pack('B',x)#转换为字节流字符串，B代表unsigned char
            f.write(s)

        #f.write(FileFlag)

Test()
