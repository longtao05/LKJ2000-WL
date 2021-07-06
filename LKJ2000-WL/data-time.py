#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 14:09
# @Author  : admin
# @Site    :
# @File    : time_api.py
# @Software: PyCharm

import time

'''
常规时间转换为时间戳
'''
test1 = '2019-8-01 00:00:00'
def time_data1(time_sj):                #传入单个时间比如'2019-8-01 00:00:00'，类型为str
    data_sj = time.strptime(time_sj,"%Y-%m-%d %H:%M:%S")       #定义格式
    time_int = int(time.mktime(data_sj))
    return time_int             #返回传入时间的时间戳，类型为int



'''
时间戳转换年月日时间格式
'''
test2 = 1564588800
def time_data2(time_sj):     #传入参数
    data_sj = time.localtime(time_sj)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S",data_sj)            #时间戳转换正常时间
    return time_str       #返回日期，格式为str


#时间戳转换为日期:0转换为2000-01-01 00:00:00
def TimestampToData(time_sj):
    time_sj+=946656000 #1970-01-01 00：00：00 ~2000-01-01 00：00：00 的时间戳
    data_sj = time.localtime(time_sj)
    return data_sj

#琪日期转换为时间戳 :2000-01-01 00:00:00 为 0
def DataToTimestamp(time_sj):
    time_sj+=946656000 #1970-01-01 00：00：00 ~2000-01-01 00：00：00 的时间戳
    data_sj = time.localtime(time_sj)
    return data_sj



if __name__ == '__main__':
    startdata = '2000-01-01 00:00:00'
    test1 = '2000-01-01 00:00:59'
    test2 = 0 + 946656000
    time1_def = time_data1(test1) - time_data1(startdata)
    print('函数一将日期转换为时间戳----->:',time1_def)
    time2_def = time_data2(test2)
    print('函数二将时间戳转换为常规日期----->:',time2_def)

    data = TimestampToData(6974580)
    print(data.tm_year)
    print(TimestampToData(677236306))


