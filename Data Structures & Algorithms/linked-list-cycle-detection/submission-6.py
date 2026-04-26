# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = ListNode()
        tail.next = head

        seen = []

        while head != None:
            if head in seen: return True
            seen.append(head)
            head = head.next
            tail = tail.next

        return False