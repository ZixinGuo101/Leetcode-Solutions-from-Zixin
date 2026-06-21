# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if root is None:
                return None, None, 0, True
            l_min, l_max, l_sum, l_is_valid = dfs(root.left)
            r_min, r_max, r_sum, r_is_valid = dfs(root.right)

            if l_is_valid and r_is_valid and \
               (l_max is None or root.val > l_max) and \
               (r_min is None or root.val < r_min):
               tree_sum = root.val + l_sum + r_sum
               new_min = l_min if l_min else root.val
               new_max = r_max if r_max else root.val
               self.res = max(self.res, tree_sum)
               return new_min, new_max, tree_sum, True
            
            return None, None, 0, False
        
        dfs(root)
        return self.res

               