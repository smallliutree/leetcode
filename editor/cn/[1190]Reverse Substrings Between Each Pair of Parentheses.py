# You are given a string s that consists of lower case English letters and 
# brackets. 
# 
#  Reverse the strings in each pair of matching parentheses, starting from the 
# innermost one. 
# 
#  Your result should not contain any brackets. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "(abcd)"
# Output: "dcba"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is 
# reversed.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, 
# the whole string.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s only contains lower case English characters and parentheses. 
#  It is guaranteed that all parentheses are balanced. 
#  
#  Related Topics


# from typing import

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # if not s:
        #     return ''
        # n = len(s)
        # left = 0
        # while left < n and s[left] != '(':
        #     left += 1
        # if left >= n:
        #     return s
        # tmp = 1
        # for right in range(left + 1, n):
        #     if s[right] == ')':
        #         tmp -= 1
        #     if s[right] == '(':
        #         tmp += 1
        #     if tmp == 0:
        #         break
        # return s[:left] + self.reverseParentheses(s[left + 1: right])[::-1] + self.reverseParentheses(s[right + 1:])
        tmp = ''
        stack = []
        for c in s:
            if c == '(':
                stack.append(tmp)
                tmp = ''
            elif c == ')':
                if stack:
                    pre = stack.pop()
                else:
                    pre = ''
                pre += tmp[::-1]
                tmp = pre
            else:
                tmp += c
        return tmp
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for s in ["((asd)(u(love)i))", "(abcd)", "(u(love)i)", "(ed(et(oc))el)"]:
        print(Solution().reverseParentheses(s))
