# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = ListNode()
        tail.next = head

        while head != None:
            head = head.next
            if head != None:
                head = head.next
                tail = tail.next
            if head == tail: return True

        return False