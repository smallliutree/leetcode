# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
#  Related Topics

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        # q = deque()
        def dfs(x, y):
            if grid[x][y] != '1':
                return
            grid[x][y] = '-1'
            for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if 0 <= a < m and 0 <= b < n:
                    dfs(a, b)

        for i in range(m):
            for j in range(n):
                # print(i, j, grid)
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1

        # print(grid)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print(Solution().numIslands(grid))
