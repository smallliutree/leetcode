# Given an array of non-negative integers nums, you are initially positioned at 
# the first index of the array. 
# 
#  Each element in the array represents your maximum jump length at that 
# position. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  You can assume that you can always reach the last index. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 
# step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,3,0,1,4]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 1000 
#  
#  Related Topics

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [n] * n
        # dp[0] = 0
        # for i in range(n - 1):
        #     for j in range(nums[i]):
        #         if i + j + 1 >= n:
        #             break
        #         dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
        # # print(dp)
        # return dp[-1]
        if len(nums) == 1:
            return 0
        ans = 0
        far = 0
        tmp = 0
        for i in range(n - 1):
            tmp = max(tmp, i + nums[i])
            if i == far:
                ans += 1
                far = tmp
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1,1,1,1]
    print(Solution().jump(n))
