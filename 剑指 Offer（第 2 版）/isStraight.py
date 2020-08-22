# -*- coding: utf-8 -*-
"""
剑指 Offer 61. 扑克牌中的顺子
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，
A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True

示例 2:

输入: [0,0,1,2,5]
输出: True 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .
"""
from typing import List


class Solution:
    def isStraight_1(self, nums: List[int]) -> bool:
        """
        方法一： 集合 Set + 遍历
        时间复杂度 O(N) = O(5) = O(1)： 其中 N 为 nums 长度，本题中 N≡5 ；遍历数组使用 O(N) 时间。
        空间复杂度 O(N) = O(5) = O(1)： 用于判重的辅助 Set 使用 O(N) 额外空间。
        :param nums:
        :return:
        """
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat: return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子

    def isStraight_2(self, nums: List[int]) -> bool:
        """
        方法二：排序 + 遍历
        时间复杂度 O(NlogN)=O(5log5)=O(1) ： 其中 N 为 nums 长度，本题中 N≡5 ；数组排序使用 O(NlogN) 时间。
        空间复杂度 O(1)： 变量 joker 使用 O(1) 大小的额外空间。
        :param nums:
        :return:
        """
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat: return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]

    solution = Solution()
    print(solution.isStraight_1(nums))
    print(solution.isStraight_2(nums))

