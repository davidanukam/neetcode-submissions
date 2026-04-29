# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        table = []
        
        curr = head
        while curr != None:
            if curr in table:
                return True
            table.append(curr)
            curr = curr.next
        return False