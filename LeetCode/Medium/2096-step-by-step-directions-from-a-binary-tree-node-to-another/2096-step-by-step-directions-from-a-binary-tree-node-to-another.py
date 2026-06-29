# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start_path = None
        self.dest_path = None
        path = []

        def dfs(root):
            if root is None:
                return
            if root.val == startValue:
                self.start_path = path.copy()
            if root.val == destValue:
                self.dest_path = path.copy()
            path.append('L')
            dfs(root.left)
            path[-1] = 'R'
            dfs(root.right)
            path.pop()
            return
        
        dfs(root)
        i = 0
        while i < min(len(self.start_path), len(self.dest_path)) and self.start_path[i] == self.dest_path[i]:
            i += 1
        return 'U' * (len(self.start_path) - i) + ''.join(self.dest_path[i:])