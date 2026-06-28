# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        def findSum(root: Optional[TreeNode], lastSum: int) -> int:
            if root is None:
                return 0
            lastSum += root.val
            res = d[lastSum - targetSum]
            d[lastSum] += 1
            l = findSum(root.left, lastSum)
            r = findSum(root.right, lastSum)
            d[lastSum] -= 1
            # print("node: ", root.val, res, l, r)
            return res + l + r
        return findSum(root, 0)