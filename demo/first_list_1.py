print("hello python")

# 实现the holy Grail ,1975 ,Terry Jone& Terry Gilliam ,91 mins
#  Graham Chapman
#     Michal Palin ,Join Cless,  ;


# 列表的学习
movies = ["the holy grail", "the life of brain", "the meaning of life"]
print(movies[0])
# 1.1 列表的长度
print(len(movies))
# 1.2 删除元素
movies.pop(2)
# 1.3 增加元素,位置在最后一位
movies.append("the only of life")
# 1.4 插入一个元素;
movies.insert(2, "hello")
print(movies, len(movies))
# 1.5移除元素;
movies.remove("hello")
# 1.6 插入的数据类型 没有任何限制 可以是任何类型
movies.insert(1, [1945, 2008])
movies.insert(3, 1920)
movies.insert(5, 1936)
print(movies, len(movies))
print(movies[1][0])

