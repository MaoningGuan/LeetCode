# -*- coding: utf-8 -*-
"""
剑指 Offer 18. 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
"""
from utils import generateList, printList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        """
        单指针遍历
        间复杂度 O(N) ： N 为链表长度，删除操作平均需循环 N/2 次，最差 N 次。
        空间复杂度 O(1) ： pre 占用常数大小额外空间。
        :param head:
        :param val:
        :return:
        """
        if not head:
            return

        if head.val == val:
            return head.next

        pre = ListNode(0)
        pre.next = head
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
                break
            pre = pre.next
        return head


if __name__ == '__main__':
    head = generateList([-3, 5, -99])
    val = -3

    solution = Solution()
    printList(solution.deleteNode(head, val))
