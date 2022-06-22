# Implement pow(x, n), which calculates x raised to the power n (i.e., xⁿ). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#  
# 
#  Example 2: 
# 
#  
# Input: x = 2.10000, n = 3
# Output: 9.26100
#  
# 
#  Example 3: 
# 
#  
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2⁻² = 1/2² = 1/4 = 0.25
#  
# 
#  
#  Constraints: 
# 
#  
#  -100.0 < x < 100.0 
#  -2³¹ <= n <= 2³¹-1 
#  -10⁴ <= xⁿ <= 10⁴ 
#  
#  Related Topics 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            n_flag = True
        else:
            n_flag = False
            
        if x == 0:
            return 0
        elif x < 0:
            x = -x
            x_flag = True
        else:
            x_flag = False
        
        ans = 1
        if x_flag and n & 1 == 0:
            x_flag = False

        while n:
            tmp = n & 1
            if tmp:
                ans *= x
            x *= x
            n >>= 1

        if x_flag:
            ans = -ans
        if n_flag:
            ans = 1 / ans

        return ans  
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().myPow(2, -2))
