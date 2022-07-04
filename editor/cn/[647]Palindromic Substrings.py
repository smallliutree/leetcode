# Given a string s, return the number of palindromic substrings in it. 
# 
#  A string is a palindrome when it reads the same backward as forward. 
# 
#  A substring is a contiguous sequence of characters within the string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists of lowercase English letters. 
#  
#  Related Topics


from typing import List
from collections import defaultdict, Counter
from functools import reduce
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.func(s[i: j + 1]):
                    ans += 1
        return ans

    def func(self, s):
        left, right = 0, len(s) - 1
        while right > left:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for s in [
        "abc",
        "aaa"
    ]:
        print(Solution().countSubstrings(s))
