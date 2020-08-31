# -*- coding: utf-8 -*-
"""
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
"""
from utils import deserialize, serialize


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree_1(self, root: TreeNode) -> TreeNode:
        """
        辅助栈（或队列）：广度优先搜索
        时间复杂度 O(N)： 其中 N 为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点，占用 O(N) 时间。
        空间复杂度 O(N)： 最差情况下（当为满二叉树时），栈 stack 最多同时存储 N/2 个节点，占用 O(N) 额外空间
        :param root:
        :return:
        """
        if not root:
            return

        import collections
        queue = collections.deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node.left, node.right = node.right, node.left
        return root

    def mirrorTree_2(self, root: TreeNode) -> TreeNode:
        """
        递归：深度优先搜索
        时间复杂度 O(N)： 其中 N 为二叉树的节点数量，建立二叉树镜像需要遍历树的所有节点，占用 O(N) 时间。
        空间复杂度 O(N)： 最差情况下（当二叉树退化为链表），递归时系统需使用 O(N) 大小的栈空间。
        :param root:
        :return:
        """
        if not root: return
        root.left, root.right = self.mirrorTree_2(root.right), self.mirrorTree_2(root.left)
        return root


if __name__ == '__main__':
    solution = Solution()

    root = deserialize("[4,2,7,1,3,6,9]")
    print(serialize(solution.mirrorTree_1(root)))

    root = deserialize("[4,2,7,1,3,6,9]")
    print(serialize(solution.mirrorTree_2(root)))
