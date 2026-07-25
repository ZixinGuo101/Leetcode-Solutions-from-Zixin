# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        tv = target.val
        path = []
        def findPath(root):
            if root is None:
                return False
            if root.val == tv:
                path.append(root)
                return True
            path.append(root)
            lv = findPath(root.left)
            rv = findPath(root.right)
            if not lv and not rv:
                path.pop()
                return False
            return True
        findPath(root)
        self.res = []
        self.s = set()
        def findDistance(root, d):
            if root is None or root.val in self.s:
                return
            if d == 0:
                self.res.append(root.val)
                return
            findDistance(root.left, d-1)
            findDistance(root.right, d-1)
            return
        n = len(path)
        t = min(n, k+1)
        for i in range(t):
            findDistance(path[n-i-1], k-i)
            self.s.add(path[n-i-1].val)
        return self.res
