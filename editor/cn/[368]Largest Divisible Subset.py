# # Given a set of distinct positive integers nums, return the largest subset 
# # answer such that every pair (answer[i], answer[j]) of elements in this 
# subset 
# # satisfies: 
# # 
# # 
# # answer[i] % answer[j] == 0, or 
# # answer[j] % answer[i] == 0 
# # 
# # 
# # If there are multiple solutions, return any of them. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: nums = [1,2,3]
# # Output: [1,2]
# # Explanation: [1,3] is also accepted.
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: nums = [1,2,4,8]
# # Output: [1,2,4,8]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # 1 <= nums.length <= 1000 
# # 1 <= nums[i] <= 2 * 10⁹ 
# # All the integers in nums are unique. 
# # 
# # Related Topics
# 


from typing import List
from collections import defaultdict, Counter
from functools import reduce


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        ans = [nums[0]]
        for i in range(len(nums)):
            # print(dp)
            for j in range(i - 1, -1, -1):
                if nums[i] % dp[j][-1] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    # print(dp[i], dp[j])
                    dp[i] = dp[j][:]
                    dp[i].extend([nums[i]])
                    # print(dp, nums[i])
                    if len(dp[i]) > len(ans):
                        ans = dp[i]
        # print(dp)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for nums in [
        [1, 2, 3],
        [1, 2, 4, 8],
        [1],
        [4, 8, 10, 240]
    ]:
        print(Solution().largestDivisibleSubset(nums))
