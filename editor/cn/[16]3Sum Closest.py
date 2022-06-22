# 2022-04-14 10:24:50
# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target. 
# 
#  Return the sum of the three integers. 
# 
#  You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,0,0], target = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        ret = -1
        for i in range(n):
            left, right = i + 1, n - 1
            t = target - nums[i]
            while left < right:
                tmp = nums[left] + nums[right]
                x = abs(tmp - t)
                if tmp == t:
                    return target
                elif tmp > t:
                    # print('+', tmp, t, i, left, right)
                    right -= 1
                    if x < ans:
                        ans = x
                        ret = tmp + nums[i]
                else:
                    # print(tmp, t, i, left, right)
                    left += 1
                    if x < ans:
                        ans = x
                        ret = tmp + nums[i]
        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().threeSumClosest(nums=[1, 1, 1, 0], target=-100))
    print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
    print(Solution().threeSumClosest(nums=[0,0,0], target = 1))
