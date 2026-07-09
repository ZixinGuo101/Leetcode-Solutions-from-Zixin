# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        sub_sum = []
        def getTotal(root):
            if root is None:
                return 0
            l_sum = getTotal(root.left)
            r_sum = getTotal(root.right)
            cur = l_sum + r_sum + root.val
            sub_sum.append(cur)
            return cur
        total_sum = getTotal(root)
        return max(s * (total_sum - s) for s in sub_sum) % MOD