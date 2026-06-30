# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        t = TreeNode(val)
        cur = root
        pre = None
        while cur and cur.val > val:
            pre = cur
            cur = cur.right
        t.left = cur
        if cur == root:
            return t
        else:
            pre.right = t
            return root
