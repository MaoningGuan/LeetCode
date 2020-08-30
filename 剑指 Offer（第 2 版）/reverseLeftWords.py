# -*- coding: utf-8 -*-
"""
剑指 Offer 58 - II. 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
 

限制：

1 <= k < s.length <= 10000
"""


class Solution:
    def reverseLeftWords_1(self, s: str, n: int) -> str:
        """
        方法一：字符串切片
        时间复杂度 O(N) ： 其中 N 为字符串 s 的长度，字符串切片函数为线性时间复杂度（参考资料）；
        空间复杂度 O(N) ： 两个字符串切片的总长度为 N 。
        :param s:
        :param n:
        :return:
        """
        return s[n:] + s[:n]

    def reverseLeftWords_2(self, s: str, n: int) -> str:
        """
        方法二：列表遍历拼接
        时间复杂度 O(N) ： 线性遍历 s 并添加，使用线性时间；
        空间复杂度 O(N) ： 新建的辅助 res 使用 O(N) 大小的额外空间。
        :param s:
        :param n:
        :return:
        """
        res = []

        # for i in range(n, len(s)):
        #     res.append(s[i])
        # for i in range(n):
        #     res.append(s[i])

        # 利用求余运算，可以简化代码。
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])

        return ''.join(res)

    def reverseLeftWords_3(self, s: str, n: int) -> str:
        """
        方法三：字符串遍历拼接
        时间复杂度 O(N)： 线性遍历 s 并添加，使用线性时间；
        空间复杂度 O(N)： 假设循环过程中内存会被及时回收，
        内存中至少同时存在长度为 N 和 N−1 的两个字符串（新建长度为 N 的 res 需要使用前一个长度 N−1 的 res ），
        因此至少使用 O(N) 的额外空间。
        :param s:
        :param n:
        :return:
        """
        res = ""

        # for i in range(n, len(s)):
        #     res += s[i]
        # for i in range(n):
        #     res += s[i]

        # 利用求余运算，可以简化代码。
        for i in range(n, n + len(s)):
            res += s[i % len(s)]

        return res


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    solution = Solution()
    print(solution.reverseLeftWords_1(s, k))
    print(solution.reverseLeftWords_2(s, k))
    print(solution.reverseLeftWords_3(s, k))
