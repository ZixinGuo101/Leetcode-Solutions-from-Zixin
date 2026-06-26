# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = chr(ord('a') + 26)
        def dfs(root: Optional[TreeNode], path: str):
            if root is None:
                return
            path = chr(ord('a') + root.val) + path
            if root.left is None and root.right is None:
                if path < self.res:
                    self.res = path
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            return
        dfs(root, "")
        return self.res