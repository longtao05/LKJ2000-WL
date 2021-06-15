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
from SNDataHandle import *

global DEBUG
DEBUG = True
global LOG
LOG = True
class SerialPort:
    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self,data):
        #self.port.write(bytes.fromhex(data))
        self.port.write(data)
        print("发送数据：",binascii.b2a_hex(data))
        f = open('./log/log1.txt', 'ab') # 若是'wb'就表示写二进制文件
        f.write(binascii.b2a_hex(data))
        f.write(b'\r\n')
        f.close()



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

            else:
                pass
                #time.sleep(1)
                #print("串口无数据")

serialPort = 'COM6'  # 串口
baudRate = 115200  # 波特率C
is_exit=False
data_bytes=bytearray()
global data_Effbytes
data_Effbytes=bytearray()


#按铁科协议解析数据
def TKprotocolAnalysis():
    global data_Effbytes
    #主线程:对读取的串口数据进行处理过滤
    data_len=len(data_bytes)
    i=0
    invalidflag = 0

    while(i<data_len-1):
        #数据头 10 02 a5
        if(data_bytes[i]==0x10 and data_bytes[i+1]==0x02 and data_bytes[i+2]==0xA5):
            i=i+3
            while(i<dataB_len-1):
                #处理数据中0x10后的
                if(data_bytes[i]==0x10 and data_bytes[i+1]==0x00 and data_bytes[i+1]!=0x03):
                    #删除0xff
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=2

                elif(data_bytes[i]==0x5A and data_bytes[i+1]==0x10 and data_bytes[i+2]==0x03):

                    print("1111111111111")
                    print("串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
                    print("有效数据：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
                    print("2222222222222")
                    #一包有效数据完整，进行数据处理
                    send_data = data_handle(data_Effbytes)
                    mSerial.send_data(send_data)
                    invalidflag = 1

                    break
                else:
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=1
        else:
            i=i+1



    return i

#按SN协议解析数据
def SNprotocolAnalysis():
    global data_Effbytes
    #主线程:对读取的串口数据进行处理过滤
    data_len=len(data_bytes)
    i=0
    invalidflag = 0

    while(i<data_len-1):
        #数据头 10 02
        if(data_bytes[i]==0x10 and data_bytes[i+1]==0x02):
            i=i+2
            while(i<data_len-1):
                #处理数据中0x10后的
                if(data_bytes[i]==0x10 and data_bytes[i+1]==0x00 and data_bytes[i+1]!=0x03):
                    #删除0x00
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=2

                elif(data_bytes[i]==0x10 and data_bytes[i+1]==0x03):

                    print("33333333333333")
                    print("串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
                    print("有效数据：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
                    print("44444444444444")
                    #一包有效数据完整，进行数据处理
                    send_data = SN_data_handle(mSerial,data_Effbytes)
                    #mSerial.send_data(send_data)
                    invalidflag = 1
                    break
                else:
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=1
        else:
            i=i+1

    if(0 == invalidflag):
        print('9'*9)
        print("无效的串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
        f = open('./log/log2.txt', 'ab') # 若是'wb'就表示写二进制文件
        f.write(binascii.b2a_hex(data_bytes))
        f.write(b'\r\n')
        f.close()
    return i
if __name__ == '__main__':
    #打开串口
    mSerial = SerialPort(serialPort, baudRate)

    #mSerial.send_data("11 22 33 44")
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
        #i = TKprotocolAnalysis()
        i = SNprotocolAnalysis()
        data_bytes[0:i]=b''
        data_Effbytes[0:]=b''
        #延时1秒后，发送启动升级信息
        time.sleep(0.05)

        #send_data = SN_UpgradePlanCancelled()
        #mSerial.send_data(send_data)

