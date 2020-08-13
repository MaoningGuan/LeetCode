# -*- coding: utf-8 -*-
"""
253. 会议室 II
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1
"""
from typing import List


class Solution:
    def minMeetingRooms_1(self, intervals: List[List[int]]) -> int:
        """
        方法一：优先队列
        时间复杂度：O(NlogN) 。最小堆的查找、插入和删除最小值操作只消耗O(logN) 的时间，在最坏的情况下，我们要对堆进行 N 次查找并删除最小值操作，
        总的时间复杂度为 (NlogN)(NlogN)。
        :param intervals:
        :return:
        """
        import heapq
        intervals = intervals.copy()
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

    def minMeetingRooms_2(self, intervals: List[List[int]]) -> int:
        """
        方法二：有序化（双指针）
        时间复杂度: O(NlogN)。我们所做的只是将 开始时间 和 结束时间 两个数组分别进行排序。每个数组有 N 个元素，因为有 N 个时间间隔。
        空间复杂度: O(N)。我们建立了两个 N 大小的数组。分别用于记录会议的开始时间和结束时间。
        :param intervals:
        :return:
        """
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms


if __name__ == '__main__':
    solution = Solution()

    # (1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)
    meetings = [[1, 10], [3, 19], [8, 12], [2, 7], [11, 30], [10, 20]]
    print(solution.minMeetingRooms_1(meetings))
    # print(meetings)
    print(solution.minMeetingRooms_2(meetings))
    # print(meetings)

