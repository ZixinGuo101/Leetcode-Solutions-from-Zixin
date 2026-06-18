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
        self.merge(root)
    
    def merge(self, node):
        if node is None:
            return None
        left, right = node.left, node.right
        tail = node
        if left:
            tail = self.merge(left)
            node.right = left
            node.left = None
        if right:
            tail.right = right
            tail = self.merge(right)
        return tail
                
        

        