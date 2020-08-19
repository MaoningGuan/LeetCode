# -*- coding: utf-8 -*-
"""
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
 
示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

提示：
0 <= num < 231
"""


class Solution:
    def translateNum_1(self, num: int) -> int:
        """
        方法一：字符串遍历
        时间复杂度 O(N)： N 为字符串 s 的长度（即数字 num 的位数 log(num) ），其决定了循环次数。
        空间复杂度 O(N)： 字符串 s 使用 O(N) 大小的额外空间。
        :param num:
        :return:
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a

    def translateNum_2(self, num: int) -> int:
        """
        方法二：数字求余
        时间复杂度 O(N)： N 为字符串 s 的长度（即数字 num 的位数 log(num) ），其决定了循环次数。
        空间复杂度 O(1)： 几个变量使用常数大小的额外空间。
        :param num:
        :return:
        """
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a

if __name__ == '__main__':
    num = 25
    solution = Solution()
    print(solution.translateNum_1(num))
    print(solution.translateNum_2(num))
