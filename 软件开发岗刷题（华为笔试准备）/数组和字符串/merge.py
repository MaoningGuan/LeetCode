# -*- coding: utf-8 -*-
"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。



示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        时间复杂度：O(NlogN)，为Python排序函数Timsort算法的时间复杂度
        空间复杂度：O(N)，当各个区间都不能合并的时候，需要跟输入列表一样的存储空间O(N)。
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]

    solution = Solution()
    print(solution.merge(intervals))
