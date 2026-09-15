# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = {}

        def subList(r, l):
            if r:
                if l in output:
                    output[l].append(r.val)
                else:
                    output[l] = [r.val]

                if r.left:
                    left = subList(r.left, l + 1)
                if r.right:
                    right = subList(r.right, l + 1)
        
        subList(root, 0)

        return list(output.values())