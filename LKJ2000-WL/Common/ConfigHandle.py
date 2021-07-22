#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import configparser
from pathlib import Path

#模块导入
sys.path.append(r"..\\")
import CommFun
import Mygol
Mygol._init()

def initGol():
    mygolList=['StopSendActReply','PlanCancelledFlag','serialPort','LOG','PlanCancelled','WLFileFlag','UpdataModeType','UpgradePlanVer','StopFlag','TrainNum','DataType','OrderID','VoucherCode','ManCode','UpgradeInfo','PlanStartTime','CopeMacTest','DelayPerPack']
    for i in range(len(mygolList)):
        Mygol.set_value(mygolList[i],0)



#读取配置项到全局变量
def readConfig():
    config = configparser.ConfigParser()
    initGol()
    #难搞啊
    if(Path('./config.conf').is_file()):
        config.read(os.path.join(os.getcwd(),"config.conf"),encoding = "utf-8")
        #config.read('E:\软件重构\LKJ2000\config.conf',encoding = "utf-8")
        #获取标签列表
        lists_header = config.sections()


        Mygol.set_value('serialPort',config['SerialConfig']['serialPort'])
        Mygol.set_value('baudRate',int(config['SerialConfig']['baudRate']))
        Mygol.set_value('LOG',int(config['SerialConfig']['LOG']))
        Mygol.set_value('PlanCancelled',int(config['SerialConfig']['PlanCancelled']))
        Mygol.set_value('WLFileFlag',int(config['SerialConfig']['WLFileFlag']))
        Mygol.set_value('UpdataModeType',int(config['SerialConfig']['UpdataModeType']))
        Mygol.set_value('UpgradePlanVer',int(config['SerialConfig']['UpgradePlanVer'],16))
        Mygol.set_value('StopFlag',int(config['SerialConfig']['StopFlag']))
        Mygol.set_value('TrainNum',int(config['SerialConfig']['TrainNum']))
        Mygol.set_value('DataType',int(config['SerialConfig']['DataType']))
        Mygol.set_value('OrderID',config['SerialConfig']['OrderID'])
        Mygol.set_value('VoucherCode',int(config['SerialConfig']['VoucherCode']))
        Mygol.set_value('ManCode',int(config['SerialConfig']['ManCode']))
        Mygol.set_value('UpgradeCount',int(config['SerialConfig']['UpgradeCount']))

        Mygol.set_value('CaseNum',int(config['TestCase']['CaseNum']))
        Mygol.set_value('CaseNum',int(config['TestCase']['CopeMacTest']))


        Mygol.set_value('PlanStartTime',CommFun.TimestampToData(CommFun.DataToTimestamp((config['TKConfig']['PlanStartTime']))))
        Mygol.set_value('PlanEffectiveTime',CommFun.TimestampToData(CommFun.DataToTimestamp((config['TKConfig']['PlanEffectiveTime']))))






