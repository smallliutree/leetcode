# -*- coding: utf-8 -*-
# @Time : 2022/7/4 18:23
# @Author : minghe_liu
# @File : 剑指2 007
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        print(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                res = nums[left] + nums[right]
                print(target, res, left, right)
                if res == target:
                    ans.append([-target, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif res > target:
                    right -= 1
                else:
                    left += 1
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([1,-1,-1,0]))

