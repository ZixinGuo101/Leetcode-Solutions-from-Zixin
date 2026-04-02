# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, res):
        if root != None:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
    
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        self.inorder(root, res)

        return res
    

        
        