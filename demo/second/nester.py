from builtins import print

"""对 list 进行打印的操作"""


def print_lol(the_list, indent=False, number=0):
    """遍历整个集合的:
    1.假如是集合继续往下遍历
    2.不是集合 打印整个列表"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, number + 1)
        else:
            _range(number, indent)
            print(each_item)


def _range(number, indent):
    if indent:
        for each_item in range(number):
            print("\t", end="")
