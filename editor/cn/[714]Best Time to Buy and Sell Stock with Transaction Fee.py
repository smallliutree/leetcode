# You are given an array prices where prices[i] is the price of a given stock 
# on the iᵗʰ day, and an integer fee representing a transaction fee. 
# 
#  Find the maximum profit you can achieve. You may complete as many 
# transactions as you like, but you need to pay the transaction fee for each transaction. 
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you 
# must sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 5 * 10⁴ 
#  1 <= prices[i] < 5 * 10⁴ 
#  0 <= fee < 5 * 10⁴ 
#  
#  Related Topics


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, sell = [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i] - fee)
        # print(sell, hold)
        return sell[-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    for p, f in [
        ([1, 3, 2, 8, 4, 9], 2),
        ([1, 3, 7, 5, 10, 3], 3)
    ]:
        print(Solution().maxProfit(p, f))
