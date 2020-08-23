# -*- coding: utf-8 -*-
"""
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        """
        位运算
        时间复杂度 O(1) ： 最差情况下（例如 a = 0x7fffffff , b = 1时），需循环 32 次，
        使用 O(1) 时间；每轮中的常数次位操作使用 O(1) 时间。
        空间复杂度 O(1) ： 使用常数大小的额外空间。
        :param a:
        :param b:
        :return:
        """
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    a = 1
    b = 2
    solution = Solution()
    print(solution.add(a, b))
