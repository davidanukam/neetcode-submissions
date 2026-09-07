# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        pointer_map = {}

        new_map = {}

        index = 0
        curr = head
        while curr != None:
            node_map[curr] = index
            new_map[index] = Node(curr.val)
            curr = curr.next
            index += 1
        
        index = 0
        for key, value in node_map.items():
            data = []
            n = key.next
            if n == None:
                data.append(None)
            else:
                data.append(node_map[n])

            r = key.random
            if r == None:
                data.append(None)
            else:
                data.append(node_map[r])
            
            pointer_map[index] = data
            index += 1
        
        index = 0
        for key, value in new_map.items():
            n = pointer_map[index][0]
            if n == None:
                value.next = None
            else:
                value.next = new_map[n]

            r = pointer_map[index][1]
            if r == None:
                value.random = None
            else:
                value.random = new_map[r]
            index += 1
        
        return new_map[0] if len(new_map) else None
