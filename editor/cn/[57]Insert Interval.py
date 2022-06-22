# You are given an array of non-overlapping intervals intervals where intervals[
# i] = [starti, endi] represent the start and the end of the iᵗʰ interval and 
# intervals is sorted in ascending order by starti. You are also given an interval 
# newInterval = [start, end] that represents the start and end of another interval. 
# 
#  Insert newInterval into intervals such that intervals is still sorted in 
# ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary). 
# 
#  Return intervals after the insertion. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= intervals.length <= 10⁴ 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 10⁵ 
#  intervals is sorted by starti in ascending order. 
#  newInterval.length == 2 
#  0 <= start <= end <= 10⁵ 
#  
#  Related Topics 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        index = 0
        while index < len(intervals):
            x, y = intervals[index][0], intervals[index][1]
            if y < newInterval[0]:
                ans.append([x, y])
                index += 1
                continue

            if x > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[index:])
                return ans

            if x <= newInterval[0] and y >= newInterval[1]:
                ans.extend(intervals[index:])
                return ans

            tmp = [min(x, newInterval[0]), max(y, newInterval[1])]
            for k in range(index + 1, len(intervals)):
                i, j = intervals[k][0], intervals[k][1]
                if j <= tmp[1]:
                    continue
                elif i <= tmp[1]:
                    tmp[1] = j
                    ans.append(tmp)
                    ans.extend(intervals[k + 1:])
                    return ans
                else:
                    ans.append(tmp)
                    ans.extend(intervals[k:])
                    return ans
            else:
                ans.append(tmp)
                return ans
        ans.append(newInterval)
        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    intervals = [[1, 5]]
    newInterval = [2, 7]
    print(Solution().insert(intervals, newInterval))
