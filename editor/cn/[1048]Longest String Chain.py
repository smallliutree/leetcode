# You are given an array of words where each word consists of lowercase English 
# letters. 
# 
#  wordA is a predecessor of wordB if and only if we can insert exactly one 
# letter anywhere in wordA without changing the order of the other characters to make 
# it equal to wordB. 
# 
#  
#  For example, "abc" is a predecessor of "abac", while "cba" is not a 
# predecessor of "bcad". 
#  
# 
#  A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, 
# where word1 is a predecessor of word2, word2 is a predecessor of word3, and so 
# on. A single word is trivially a word chain with k == 1. 
# 
#  Return the length of the longest possible word chain with words chosen from 
# the given list of words. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", 
# "pcxbc", "pcxbcf"].
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word 
# chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the 
# letters is changed.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length <= 16 
#  words[i] only consists of lowercase English letters. 
#  
#  Related Topics 数组 哈希表 双指针 字符串 动态规划 👍 177 👎 0


from typing import List
from collections import defaultdict, Counter
from functools import reduce
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = [1] * (l := len(words))
        for i in range(l):
            for j in range(i):
                is_sub = self.match_str(words[i], words[j])
                # print(is_sub)
                if is_sub:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)

    def match_str(self, long_str, short_str):
        # print(long_str, short_str)
        m, n = len(long_str), len(short_str)
        if m != n + 1:
            return False
        left = right = 0
        while left < m and right < n:
            if long_str[left] == short_str[right]:
                left += 1
                right += 1
            else:
                if long_str[left + 1:] != short_str[right:]:
                    return False
                return True
        return True

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    for words in [
        ["a", "b", "ba", "bca", "bda", "bdca"],
        ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"],
        ["abcd", "dbqca"]
    ]:
        print(Solution().longestStrChain(words))
