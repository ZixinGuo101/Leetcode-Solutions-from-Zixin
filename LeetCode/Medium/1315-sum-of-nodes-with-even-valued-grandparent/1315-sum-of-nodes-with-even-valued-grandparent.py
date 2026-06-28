# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], parents: Optional[TreeNode], grandparents: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            s = 0
            if grandparents and grandparents.val & 1 == 0:
                s = root.val
            ls = dfs(root.left, root, parents)
            rs = dfs(root.right, root, parents)
            return s + ls + rs
        return dfs(root, None, None)