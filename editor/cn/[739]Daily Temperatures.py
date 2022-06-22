# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait 
# after the iᵗʰ day to get a warmer temperature. If there is no future day for 
# which this is possible, keep answer[i] == 0 instead. 
# 
#  
#  Example 1: 
#  Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#  Example 2: 
#  Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#  Example 3: 
#  Input: temperatures = [30,60,90]
# Output: [1,1,0]
#  
#  
#  Constraints: 
# 
#  
#  1 <= temperatures.length <= 10⁵ 
#  30 <= temperatures[i] <= 100 
#  
#  Related Topics 

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        ans = [0] * len(temperatures)
        for index, value in enumerate(temperatures[1:]):
            # print(index, value, stack, ans)
            while stack:
                if value > stack[-1][1]:
                    i, v = stack.pop()
                    ans[i] = index + 1 - i
                else:
                    stack.append((index + 1, value))
                    break
            else:
                stack.append((index + 1, value))
        return ans
            
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    t = [30,60, 90]
    print(Solution().dailyTemperatures(t))
