# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def search(root):
            if root is None:
                return 0
            if root.val > high:
                return search(root.left)
            if root.val < low:
                return search(root.right)
            l = search(root.left)
            r = search(root.right)
            return root.val + l + r
            
        return search(root)
