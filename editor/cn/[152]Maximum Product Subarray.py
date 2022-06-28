# Given an integer array nums, find a contiguous non-empty subarray within the 
# array that has the largest product, and return the product. 
# 
#  The test cases are generated so that the answer will fit in a 32-bit integer.
#  
# 
#  A subarray is a contiguous subsequence of the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
# integer. 
#  
#  Related Topics


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maximum, minimum = [0] * n, [0] * n
        maximum[0] = nums[0]
        minimum[0] = nums[0]
        for i in range(1, n):
            maximum[i] = max(maximum[i - 1] * nums[i], minimum[i - 1] * nums[i], nums[i])
            minimum[i] = min(maximum[i - 1] * nums[i], minimum[i - 1] * nums[i], nums[i])
        # print(maximum, minimum)
        return max(maximum)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for n in [
        [2, 3, -2, 4],
        [-2, 0, -1]
    ]:
        print(Solution().maxProduct(n))
