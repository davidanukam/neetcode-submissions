# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(r, m):
            if r:
                if r.val >= m:
                    self.count += 1
                    m = r.val

                dfs(r.left, m)
                dfs(r.right, m)
        
        dfs(root, -101)

        return self.count
                