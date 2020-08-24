# -*- coding: utf-8 -*-
"""
剑指 Offer 33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true


提示：

数组长度 <= 1000
"""


class Solution:
    def verifyPostorder_1(self, postorder: [int]) -> bool:
        """
        递归分治
        时间复杂度 O(N^2)： 每次调用 recur(i,j) 减去一个根节点，因此递归占用 O(N) ；
        最差情况下（即当树退化为链表），每轮递归都需遍历树所有节点，占用 O(N) 。
        空间复杂度 O(N) ： 最差情况下（即当树退化为链表），递归深度将达到 N 。
        :param postorder:
        :return:
        """

        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

    def verifyPostorder_2(self, postorder: [int]) -> bool:
        """
        时间复杂度 O(N) ： 遍历 postorder 所有节点，各节点均入栈 / 出栈一次，使用 O(N) 时间。
        空间复杂度 O(N) ： 最差情况下，单调栈 stack 存储所有节点，使用 O(N) 额外空间。
        :param postorder:
        :return:
        """
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while (stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


if __name__ == '__main__':
    postorder = [4, 8, 6, 12, 16, 14, 10]
    solution = Solution()
    print(solution.verifyPostorder_1(postorder))
    print(solution.verifyPostorder_2(postorder))
