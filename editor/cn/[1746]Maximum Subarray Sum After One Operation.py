# You are given an integer array nums. You must perform exactly one operation 
# where you can replace one element nums[i] with nums[i] * nums[i]. 
# 
#  Return the maximum possible subarray sum after exactly one operation. The 
# subarray must be non-empty. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,-1,-4,-3]
# Output: 17
# Explanation: You can perform the operation on index 2 (0-indexed) to make 
# nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17. 
# 
#  Example 2: 
# 
#  
# Input: nums = [1,-1,1,1,-1,-1,1]
# Output: 4
# Explanation: You can perform the operation on index 1 (0-indexed) to make 
# nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  Related Topics 数组 动态规划 👍 20 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[0] * (n := len(nums)) for _ in range(2)]
        dp[0][0] = nums[0]
        dp[1][0] = nums[0] ** 2
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1] + nums[i], 0)
            dp[1][i] = max(dp[1][i - 1] + nums[i], dp[0][i - 1] + nums[i] ** 2)
        # print(dp)
        return max(dp[1])


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for num in [
        [2, -1, -4, -3],
        [1, -1, 1, 1, -1, -1, 1],
        [-4, -49, -12, -75, -48, 46, 72, 10, 51, -51, 26, -74, 70, -1, -25, 29, 27]
    ]:
        print(Solution().maxSumAfterOperation(num))
