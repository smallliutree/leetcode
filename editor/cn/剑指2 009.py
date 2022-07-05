# -*- coding: utf-8 -*-
# @Time : 2022/7/5 10:25
# @Author : minghe_liu
# @File : 剑指2 009
"""
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        tmp = 1
        ans = 0
        while right < len(nums):
            tmp *= nums[right]
            while tmp >= k and left <= right:
                tmp //= nums[left]
                left += 1
            while nums[right] >= k and right < len(nums) - 1:
                right += 1
                left = right
                tmp = nums[right]
            if tmp >= k:
                break
            ans += right - left + 1
            right += 1
        return ans
