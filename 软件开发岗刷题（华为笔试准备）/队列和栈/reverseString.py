# -*- coding: utf-8 -*-
"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""
from typing import List


class Solution:
    def reverseString_1(self, s: List[str]) -> None:
        """
        方法一：双指针（递归）
        时间复杂度：O(N)。执行了 N/2 次的交换。
        空间复杂度：O(N)，递归过程中使用的堆栈空间 N/2 。
        Do not return anything, modify s in-place instead.
        """

        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        return s

    def reverseString_2(self, s):
        """
        方法二：双指针法（迭代）
        时间复杂度：O(N)。执行了 N/2 次的交换。
        空间复杂度：O(1)，只使用了常数级空间。
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s


if __name__ == '__main__':
    s = ["H", "a", "n", "n", "a", "h"]

    solution = Solution()
    print(solution.reverseString_1(s))
    s = ["H", "a", "n", "n", "a", "h"]
    print(solution.reverseString_2(s))
