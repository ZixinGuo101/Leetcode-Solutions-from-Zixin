# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find(root: TreeNode, maxValue: int) -> int:
            if root is None:
                return 0
            res = 1 if root.val >= maxValue else 0
            maxValue = max(root.val, maxValue)
            return res + find(root.left, maxValue) +find(root.right, maxValue)
        return find(root, float(-inf))
