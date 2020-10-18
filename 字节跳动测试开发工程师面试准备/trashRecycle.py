# -*- coding: utf-8 -*-
"""
Python的垃圾回收机制
"""
import sys
class A():
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' %str(hex(id(self))))

def f1():
    '''循环引用变量与删除变量'''
    while True:
        c1=A()
        del c1

def func(c):
    print('obejct refcount is: ',sys.getrefcount(c)) #getrefcount()方法用于返回对象的引用计数


if __name__ == '__main__':
   #生成对象
    a=A()
    func(a)

    #增加引用
    b=a
    func(a)

    #销毁引用对象b
    del b
    func(a)