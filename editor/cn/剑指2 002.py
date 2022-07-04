# -*- coding: utf-8 -*-
# @Time : 2022/7/4 14:52
# @Author : minghe_liu
# @File : 剑指2 002
"""
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。

输入为 非空 字符串且只包含数字 1 和 0。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a, b, m, n = b, a, n, m
        left, right = m - 1, n - 1
        ans = ''
        carry = 0
        while left >= 0 and right >= 0:
            tmp = int(a[left]) + int(b[right]) + carry
            carry = tmp // 2
            tmp %= 2
            ans += str(tmp)
            left -= 1
            right -= 1
        while left >= 0:
            tmp = int(a[left]) + carry
            carry = tmp // 2
            tmp %= 2
            ans += str(tmp)
            left -= 1
        if carry:
            ans += '1'
        return ans[::-1]

