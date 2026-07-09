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
                return
            mx = root.val if root.val > mx else mx
            mn = root.val if root.val < mn else mn
            cur = max(abs(mx - root.val), abs(mn - root.val))
            self.res = max(self.res, cur)
            dfs(root.left, mx, mn)
            dfs(root.right, mx, mn)
            return
        
        dfs(root, root.val, root.val)
        return self.res