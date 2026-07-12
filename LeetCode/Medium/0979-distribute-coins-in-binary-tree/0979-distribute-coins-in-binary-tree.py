# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def move(root):
            if root is None:
                return 0
            lm = move(root.left)
            rm = move(root.right)
            self.res += abs(lm) + abs(rm)
            return lm + rm + root.val - 1
        move(root)
        return self.res