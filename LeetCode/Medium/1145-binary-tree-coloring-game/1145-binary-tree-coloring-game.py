# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.is_find = False
        self.x_node = TreeNode()
        def find(root):
            if root is None or self.is_find:
                return
            if root.val == x:
                self.x_node = root
                self.is_find = True
                return
            find(root.left)
            find(root.right)
            return
        def count(root):
            if root is None:
                return 0
            return count(root.left) + count(root.right) + 1
        find(root)
        x_left = count(self.x_node.left)
        x_right = count(self.x_node.right)
        r = n - (x_left + x_right + 1)
        return r > n // 2 or x_left > n // 2 or x_right > n // 2
        # return n > 2 * (x_left + x_right + 1) or max(x_right, x_left) > (min(x_right, x_left) + 1 + r)
