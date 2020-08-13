# -*- coding: utf-8 -*-
"""
739. 每日温度
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
from typing import List


class Solution:
    def dailyTemperatures_1(self, T: List[int]) -> List[int]:
        """
        方法一：暴力法
        时间复杂度：O(nm)
        空间复杂度：O(m)
        :param T:
        :return:
        """
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10 ** 9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans

    def dailyTemperatures_2(self, T: List[int]) -> List[int]:
        """
        方法二：单调栈
        时间复杂度：O(n)，其中 n 是温度列表的长度。正向遍历温度列表一遍，对于温度列表中的每个下标，最多有一次进栈和出栈的操作。
        空间复杂度：O(n)，其中 n 是温度列表的长度。需要维护一个单调栈存储温度列表中的下标。
        :param T:
        :return:
        """
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    solutiuon = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solutiuon.dailyTemperatures_1(temperatures))
    print(solutiuon.dailyTemperatures_2(temperatures))
