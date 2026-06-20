# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.count = 0
        def dfs(root):
            if root is None:
                return
            dfs(root.right)
            root.val += self.count
            self.count = root.val
            dfs(root.left)
        dfs(root)
        return root