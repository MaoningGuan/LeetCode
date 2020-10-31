# -*- coding: utf-8 -*-
"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/17_telephone_keypad.png

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法：回溯（使用递归来实现回溯算法）
        时间复杂度：O(3^m x 4^n)
        空间复杂度：O(m+n)
        其中 m 是输入中对应 3 个字母的数字个数（包括数字 2、3、4、5、6、8），
        n 是输入中对应 4 个字母的数字个数（包括数字 7、9），m+n 是输入数字的总个数。
        :param digits:
        :return:
        """
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == '__main__':
    digits = "23"

    solution = Solution()
    print(solution.letterCombinations(digits))
