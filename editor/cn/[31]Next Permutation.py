# A permutation of an array of integers is an arrangement of its members into a 
# sequence or linear order. 
# 
#  
#  For example, for arr = [1,2,3], the following are considered permutations of 
# arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1]. 
#  
# 
#  The next permutation of an array of integers is the next lexicographically 
# greater permutation of its integer. More formally, if all the permutations of the 
# array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the 
# sorted container. If such arrangement is not possible, the array must be 
# rearranged as the lowest possible order (i.e., sorted in ascending order). 
# 
#  
#  For example, the next permutation of arr = [1,2,3] is [1,3,2]. 
#  Similarly, the next permutation of arr = [2,3,1] is [3,1,2]. 
#  While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does 
# not have a lexicographical larger rearrangement. 
#  
# 
#  Given an array of integers nums, find the next permutation of nums. 
# 
#  The replacement must be in place and use only constant extra memory. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: [1,3,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1]
# Output: [1,2,3]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,1,5]
# Output: [1,5,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = nums[-1]
        n = [pre]
        left = None
        for left in range(len(nums) - 2, -1, -1):
            # print(left, nums[left], pre)
            n.append(nums[left])
            if nums[left] < pre:
                break
            pre = nums[left]
        else:
            nums.sort()
            return
        if left is None:
            return
        # print(left)
        n.sort()
        target = nums[left]

        def quick_sort(number, l, r):
            if l >= r:
                return
            le, ri = l, r
            p = number[l]
            while le < ri:
                while le < ri and number[ri] >= p:
                    ri -= 1
                number[le] = number[ri]
                while le < ri and number[le] <= p:
                    le += 1
                number[ri] = number[le]
                number[le] = p
            quick_sort(number, l, le - 1)
            quick_sort(number, le + 1, r)

        quick_sort(nums, left + 1, len(nums) - 1)
        # print(nums, target, left, nums[left])
        for i in range(left + 1, len(nums)):
            if nums[i] > target:
                nums[i], nums[left] = nums[left], nums[i]
                return
        # print(nums)

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    case = [3]
    Solution().nextPermutation(case)
    print(case)
