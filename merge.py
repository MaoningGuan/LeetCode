# -*- coding: utf-8 -*-
"""
56. 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution:
    def merge_1(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        关茂柠的解法：
        优先队列
        时间复杂度：O(NlogN)
        空间复杂度：O(N)
        :param intervals:
        :return:
        """
        import heapq
        intervals = intervals.copy()
        if not intervals:
            return []

        intervals_merge = []
        intervals.sort(key=lambda x: x[0])
        # 用于构建最大堆
        heapq.heappush(intervals_merge, (-intervals[0][1], intervals[0]))

        for interval in intervals[1:]:
            ending, largest_interval = heapq.heappop(intervals_merge)
            # print(ending, largest_interval)
            if -ending >= interval[0]:
                if -ending < interval[1]:
                    largest_interval[1] = interval[1]
                    ending = -interval[1]
                heapq.heappush(intervals_merge, (ending, largest_interval))
            else:
                heapq.heappush(intervals_merge, (ending, largest_interval))
                heapq.heappush(intervals_merge, (-interval[1], interval))

        return sorted([x[1] for x in intervals_merge])

    def merge_2(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        LeetCode官方解法：
        排序解法
        时间复杂度：O(nlogn)，其中 n 为区间的数量。
        除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlogn)。
        空间复杂度：O(logn)，其中 n 为区间的数量。
        这里计算的是存储答案之外，使用的额外空间。O(logn) 即为排序所需要的空间复杂度。
        :param intervals:
        :return:
        """
        intervals = intervals.copy()
        if not intervals:
            return []

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
    solution = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge_1(intervals))
    print(intervals)
    print(solution.merge_2(intervals))
    print(intervals)
