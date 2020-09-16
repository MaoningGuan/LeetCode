# -*- coding: utf-8 -*-
# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# -*- coding: utf-8 -*-

import sys

# 0,1,2,3,4,3,2,1,5,6,5,7,8,9,8,7,5,1,0
success_path = [str(c) for c in [0, 1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7, 8, 9, 8, 7, 5, 1, 0]]
bad_path = ['A', 'B', 'C', 'D', 'E', 'F']

from itertools import groupby


def main(path):
    i = 0
    for j in range(len(path)):
        if path[j] in bad_path:
            return 'Collision'
        elif path[j] == '-1':
            return 'Out of path'

    news_paths = [x[0] for x in groupby(path)]
    if news_paths == success_path:
        return 'Success'
    else:
        return 'Bad path'


if __name__ == '__main__':
    for line in sys.stdin:
        path = line.strip().split(',')
        # print(path)
        print(main(path))
