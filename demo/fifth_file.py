# 处理数据
import os
from builtins import print

os.chdir("E:\python_workspace")


# 处理异常的数据;
def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, second) = time_string.split(splitter, 2)
    return mins + "." + second


with open("data.txt") as sp:
    read_line = sp.readlines()

for item_data in read_line:
    sp = item_data.strip().split(",")

    """创建一个新的列   表保存转化后的数据
        迭代    每个数据
        迭代每个数据
        迭代完成处理异常的数据
        追加到新的   集合中"""
    # new_data = []
    # for item_sp in sp:
    #     new_data.append(sanitize(item_sp))
    # 使用列表推到的方式
    new_data = [sanitize(time_string) for time_string in sp]
    new_data.sort()
    # reverse 升序处理;
    # set() 工厂方法 获得一个不重合的集合
    print(sorted(set(new_data), reverse=False)[0:30])
    # unique_data = []
    # for each_t in new_data:
    #     if each_t not in unique_data:
    #         unique_data.append(each_t)

    # print(unique_data[0:3])

# 数据的排序;
data = [1, 3, 4, 2, 6, 5]
# 1.
# data.sort()
data2 = sorted(data)
print(data2)

# 测试数据;
mins = [1, 2, 3]

secs = [m * 60 for m in mins]
print(secs)
