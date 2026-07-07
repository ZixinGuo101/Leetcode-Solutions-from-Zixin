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
            cur = path = 0
            if root.left and root.left.val == root.val:
                cur += lv + 1
                path = max(path, lv + 1)
            if root.right and root.right.val == root.val:
                cur += rv + 1
                path = max(path, rv + 1)
            self.res = max(self.res, cur)
            return path
        
        dfs(root)
        return self.res
            