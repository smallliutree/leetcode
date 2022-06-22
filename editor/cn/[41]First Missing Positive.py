# Given an unsorted integer array nums, return the smallest missing positive 
# integer. 
# 
#  You must implement an algorithm that runs in O(n) time and uses constant 
# extra space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,0]
# Output: 3
#  Example 2: 
#  Input: nums = [3,4,-1,1]
# Output: 2
#  Example 3: 
#  Input: nums = [7,8,9,11,12]
# Output: 1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁵ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  
#  Related Topics 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        _max = 
        for i in nums:
            
# leetcode submit region end(Prohibit modification and deletion)
