#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import configparser
#模块导入
sys.path.append(r"..\\")
import Mygol


#读取配置项到全局变量
def readConfig():
    config = configparser.ConfigParser()
    #难搞啊
    config.read(os.path.join(os.getcwd(),"config.conf"),encoding = "utf-8")
    #config.read('E:\软件重构\LKJ2000\config.conf',encoding = "utf-8")
    #获取标签列表
    print(os.path.join(os.getcwd(),"config.conf"))
    lists_header = config.sections()

    #serialPort = config['SerialConfig']['serialPort']
    #baudRate = int(config['SerialConfig']['baudRate'])
    Mygol.set_value('serialPort',config['SerialConfig']['serialPort'])
    Mygol.set_value('baudRate',int(config['SerialConfig']['baudRate']))

    Mygol.set_value('LOG',int(config['SerialConfig']['LOG']))
    Mygol.set_value('PlanCancelled',int(config['SerialConfig']['PlanCancelled']))
    Mygol.set_value('PlanCancelledFlag',0)
    Mygol.set_value('WLFileFlag',int(config['SerialConfig']['WLFileFlag']))
    Mygol.set_value('UpdataModeType',int(config['SerialConfig']['UpdataModeType']))
    Mygol.set_value('UpgradePlanVer',int(config['SerialConfig']['UpgradePlanVer'],16))
    Mygol.set_value('StopFlag',int(config['SerialConfig']['StopFlag']))
