# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.path = 0

        def traverse(root):
            if root is None:
                return
            self.path = (self.path << 1) + root.val
            if root.left is None and root.right is None:
                self.res += self.path
            else:
                traverse(root.left)
                traverse(root.right)
            self.path >>= 1
            return
        
        traverse(root)
        return self.res