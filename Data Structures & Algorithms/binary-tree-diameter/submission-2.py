# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    dia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_dia(root) -> int:
            if root:
                left = get_dia(root.left)
                right = get_dia(root.right)
                sub_dia = left + right
                self.dia = max(self.dia, sub_dia)
                return max(left, right) + 1
            return 0
        
        get_dia(root)
        return self.dia
