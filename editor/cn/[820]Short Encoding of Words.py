# A valid encoding of an array of words is any reference string s and array of 
# indices indices such that: 
# 
#  
#  words.length == indices.length 
#  The reference string s ends with the '#' character. 
#  For each index indices[i], the substring of s starting from indices[i] and 
# up to (but not including) the next '#' character is equal to words[i]. 
#  
# 
#  Given an array of words, return the length of the shortest reference string 
# s possible of any valid encoding of words. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5
# ].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the 
# next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next 
# '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the 
# next '#' is underlined in "time#bell#"
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 2000 
#  1 <= words[i].length <= 7 
#  words[i] consists of only lowercase letters. 
#  
#  Related Topics
from collections import defaultdict
from functools import reduce
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        Trie = lambda: defaultdict(Trie)
        t = Trie()
        # for word in set(words):
        #     node = t[word[-1]]
        #     for c in word[-2::-1]:
        #         node = node[c]
        # # print(t)
        #
        # ans = 0
        #
        # def dfs(d, tmp):
        #     nonlocal ans
        #     if not d.values():
        #         ans += tmp + 1
        #         return
        #     for _d in d.values():
        #         dfs(_d, tmp + 1)
        #
        # dfs(t, 0)
        # return ans
        words = list(set(words))
        nodes = [reduce(dict.__getitem__, word[::-1], t) for word in words]

        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
