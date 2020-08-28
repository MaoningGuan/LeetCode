# -*- coding: utf-8 -*-
"""
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：
1 ≤ k ≤ 二叉搜索树元素个数
"""
from utils import deserialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        时间复杂度 O(N) ： 当树退化为链表时（全部为右子节点），无论 k 的值大小，递归深度都为 N ，占用 O(N) 时间。
        空间复杂度 O(N) ： 当树退化为链表时（全部为右子节点），系统使用 O(N) 大小的栈空间。
        :param root:
        :param k:
        :return:
        """
        q = [root]
        res = []
        while q:
            temp = []
            for node in q:
                res.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        res.sort(reverse=True)
        return res[k - 1]


if __name__ == '__main__':
    root = deserialize("[3,1,4,null,2]")
    k = 1

    solution = Solution()
    print(solution.kthLargest(root, k))
