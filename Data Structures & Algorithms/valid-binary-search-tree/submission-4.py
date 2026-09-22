# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkTree(root, s, l):
            if root:
                if not (s < root.val and root.val < l): return False

                left = checkTree(root.left, s, root.val)
                if left:
                    return checkTree(root.right, root.val, l)
                return False
            return True

        return checkTree(root, -1000000001, 1000000001)