# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def back_track(tmp):
            if len(tmp) == n:
                ans.append(tmp[:])
                return
            for i in nums:
                if i not in tmp:
                    tmp.append(i)
                    back_track(tmp)
                    tmp.pop()

        back_track([])
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    n = [1, 2, 3]
    print(Solution().permute(n))
