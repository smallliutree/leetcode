# Given an m x n binary matrix filled with 0's and 1's, find the largest square 
# containing only 1's and return its area. 
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1",
# "1"],["1","0","0","1","0"]]
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: matrix = [["0"]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] is '0' or '1'. 
#  
#  Related Topics


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = 0 if matrix[i][j] == '0' else 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if dp[i + 1][j + 1] == 1:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    ans = max(ans, dp[i + 1][j + 1])

        # print(dp)
        return ans ** 2


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for m in [
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "1", "1", "1"]],
        [["0", "1"], ["1", "0"]],
        [["0"]]
    ]:
        print(Solution().maximalSquare(m))
