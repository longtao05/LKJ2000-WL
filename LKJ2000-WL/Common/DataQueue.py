#encoding:utf-8
#系统库导入
import sys
import os
import binascii

import threading 

get_data_lock = threading.Lock()
get_Hdata_lock = threading.Lock()
send_data_lock = threading.Lock()
send_Hdata_lock = threading.Lock()


global ser_get_data_bytes
global ser_send_data_bytes
global ser_get_Hdata_bytes
global ser_send_Hdata_bytes

ser_get_data_bytes = bytearray()
ser_send_data_bytes = bytearray()
ser_get_Hdata_bytes = bytearray()
ser_send_Hdata_bytes = bytearray()

class DataQueue():
    def __init__(self):
       pass

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
