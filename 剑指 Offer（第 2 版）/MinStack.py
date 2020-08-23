# -*- coding: utf-8 -*-
"""
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 
提示：

各函数的调用总次数不超过 20000 次
"""


class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        res = self.A.pop()
        if res == self.B[-1]:
            self.B.pop()
        return res

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-4)
    obj.push(-2)
    obj.push(2)
    print(obj.pop())
    print(obj.top())
    print(obj.min())
