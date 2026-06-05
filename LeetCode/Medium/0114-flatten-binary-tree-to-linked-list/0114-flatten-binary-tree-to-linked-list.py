# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        
        self.flatten(root.left)
        self.flatten(root.right)

        r = root.right
        root.right = root.left
        root.left = None

        l = root
        while l.right:
            l = l.right
        l.right = r

        return root
        