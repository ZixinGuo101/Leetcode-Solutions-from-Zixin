# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.res = None
        self.index = False
        def dfs(root):
            if root is None or self.index:
                return
            if root.val == target.val:
                self.res = root
                self.index = True
                return
            dfs(root.left)
            dfs(root.right)
            return
        dfs(cloned)
        return self.res