# -*- coding: utf-8 -*-
# @Time : 2022/7/5 10:15
# @Author : minghe_liu
# @File : 剑指2 008
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        tmp = 0
        ans = len(nums) + 1
        while right < len(nums):
            tmp += nums[right]
            if tmp >= target:
                while tmp - nums[left] >= target:
                    tmp -= nums[left]
                    left += 1
                ans = min(ans, right - left + 1)
            right += 1
        if ans > len(nums):
            return 0
        return ans
