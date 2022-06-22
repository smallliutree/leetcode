# Given an input string (s) and a pattern (p), implement wildcard pattern 
# matching with support for '?' and '*' where: 
# 
#  
#  '?' Matches any single character. 
#  '*' Matches any sequence of characters (including the empty sequence). 
#  
# 
#  The matching should cover the entire input string (not partial). 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not 
# match 'b'.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length, p.length <= 2000 
#  s contains only lowercase English letters. 
#  p contains only lowercase English letters, '?' or '*'. 
#  
#  Related Topics 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        print(dp, m, n)
        for i in range(m):
            for j in range(n):
                if p[j] == '?' or s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j] and True
                elif p[j] == '*':
                    for k in range(j + 1, n + 1):
                        dp[i + 1][k] = dp[i][j] and True
                else:
                    dp[i + 1][j + 1] = False
                    for k in range(j, n):
                        if dp[i][k]:
                            if s[i] == p[k]:
                                dp[i + 1][k + 1] = True
                        else:
                            break
            if not any(dp[i + 1]):
                print(dp)
                return False
        print(dp)
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().isMatch('aa', '*'))
