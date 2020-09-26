# -*- coding: utf-8 -*-
def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longestPalindrome(s: str) -> int:
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return 1 if len(s[start: end + 1]) == len(s) else 0


if __name__ == '__main__':
    while True:
        try:
            num = int(input().strip())
            s = bin(num).replace('0b', '')
            print(longestPalindrome(s))
        except:
            break


