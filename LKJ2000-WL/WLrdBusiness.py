#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import threading
import binascii
from datetime import datetime
import struct
import csv
import time
import os
import Comm
from DataHandle import *
from SNDataHandle import *

global DEBUG
DEBUG = True

class SerialPort:
    def __init__(self, port, buand):
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()
    #测试2002包周期包：
    def ActiDetectionInfoReply(mSerial):
        #send_data = '1002da9d000004206a00290000000000000072656c6f6164207465737400326b646174612e7a6d620000e68ea5e694b6e58800000c0b051500000c1407154433221101010300000012340000000000000000000000000000000000000000000000000000000000000000000014131003'
        while not is_exit:
            send_data ='100200ff780002201a003f1a0000d8004000040101020304050601017e6f1003'
            #3s未回复会产生重连
            time.sleep(2.5)
            #mSerial.send_data(bytes.fromhex(send_data))
            mSerial.port.write(bytes.fromhex(send_data))
    #测试200A包周期包：
    def HostEventInfoReply(mSerial):
        while not is_exit:
            send_data ='1002083f31000a200e00f60a000001006c201003'
            #3s未回复会产生重连
            time.sleep(0.8)
            #mSerial.send_data(bytes.fromhex(send_data))
            mSerial.port.write(bytes.fromhex(send_data))
    def Test_UpgradePlanCancelled(mSerial):
        global is_exit
        x = 1
        z = 2
        while not is_exit:
            time.sleep(10)
            SN_UpgradePlanCancelled(x,z)
            print("1111111111111")
            time.sleep(200)
    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self,data):
        global LOG
        #self.port.write(bytes.fromhex(data))
        self.port.write(data)
        if(1==LOG):
            print("发送数据：",binascii.b2a_hex(data))
            f = open('./log/sendlog.txt', 'ab') # 若是'wb'就表示写二进制文件
            f.write(binascii.b2a_hex(data))
            f.write(b'\r\n')
            f.close()


    def read_all(port, chunk_size=200):
        global is_exit
        global data_bytes
        '''Read all characters on the serial port and return them.'''
        if not port.timeout:
            raise TypeError('Port needs to have a timeout set!')

        #read_buffer = b''

        #while True:
        while not is_exit:
            # Read in chunks. Each chunk will wait as long as specified by
            # timeout. Increase chunk_size to fail quicker
            byte_chunk = port.read(size=chunk_size)
            data_bytes += byte_chunk
            if not len(byte_chunk) == chunk_size:
                break

        return data_bytes
    def read_data(self):
        global is_exit
        global data_bytes
        global LOG
        while not is_exit:
            count = self.port.inWaiting()

            if count > 0:
                #print(count)
                rec_str = self.port.read(count)
                data_bytes=data_bytes+rec_str
                #print('当前数据接收总字节数：'+str(len(data_bytes))+' 本次接收字节数：'+str(len(rec_str)))
                #print(str(datetime.now()),':',binascii.b2a_hex(rec_str))
                if(1==LOG):
                    f = open('./log/getlog.txt', 'ab') # 若是'wb'就表示写二进制文件
                    f.write(binascii.b2a_hex(data_bytes))
                    f.write(b'\r\n')
                    f.close()
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


'''#按铁科协议解析数据
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

'''
#按SN协议解析数据
def SNprotocolAnalysis():
    global data_Effbytes
    #主线程:对读取的串口数据进行处理过滤
    data_len=len(data_bytes)
    i=0
    invalidflag = 0

    while(i<data_len-1):
        invalidflag = 2
        #数据头 10 02
        if(data_bytes[i]==0x10 and data_bytes[i+1]==0x02):
            i=i+2
            while(i<data_len-1):
                #处理数据中0x10后的
                #随时更新，保证切片数据也能处理
                data_len=len(data_bytes)

                if(data_bytes[i]==0x10 and data_bytes[i+1]==0x00):
                    #删除0x00
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=2

                elif(data_bytes[i]==0x10 and data_bytes[i+1]==0x03):

                    #print("33333333333333")
                    print("串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
                    print("有效数据：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
                    #print("44444444444444")
                    #一包有效数据完整，进行数据处理
                    send_data = SN_data_handle(mSerial,data_Effbytes)
                    #mSerial.send_data(send_data)
                    invalidflag = 1
                    break
                else:
                    data_Effbytes =data_Effbytes + data_bytes[i].to_bytes(1,byteorder='little', signed=False)
                    i+=1
                    invalidflag = 4
                    #print("数据1：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
                    #print("数据2：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
        else:
            i=i+1

    '''if(2 == invalidflag or 4 == invalidflag):
        print("i=",i)
        print("i=",data_bytes[i].to_bytes(1,byteorder='little', signed=False))
        print("len=",data_len)
        print(invalidflag)
        print("无效的串口数据：",str(datetime.now()),':',binascii.b2a_hex(data_bytes))
        print("无效的数据：",str(datetime.now()),':',binascii.b2a_hex(data_Effbytes))
        f = open('./log/log2.txt', 'ab') # 若是'wb'就表示写二进制文件
        f.write(binascii.b2a_hex(data_bytes)+binascii.b2a_hex(invalidflag.to_bytes(length=2,byteorder='big',signed=False)))
        f.write(b'\r\n')
        f.close()'''
    return i

#删除调试log
def dellogfile():
    path = './log/log.txt'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
        os.remove(path)
    path = './log/getlog.txt'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
        os.remove(path)
    path = './log/sendlog.txt'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
        os.remove(path)






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

    #新增周期包发送线程；防止串口数据切片后，周期包识别为无效包，导致主机重C连
    t2 = threading.Thread(target=mSerial.ActiDetectionInfoReply)
    t2.setDaemon(True)
    t2.start()

    #事件处理
    #t3 = threading.Thread(target=mSerial.Test_UpgradePlanCancelled)
    #t3.setDaemon(True)
    #t3.start()
    #删除调试log
    dellogfile()
    while not is_exit:
        #i = TKprotocolAnalysis()
        i = SNprotocolAnalysis()
        data_bytes[0:i]=b''
        data_Effbytes[0:]=b''
        #延时1秒后，发送启动升级信息
        #time.sleep(2)

        #send_data = SN_ActiDetectionInfoReply()
        #mSerial.send_data(send_data)

