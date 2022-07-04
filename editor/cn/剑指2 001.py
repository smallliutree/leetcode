# -*- coding: utf-8 -*-
# @Time : 2022/7/4 14:32
# @Author : minghe_liu
# @File : 剑指2 001
"""
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == 0:
            return 0
        is_neg = True if (a < 0 and b > 0) or (a > 0 and b < 0) else False
        a = abs(a)
        b = abs(b)
        left, right = 1, a
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            res = self.quick_multiply(b, mid)
            if res == a:
                return mid
            elif res > a:
                right = mid - 1
            else:
                left = mid

        return left

    def quick_multiply(self, a, b):
        ans = 0
        while b:
            if b & 1 == 1:
                ans += a
            a <<= 1
            b >>= 1
        return ans


if __name__ == '__main__':
    print(Solution().divide(7, -3))
