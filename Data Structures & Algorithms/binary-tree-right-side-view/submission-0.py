# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lvls = {}

        def dfs(r, lvls, l):
            if r:
                if l in lvls:
                    lvls[l].append(r)
                else:
                    lvls[l] = [r]

                left = dfs(r.left, lvls, l + 1)
                right = dfs(r.right, lvls, l + 1)

        dfs(root, lvls, 0)

        output = []
        for key, value in lvls.items():
            output.append(value[-1].val)

        return output