# Given a binary array nums, return the maximum number of consecutive 1's in 
# the array if you can flip at most one 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1
# s. After flipping, the maximum number of consecutive 1s is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,0,1,1,0,1]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] is either 0 or 1. 
#  
# 
#  
#  Follow up: What if the input numbers come in one by one as an infinite 
# stream? In other words, you can't store all numbers coming from the stream as it's 
# too large to hold in memory. Could you solve it efficiently? 
#  Related Topics


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = list(map(lambda x: len(x), ''.join(map(str, nums)).split('0')))
        # print(ans)
        if (n := len(ans)) == 1:
            return ans[0]
        if n < 3:
            return sum(ans) + 1
        ret = ans[0] + ans[1]
        for i in range(2, n):
            ret = max(ans[i] + ans[i - 1], ret)
        return ret + 1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for num in [
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 0, 1],
        [1],
        [1, 1],
        [0]
    ]:
        print(Solution().findMaxConsecutiveOnes(n))
