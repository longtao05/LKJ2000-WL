# -*- encoding=utf-8 -*-
import sys
import serial
import time
import binascii

#log日志记录 1：记录 非1：不记录
global LOG
LOG = 1

#计划取消包发送 1：发送 非1：不发送
global PlanCancelled
PlanCancelled = 0

global WLFileFlag #换装标识 0:换装信息无效 1：线路数据 2：控制参数 3：控制参数和线路数据
WLFileFlag = 3

global UpdataModeType #1:自动更新 2:确认更新 3:凭证码
UpdataModeType = 1

global UpgradePlanVer #升级计划版本
UpgradePlanVer = 0x1506110200000000

#换装通知发送标志 # 0 发送
global Flag
Flag = 0



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
  #return ''.join(['%02X' % b for b in bs])

#print(int('0x82c8',16))
