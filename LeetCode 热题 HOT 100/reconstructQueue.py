# -*- coding: utf-8 -*-
"""
406. 根据身高重建队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from typing import List


class Solution(object):
    def reconstructQueue(self, people):
        """
        排序的时间复杂度：O(NlogN) 的时间
        插入list的时间复杂度：O(N^2)
        空间复杂度：O(N)，输出队列使用的空间。
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    solution = Solution()
    print(solution.reconstructQueue(people))
