# -*- coding: utf-8 -*-
"""
151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。



示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


进阶：

请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
"""
class Solution:
    def reverseWords_1(self, s: str) -> str:
        """
        Python内置函数
        时间复杂度 O(N)
        空间复杂度 O(N) ： 单词列表 strs 占用线性大小的额外空间。
        :param s:
        :return:
        """
        return ' '.join(s.split()[::-1])

    def reverseWords_2(self, s: str) -> str:
        """
        自定义函数
        时间复杂度 O(N) ： 其中 N 为字符串 s 的长度，线性遍历字符串。
        空间复杂度 O(N)
        :param s:
        :return:
        """
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1  # 搜索首个空格
            res.append(s[i + 1: j + 1])  # 添加单词
            while s[i] == ' ': i -= 1  # 跳过单词间空格
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回



if __name__ == '__main__':
    s = "hello world!  "

    solution = Solution()
    print(solution.reverseWords_1(s))
    print(solution.reverseWords_2(s))
