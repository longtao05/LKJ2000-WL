#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import serial
from datetime import datetime

#模块导入
sys.path.append(r"..\Common")
import Mygol
from DataQueue import *

import DataQueue

class SerialPortData():
    def __init__(self):
        self.Dataqueue = DataQueue.DataQueue()
        serialPort = Mygol.get_value('serialPort')
        baudRate = Mygol.get_value('baudRate')
        self.port = serial.Serial(serialPort, baudRate)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        data = self.Dataqueue.get_send_Hdata()
        data_len = len(data)
        if(data_len<300 and data_len >10):
            self.port.write(data)
            print("发送数据： ",str(datetime.now()),':',binascii.b2a_hex(data))

    def read_data(self):
        global is_exit
        #ser_rawdata_bytes = b''
        count = self.port.inWaiting()
        if count > 0:
            rec_str = self.port.read(count)
            self.Dataqueue.set_get_data(rec_str)
