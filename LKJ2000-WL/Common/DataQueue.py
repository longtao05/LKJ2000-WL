#encoding:utf-8
#系统库导入
import sys
import os
import binascii

import threading
import queue  # 不能用于多进程之间的通讯，可以用于多线程间的通讯
from multiprocessing import Queue  # 可以用于进程之间的数据共享

get_data_lock = threading.Lock()
get_Hdata_lock = threading.Lock()
send_data_lock = threading.Lock()
send_Hdata_lock = threading.Lock()
canA_recv_data_lock = threading.Lock()
canB_recv_data_lock = threading.Lock()
can_send_data_lock = threading.Lock()


global ser_get_data_bytes
global ser_send_data_bytes
global ser_get_Hdata_bytes
global ser_send_Hdata_bytes

ser_get_data_bytes = bytearray()
ser_send_data_bytes = bytearray()
ser_get_Hdata_bytes = bytearray()
ser_send_Hdata_bytes = bytearray()

canA_recv_data =  Queue()  # 创建一个队列对象,队列长度为1000
canB_recv_data =  Queue()  # 创建一个队列对象,队列长度为1000
can_send_data =  Queue()  # 创建一个队列对象,队列长度为1000

class DataQueue():
    def __init__(self):
        pass
    def put_canA_recv_data(self,data):
        ret = False
        with canA_recv_data_lock:
            if(False == canA_recv_data.full()):
                canA_recv_data.put(data)
                ret = True
                #调试
                #print(hex(canA_recv_data.get().ID))
        return ret
    def get_canA_recv_data(self):
        ret = False
        data = ''
        with canA_recv_data_lock:
            if(False == canA_recv_data.empty()):
                data = canA_recv_data.get()
                ret = True
        return [ret, data]

    def put_can_send_data(self,data):
        ret = False
        with can_send_data_lock:
            if(False == can_send_data.full()):
                can_send_data.put(data)
                ret = True
                #调试
                #print(hex(can_send_data.get().ID))
        return ret
    def get_can_send_data(self):
        ret = False
        data = ''
        with can_send_data_lock:
            if(False == can_send_data.empty()):
                data = can_send_data.get()
                ret = True
        return [ret, data]
    def put_canB_recv_data(self,data):
        ret = False
        with canB_recv_data_lock:
            if(False == canB_recv_data.full()):
                canB_recv_data.put(data)
                ret = True
                #调试
                #print(hex(canA_recv_data.get().ID))
        return ret
    def get_canB_recv_data(self):
        ret = False
        data = ''
        with canB_recv_data_lock:
            if(False == canB_recv_data.empty()):
                data = canB_recv_data.get()
                ret = True
        return [ret, data]
    def set_get_data(self,dbytes):
        global ser_get_data_bytes
        with get_data_lock:
            ser_get_data_bytes += dbytes

    def get_get_data(self):
        global ser_get_data_bytes
        retdata = b''
        with get_data_lock:
            retdata = ser_get_data_bytes
            ser_get_data_bytes = b''
        return retdata


    def set_get_Hdata(self,dbytes):
        global ser_get_Hdata_bytes
        with get_Hdata_lock:
            ser_get_Hdata_bytes += dbytes

    def get_get_Hdata(self):
        global ser_get_Hdata_bytes
        retdata = b''
        with get_Hdata_lock:
            retdata =  ser_get_Hdata_bytes
            ser_get_Hdata_bytes = b''
        return retdata

    def set_send_data(self,dbytes):
        global ser_send_data_bytes
        with send_data_lock:
            ser_send_data_bytes += dbytes

    def get_send_data(self):
        global ser_send_data_bytes
        retdata = b''
        with send_data_lock:
            retdata =  ser_send_data_bytes
            ser_send_data_bytes = b''
        return retdata

    def set_send_Hdata(self,dbytes):
        with send_Hdata_lock:
            global ser_send_Hdata_bytes
            ser_send_Hdata_bytes += dbytes

    def get_send_Hdata(self):
        global ser_send_Hdata_bytes
        retdata = b''
        with send_Hdata_lock:
            retdata = ser_send_Hdata_bytes
            ser_send_Hdata_bytes = b''
        return retdata
