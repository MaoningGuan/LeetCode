# -*- coding: utf-8 -*-
"""
27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。



示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
from typing import List


class Solution:
    def removeElement_1(self, nums: List[int], val: int) -> int:
        """
        双指针1
        时间复杂度：O(n)，
        假设数组总共有 n 个元素，i 和 j 至多遍历 2n 步。
        空间复杂度：O(1)。
        :param nums:
        :param val:
        :return:
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """
        双指针2
        时间复杂度：O(n)，
        i 和 n 最多遍历 nn 步。在这个方法中，赋值操作的次数等于要删除的元素的数量。因此，如果要移除的元素很少，效率会更高。
        空间复杂度：O(1)。
        :param nums:
        :param val:
        :return:
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


if __name__ == '__main__':
    val = 2

    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.removeElement_1(nums, val))
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.removeElement_2(nums, val))
