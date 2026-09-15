# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p1 = []
        p2 = []

        def dfs(r, n, l):
            if r:
                l.append(r.val)
                if r.val == n.val:
                    return True
                left = dfs(r.left, n, l)
                if not left:
                    l.pop()
                    right = dfs(r.right, n, l)
                    if not right:
                        l.pop()
                        return False
                    return True
                return True
            l.append(None)
            return False
        
        dfs(root, p, p1)
        dfs(root, q, p2)

        mp = p1 if len(p1) >= len(p2) else p2
        sp = p1 if mp == p2 else p2

        for i in range(len(mp) - 1, -1, -1):
            if mp[i] in sp:
                return TreeNode(mp[i])