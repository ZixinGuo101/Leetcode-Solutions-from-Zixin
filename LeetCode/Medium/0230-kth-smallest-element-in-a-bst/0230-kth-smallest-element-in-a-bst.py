# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = 0
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            traverse(root.right)
        traverse(root)
        return self.res