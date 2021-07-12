#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
import struct


#模块导入


def str_to_hex(s):
    """
    字符串 转 16进制
    :param s:
    :return:
    """
    return ' '.join([c.encode().hex() for c in s])

def hex_to_str(s):
    """
    16进制转 str
    :param s:
    :return:
    """
    return bytes.fromhex(s).decode()


def int_to_binascii(data,bits):

  return binascii.b2a_hex(data.to_bytes(bits,byteorder='little', signed=False))

def bytesToHexString(bs):

  hex_str = ''

  for item in bs:

    hex_str += str(hex(item))[2:].zfill(2).upper() + " "

  return hex_str
  #return ''.join(['%02X' % b for b in bs])

#print(int('0x82c8',16))



#时间戳转换为日期:0转换为2000-01-01 00:00:00
def TimestampToData(time_sj):
    time_sj+=946656000 #1970-01-01 00：00：00 ~2000-01-01 00：00：00 的时间戳
    data_sj = time.localtime(time_sj)
    return data_sj
#日期转换为时间戳:2000-01-01 00:00:00转换为0
def DataToTimestamp(time_sj):
    # 转换成时间数组
    timeArray = time.strptime(time_sj, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))-946656000
    return timestamp






