# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.path = []
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.path.append(str(root.val))
            self.res += int(''.join(self.path))
            self.path.pop()
            return
        self.path.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)
        self.path.pop()
        return
