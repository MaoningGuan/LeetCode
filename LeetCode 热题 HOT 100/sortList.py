# -*- coding: utf-8 -*-
"""
148. 排序链表
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]

提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
"""
from utils import ListNode, generateList, printList


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        解答一：归并排序（递归法）
        时间复杂度：O(NlogN)
        空间复杂度：O(N)
        :param head:
        :return:
        """
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


if __name__ == '__main__':
    nums = [4, 2, 1, 3]
    head = generateList(nums)
    printList(head)

    solution = Solution()
    printList(solution.sortList(head))
