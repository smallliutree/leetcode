# You are given an integer array jobs, where jobs[i] is the amount of time it 
# takes to complete the iᵗʰ job. 
# 
#  There are k workers that you can assign jobs to. Each job should be assigned 
# to exactly one worker. The working time of a worker is the sum of the time it 
# takes to complete all jobs assigned to them. Your goal is to devise an optimal 
# assignment such that the maximum working time of any worker is minimized. 
# 
#  Return the minimum possible maximum working time of any assignment. 
# 
#  
#  Example 1: 
# 
#  
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= jobs.length <= 12 
#  1 <= jobs[i] <= 10⁷ 
#  
#  Related Topics


from typing import List
import flask

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        sum_list = [0] * (1 << n)
        for i in range(1, 1 << n):
            _i = i
            tmp = 0
            while i & 1 != 1:
                tmp += 1
                i >>= 1
            sum_list[_i] = sum_list[_i & _i - 1] + jobs[tmp]
        print(sum_list)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    j = [3,2,3]
    k = 3
    print(Solution().minimumTimeRequired(j, k))
