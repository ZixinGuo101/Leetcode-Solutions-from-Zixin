# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if root is None:
                return None
            l = dfs(root.left)
            r = dfs(root.right)
            if l is not None:
                root.right, l.right = root.left, root.right
                root.left = None
                return l if r is None else r
            return root if r is None else r
        
        dfs(root)
            

            
        