# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        self.memo = {}
        return self.build(1, n)
    
    def build(self, lo, hi):
        res = []
        if lo > hi:
            res.append(None)
            return res
        if (lo, hi) in self.memo:
            return self.memo[(lo, hi)]
        for i in range(lo, hi+1):
            leftList = self.build(lo, i-1)
            rightList = self.build(i+1, hi)
            for left in leftList:
                for right in rightList:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        self.memo[(lo, hi)] = res
        return res