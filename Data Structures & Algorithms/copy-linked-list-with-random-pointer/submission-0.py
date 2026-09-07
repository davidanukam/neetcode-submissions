# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        next_map = {}
        random_map = {}

        index = 0
        curr = head
        while curr != None:
            node_map[curr] = index
            curr = curr.next
            index += 1
        
        index = 0
        curr = head
        for key, value in node_map.items():
            if key.next == None:
                next_map[index] = None
            else:
                next_map[index] = node_map[key.next]

            if key.random == None:
                random_map[index] = None
            else:
                random_map[index] = node_map[key.random]
            index += 1
        
        new_map = {}

        index = 0
        curr = head
        while curr != None:
            new_map[index] = Node(curr.val)
            curr = curr.next
            index += 1
        
        index = 0
        for key, value in new_map.items():
            value.next = new_map[next_map[index]] if next_map[index] != None else None
            value.random = new_map[random_map[index]] if random_map[index] != None else None
            index += 1
        
        return new_map[0] if len(new_map) else None
        
        

