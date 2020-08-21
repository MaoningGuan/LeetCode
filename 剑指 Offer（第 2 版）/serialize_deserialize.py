# -*- coding: utf-8 -*-
"""
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        时间复杂度 O(N) ： N 为二叉树的节点数，层序遍历需要访问所有节点，
        最差情况下需要访问 N + 1 个 null ，总体复杂度为 O(2N + 1) = O(N)。
        空间复杂度 O(N) ： 最差情况下，队列 queue 同时存储 (N+1) / 2 个节点（或 N+1 个 null ），使用 O(N) ；
        列表 res 使用 O(N) 。
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = list()
        queue.append(root)
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        while res[-1] == "null":
            res.pop()
        res = "[" + ",".join(res) + "]"
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        时间复杂度 O(N) ： N 为二叉树的节点数，按层构建二叉树需要遍历整个 vals ，其长度最大为 2N+1 。
        空间复杂度 O(N) ： 最差情况下，队列 queue 同时存储 (N+1) / 2 个节点，因此使用 O(N) 额外空间。
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = list()
        queue.append(root)
        while queue:
            node = queue.pop(0)
            try:
                if vals[i] != "null":
                    node.left = TreeNode(int(vals[i]))
                    queue.append(node.left)
            except IndexError:
                pass
            i += 1
            try:
                if vals[i] != "null":
                    node.right = TreeNode(int(vals[i]))
                    queue.append(node.right)
            except IndexError:
                pass
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    nodes = "[1,2,3,null,null,4,5]"

    codec = Codec()
    root = codec.deserialize(nodes)
    print(codec.serialize(root))
