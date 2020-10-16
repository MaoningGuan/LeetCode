# -*- coding: utf-8 -*-
"""
python装饰器实现函数运行时间统计
"""
import time
from functools import wraps


def print_run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration_time = start - end
        print('Execute time of %s is: %s seconds.' % (func.__name__, duration_time))
        return result

    return wrapper


@print_run_time
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(add(1, 3))
