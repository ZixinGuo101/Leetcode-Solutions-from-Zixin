# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        self.res = []
        self.path = []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.path.append(str(root.val))
            cur = '->'.join(self.path)
            self.res.append(cur)
            self.path.pop()
            return
        self.path.append(str(root.val))
        self.dfs(root.left)
        self.dfs(root.right)
        self.path.pop()
        return
        