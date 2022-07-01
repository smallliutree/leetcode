# Given an integer array nums, return the number of longest increasing 
# subsequences. 
# 
#  Notice that the sequence has to be strictly increasing. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 
# 3, 5, 7].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of the longest increasing subsequence is 1, and there 
# are 5 increasing subsequences of length 1, so output 5.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2000 
#  -10⁶ <= nums[i] <= 10⁶ 
#  
#  Related Topics 树状数组 线段树 数组 动态规划 👍 615 👎 0


from typing import List
from collections import defaultdict, Counter
from functools import reduce
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # n, max_len, ans = len(nums), 0, 0
        # dp = [1] * n
        # cnt = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             if dp[j] + 1 > dp[i]:
        #                 dp[i] = dp[j] + 1
        #                 cnt[i] = cnt[j]
        #             elif dp[j] + 1 == dp[i]:
        #                 cnt[i] += cnt[j]
        #     if dp[i] > max_len:
        #         max_len = dp[i]
        #         ans = cnt[i]
        #     elif dp[i] == max_len:
        #         ans += cnt[i]
        # return ans
        d, cnt = [], []
        for v in nums:
            index = self.bisect(len(d), lambda x: d[x][-1] >= v)
            c = 1
            if index > 0:
                k = self.bisect(len(d[index - 1]), lambda x: d[index - 1][x] < v)
                c = cnt[index - 1][-1] - cnt[index - 1][k]
            if index == len(d):
                d.append([v])
                cnt.append([0, c])
            else:
                d[index].append(v)
                cnt[index].append(cnt[index][-1] + c)
        print(d, cnt)
        return cnt[-1][-1]

    @staticmethod
    def bisect(n, func):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if func(mid):
                right = mid
            else:
                left = mid + 1
        return left
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for nums in [
        [1, 3, 5, 4, 7],
        [2, 2, 2, 2, 2]
    ]:
        print(Solution().findNumberOfLIS(nums))
