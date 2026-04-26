# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        start = output

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                output.next = list1
                output = output.next
                list1 = list1.next
            else:
                output.next = list2
                output = output.next
                list2 = list2.next
        while list1 != None:
            output.next = list1
            output = output.next
            list1 = list1.next
        while list2 != None:
            output.next = list2
            output = output.next
            list2 = list2.next
        
        return start.next