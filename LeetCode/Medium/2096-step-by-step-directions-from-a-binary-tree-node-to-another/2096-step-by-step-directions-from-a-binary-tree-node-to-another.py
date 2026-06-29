# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path = []
        res = []
        self.start = TreeNode()
        self.is_find_start = False
        self.is_find_dest = False
        def findStart(root):
            if root is None or self.is_find_start:
                return
            if root.val == startValue:
                self.is_find_start = True
                self.start = root
                return
            start_path.append(root)
            findStart(root.left)
            findStart(root.right)
            if not self.is_find_start:
                start_path.pop()
            return
        def findDest(root):
            if root is None:
                return False
            if root.val == destValue:
                self.is_find_dest = True
                return True
            res.append('L')
            if not findDest(root.left):
                res.pop()
            else:
                return True
            res.append('R')
            if not findDest(root.right):
                res.pop()
            else:
                return True
            return False
        
        findStart(root)
        findDest(self.start)
        if res:
            return ''.join(res)
        # print(start_path)
        for i in range(len(start_path)-1, -1, -1):
            res.append('U')
            findDest(start_path[i])
            if self.is_find_dest:
                return ''.join(res)
