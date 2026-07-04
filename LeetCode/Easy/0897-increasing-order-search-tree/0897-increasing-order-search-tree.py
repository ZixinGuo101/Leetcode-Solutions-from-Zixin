# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.stk = None
        self.root = None

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            node.left = None
            if self.stk is None:
                self.root = node
                self.stk = node
            else:
                self.stk.right = node
                self.stk = node
            dfs(node.right)
            return
        
        dfs(root)
        return self.root
            