# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.depth = 0
        self.max = 0
    def traverse(self, root):
        if root is None:
            return
        
        self.depth += 1

        if root.left is None and root.right is None:
            self.max = max(self.max, self.depth)
        if root.left is not None:
            self.traverse(root.left)
        if root.right is not None:
            self.traverse(root.right)
        
        self.depth -= 1

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.traverse(root)
        return self.max

        