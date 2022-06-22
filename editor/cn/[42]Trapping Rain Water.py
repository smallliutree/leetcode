# Given n non-negative integers representing an elevation map where the width 
# of each bar is 1, compute how much water it can trap after raining. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [
# 0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
# are being trapped.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [4,2,0,3,2,5]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10^4
#  0 <= height[i] <= 10^5
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height):
        tmp = []
        for i in range(1, len(height) - 1):
            if height[i] >= height[i - 1] and height[i] >= height[i + 1]:
                tmp.append((i, height[i]))
        index = iter(tmp)
        flag = index.next()
        ans = 0
        for i, v in enumerate(height):
            if i < flag[0]:
                ans += flag[1] - v
            else:
                try:
                    flag = index.next()
                except StopIteration:
                    for remain in height[i + 1:]:
                        ans += v - remain
                        return ans
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print Solution().trap(height)
