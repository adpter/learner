from builtins import sorted


# 创建一个类,同时可以使用继承的方式(List) 支持多继承
class Athlete(list):

    def __init__(self, a_name, a_bob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.bob = a_bob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


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


vera = Athlete("123")
vera.append("235-00")
print(vera.top3())
print(type(vera))
print(dir(vera))
