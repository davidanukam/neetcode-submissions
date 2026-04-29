# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [root]
        while len(q):
            n = q.pop()
            temp_left = n.left
            n.left = n.right
            n.right = temp_left
            q.append(n.left) if n.left else None
            q.append(n.right) if n.right else None
        return root