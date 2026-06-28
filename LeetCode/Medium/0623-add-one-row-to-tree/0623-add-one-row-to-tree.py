# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            cur = TreeNode(val)
            cur.left = root
            return cur
        def addNode(root, height):
            if root is None:
                return
            if height == depth - 1:
                old_left = root.left
                old_right = root.right
                root.left = TreeNode(val)
                root.right = TreeNode(val)
                root.left.left = old_left
                root.right.right = old_right
                return
            addNode(root.left, height + 1)
            addNode(root.right, height + 1)
            return
        addNode(root, 1)
        return root