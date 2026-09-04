# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = None
        p2 = head
        p3 = head.next

        # Get the length of the Linked List
        length = 1
        while p2.next != None:
            p2 = p2.next
            length += 1
        
        # Reset pointer
        p2 = head

        index_to_remove = length - n

        curr_index = 0
        while curr_index < length:
            if curr_index == index_to_remove:
                if p1 == None:
                    if p3:
                        return p3
                    else:
                        return None
                else:
                    p1.next = p3
                    break
            else:
                p1 = p2
                p2 = p3
                p3 = p3.next
                curr_index += 1
        
        return head
