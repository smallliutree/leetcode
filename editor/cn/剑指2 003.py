# -*- coding: utf-8 -*-
# @Time : 2022/7/4 14:59
# @Author : minghe_liu
# @File : 剑指2 003
"""
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        tmp = 1
        k = tmp
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[i - tmp] + 1)
            k -= 1
            if k == 0:
                tmp *= 2
                k = tmp
        return ans


if __name__ == '__main__':
    print(Solution().countBits(5))

