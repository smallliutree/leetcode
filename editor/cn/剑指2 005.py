# -*- coding: utf-8 -*-
# @Time : 2022/7/4 16:52
# @Author : minghe_liu
# @File : 剑指2 005
"""
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。

"""
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        words = list(map(set, words))
        # print(words)
        ans = 0
        for i in range(len(words)):
            for j in range(i, len(words)):
                if not words[i] & words[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

if __name__ == '__main__':
    print(Solution().maxProduct(["abcw", "foo", "bar", "fxyz", "abcdef"]))
