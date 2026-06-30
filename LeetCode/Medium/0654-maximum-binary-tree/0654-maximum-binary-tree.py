# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = None
        stk = []
        for num in nums:
            cur = TreeNode(num)
            while stk and num > stk[-1].val:
                cur.left = stk.pop()
            if stk:
                stk[-1].right = cur
            else:
                root = cur
            stk.append(cur)
        return root