import os  #引入os 库，os是python自带的库

os.system("pyinstaller -F -p ./Common;./BusinessManager;./Comm;./DataManager;./Graphic;./SysDataPreProc;./LogSys; --distpath package --workpath package Main.py -n WLLKJ2000")

os.system("copy .\config.conf .\package\config.conf")
os.system("copy .\说明.txt .\package\说明.txt")
os.system("xcopy .\data .\package\data /s")
