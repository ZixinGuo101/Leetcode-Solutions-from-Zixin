# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if root is None:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            self.res += abs(lv - rv)
            return lv + rv + root.val
        
        dfs(root)
        return self.res