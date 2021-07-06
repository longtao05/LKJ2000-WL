# -*- coding: utf-8 -*-

#全局变量管理；主函数初始化一次
def _init():#初始化
    global _global_dict
    _global_dict = {}

def set_value(key,value):
    """ 定义一个全局变量 """
    _global_dict[key] = value

""" 获得一个全局变量,不存在则返回默认值 """
def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
