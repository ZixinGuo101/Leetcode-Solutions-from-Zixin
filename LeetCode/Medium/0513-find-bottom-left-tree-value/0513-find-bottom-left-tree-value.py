# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        cur = [root]
        res = 0
        while cur:
            nxt = []
            for node in cur:
                res = node.val
                if node.right:
                    nxt.append(node.right)
                if node.left:
                    nxt.append(node.left)
            cur = nxt
        return res