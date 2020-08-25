# -*- coding: utf-8 -*-
"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

限制：

0 <= s 的长度 <= 10000
"""


class Solution:
    def replaceSpace_1(self, s: str) -> str:
        """
        使用内置函数
        :param s:
        :return:
        """
        s = s.replace(' ', '%20')
        return s

    def replaceSpace_2(self, s: str) -> str:
        """
        不使用内置函数
        时间复杂度 O(N) ： 遍历使用 O(N) ，每轮添加（修改）字符操作使用 O(1) ；
        空间复杂度 O(N) ： Python 新建的 list 和 Java 新建的 StringBuilder 都使用了线性大小的额外空间。
        :param s:
        :return:
        """
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)


if __name__ == '__main__':
    s = "We are happy."
    solution = Solution()
    print(solution.replaceSpace_1(s))
    print(s)
    print(solution.replaceSpace_2(s))
    print(s)
