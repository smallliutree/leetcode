# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the 
# histogram. 
# 
#  
#  Example 1: 
# 
#  
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#  
# 
#  Example 2: 
# 
#  
# Input: heights = [2,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= heights.length <= 10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
#  Related Topics

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left, right = [], []
        for index, value in enumerate(heights):
            while stack and heights[stack[-1]] >= value:
                stack.pop()
            if stack:
                left.append(stack[-1])
            else:
                left.append(-1)
            stack.append(index)
        print(left)
        stack = []
        n = len(heights)
        for index, value in enumerate(heights[::-1]):
            while stack and heights[stack[-1]] >= value:
                stack.pop()
            if stack:
                right.append(stack[-1])
            else:
                right.append(n)
            stack.append(n - index - 1)
        print(right[::-1])
        right = right[::-1]
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right[i] - left[i] - 1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for h in [[2, 1, 5, 6, 2, 3], [2, 4], [6, 7, 5, 1, 4, 5, 9, 3], [1, 1]]:
        print(Solution().largestRectangleArea(h))
