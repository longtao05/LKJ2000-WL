import os  #引入os 库，os是python自带的库

os.system("pyinstaller -F WLrdBusiness.py")

os.system("copy .\config.conf .\dist\config.conf")
os.system("copy .\说明.txt .\dist\说明.txt")
