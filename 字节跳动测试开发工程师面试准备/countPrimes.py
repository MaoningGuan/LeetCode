# -*- coding: utf-8 -*-
"""
质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0


提示：

0 <= n <= 5 * 106
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        求n以内的所有质数个数（纯python代码）
        解题思路：
        效率提升的关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：
        要得到自然数n以内的全部质数，必须把不大于根号n的所有质数的倍数剔除，剩下的就是质数。
        时间复杂度：O(n^(0.5))
        孔家复杂度：O(n)
        """
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号n的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)


if __name__ == '__main__':
    solution = Solution()
    while True:
        try:
            n = int(input().strip())
            print(solution.countPrimes(n))
        except:
            break
