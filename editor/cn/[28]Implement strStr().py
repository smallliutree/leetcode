2022-04-12 11:01:57
# Implement strStr(). 
# 
#  Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "hello", needle = "ll"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
#  Related Topics 双指针 字符串 字符串匹配 👍 1376 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return len(haystack.split(needle)[0])
# leetcode submit region end(Prohibit modification and deletion)
