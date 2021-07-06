#encoding:utf-8
#系统库导入
import sys
import os
import binascii
import configparser
import comm
#模块导入
sys.path.append(r"..\\")
import Mygol

Mygol._init()
#读取配置项到全局变量
def readConfig():
    config = configparser.ConfigParser()
    #难搞啊
    config.read(os.path.join(os.getcwd(),"config2.conf"),encoding = "utf-8")
    #config.read('E:\软件重构\LKJ2000\config.conf',encoding = "utf-8")
    #获取标签列表
    print(os.path.join(os.getcwd(),"config.conf"))
    lists_header = config.sections()

    with open('./data/param.dat', 'rb') as paramdat:
        param = paramdat.read()

    Mygol.set_value('ParamVerInfo[0]',int(binascii.b2a_hex(param[28:29])))
    Mygol.set_value('ParamVerInfo[1]',int(binascii.b2a_hex(param[29:30])))
    Mygol.set_value('ParamVerInfo[2]',int(binascii.b2a_hex(param[30:31])))
    Mygol.set_value('ParamVerInfo[3]',int(binascii.b2a_hex(param[31:32])))

    print(int(binascii.b2a_hex(param[28:32])))
    print(Mygol.get_value('ParamVerInfo[0]'))
    print(Mygol.get_value('ParamVerInfo[1]'))
    print(Mygol.get_value('ParamVerInfo[2]'))
    print(Mygol.get_value('ParamVerInfo[3]'))


    with open('./data/2kdata.bin', 'rb') as k2databin:
        k2datab = k2databin.read()
    Mygol.set_value('K2dataVerInfo[0]',int(binascii.b2a_hex(k2datab[8:9]),16))
    Mygol.set_value('K2dataVerInfo[1]',int(binascii.b2a_hex(k2datab[9:10]),16))
    Mygol.set_value('K2dataVerInfo[2]',int(binascii.b2a_hex(k2datab[10:11]),16))
    Mygol.set_value('K2dataVerInfo[3]',int(binascii.b2a_hex(k2datab[11:12]),16))

    x= k2datab[8:12].to_bytes(1,byteorder='little', signed=False)

    print(x)



    print(xxx)
    print((binascii.b2a_hex(k2datab[8:12])))

    print(Mygol.get_value('K2dataVerInfo[0]'))
    print(Mygol.get_value('K2dataVerInfo[1]'))
    print(Mygol.get_value('K2dataVerInfo[2]'))
    print(Mygol.get_value('K2dataVerInfo[3]'))


    #需要把秒转换为日期数
    Mygol.set_value('K2dataVerInfoTime',int(binascii.b2a_hex(k2datab[12:16]),16))




    with open('./data/index.dat', 'rb') as f:
        x = f.read()
    print(binascii.b2a_hex(x))
    print(binascii.b2a_hex(x[0:1]))
    print(binascii.b2a_hex(x[28:32]))
    print(binascii.b2a_hex(x[32:36]))

    #serialPort = config['SerialConfig']['serialPort']
    #baudRate = int(config['SerialConfig']['baudRate'])
    Mygol.set_value('serialPort',config['SerialConfig']['serialPort'])
    Mygol.set_value('baudRate',int(config['SerialConfig']['baudRate']))
    Mygol.set_value('dataType',config['DataTypeConfig']['dataType'])
    Mygol.set_value('LOG',int(config['SerialConfig']['LOG']))
    Mygol.set_value('SendLOG',int(config['SerialConfig']['SendLOG']))
    Mygol.set_value('UpgradeInfo',int(config['SerialConfig']['UpgradeInfo']))
    Mygol.set_value('PlanCancelled',int(config['SerialConfig']['PlanCancelled']))
    Mygol.set_value('WLFileFlag',int(config['SerialConfig']['WLFileFlag']))
    Mygol.set_value('UpdataModeType',int(config['SerialConfig']['UpdataModeType']))
    Mygol.set_value('UpgradePlanVer',int(config['SerialConfig']['UpgradePlanVer'],16))

    #包数据
#    Mygol.set_value('0x1001','')

    #print(config['SerialConfig']['LOG'])
readConfig()
