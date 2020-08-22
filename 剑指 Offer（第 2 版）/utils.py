# -*- coding: utf-8 -*-
"""
功能函数
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l: List[int]) -> ListNode:
    """
    由list来构造链表
    :param l:
    :return:
    """
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    """
    打印链表
    :param l:
    :return:
    """
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root: TreeNode) -> List[List[int]]:
    """
    按层打印二叉树，包含空子节点
    :param root:
    :return:
    """
    import collections
    if not root:
        return []

    res, q = [], collections.deque()
    q.append(root)
    while q:
        # 输出是二维数组
        temp = []
        for x in range(len(q)):
            node = q.popleft()
            if node:
                temp.append(node.val)
            else:
                temp.append(None)
                continue
            if node.left:
                q.append(node.left)
            else:
                q.append(None)
            if node.right:
                q.append(node.right)
            else:
                q.append(None)
        res.append(temp)
    # 去掉最后一层的全空子节点
    res = res[:-1]
    print(res)
    return res


def printTree_2(root: TreeNode) -> List[List[int]]:
    """
    按层打印二叉树，不包含空子节点
    :param root:
    :return:
    """
    import collections
    if not root:
        return []

    res, q = [], collections.deque()
    q.append(root)
    while q:
        # 输出是二维数组
        temp = []
        for x in range(len(q)):
            node = q.popleft()
            temp.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(temp)
    print(res)
    return res


def serialize(root):
    """Encodes a tree to a single string.
    二叉树序列化成字符串
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


def deserialize(data):
    """Decodes your encoded data to tree.
    字符串反序列化成二叉树
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