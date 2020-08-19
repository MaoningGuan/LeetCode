# -*- coding: utf-8 -*-
"""
剑指 Offer 13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20
"""


class Solution:
    def movingCount_1(self, m: int, n: int, k: int) -> int:
        """
        方法一：深度优先遍历 DFS
        M,N 分别为矩阵行列大小。
        时间复杂度 O(MN)： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN) 。
        空间复杂度 O(MN)： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN) 的额外空间。
        :param m:
        :param n:
        :param k:
        :return:
        """

        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
                                                                                   sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount_2(self, m: int, n: int, k: int) -> int:
        """
        方法二：广度优先遍历 BFS
        M,N 分别为矩阵行列大小。
        时间复杂度 O(MN)： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN) 。
        空间复杂度 O(MN)： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN) 的额外空间。
        :param m:
        :param n:
        :param k:
        :return:
        """
        queue, visited, = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited: continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)


if __name__ == '__main__':
    m = 2
    n = 3
    k = 1

    solution = Solution()
    print(solution.movingCount_1(m, n, k))
    print(solution.movingCount_2(m, n, k))

