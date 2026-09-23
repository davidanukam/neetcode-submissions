# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Use inorder traversal
        a = []
        def inorder(r, a):
            if r:
                inorder(r.left, a)
                a.append(r.val)
                inorder(r.right, a)
                return
            return

        inorder(root, a)

        return a[k - 1]