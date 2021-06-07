# -*- encoding=utf-8 -*-
import sys
import serial
import time
import binascii

#import writeLog

from CRC import *
from Comm import *
from WLTypeDef import *
#from ActiDetectionInfoReply import *

class COM:
  def __init__(self, port, baud):
    self.port = port #com端口
    self.baud = int(baud) #波特率
    self.open_com = None
    #self.log = writeLog.writeLog('ITC_LOG.LOG')
    self.get_data_flag = True
    self.real_time_data = ''
    self.getData = []
    self.szTemp = TSciParseInfo()

  # return real time data form com
  def get_real_time_data(self):
    return self.real_time_data

  def clear_real_time_data(self):
    self.real_time_data = ''

  # set flag to receive data or not
  def set_get_data_flag(self, get_data_flag):
    self.get_data_flag = get_data_flag

  def open(self):
    try:
      self.open_com = serial.Serial(self.port, self.baud)
    except Exception as e:
      #self.log.error('Open com fail:{}/{}'.format(self.port, self.baud))
      #self.log.error('Exception:{}'.format(e))
      print("端口打开异常")

  def close(self):
    if self.open_com is not None and self.open_com.isOpen:
      self.open_com.close()

  def send_data(self, data):
    if self.open_com is None:
      self.open()
    #success_bytes = self.open_com.write(data.encode('UTF-8'))
    success_bytes = self.open_com.write(bytes.fromhex(data))

    return success_bytes

  def get_data(self, over_time=0.1):
    all_data = ''
    if self.open_com is None:
      self.open()
    start_time = time.time()
    #print(start_time)

    while True:
      end_time = time.time()
      if end_time - start_time < over_time and self.get_data_flag:
        data = self.open_com.read(self.open_com.inWaiting())
        #休眠0.1秒
        time.sleep(0.1)
        #print(data)
        #print(end_time)
        #print(over_time)
        #data = self.open_com.read() # read 1 size
        #data = self.open_com.readline() # read 1 line \n
        #data = self.open_com.readall() # read 1 line EOF


        data = bytesToHexString(data)

        self.getData.append(data)


        #x = ' '.join([c.encode().hex() for c in data])


        if data != '':
          #self.log.info('Get data is:{}'.format(data))
          all_data = all_data + data
          self.real_time_data = all_data
        else:
            print("get data end")
      else:
        self.set_get_data_flag(True)
        break
    return all_data

def send_data_test(com):
  hexnum = '00 18 11 01 10 02 00 00 00 00 00 15 03 03 12 34 56 78 01 00'
  lkjdata = '10 02 00 00 0C 10 00 00 00 00 00 0E 00 00 00 BE 00 10 03 00'
  #com.send_data(crc16Add(hexnum))
  #time.sleep(1)

  #发送数据到端口
  com.send_data('00 18 11 01 10 02 00 00 00 00 00 15 03 03 12 34 56 78 01 00 23 98')

def get_data_test(com):
    #获取端口数据
    data =com.get_data()
    #print(data)

    #data=data.replace("\\","\\\\")
    #print(data)

    #data = '\x11'
    #data = ' '.join([c.encode().hex() for c in data])
    #print(data)
    #print(type(data))

if __name__ == '__main__':
  print("start")

  com = COM('COM4', 115200)

  com.open()
  i=0
  while(i<10):
    #send_data_test(com)
    #print("send")
    #time.sleep(1)
    get_data_test(com)
    print(com.getData)
    com.getData = []
   #print("get")
    #print(i)

    i+=1

  com.close()
  print("over")
