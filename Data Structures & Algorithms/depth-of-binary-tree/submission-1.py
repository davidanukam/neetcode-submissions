# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(root):
            while root != None:
                if root.left:
                    leftD = 1 + dfs(root.left)
                    if root.right:
                        rightD = 1 + dfs(root.right)
                        return max(leftD, rightD)
                    return leftD
                if root.right:
                    return 1 + dfs(root.right)
                return 1

        return dfs(root)