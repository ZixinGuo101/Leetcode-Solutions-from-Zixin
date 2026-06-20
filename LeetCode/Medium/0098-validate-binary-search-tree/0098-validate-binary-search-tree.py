# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stk = []
        pre = float('-inf')
        while True:
            while root:
                stk.append(root)
                root = root.left
            if not stk:
                return True
            root = stk.pop()
            if root.val <= pre:
                return False
            pre = root.val
            root = root.right