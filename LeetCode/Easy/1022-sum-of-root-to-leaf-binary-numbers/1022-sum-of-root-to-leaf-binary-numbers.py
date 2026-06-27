# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def traverse(root, n):
            if root is None:
                return
            n = (n << 1) + root.val
            if root.left is None and root.right is None:
                self.res += n
            else:
                traverse(root.left, n)
                traverse(root.right, n)
            return
        
        traverse(root, 0)
        return self.res