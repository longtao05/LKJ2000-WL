#encoding:utf-8
#系统库导入
import sys
import os
import binascii

def _init():#初始化
    global _file_global_dict
    _file_global_dict = {}

def set_value(key,value):
    """ 定义一个全局变量 """
    _file_global_dict[key] = value

""" 获得一个全局变量,不存在则返回默认值 """
def get_value(key,defValue=None):
    try:
        return _file_global_dict[key]
    except KeyError:
        return defValue
