# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.last_node = None

        def get_end(front):
            if front:
                while front.next != None:
                    if front.next == self.last_node:
                        break
                    else:
                        front = front.next
                self.last_node = front
                return self.last_node
            return None
        
        def reorder(front):
            p1 = front
            p2 = get_end(p1)

            if p1 == p2:
                p1.next = None
            elif p1.next == p2:
                p2.next = None
            else:
                p2.next = reorder(p1.next)
                p1.next = p2
            
            return p1

        reorder(head)