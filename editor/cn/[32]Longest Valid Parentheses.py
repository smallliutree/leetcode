# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#  
# 
#  Example 2: 
# 
#  
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#  
# 
#  Example 3: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] is '(', or ')'. 
#  
#  Related Topics
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack = [-1]
        # ans = 0
        # for index, value in enumerate(s):
        #     if value == '(':
        #         stack.append(index)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(index)
        #         else:
        #             ans = max(ans, index - stack[-1])
        # return ans
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = dp[i - 2] + 2
                else:
                    if i - dp[i - 1] - 1 >= 0:
                        if s[i - dp[i - 1] - 1] == '(':
                            dp[i] = dp[i - 1] + 2
                            if i - dp[i - 1] - 1 >= 1:
                                dp[i] += dp[i - dp[i - 1] - 2]
        print(dp)
        return max(dp)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    target = "()(())"
    print(Solution().longestValidParentheses(target))
