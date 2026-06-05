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
        n = len(nums)
        if n == 0:
            return
        if n == 1:
            root = TreeNode(nums[0])
            return root
        
        i, m = self.maxIdx(nums)
        root = TreeNode()
        root.val = m
        root.left = None if i == 0 else self.constructMaximumBinaryTree(nums[0:i])
        root.right = None if i == n - 1 else self.constructMaximumBinaryTree(nums[i+1:n])
        
        return root

    def maxIdx(self, nums):
        idx, m = -1, -1
        for i, num in enumerate(nums):
            if num > m:
                m = num
                idx = i
        return idx, m
        