# -*- coding: utf-8 -*-
"""
采购单（京东2017秋招真题）
样例输入
5 3
4 2 1 10 5
apple
orange
mango
6 5
3 5 1 6 8 1
peach
grapefruit
banana
orange
orange
样例输出
7 19
11 30
"""
if __name__ == '__main__':
    while True:

        n, m = map(int, input().split())

        prices = sorted(list(map(int, input().split())))
        hashmap = dict()
        for _ in range(m):
            name = input().strip()
            if name in hashmap:
                hashmap[name] = hashmap[name] + 1
            else:
                hashmap[name] = 1

        sorted_hashmap = sorted(hashmap.items(), key=lambda kv: (kv[1], kv[0]))

        max_cost = 0
        j = 0
        for i in range(len(sorted_hashmap) - 1, -1, -1):
            max_cost += sorted_hashmap[i][1] * prices[-1 - j]
            j += 1

        min_cost = 0
        j = 0
        for i in range(len(sorted_hashmap) - 1, -1, -1):
            min_cost += sorted_hashmap[i][1] * prices[j]
            j += 1


        print(min_cost, max_cost)
        # try:
        #     nm = input()  # 数据有很多空行
        #     # n, m = map(int, input().split())
        #     if nm != '':
        #         n, m = map(int, nm.split())
        #         prices = sorted(list(map(int, input().split())))
        #         hashmap = dict()
        #         for _ in range(m):
        #             name = input().strip()
        #             if name in hashmap:
        #                 hashmap[name] = hashmap[name] + 1
        #             else:
        #                 hashmap[name] = 1
        #
        #         sorted_hashmap = sorted(hashmap.items(), key=lambda kv: (kv[1], kv[0]))
        #
        #         max_cost = 0
        #         j = 0
        #         for i in range(len(sorted_hashmap) - 1, -1, -1):
        #             max_cost += sorted_hashmap[i][1] * prices[-1 - j]
        #             j += 1
        #
        #         min_cost = 0
        #         j = 0
        #         for i in range(len(sorted_hashmap) - 1, -1, -1):
        #             min_cost += sorted_hashmap[i][1] * prices[j]
        #             j += 1
        #
        #         print(min_cost, max_cost)
        #
        # except:
        #     break