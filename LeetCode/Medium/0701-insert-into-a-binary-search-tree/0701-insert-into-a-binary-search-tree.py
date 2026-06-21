# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        node = TreeNode(val)
        if not root:
            return node
        p = root
        while True:
            if val < p.val:
                if not p.left:
                    p.left = node
                    break
                p = p.left
            else:
                if not p.right:
                    p.right = node
                    break
                p = p.right
        return root