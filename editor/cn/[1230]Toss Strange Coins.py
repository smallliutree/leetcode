# You have some coins. The i-th coin has a probability prob[i] of facing heads 
# when tossed. 
# 
#  Return the probability that the number of coins facing heads equals target 
# if you toss every coin exactly once. 
# 
#  
#  Example 1: 
#  Input: prob = [0.4], target = 1
# Output: 0.40000
#  Example 2: 
#  Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# Output: 0.03125
#  
#  
#  Constraints: 
# 
#  
#  1 <= prob.length <= 1000 
#  0 <= prob[i] <= 1 
#  0 <= target <= prob.length 
#  Answers will be accepted as correct if they are within 10^-5 of the correct 
# answer. 
#  
#  Related Topics


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i - 1])
            for j in range(1, min(i + 1, target + 1)):
                dp[i][j] = dp[i - 1][j] * (1 - prob[i - 1]) + dp[i - 1][j - 1] * prob[i - 1]

        # print(dp)
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for p, t in [
        ([0.4], 1),
        ([0.5, 0.5, 0.5, 0.5, 0.5], 0)
    ]:
        print(Solution().probabilityOfHeads(p, t))
