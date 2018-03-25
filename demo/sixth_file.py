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


def get_coach_data(filename):
    try:
        with open(filename) as main_data:
            read_line = main_data.readlines()
        return set(item for item in read_line)

    except IOError as err:
        print(str('File error' + err))
        return None


search = get_coach_data("sixth_data.txt")

for search_item in search:
    da = search_item.strip().split(",")
    # (search_name, search_db) = da.pop(0), da.pop(0)
    # print(search_name + " s fastest times are:" +
    #       str(sorted(set(sanitize(t) for t in da))[0:3]))

    search_data = {"Name": da.pop(0), "DOB": da.pop(0), "data": da}
    print(search_data)

# 使用字典的方式;
