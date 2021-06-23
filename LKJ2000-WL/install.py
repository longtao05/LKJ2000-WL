import os  #引入os 库，os是python自带的库

#将要批量安装的第三方库写进一个列表
libs = ["numpy","matplotlib","pillow","sklearn","scipy","requests","jieba","pyspider",
        "quads","beautifulsoup4","wheel","networkx","sympy","pyinstaller","django",
        "flask","werobot","pyqt5","pandas","pyopengl","pypdf2","docopt","pygame"]

#无线换装安装库
WLlibs = ["serial"]
#使用try，expect结构运行，如果try部分出错，则执行except部分的代码
#对列表libs进行遍历，执行os.system命令


#os.system("pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple")

try:
    for lib in WLlibs:
        os.system("pip install " + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple")
    print("安装成功")
except:
    print("安装失败")
68740000051046000b000000010000003100000000000000000000000000000000000000000000000000000000000000  00 14 05 00 0000000000000000332d09160615010100003609

111100000910420022000000000000003100000000000000000000000000000000000000000000000000000000000000001405000300 0200 021106150000000000001258


3f1600000710160035000000
55 0001 04 00 5d 00 00 62 00 b1c6

3f160000071016003500000055000104005d00006200b1c6
