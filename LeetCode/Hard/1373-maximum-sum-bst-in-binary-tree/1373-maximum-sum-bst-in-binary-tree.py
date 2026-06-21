# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxSum = float('-inf')
        def boundary(root):
            if root.left is None and root.right is None:
                self.maxSum = max(self.maxSum, root.val)
                return root.val, root.val, root.val, True
            isValid = True
            lo = root.val
            hi = root.val
            left_sum = 0
            right_sum = 0
            if root.left:
                left_lo, left_hi, left_sum, left_isValid = boundary(root.left)
                if left_hi >= root.val or not left_isValid:
                    isValid = False
                else:
                    lo = left_lo
            if root.right:
                right_lo, right_hi, right_sum, right_isValid = boundary(root.right)
                if right_lo <= root.val or not right_isValid:
                    isValid = False
                else:
                    hi = right_hi
            if not isValid:
                return root.val, root.val, root.val, False
            tree_sum = left_sum + right_sum + root.val
            self.maxSum = max(self.maxSum, tree_sum)
            return lo, hi, tree_sum, True
        boundary(root)
        return 0 if self.maxSum < 0 else self.maxSum
        