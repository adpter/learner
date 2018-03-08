"""
文件处理:读取文件的内容及字符串的处理
读取不合法的数据是: 1.使用判断的方式忽略加载的数据
2.使用 try 和 except  异常类型:
BIF : open()
readLine()
seek() 退回到起始位置
close() 关闭文件
split()
find()
not 取反
pass python中的空语句或者 null语句
"""

import os
from builtins import print

# 切换到需要加载的目录;
os.chdir("E:\python_workspace")
# 打开需要打开的文件;
# if os.path.exists("first.txt"):
try:
    data = open("first.txt")

    for each_line in data:
        # 首先需要查找是否":" 没有返回-1 有的话返回具体的位置
        # if not each_line.find(":") != -1:
        # if  each_line.find(":") >= 0:
        try:
            (role, line_spoke) = each_line.split(":", 1)
            print(role, end="")
            print(" said: ", end="")
            print(line_spoke, end="")
        except ValueError:
            # pass
            print(each_line, end="")

    data.close()
except IOError:
    print("the data is missing")

"""(测试文档)
Man:这是一个测试文档
(pause)
OtherMain: I've told you me .
Man: 好吧 就先写这么多
(pause)
OtherMain: 在说以后的事情 Man: 这是一个东西?

"""
