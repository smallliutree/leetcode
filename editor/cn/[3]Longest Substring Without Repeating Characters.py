# Given a string s, find the length of the longest substring without repeating 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        char_set = set()
        left = 0
        char_set.add(s[left])
        ans = 1
        for right in range(left + 1, len(s)):
            tmp = s[right]
            if tmp in char_set:
                ans = max(right - left, ans)
                # print(left, right, ans)
                while s[left] != tmp:
                    char_set.remove(s[left])
                    left += 1
                left += 1
            else:
                char_set.add(tmp)
        ans = max(ans, right - left + 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
