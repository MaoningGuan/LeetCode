# -*- coding: utf-8 -*-
"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。


示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。
"""


# ==============不使用辅助栈，栈中保存差值，和另外保存最小值===============
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deq = []
        self.min_value = -1

    def push(self, x: int) -> None:
        if not self.deq:
            self.deq.append(0)
            self.min_value = x
        else:
            diff = x - self.min_value
            self.deq.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.deq:
            diff = self.deq.pop()
            if diff < 0:
                top = self.min_value - diff
                self.min_value = top
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.deq[-1] < 0 else self.deq[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.deq else -1


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
