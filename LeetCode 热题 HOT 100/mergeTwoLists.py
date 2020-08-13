# -*- coding: utf-8 -*-
"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
from utils import generateList, printList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists_1(self, l1, l2):
        """
        递归法
        时间复杂度：O(n + m)
        :param l1:
        :param l2:
        :return:
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists_1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_1(l1, l2.next)
            return l2

    def mergeTwoLists_2(self, l1, l2):
        """
        迭代法
        时间复杂度：O(n + m)
        :param l1:
        :param l2:
        :return:
        """
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next


if __name__ == '__main__':
    list_node_1 = generateList([1, 2, 4])
    list_node_2 = generateList([1, 3, 4])

    solution = Solution()

    # printList(solution.mergeTwoLists_1(list_node_1, list_node_2))
    printList(solution.mergeTwoLists_2(list_node_1, list_node_2))


