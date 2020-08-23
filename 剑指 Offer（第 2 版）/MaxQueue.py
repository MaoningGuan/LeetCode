# -*- coding: utf-8 -*-
"""
剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""
import collections


class MaxQueue:

    def __init__(self):
        self.deque = collections.deque()
        self.queue = collections.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:  # self.queue的队尾会在self.deque的队尾，所以只需要判断self.deque是否为空 或者使用not self.queue
            return -1
        ans = self.queue.popleft()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans


if __name__ == '__main__':
    # Your MaxQueue object will be instantiated and called as such:
    obj = MaxQueue()
    obj.push_back(1)
    obj.push_back(2)
    print(obj.max_value())
    print(len(obj.queue))
    print(obj.pop_front())
    print(obj.max_value())
    print(len(obj.queue))
    print(obj.pop_front())
    print(obj.pop_front())
    print(len(obj.deque))
