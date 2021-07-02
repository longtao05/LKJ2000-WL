
# coding:utf-8

import sys
import serial
import time
import binascii
import configparser

#是否使用配制文件 1:使用 非1：不使用
global IsUseConfig
IsUseConfig = 1


#log日志记录 1：记录 非1：不记录
global LOG
#LOG = 1

#计划取消包发送 1：发送 非1：不发送
global PlanCancelled
#PlanCancelled = 0


global WLFileFlag#换装标识 0:换装信息无效 1：线路数据 2：控制参数 3：控制参数和线路数据
#WLFileFlag = 3

global UpdataModeType #1:自动更新 2:确认更新 3:凭证码
#UpdataModeType = 2

global UpgradePlanVer #升级计划版本
#UpgradePlanVer = 0x1506110200000000

#换装通知发送标志 # 0 发送
global Flag
#Flag = 0

#串口
global serialPort
#serialPort = 'COM5'  # 串口



#import ctypes
from ctypes import *


def readConfig():
  global IsUseConfig
  global LOG
  global PlanCancelled
  global WLFileFlag
  global UpdataModeType
  global UpgradePlanVer
  global Flag
  global serialPort
  config = configparser.ConfigParser()
  config.read('config.conf',encoding = "utf-8")

  if(1 == IsUseConfig):

    lists_header = config.sections()  # 配置组名, ['luzhuo.me', 'mysql'] # 不含'DEFAULT'
    #print(lists_header)
    LOG = int(config['Data']['LOG'])
    PlanCancelled = int(config['Data']['PlanCancelled'])
    WLFileFlag = int(config['Data']['WLFileFlag'])
    UpdataModeType = int(config['Data']['UpdataModeType'])
    UpgradePlanVer = int(config['Data']['UpgradePlanVer'],16)
    Flag = int(config['Data']['Flag'])
    serialPort = config['Data']['serialPort']
    #print(serialPort)
  else:
    LOG = 1
    PlanCancelled = 0
    WLFileFlag = 3
    UpdataModeType = 2
    UpgradePlanVer = 0x1506110200000000
    Flag = 0
    serialPort = 'COM6'

  return config



readConfig()



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
