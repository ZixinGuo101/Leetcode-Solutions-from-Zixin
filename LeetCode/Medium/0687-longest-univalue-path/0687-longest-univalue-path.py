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
            if not root:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            l_length = r_length = 0
            if root.left and root.left.val == root.val:
                l_length = lv + 1
            if root.right and root.right.val == root.val:
                r_length = rv + 1
            self.res = max(self.res, l_length + r_length)
            return max(l_length, r_length)
        
        dfs(root)
        return self.res
            