# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros. 
# 
#  
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
#  
# 
#  Given a string s containing only digits, return all possible valid IP 
# addresses that can be formed by inserting dots into s. You are not allowed to reorder 
# or remove any digits in s. You may return the valid IP addresses in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#  
# 
#  Example 2: 
# 
#  
# Input: s = "0000"
# Output: ["0.0.0.0"]
#  
# 
#  Example 3: 
# 
#  
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 20 
#  s consists of digits only. 
#  
#  Related Topics
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if all(map(self.is_valid, [s[:i], s[i: j], s[j: k], s[k:]])):
                        ans.append('.'.join([s[:i], s[i: j], s[j: k], s[k:]]))
        return ans

    def is_valid(self, s):
        if not s:
            return False
        if 0 <= int(s) <= 255 and str(int(s)) == s:
            return True
        return False
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    a = '0000'
    print(Solution().restoreIpAddresses(a))
