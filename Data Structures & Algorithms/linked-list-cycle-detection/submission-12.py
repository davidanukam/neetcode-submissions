# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while p1 != None and p2 != None:
            if not p1.next:
                return False
            p1 = p1.next.next
            if not p1:
                return False
            if p1.next == p2:
                return True
            p2 = p2.next
        return False