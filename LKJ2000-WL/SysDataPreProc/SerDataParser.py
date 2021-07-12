#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import time
from datetime import datetime

#模块导入
sys.path.append(r"..\Common")

import Mygol
import DataQueue

global data
data = bytearray()
global data_Effbytes
data_Effbytes=bytearray()

send_bytes=bytearray()


class SerDataParser():
    def __init__(self):
        self.Dataqueue = DataQueue.DataQueue()

    #原始数据转译处理，后续改进。
    def SerGetDataTran(self):
        #数据写文件
        global data
        global data_Effbytes
        data = data + self.Dataqueue.get_get_data()
        data_len = len(data)
        i = 0
        n=0
        while(i<data_len-1):
            #数据头 10 02

            if(data[i]==0x10 and data[i+1]==0x02):
                n = i
                i=i+2
                while(i<data_len-1):
                    #处理数据中0x10后的
                    if(data[i]==0x10 and data[i+1]==0x00):
                        #删除0x00
                        data_Effbytes =data_Effbytes + data[i].to_bytes(1,byteorder='little', signed=False)
                        i+=2

                    elif(data[i]==0x10 and data[i+1]==0x03):
                        print("串口数据   ",str(datetime.now()),':',binascii.b2a_hex(data))
                        #print("解译后：  ",binascii.b2a_hex(data_Effbytes))
                        self.Dataqueue.set_get_Hdata(data_Effbytes)
                        data_Effbytes[0:]=b''
                        #继续解析下一包
                        i+=2
                        n=i
                        break
                    else:
                        data_Effbytes =data_Effbytes + data[i].to_bytes(1,byteorder='little', signed=False)
                        i+=1
            else:
                i=i+1
        #防止一包数据不完整发生丢失
        if(data != data[n:]):
            data = data[n:]
        data_Effbytes[0:]=b''



    #数据转译处理。
    def SerSendDataTran(self):
        send_data = self.Dataqueue.get_send_data()
        global send_bytes
        data_len=len(send_data)

        #data_len = binascii.b2a_hex(send_data[5:7])
        #print("11111111111111",data_len)


        i=0
        #添加头标识
        if(data_len<200 and data_len>0):
            if(1==Mygol.get_value('LOG')):
                f = open('./log/log.txt', 'ab') # 若是'wb'就表示写二进制文件
                #f.write(b'Senddata:'+str.encode(str(datetime.now()))+b':\n'+binascii.b2a_hex(send_data))
                f.write('发送数据:  时间戳:'.encode('utf-8')+str.encode(str(datetime.now()))+'  包类型:'.encode('utf-8')+binascii.b2a_hex(send_data[4:6])+b"\r\n"+binascii.b2a_hex(send_data))

                f.write(b'\r\n')
                f.close()

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
            send_data = send_bytes
            send_data = bytes(send_data)
            self.Dataqueue.set_send_Hdata(send_bytes)

            send_bytes[0:]=b''
            send_data=b''
