# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(root: Optional[TreeNode], layer: int):
            if root is None:
                return
            if len(self.res) < layer:
                self.res.append(root.val)
            dfs(root.right, layer + 1)
            dfs(root.left, layer + 1)
            return
        dfs(root, 1)
        return self.res