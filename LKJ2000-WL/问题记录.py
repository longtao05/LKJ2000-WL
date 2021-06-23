#报错：module ‘serial’ has no attribute ‘Serial’
#解决办法：1、卸载serial；2、卸载pyserial；3、重新打开你的编辑器。
#pip uninstall serial
#pip uninstall pyserial
#pip install pyserial


#os.system("pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple")

os.system("pip uninstall  serial")
os.system("pip uninstall pyserial")
os.system("pip install pyserial -i https://pypi.tuna.tsinghua.edu.cn/simple")
