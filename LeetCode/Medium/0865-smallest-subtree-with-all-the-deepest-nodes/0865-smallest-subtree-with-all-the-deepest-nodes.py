# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if root is None:
                return 0, None
            ld, la = dfs(root.left)
            rd, ra = dfs(root.right)
            if ld == rd:
                return ld + 1, root
            return (ld + 1, la) if ld > rd else (rd + 1, ra)
        
        return dfs(root)[1]