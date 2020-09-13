# -*- coding: utf-8 -*-
"""
150. 逆波兰表达式求值
根据 逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。



说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: 该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。
逆波兰表达式主要有以下两个优点：

去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。
"""
from typing import List


# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         def calculate(a, b, operate):
#             if operate == '+':
#                 return a + b
#             elif operate == '-':
#                 return a - b
#             elif operate == '*':
#                 return a * b
#             else:
#                 if a * b < 0:  # 防止出现 -10 // 20 == -1  , -12 // 5 = -3等情况
#                     return abs(a) // abs(b) * -1
#                 else:
#                     return a // b
#
#         stack = []
#         s = {'+', '-', '*', '/'}
#         for c in tokens:
#             if c not in s:
#                 stack.append(int(c))
#             else:
#                 b = stack.pop()
#                 a = stack.pop()
#                 stack.append(calculate(a, b, c))
#
#         return stack[-1]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        PopList = []
        for i in tokens:
            if i in "+-*/":
                tmp = PopList.pop()
                tmp2 = PopList.pop()
                PopList.append(str(int(eval(tmp2 + i + tmp))))
            else:
                PopList.append(i)
        return int(PopList[0])


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    solution = Solution()
    print(solution.evalRPN(tokens))
