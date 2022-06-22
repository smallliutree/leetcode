# Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
# the median of the two sorted arrays. 
# 
#  The overall run time complexity should be O(log (m+n)). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10^6 <= nums1[i], nums2[i] <= 10^6
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # m, n = len(nums1), len(nums2)
        # infinity = float('inf')
        # if m > n:
        #     m, n, nums1, nums2 = n, m, nums2, nums1
        # t = (m + n + 1) // 2
        # left, right = 0, m
        # a, b = 0, 0
        # while left <= right:
        #     i = (left + right) // 2
        #     j = t - i
        #     i0 = -infinity if i == 0 else nums1[i - 1]
        #     i1 = infinity if i == m else nums1[i]
        #     j0 = -infinity if j == 0 else nums2[j - 1]
        #     j1 = infinity if j == n else nums2[j]
        #     if i0 <= j1:
        #         a, b = max(i0, j0), min(i1, j1)
        #         left = i + 1
        #     else:
        #         right = i - 1
        # # print a, b
        # return float(a + b) / 2 if (m + n) & 1 == 0 else a
        m, n = len(nums1), len(nums2)
        if (m + n) & 1 == 1:
            return self.find_k((m + n + 1) // 2, nums1, nums2, m, n)
        else:
            return float(self.find_k((m + n) // 2, nums1, nums2, m, n) + self.find_k((m + n) // 2 + 1, nums1, nums2, m, n)) / 2

    def find_k(self, k, nums1, nums2, m, n):
        index1, index2 = 0, 0
        while True:
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            _index1 = min(index1 + k // 2 - 1, m - 1)
            _index2 = min(index2 + k // 2 - 1, n - 1)
            if nums1[_index1] <= nums2[_index2]:
                k -= _index1 - index1 + 1
                index1 = _index1 + 1
            else:
                k -= _index2 - index2 + 1
                index2 = _index2 + 1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    nums1 = [1,4]
    nums2 = []
    print Solution().findMedianSortedArrays(nums1, nums2)
