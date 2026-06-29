# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_h = self.getHeight(subRoot)

        def dfs(root):
            if root is None:
                return 0, False
            lh, l_is_find = dfs(root.left)
            rh, r_is_find = dfs(root.right)
            if l_is_find or r_is_find:
                return 0, True
            h = max(lh, rh) + 1
            return h, h == sub_h and self.isSame(root, subRoot)
        
        return dfs(root)[1]
    
    def getHeight(self, root):
        if root is None:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        return max(lh, rh) + 1
    
    def isSame(self, r1, r2):
        if r1 is None or r2 is None:
            return r1 is r2
        return r1.val == r2.val and self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)