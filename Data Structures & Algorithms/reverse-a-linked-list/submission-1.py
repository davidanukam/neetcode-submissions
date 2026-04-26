# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ans = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        self.reverse(None, head)
        return self.ans
    
    def reverse(self, prev: Optional[ListNode], curr: Optional[ListNode]):
        if curr.next == None:
            self.ans = curr
        else:
            self.reverse(curr, curr.next)
        curr.next = prev
        
