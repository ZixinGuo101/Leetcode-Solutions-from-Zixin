# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        root = None
        stk = []
        for num in nums:
            cur = TreeNode(num)
            while stk and stk[-1].val < cur.val:
                cur.left = stk[-1]
                stk.pop()
            if not stk:
                root = cur
            else:
                stk[-1].right = cur
            stk.append(cur)
        return root
