# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def remove(root, total):
            if root is None:
                return None
            if not root.left and not root.right:
                return root if total + root.val >= limit else None
            root.left = remove(root.left, total + root.val)
            root.right = remove(root.right, total + root.val)
            if not root.left and not root.right:
                return None
            return root
        return remove(root, 0)