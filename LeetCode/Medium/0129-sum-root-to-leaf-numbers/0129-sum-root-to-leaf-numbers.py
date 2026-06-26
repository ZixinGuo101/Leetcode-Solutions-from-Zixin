# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, value):
            if root is None:
                return
            new_value = root.val + value * 10
            if root.left is None and root.right is None:
                self.res += new_value
            else:
                dfs(root.left, new_value)
                dfs(root.right, new_value)
            return
        dfs(root, 0)
        return self.res