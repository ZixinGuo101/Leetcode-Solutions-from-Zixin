# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d = {}
        d[0] = 1
        def findSum(root: Optional[TreeNode], lastSum: int) -> int:
            if root is None:
                return 0
            cur = root.val + lastSum
            res = 0
            if cur - targetSum in d:
                res = d[cur - targetSum]
            d[cur] = d.get(cur, 0) + 1
            l = findSum(root.left, cur)
            r = findSum(root.right, cur)
            if d[cur] - 1 == 0:
                d.pop(cur)
            else:
                d[cur] -= 1
            # print("node: ", root.val, res, l, r)
            return res + l + r
        return findSum(root, 0)