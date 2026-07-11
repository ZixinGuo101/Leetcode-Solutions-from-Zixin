# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, parent):
            if root is None:
                return False, False
            l_is_moni, l_has_moni = dfs(root.left, root)
            r_is_moni, r_has_moni = dfs(root.right, root)
            l_need_moni = not l_is_moni and root.left
            r_need_moni = not r_is_moni and root.right
            root_need_moni = not l_has_moni and not r_has_moni and not parent
            if l_need_moni or r_need_moni or root_need_moni:
                self.res += 1
                return True, True
            return l_has_moni or r_has_moni, False
        dfs(root, None)
        return self.res