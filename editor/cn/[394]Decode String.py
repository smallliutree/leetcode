# Given an encoded string, return its decoded string. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed to 
# be a positive integer. 
# 
#  You may assume that the input string is always valid; there are no extra 
# white spaces, square brackets are well-formed, etc. Furthermore, you may assume 
# that the original data does not contain any digits and that digits are only for 
# those repeat numbers, k. For example, there will not be input like 3a or 2[4]. 
# 
#  The test cases are generated so that the length of the output will never 
# exceed 10⁵. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#  
# 
#  Example 2: 
# 
#  
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 30 
#  s consists of lowercase English letters, digits, and square brackets '[]'. 
#  s is guaranteed to be a valid input. 
#  All the integers in s are in the range [1, 300]. 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # tmp = ''
        # num = ''
        # for c in s:
        #     # print(c, tmp, stack)
        #     if c.isdigit():
        #         if tmp:
        #             stack.append(tmp)
        #         tmp = ''
        #         num += c
        #     elif c == '[':
        #         if num:
        #             stack.append(num)
        #             num = ''
        #     elif c == ']':
        #         num = stack.pop()
        #         tmp *= int(num)
        #         num = ''
        #         if stack and stack[-1].isalpha():
        #             pre = stack.pop()
        #             tmp = pre + tmp
        #     else:
        #         tmp += c
        # return tmp
        if not s:
            return ''
        left, right = 0, len(s) - 1
        num = ''
        while left < right and s[left].isdigit():
            num += s[left]
            left += 1
        tmp = 1
        for right in range(left + 1, len(s)):
            if s[right] == '[':
                tmp += 1
            if s[right] == ']':
                tmp -= 1
            if tmp == 0:
                break
        return int(num) * self.decodeString(s[left + 1: right]) + self.decodeString(s[right + 1])
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef", "10[aa]", "3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "3[a10[bc]]"]
    for ss in s:
        print(Solution().decodeString(ss))
