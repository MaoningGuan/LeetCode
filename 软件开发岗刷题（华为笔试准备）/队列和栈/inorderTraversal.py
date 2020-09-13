# -*- coding: utf-8 -*-
"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""
from typing import List

from utils import deserialize, TreeNode

"""
颜色标记法-一种通用且简明的树遍历方法
其核心思想如下：

使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
如果遇到的节点为灰色，则将节点的值输出。

特点：兼具栈迭代方法的高效，又像递归方法一样简洁易懂，更重要的是，这种方法对于前序、中序、后序遍历，能够写出完全一致的代码。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         WHITE, GRAY = 0, 1
#         res = []
#         stack = [(WHITE, root)]
#         while stack:
#             color, node = stack.pop()
#             if node is None: continue
#             if color == WHITE:
#                 stack.append((WHITE, node.right))
#                 stack.append((GRAY, node))
#                 stack.append((WHITE, node.left))
#             else:
#                 res.append(node.val)
#         return res
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst


if __name__ == '__main__':
    nodes = '[1,null,2,3]'
    root = deserialize(nodes)

    solution = Solution()
    print(solution.inorderTraversal(root))
