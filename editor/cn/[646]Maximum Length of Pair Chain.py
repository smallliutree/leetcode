# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and 
# lefti < righti. 
# 
#  A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can 
# be formed in this fashion. 
# 
#  Return the length longest chain which can be formed. 
# 
#  You do not need to use up all the given intervals. You can select pairs in 
# any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
#  
# 
#  Example 2: 
# 
#  
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
#  
# 
#  
#  Constraints: 
# 
#  
#  n == pairs.length 
#  1 <= n <= 1000 
#  -1000 <= lefti < righti <= 1000 
#  
#  Related Topics


from typing import List
from collections import defaultdict, Counter
from functools import reduce
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[0], x[1]))
        ans = 0
        last = None
        for pair in pairs:
            # print(last)
            if last is None or pair[0] > last:
                ans += 1
                last = pair[1]
            elif pair[1] < last:
                last = pair[1]
        # print(ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for pairs in [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 2], [7, 8], [4, 5]],
        [[2, 8], [1, 8], [-8, 0], [-6, -1], [7, 9], [-8, 5]]
    ]:
        print(Solution().findLongestChain(pairs))
