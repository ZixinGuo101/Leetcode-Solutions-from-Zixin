# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.path = 0
        
        def dfs(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            self.path ^= (1 << root.val)
            if root.left is None and root.right is None:
                if self.path & (self.path - 1) == 0:
                    self.res += 1
            else:
                dfs(root.left)
                dfs(root.right)
            self.path ^= (1 << root.val)
            return
        
        dfs(root)
        return self.res