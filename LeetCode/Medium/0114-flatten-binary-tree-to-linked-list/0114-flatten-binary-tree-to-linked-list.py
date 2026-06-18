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
        return
    
    def merge(self, node):
        if node is None:
            return None
        lastLeft = self.merge(node.left)
        lastRight = self.merge(node.right)
        if lastLeft is None:
            if lastRight is None:
                return node
            else:
                return lastRight
        else:
            temp = node.right
            node.right = node.left
            lastLeft.right = temp
            node.left = None
            if lastRight is None:
                return lastLeft
            else:
                return lastRight
                
        

        