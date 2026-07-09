# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs1(root):
            if root is None:
                return 0
            ls = dfs1(root.left)
            rs = dfs1(root.right)
            return root.val + ls + rs
        totalSum = dfs1(root)
        self.res = 0
        def dfs2(root):
            if root is None:
                return 0
            l = dfs2(root.left)
            r = dfs2(root.right)
            cur = l + r + root.val
            self.res = max(self.res, cur * (totalSum - cur))
            return cur
        dfs2(root)
        return self.res % (10 ** 9 + 7)
