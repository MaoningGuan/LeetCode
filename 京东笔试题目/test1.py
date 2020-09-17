# -*- coding: utf-8 -*-
"""
5 4
1 3 1
3 4 0
2 5 1
3 2 1
"""
if __name__ == '__main__':
    # while True:
    #     nm = list(map(int, input().split()))
    #     N = nm[0]
    #     M = nm[1]
    #
    #     hashset = set([1])
    #     sum = 0
    #
    #     nums = []
    #     for _ in range(M):
    #         abc = list(map(int, input().split()))
    #         a = abc[0]
    #         b = abc[1]
    #         c = abc[2]
    #         if c == 0:
    #             continue
    #         nums.append([a, b])
    #
    #     while nums:
    #         flag = False
    #         for i in range(len(nums)):
    #             if nums[i][0] in hashset or nums[i][1] in hashset:
    #                 flag = True
    #                 hashset.add(nums[i][0])
    #                 hashset.add(nums[i][1])
    #                 nums[i][0] = -1
    #                 nums[i][1] = -1
    #                 # nums.pop(i)
    #         if flag is False:
    #             break
    #
    #     print(len(hashset) - 1)
    while 1:
        N, M = map(int, input().split())
        res = []
        for i in range(M):
            a, b, c = map(int, input().split())
            if c == 1:
                r = [a, b] if a < b else [b, a]
                res.append(r)
        s = set()
        s.add(1)
        # print(res)
        res.sort()
        # print(res)
        for i in res:
            if i[0] in s:
                s.add(i[1])
        print(len(s) - 1)


