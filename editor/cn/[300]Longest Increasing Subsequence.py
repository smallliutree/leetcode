# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  A subsequence is a sequence that can be derived from an array by deleting 
# some or no elements without changing the order of the remaining elements. For 
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
#  Related Topics 数组 二分查找 动态规划 👍 2590 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if not stack or i > stack[-1]:
                stack.append(i)
            else:
                index = self.binary_search(stack, i)
                if index is not None:
                    stack[index] = i
        print(stack)
        return len(stack)

    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    # print(Solution().binary_search([1,2,3],2.9))
    for nums in [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
        [5, 7, 2, 3, 4]
    ]:
        print(Solution().lengthOfLIS(nums))
