# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.mf = 0
        self.mfv = []
        self.v2f = dict()
        
        def dfs(root):
            if root is None:
                return 0
            lv = dfs(root.left)
            rv = dfs(root.right)
            cur = lv + rv + root.val
            self.v2f[cur] = self.v2f.get(cur, 0) + 1
            if self.v2f[cur] > self.mf:
                self.mf = self.v2f[cur]
                self.mfv = [cur]
            elif self.v2f[cur] == self.mf:
                self.mfv.append(cur)
            return cur
        
        dfs(root)
        return self.mfv
