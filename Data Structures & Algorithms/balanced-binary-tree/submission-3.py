# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            if self.is_balanced:
                if abs(leftHeight - rightHeight) > 1:
                    self.is_balanced = False
            
            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return self.is_balanced