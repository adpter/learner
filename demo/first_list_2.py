# 处理列表的数据

# 函数  def 函数名(参数):

from demo.second import nester

print("************数据的处理******************")
fav_movies = ["one", "two", "there"]


def print_movies_1():
    for each_flick in fav_movies:
        print(each_flick)


def print_movies_2():
    count = 0
    while count < len(fav_movies):
        print(fav_movies[count])
        count += 1


# 打印每一个详细的信息(使用递归的方式);

def print_movies(item):
    for item_list in item:
        # 判断数据类型
        if isinstance(item_list, list):
            print_movies(item_list)
        else:
            print(item_list)


# 2.1 数据的迭代
there_list = ["1_one", "1_two", "1_there"]
there_list.insert(2, ["123", "234"])
fav_movies.insert(2, there_list)
# print_movies_1()
# print_movies_2()
# print_movies(fav_movies)

nester.print_lol(fav_movies, False, 5)
