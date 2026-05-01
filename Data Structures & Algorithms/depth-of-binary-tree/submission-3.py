# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        num = 1
        node = root
        numLeft = self.maxDepth(node.left)
        numRight = self.maxDepth(node.right)
        num += max(numLeft, numRight)
        return num