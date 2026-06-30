# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n & 1:
            return []
        dp = [[] for _ in range(n+1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, n+1, 2):
            for j in range(1, i, 2):
                k = i - j - 1
                for left in dp[j]:
                    for right in dp[k]:
                        root = TreeNode(0, left, right)
                        dp[i].append(root)
        return dp[n]