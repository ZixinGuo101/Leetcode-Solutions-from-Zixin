# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], indi: bool) -> int:
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return root.val if indi else 0
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)
