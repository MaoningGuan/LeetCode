# -*- coding: utf-8 -*-
"""
286. 墙与门
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：

给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque


class Solution(object):
    def __init__(self):
        # 设定四个遍历方向
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 右，下，左，上

    def wallsAndGates(self, rooms):
        """
        时间复杂度： O(mn)
        空间复杂度： O(mn)
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return rooms
        m, n = len(rooms), len(rooms[0])
        # 标记已访问
        marked = [[False for _ in range(n)] for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    marked[i][j] = True
                    queue.append((i, j))
                elif rooms[i][j] == -1:
                    marked[i][j] = True
        self.__BFS(queue, rooms, m, n, marked)
        return rooms

    def __BFS(self, queue, rooms, m, n, marked):
        step = 0
        while queue:
            step += 1
            times = len(queue)
            for _ in range(times):
                x, y = queue.popleft()
                for direciton in self.directions:
                    new_x = x + direciton[0]
                    new_y = y + direciton[1]
                    if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and not marked[new_x][new_y]:
                        rooms[new_x][new_y] = step
                        marked[new_x][new_y] = True
                        queue.append((new_x, new_y))


if __name__ == '__main__':
    rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
             [2147483647, -1, 2147483647, -1],
             [0, -1, 2147483647, 2147483647]]
    solution = Solution()
    print(solution.wallsAndGates(rooms))
