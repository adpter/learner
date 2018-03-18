import os
from builtins import print

from demo.second.nester import print_lol
import pickle

os.chdir("E:\python_workspace")

man = []
other = []

try:
    """w 写的模式  打开指定的文件,假如没有没有,之间创建一个文件 有则打开文件并清空里边的内容
      w+ 打开一个文件进行写和读 不清除文件的内容;
      r 读的模式(默认)"""
    data = open("first.txt")

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(":", 1)
            # 去掉空白的字符串
            line_spoken = line_spoken.strip()
            if role == "Man":
                man.append(line_spoken)
            elif role == "OtherMain":
                other.append(line_spoken)
        except ValueError:
            # print("read is error ")
            pass
    data.close()
except IOError:
    print("The datafile is missing!")

    """把数据写进文件中1"""

# try:
#     man_file = open("man_data.txt", "w")
#     other_file = open("other_data.txt", "w")
#
#     print(man, file=man_file)
#     print(other, file=other_file)
#     # 异常信息的处理 as error 打印出错误的信息;
# except IOError as err:
#     print("file error", str(err))
#
# finally:
#     # locals()?
#     if "data" in locals():
#         man_file.close()
#     other_file.close()

# with 使用with() 无论with中出现任何错误 都会执行file.close()
# try:
#     with open("man_data.txt", "w") as man_file, open("other_data.txt", "w") as other_file:
#         print(man, file=man_file)
#         print(other, file=other_file)
# except IOError as error:
#     print("File is Error" + str(error))

#
# with open("man_data.txt") as mdf:
#     print_lol(man, fh=mdf)

with open("mydata.txt", "wb") as man_file:
    # 写入数据(保存为二进制的文件)
    pickle.dump(["1", "2", "3"], man_file)

with open("mydata.txt", "rb") as man_file:
    # 读取文件恢复文件的
    a_list = pickle.load(man_file)

print(a_list)
