# -*- encoding=utf-8 -*-
import sys
import serial
import time
import binascii

#import ctypes
from ctypes import *

from Comm import*

def str_to_hex(s):
    """
    字符串 转 16进制
    :param s:
    :return:
    """
    return ' '.join([c.encode().hex() for c in s])

def hex_to_str(s):
    """
    16进制转 str
    :param s:
    :return:
    """
    return bytes.fromhex(s).decode()
'''def test():
  a = [12, 48, 100, 10, 58]
  b = map(lambda x: hex(x).split(‘x’)[1].zfill(2), a)
  print(list(b), type(list(b)))
'''
def hexShow(argv):        #十六进制显示 方法1
    try:
        result = ''
        hLen = len(argv)
        for i in range(hLen):
         hvol = argv[i]
         hhex = '%02x'%hvol
         result += hhex+' '
        print('hexShow:',result)
    except:
        pass


def test():
  #print(windll.kernel32)
  #print(cdll.msvcrt)
  libc = cdll.msvcrt
  #print(libc.time(None))
  #print(hex(windll.kernel32.GetModuleHandleA(None)))

  #print(c_int())
  #print(c_wchar_p("Hello, World"))
  printf = libc.printf
  printf(b"Hello, %s\n", b"World!")
 #print(111)
class POINT(Structure):
  _fields_ = [("x",c_int),
              ("y",c_char),
              ("z",c_char)]
class RECT(Structure):
  _fields_ = [("upperleft",POINT),
              ("lowright",POINT)]


def bytesToHexString(bs):

# hex_str = ‘‘

# for item in bs:

# hex_str += str(hex(item))[2:].zfill(2).upper() + " "

# return hex_str
  return ''.join(['%02X' % b for b in bs])

if __name__ == '__main__':
  pass


  #print(str_to_hex("1234"))
  #print(hex_to_str('79 00 33 34'))
  '''print(bytesToHexString(b'\x11'))
  test()
  point = POINT(10,20)
  print(POINT.x,POINT.y,POINT.z)
  print(point.x,point.y,point.z)
  rc = RECT(POINT(1,2),(3,4))
  print(rc.upperleft.x,rc.upperleft.y,rc.upperleft.z,rc.lowright.x,rc.lowright.y,rc.lowright.z)
print(str_to_hex('\x11'))
print(hex_to_str('5c 78 31 31'))
print(hex_to_str('11'))
t = serial.Serial('com3',115200)

time.sleep(1)     #sleep() 与 inWaiting() 最好配对使用
num=t.inWaiting()

data= str(binascii.b2a_hex(t.read(num)))[2:-1] #十六进制显示方法2
print(data)
print(type(data))
#data =str_to_hex(data)
hexShow(data)
print(data)
print(type(data))
serial.Serial.close(t)'''

'''L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
'''
# 爬取三个网址的信息
# import requests
# response = requests.get("https://www.baidu.com")
# print(response.text)
# requests.get("https://www.cnblogs.com/liunaixu/")
# print(response.text)
# requests.get("https://www.cnblogs.com/linhaifeng/")
# print(response.text)

# 优化上面代码：写一个下载的功能，
# 传参的方案一：
# import requests
# def get(url):
#     # response = requests.get("https://www.baidu.com")
#     # print(response.text)
#     response = requests.get(url)
#     print(len(response.text))
# get("https://www.baidu.com")
# get("https://www.cnblogs.com/liunaixu/")
# get("https://www.cnblogs.com/linhaifeng/")

# 使用闭包函数：方案二
import requests
def outter(url):
    # url='https://www.baidu.com' # 不能写死
    def get():
        response = requests.get(url)
        print(len(response.text))
    return get

baidu = outter('https://www.baidu.com')   # 拿到outter的内存地址
baidu()

bokeyuan = outter('https://www.cnblogs.com/liunaixu/')
bokeyuan()
