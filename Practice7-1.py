"""
date:2021/10/13
aothor:cpytt
"""
import math


def square_root(a):
    """
    利用牛顿迭代法求a的平方根
    x:a平方根的估计值
    """
    x = a / 2
    while True:
        # print(x)
        y = (x + (a / x)) / 2
        if y == x:
            return y
        x = y


def test_square_root():
    """
    输出一个列表：
    第一列是一个数，a；
    第二列是数a的平方根，使用mysqrt函数计算；
    第三列是使用math.sqrt计算出的平方根；
    第四列是两种计算结果的差值的绝对值；

    其中每一行的输出才用了format格式化函数
    参考网址：https://www.runoob.com/python/att-string-format.html
    """
    print('a     mysqrt(a)           math.sqrt(a)        diff')
    print('-     ---------           ------------        ----')
    for i in range(9):
        print('{:<6}{:<20}{:<20}{}'.format(float(i + 1),
                                           square_root(i + 1),
                                           math.sqrt(i + 1),
                                           abs(square_root(i + 1) - math.sqrt(i + 1))))


test_square_root()
