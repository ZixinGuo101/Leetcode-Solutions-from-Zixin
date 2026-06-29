# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        res = False
        if root.val == subRoot.val:
            res = self.isSame(root, subRoot)
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r1, r2):
        if r1 is None or r2 is None:
            return r1 is r2
        return r1.val == r2.val and self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)