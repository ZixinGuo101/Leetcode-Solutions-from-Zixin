# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dummy = TreeNode(-1)
        self.pre = self.dummy

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            node.left = None
            self.pre.right = node
            self.pre = node
            dfs(node.right)
            return
        
        dfs(root)
        return self.dummy.right
            