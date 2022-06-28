# There are n children standing in a line. Each child is assigned a rating 
# value given in the integer array ratings. 
# 
#  You are giving candies to these children subjected to the following 
# requirements: 
# 
#  
#  Each child must have at least one candy. 
#  Children with a higher rating get more candies than their neighbors. 
#  
# 
#  Return the minimum number of candies you need to have to distribute the 
# candies to the children. 
# 
#  
#  Example 1: 
# 
#  
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 
# 2 candies respectively.
#  
# 
#  Example 2: 
# 
#  
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == ratings.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= ratings[i] <= 2 * 10⁴ 
#  
#  Related Topics


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        asc = des = 0
        pre = 1
        ans = 1
        for i in range(1, n := len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if ratings[i] == ratings[i - 1]:
                    asc = 0
                else:
                    asc += 1
                pre = asc + 1
                ans += asc + 1
                des = 0
            else:
                asc = 0
                des += 1
                ans += des
                if des >= pre:
                    ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for rate in [
        [1, 0, 2],
        [1, 2, 2],
        [1, 3, 2, 2, 1]
    ]:
        print(Solution().candy(rate))
