# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        def findValue(root):
            if root is None:
                return 0
            leftValue = findValue(root.left)
            rightValue = findValue(root.right)
            maxValue = max(root.val, root.val+leftValue, root.val+rightValue)
            self.res = max(self.res, maxValue, root.val+leftValue+rightValue)
            return maxValue
        findValue(root)
        return self.res