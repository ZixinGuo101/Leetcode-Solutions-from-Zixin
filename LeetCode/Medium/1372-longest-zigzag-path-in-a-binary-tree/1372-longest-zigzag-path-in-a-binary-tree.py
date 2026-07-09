# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def path(root):
            if root is None:
                return -1, -1
            left_left, left_right = path(root.left)
            right_left, right_right = path(root.right)
            l = left_right + 1
            r = right_left + 1
            self.res = max(self.res, l, r)
            return l, r
        path(root)
        return self.res
            