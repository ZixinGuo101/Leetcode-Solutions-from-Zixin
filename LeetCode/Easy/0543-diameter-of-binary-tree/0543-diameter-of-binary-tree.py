# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_diameter = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDepth(root)
        return self.max_diameter
    
    def maxDepth(self, node):
        if node is None:
            return 0
        leftMax = self.maxDepth(node.left)
        rightMax = self.maxDepth(node.right)
        self.max_diameter = max(self.max_diameter, leftMax + rightMax)
        return 1 + max(leftMax, rightMax)
            
        