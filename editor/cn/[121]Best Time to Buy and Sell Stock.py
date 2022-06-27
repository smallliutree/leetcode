# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day. 
# 
#  You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock. 
# 
#  Return the maximum profit you can achieve from this transaction. If you 
# cannot achieve any profit, return 0. 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you 
# must buy before you sell.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴ 
#  
#  Related Topics


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimize, ans = prices[0], 0
        n = len(prices)
        for i in range(1, n):
            minimize, ans = min(minimize, prices[i]), max(ans, prices[i] - minimize)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    for p in [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [2]
    ]:
        print(Solution().maxProfit(p))
