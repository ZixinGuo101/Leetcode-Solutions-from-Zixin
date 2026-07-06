# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if root is None:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            if lv == 0:
                root.left = None
            if rv == 0:
                root.right = None
            return lv + rv + root.val
        
        dfs(root)
        return root if dfs(root) else None