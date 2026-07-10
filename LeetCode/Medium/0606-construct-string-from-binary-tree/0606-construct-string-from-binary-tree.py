# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def dfs(root):
            if root is None:
                return
            self.res.append(str(root.val))
            if root.left is None and root.right is None:
                return
            
            self.res.append('(')
            if root.left is not None:
                dfs(root.left)
            self.res.append(')')

            if root.right is not None:
                self.res.append('(')
                dfs(root.right)
                self.res.append(')')
            return
        dfs(root)
        return ''.join(self.res)
