# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.md = 0
        self.res = 0
        def dfs(root: Optional[TreeNode], depth: int) -> None:
            if root is None:
                return
            if depth > self.md:
                self.md = depth
                self.res = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return
        dfs(root, 1)
        return self.res