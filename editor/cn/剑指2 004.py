# -*- coding: utf-8 -*-
# @Time : 2022/7/4 16:48
# @Author : minghe_liu
# @File : 剑指2 004
"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
"""
from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for k, v in d.items():
            if v == 1:
                return k
