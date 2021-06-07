#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time

from DataHandle import *

class SerialPort:
    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        self.open_com = None
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        self.port.write('')

    def send_data(self, data):
    if self.open_com is None:
      self.open()
    #success_bytes = self.open_com.write(data.encode('UTF-8'))
    success_bytes = self.open_com.write(bytes.fromhex(data))
    return success_bytes

    def read_data(self):
        global is_exit
        global data_bytes
        while not is_exit:
            count = self.port.inWaiting()
            if count > 0:
                rec_str = self.port.read(count)
                data_bytes=data_bytes+rec_str
                print('当前数据接收总字节数：'+str(len(data_bytes))+' 本次接收字节数：'+str(len(rec_str)))
                print(str(datetime.now()),':',binascii.b2a_hex(rec_str))


serialPort = 'COM1'  # 串口
baudRate = 115200  # 波特率C
is_exit=False
data_bytes=bytearray()
global data_Effbytes
data_Effbytes=bytearray()


if __name__ == '__main__':
    #打开串口
    mSerial = SerialPort(serialPort, baudRate)

    '''#文件写入操作
    #filename=input('请输入文件名：比如test.csv:')
    filename='test.csv'
    dt=datetime.now()
    nowtime_str=dt.strftime('%y-%m-%d %I-%M-%S')  #时间
    filename=nowtime_str+'_'+filename
    out=open(filename,'a+')
    csv_writer=csv.writer(out)'''

    #开始数据读取线程
    t1 = threading.Thread(target=mSerial.read_data)
    t1.setDaemon(True)
    t1.start()


    #开始数据处理线程
    '''t2 = threading.Thread(target=data_handle)
    t2.setDaemon(True)
    t2.start()'''


    while not is_exit:
        #主线程:对读取的串口数据进行处理过滤
        data_len=len(data_bytes)
        i=0
        while(i<data_len-1):
            #数据头
            if(data_bytes[i]==0x10 and data_bytes[i+1]==0x02):
                i=i+2
                while(i<data_len-1):
                    #处理数据中0x10后的
                    if(data_bytes[i]==0x10 and data_bytes[i+1]==0x00 and data_bytes[i+1]!=0x03):
                        pass
                        #删除0xff
                        data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                        i+=2

                    elif(data_bytes[i]==0x10 and data_bytes[i+1]==0x03):
                        print("1111111111111")
                        print("串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
                        print("有效数据：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
                        print("2222222222222")
                        #一包有效数据完整，进行数据处理
                        data_handle(data_Effbytes)
                        break
                    else:
                        data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                        i+=1
            else:
                i=i+1
        data_bytes[0:i]=b''
        data_Effbytes[0:]=b''
