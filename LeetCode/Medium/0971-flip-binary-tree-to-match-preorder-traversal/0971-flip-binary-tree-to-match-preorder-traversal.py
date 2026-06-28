# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        self.idx = 0
        self.indi = True
        def flip(root: Optional[TreeNode]) -> None:
            if not self.indi or root is None:
                return
            if root.val != voyage[self.idx]:
                self.indi = False
                return
            '''
            if root.left is None and root.right is None:
                self.idx += 1
                return
            '''
            if root.left and root.left.val != voyage[self.idx + 1]:
                if not root.right or root.right.val != voyage[self.idx + 1]:
                    self.indi = False
                    return
                else:
                    res.append(root.val)
                    root.left, root.right = root.right, root.left
            self.idx += 1
            flip(root.left)
            flip(root.right)
        flip(root)
        return res if self.indi else [-1]
