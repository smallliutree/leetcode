# You are given the head of a singly linked-list. The list can be represented 
# as: 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  Reorder the list to be on the following form: 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#  
# 
#  You may not modify the values in the list's nodes. Only nodes themselves may 
# be changed. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 5 * 10⁴]. 
#  1 <= Node.val <= 1000 
#  
#  Related Topics 栈 递归 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # print('====')
        if not head:
            return
        l1 = head
        node = self.find_mid(head)
        l2 = node.next
        node.next = None
        l2 = self.reverseList(l2)
        # print(l1 is head)
        self.mergeList(l1, l2)

    def find_mid(self, head: ListNode):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        return slow

    def reverseList(self, head: ListNode):
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre

    def mergeList(self, l1, l2):
        while l1 and l2:
            tmp1, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    tmp = [1, 2, 3, 4]
    fake = ListNode()
    ans = fake
    for i in tmp:
        fake.next = ListNode(i)
        fake = fake.next
    head = ans.next
    Solution().reorderList(ans.next)
    while head:
        print(head.val)
        head = head.next

