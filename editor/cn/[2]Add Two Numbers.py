# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes contains a 
# single digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the 
# number 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have 
# leading zeros. 
#  
#  Related Topics


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode(next=l1)
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
            else:
                break
        l2 = l2.next
        if l2:
            l1.next = l2
        if carry:
            while l1.next:
                l1.next.val += carry
                carry = l1.next.val // 10
                l1.next.val %= 10
                l1 = l1.next
            if carry:
                l1.next = ListNode(1)
        return fake.next
# leetcode submit region end(Prohibit modification and deletion)
