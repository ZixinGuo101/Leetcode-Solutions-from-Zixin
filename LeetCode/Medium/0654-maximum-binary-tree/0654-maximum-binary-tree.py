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
        root = self.construct(nums, 0, n-1)
        return root
    
    def construct(self, nums, l, r):
        if l > r:
            return None
        idx = self.max_of_nums(nums, l, r)
        cur = TreeNode(nums[idx])
        cur.left = self.construct(nums, l, idx-1)
        cur.right = self.construct(nums, idx+1, r)
        return cur
    
    def max_of_nums(self, nums, l, r):
        if l == r:
            return l
        idx = l
        for i in range(l+1, r+1):
            if nums[i] > nums[idx]:
                idx = i
        return idx
    
