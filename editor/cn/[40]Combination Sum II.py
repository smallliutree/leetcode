# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        for index, value in enumerate(candidates):
            if value > target:
                candidates = candidates[:index]
                break

        d = defaultdict(set)
        d[candidates[0]].add((candidates[0], ))

        for i in candidates[1:]:
            for k in d:
                if k + i > target:
                    break
                for v in d[k]:
                    print(v, d[k], )
                    tmp = list(v)
                    tmp.extend([i])
                    d[k + i].add(tuple(list(tmp)))

        print(d)

        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    Solution().combinationSum2([1,2,3,4], 22)
