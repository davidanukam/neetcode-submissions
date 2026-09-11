# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                if left[0] == False or right[0] == False:
                    return [False, 0]
                if abs(left[1] - right[1]) <= 1:
                    return [True, max(left[1], right[1]) + 1]
                else:
                    return [False, 0]
            return [True, 0]
        return dfs(root)[0]