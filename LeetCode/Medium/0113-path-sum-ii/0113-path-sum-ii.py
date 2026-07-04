# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.path = []
        if root is None:
            return self.res
        
        def dfs(root, target):
            if root is None:
                return
            if root.left is None and root.right is None:
                if root.val == target:
                    self.path.append(root.val)
                    self.res.append(self.path.copy())
                    self.path.pop()
                    return
            self.path.append(root.val)
            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)
            self.path.pop()
            return

        dfs(root, targetSum)
        return self.res