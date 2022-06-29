# Given two strings text1 and text2, return the length of their longest common 
# subsequence. If there is no common subsequence, return 0. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order 
# of the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  A common subsequence of two strings is a subsequence that is common to both 
# strings. 
# 
#  
#  Example 1: 
# 
#  
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#  
# 
#  Example 3: 
# 
#  
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text1.length, text2.length <= 1000 
#  text1 and text2 consist of only lowercase English characters. 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, m):
            dp[i][0] = 1 if text1[i] == text2[0] or dp[i - 1][0] == 1 else 0
        for j in range(1, n):
            dp[0][j] = 1 if text1[0] == text2[j] or dp[0][j - 1] == 1 else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (1 if text1[i] == text2[j] else 0))

        # print(dp)
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for text1, text2 in [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("asdfghe", "vadsdfgh")
    ]:
        print(Solution().longestCommonSubsequence(text1, text2))
