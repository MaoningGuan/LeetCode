# -*- coding: utf-8 -*-
"""
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# 0,1,2,3,4,3,2,1,5,5,5,6,5,7,8,8,8,8,8,9,8,7,5,1,0
# 0,1,2,3,4,3,2,1,5,6,5,7,8,9,8,7,5,1,0
"""
from itertools import groupby

success_path = list(map(str, [0, 1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7, 8, 9, 8, 7, 5, 1, 0]))  # 标准成功路径
bad_path = ['A', 'B', 'C', 'D', 'E', 'F']


def main(path):
    news_paths = [x[0] for x in groupby(path)]
    if news_paths[:len(success_path)] == success_path:
        return 'Success'
    else:
        for j in range(len(path)):
            if path[j] in bad_path:
                return 'Collision'
            elif path[j] == '-1':
                return 'Out of path'

    return 'Bad path'


if __name__ == '__main__':
    while True:
        try:
            path = input().split(',')
            print(path)
            print(main(path))
        except:
            break

