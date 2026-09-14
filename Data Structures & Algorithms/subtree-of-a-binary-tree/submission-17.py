# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(r, sr):
            if not r and not sr: return True
            if not r and sr: return False
            if r and not sr: return False

            if r and sr:
                if r.val == sr.val:
                    left = sametree(r.left, sr.left)
                    if left:
                        return sametree(r.right, sr.right)
                    return False
                return False
        
        if not sametree(root, subRoot):
            left = self.isSubtree(root.left, subRoot) if root.left else False
            right = self.isSubtree(root.right, subRoot) if root.right else False
            return left or right
        return True