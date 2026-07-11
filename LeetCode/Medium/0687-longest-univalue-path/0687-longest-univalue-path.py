# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if root is None:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            if root.left and root.left.val == root.val:
                lv += 1
            else:
                lv = 0
            if root.right and root.right.val == root.val:
                rv += 1
            else:
                rv = 0
            self.res = max(self.res, lv + rv)
            return max(lv, rv)
        dfs(root)
        return self.res