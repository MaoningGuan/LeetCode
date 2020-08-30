# -*- coding: utf-8 -*-
"""
剑指 Offer 17. 打印从1到最大的n位数

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


说明：

用返回一个整数列表来代替打印
n 为正整数
"""
from typing import List


class Solution:
    def printNumbers_1(self, n: int) -> List[int]:
        """
        时间复杂度 O(10^n)： 生成长度为 10^n的列表需使用 O(10^n)时间。
        空间复杂度 O(1)： 建立列表需使用 O(1)，列表作为返回结果，不计入额外空间 ）
        :param n:
        :return:
        """
        return list(range(1, 10 ** n))

    def printNumbers_2(self, n: int) -> [int]:
        """
        大数打印解法：
        时间复杂度 O(10^n)： 递归的生成的排列的数量为 10^n。
        空间复杂度 O(n) ： 字符列表 num， 使用线性大小的额外空间。
        :param n:
        :return:
        """

        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(int(s))
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return res


if __name__ == '__main__':
    n = 1
    solution = Solution()
    print(solution.printNumbers_1(n))
    print(solution.printNumbers_2(n))
