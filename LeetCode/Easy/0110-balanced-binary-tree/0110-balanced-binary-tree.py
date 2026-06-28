# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_h = dfs(root.left)
            if left_h == -1:
                return -1
            right_h = dfs(root.right)
            if right_h == -1 or abs(right_h - left_h) > 1:
                return -1
            return max(right_h, left_h) + 1
        
        return dfs(root) != -1