# Given an integer array nums, find the contiguous subarray (containing at 
# least one number) which has the largest sum and return its sum. 
# 
#  A subarray is a contiguous part of an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
#  Related Topics

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (n := len(nums)) < 2:
            return nums[0]
        first, second = nums[0], max(nums[0], 0) + nums[1]
        ans = max(first, second)
        for i in range(2, n):
            first, second = second, max(second, 0) + nums[i]
            # print(first, second, nums[i])
            ans = max(ans, second)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for num in [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8]
    ]:
        print(Solution().maxSubArray(num))
