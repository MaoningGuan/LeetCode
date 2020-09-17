# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            a = list(map(int, input().split()))
            b = list(map(int, input().split()))

            c = sorted(set(a + b))
            print(' '.join(map(str, c)))
        except:
            break
