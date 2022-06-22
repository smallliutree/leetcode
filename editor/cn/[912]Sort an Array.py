# Given an array of integers nums, sort the array in ascending order. 
# 
#  
#  Example 1: 
#  Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#  Example 2: 
#  Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 10⁴ 
#  -5 * 10⁴ <= nums[i] <= 5 * 10⁴ 
#  
#  Related Topics

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArray(self, nums: List[int], left=None, right=None) -> List[int]:
        if not left:
            left = 0
        if not right:
            right = len(nums) - 1
        if left >= right:
            return nums
        l, r = left, right
        pivot = nums[left]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[r], nums[l] = nums[r], nums[l]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[l], nums[r] = nums[r], nums[l]
        nums[l] = pivot
        self.sortArray(nums, 0, l - 1)
        self.sortArray(nums, l + 1)
        print(nums)
        return 

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [5,2,3,1]
    Solution().sortArray(n)
