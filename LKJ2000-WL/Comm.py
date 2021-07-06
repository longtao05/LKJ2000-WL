
# coding:utf-8

import sys
import serial
import time
import binascii

#import ctypes
from ctypes import *

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


#时间戳转换为日期:0转换为2000-01-01 00:00:00
def TimestampToData(time_sj):
    time_sj+=946656000 #1970-01-01 00：00：00 ~2000-01-01 00：00：00 的时间戳
    data_sj = time.localtime(time_sj)
    return data_sj

