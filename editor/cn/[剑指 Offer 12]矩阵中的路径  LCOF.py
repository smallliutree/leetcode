# # English description is not available for the problem. Please switch to 
# # Chinese. Related Topics 数组 回溯 矩阵 👍 627 👎 0
# 
"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。


"""
import copy
from typing import List
from collections import defaultdict, Counter
from functools import reduce


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m, n = len(board), len(board[0])
#         visited = [[0] * n for _ in range(m)]
#
#         def dfs(x, y, s):
#             # print(x, y, s)
#             if not s:
#                 return True
#             if board[x][y] == s[0]:
#                 if len(s) == 1:
#                     return True
#                 visited[x][y] = 1
#                 for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                     if 0 <= i < m and 0 <= j < n and visited[i][j] == 0:
#                         if dfs(i, j, s[1:]):
#                             return True
#                 visited[x][y] = 0
#             return False
#
#         for a in range(m):
#             for b in range(n):
#                 # print('======')
#                 if dfs(a, b, word):
#                     return True
#         return False

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        y_len = len(board)
        x_len = len(board[0])
        for i in range(y_len):
            for j in range(x_len):
                # 从每个格子开始 有一个能找到则成功
                # print('====')
                if self.check(i, j, 0, board, word, y_len, x_len):
                    return True
        return False

    def check(self, i, j, k, board, word, y_len, x_len):
        """
        dfs
        :param i: 横坐标
        :param j: 纵坐标
        :param k: 步长
        :param board:
        :param word:
        :param y_len:
        :param x_len:
        :return:
        """
        if i < 0 or i > y_len - 1:
            return
        if j < 0 or j > x_len - 1:
            return
        if board[i][j] != word[k]:
            # 剪枝
            return False
        # print(i, j, k, board, word, y_len, x_len, board[i][j], word[k])
        if k == len(word) - 1:
            # 走到最后一个元素
            return True
        board[i][j] += '-'  # 已走过的标记
        delta_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for delta in delta_list:
            if self.check(i+delta[0], j+delta[1], k+1, board, word, y_len, x_len):
                return True
        board[i][j] = board[i][j][0]
        return False

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for board, word in [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        ([["a", "b"], ["c", "d"]], "abcd"),
        ([['a']], 'c'),
        ([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
    ]:
        print(Solution().exist(board, word))
