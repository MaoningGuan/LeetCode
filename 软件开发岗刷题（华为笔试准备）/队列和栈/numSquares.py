# -*- coding: utf-8 -*-
"""
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n):
        """
        方法四：贪心 + BFS（广度优先搜索）

        :param n:
        :return:
        """
        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            # ! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level


if __name__ == '__main__':
    n = 12
    solution = Solution()
    print(solution.numSquares(n))
