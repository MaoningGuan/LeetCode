# -*- coding: utf-8 -*-
"""
判断一个正整数，计算有多少对质数的和等于这个正整数
"""

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    N = 10
    hashset = set()
    count = 0
    for i in range(2, N):  # N为输入的数
        if isprime(i):
            if 2 * i == N:
                count += 1
            if N - i in hashset:
                count += 1
            hashset.add(i)
    print(count)
