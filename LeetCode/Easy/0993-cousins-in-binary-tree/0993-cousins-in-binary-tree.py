# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parents = []
        depths = []
        def dfs(root, depth):
            if root is None:
                return
            if root.left and (root.left.val == x or root.left.val == y):
                depths.append(depth)
                return
            if root.right and (root.right.val == x or root.right.val == y):
                depths.append(depth)
                return
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return
        
        dfs(root, 0)
        return len(depths) == 2 and depths[0] == depths[1]
