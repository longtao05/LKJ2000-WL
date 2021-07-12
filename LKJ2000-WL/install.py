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
