# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, mx, mn):
            if root is None:
                self.res = max(self.res, mx - mn)
                return
            mx = max(root.val, mx)
            mn = min(root.val, mn)
            dfs(root.left, mx, mn)
            dfs(root.right, mx, mn)
            return
        dfs(root, root.val, root.val)
        return self.res