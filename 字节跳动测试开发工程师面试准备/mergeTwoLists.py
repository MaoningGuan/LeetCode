# -*- coding: utf-8 -*-
"""
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l):
    pre = ListNode(0)
    head = pre
    for i in l:
        pre.next = ListNode(i)
        pre = pre.next
    return head.next


def printList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode(0)
        head = pre
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return head.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]

    solution = Solution()
    printList(solution.mergeTwoLists(generateList(l1), generateList(l2)))
