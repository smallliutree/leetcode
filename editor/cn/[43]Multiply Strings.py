# Given two non-negative integers num1 and num2 represented as strings, return 
# the product of num1 and num2, also represented as a string. 
# 
#  Note: You must not use any built-in BigInteger library or convert the inputs 
# to integer directly. 
# 
#  
#  Example 1: 
#  Input: num1 = "2", num2 = "3"
# Output: "6"
#  Example 2: 
#  Input: num1 = "123", num2 = "456"
# Output: "56088"
#  
#  
#  Constraints: 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 and num2 consist of digits only. 
#  Both num1 and num2 do not contain any leading zero, except the number 0 
# itself. 
#  
#  Related Topics 


# leetcode submit region begin(Prohibit modification and deletion)
from functools import reduce


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        if m < n:
            m, n, num1, num2 = n, m, num2, num1
        ans = []
        for i in range(m - 1, -1, -1):
            carry = 0
            tmp = ''
            op1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                t = int(num2[j]) * op1 + carry
                carry = t // 10
                t %= 10
                tmp += str(t)
            if carry:
                tmp += str(carry)
            # print(op1, num2, tmp)
            tmp = tmp[::-1] + '0' * (m - i - 1)
            ans.append(tmp)

        # print(ans)
        return reduce(lambda x, y: self.add_str(x, y), ans)

    def add_str(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        if m < n:
            m, n, num1, num2 = n, m, num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        carry = 0
        ans = ''
        for i in range(n):
            tmp = int(num1[i]) + int(num2[i]) + carry
            carry = tmp // 10
            tmp %= 10
            ans += str(tmp)

        for j in range(n, m):
            tmp = int(num1[j]) + carry
            carry = tmp // 10
            tmp %= 10
            ans += str(tmp)

        if carry:
            ans += '1'

        return ans[::-1]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for x, y in [('2', '3'), ('123', '456')]:
        print(Solution().multiply(x, y))
