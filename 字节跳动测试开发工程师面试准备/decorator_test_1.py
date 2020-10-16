# -*- coding: utf-8 -*-
"""
利用闭包返回一个计数器函数，每次调用它返回递增整数
"""


def createCounter():
    num = 0

    def counter():
        nonlocal num
        num += 1
        return num

    return counter


def foo():
    print("foo")


def bar(func):
    func()


bar(foo)
