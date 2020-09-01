# -*- coding: utf-8 -*-
"""
剑指 Offer 15. 二进制中1的个数
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
 
注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight_1(self, n: int) -> int:
        """
        python内置函数

        :param n:
        :return:
        """
        count = 0
        while True:
            n, remainder = divmod(n, 2)
            if remainder == 1:
                count += 1
            if n == 0:
                return count

    def hammingWeight_2(self, n: int) -> int:
        """
        逐位判断
        时间复杂度 O(log_2 n)： 此算法循环内部仅有 移位、与、加 等基本运算，占用 O(1) ；逐位判断需循环 log_2 n次，
        其中 log_2 n 代表数字 n 最高位 1 的所在位数（例如 log_2 4 = 2, log_2 16 = 4）。
        空间复杂度 O(1)： 变量 res 使用常数大小额外空间。
        :param n:
        :return:
        """
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight_3(self, n: int) -> int:
        """
        时间复杂度 O(M) ： n&(n−1) 操作仅有减法和与运算，占用 O(1) ；
        设 M 为二进制数字 n 中 1 的个数，则需循环 M 次（每轮消去一个 1 ），占用 O(M) 。
        空间复杂度 O(1) ： 变量 res 使用常数大小额外空间。
        :param n:
        :return:
        """
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res


if __name__ == '__main__':
    n = 0b1101
    print(n)

    solution = Solution()
    print(solution.hammingWeight_1(n))
    print(solution.hammingWeight_2(n))
    print(solution.hammingWeight_3(n))

