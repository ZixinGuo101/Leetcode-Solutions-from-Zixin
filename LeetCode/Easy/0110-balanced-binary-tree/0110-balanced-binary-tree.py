# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root: Optional[TreeNode], depth: int) -> int:
            if root is None:
                return depth - 1
            depth_left = dfs(root.left, depth + 1)
            depth_right = dfs(root.right, depth + 1)
            if abs(depth_left - depth_right) > 1:
                self.res = False
            return max(depth_left, depth_right)
        
        dfs(root, 1)
        return self.res