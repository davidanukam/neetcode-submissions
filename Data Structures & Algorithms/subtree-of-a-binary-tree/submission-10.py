# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root, subRoot):
            if not root and not subRoot: return True
            if root and not subRoot: return False
            if subRoot and not root: return False
            if root.val != subRoot.val: return False
            if not root.left and not subRoot.left and not root.right and not subRoot.right:
                return True if root.val == subRoot.val else False
            
            if root.val == subRoot.val:
                left = sametree(root.left, subRoot.left)
                return sametree(root.right, subRoot.right) if left else False
        
        same = sametree(root, subRoot)
        if not same:
            if root.left:
                left = self.isSubtree(root.left, subRoot)
                if not left:
                    if root.right:
                        return self.isSubtree(root.right, subRoot)
                else:
                    return True
            if root.right:
                right = self.isSubtree(root.right, subRoot)
                if not right:
                    if root.left:
                        return self.isSubtree(root.left, subRoot)
                else:
                    return True
        return same
            