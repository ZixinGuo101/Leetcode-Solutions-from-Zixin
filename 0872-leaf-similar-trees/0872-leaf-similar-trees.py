# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.res = []
        self.leavesValue(root1)
        lv1 = self.res.copy()
        self.res = []
        self.leavesValue(root2)
        lv2 = self.res.copy()
        # print(lv1, lv2)
        if len(lv1) != len(lv2):
            return False
        for i in range(len(lv1)):
            if lv1[i] != lv2[i]:
                return False
        return True
    
    def leavesValue(self, root):
        if root is None:
            return
        if not root.left and not root.right:
            self.res.append(root.val)
        self.leavesValue(root.left)
        self.leavesValue(root.right)
        return
