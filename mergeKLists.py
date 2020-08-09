# -*- coding: utf-8 -*-
"""
23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from typing import List

from utils import generateList, printList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        优先级队列
        时间复杂度：O(n*log(k))，n是所有链表中元素的总和，k是链表个数。
        :param lists:
        :return:
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


if __name__ == '__main__':
    soltuion = Solution()

    listNode1 = generateList([1, 4, 5])
    listNode2 = generateList([1, 3, 4])
    listNode3 = generateList([2, 6])

    list_nodes = [listNode1, listNode2, listNode3]

    mergeList = soltuion.mergeKLists(list_nodes)
    printList(mergeList)

