# -*- coding: utf-8 -*-
"""
python装饰器实现函数运行时间统计
"""
import time
from functools import wraps
import random


# 装饰器函数
def print_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        print("execute time running %s: %s seconds" % (func.__name__, duration_time))
        return result

    return wrapper


# 通过注解方式声明使用装饰器
@print_info
def random_sort_1(n):
    time.sleep(3)
    return sorted([random.random() for i in range(n)])


if __name__ == "__main__":
    x = random_sort_1(100)
    print(x)
