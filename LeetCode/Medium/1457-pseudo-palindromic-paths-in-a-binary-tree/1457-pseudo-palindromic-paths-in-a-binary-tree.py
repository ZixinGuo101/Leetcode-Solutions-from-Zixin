# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(root: Optional[TreeNode], path: int) -> int:
            if root is None:
                return 0
            path ^= (1 << root.val)
            if root.left is None and root.right is None:
                return 1 if not path & (path - 1) else 0
            return dfs(root.left, path) + dfs(root.right, path)
        
        return dfs(root, 0)