# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry, res):
            if l1 and l2:
                digit = l1.val + l2.val + carry

                res.val = digit % 10
                res.next = add(l1.next, l2.next, digit // 10, ListNode())
            elif l1 and not l2:
                digit = l1.val + carry
                res.val = digit % 10
                res.next = add(l1.next, None, digit // 10, ListNode())
            elif not l1 and l2:
                digit = l2.val + carry
                res.val = digit % 10
                res.next = add(None, l2.next, digit // 10, ListNode())
            else:
                if carry == 0:
                    return None
                else:
                    return ListNode(carry)
            
            return res

        
        return add(l1, l2, 0, ListNode())