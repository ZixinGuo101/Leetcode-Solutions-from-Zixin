# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def bfs(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            cur = [root]
            while cur:
                nxt = []
                sz = len(cur)
                for node in cur:
                    if node.left:
                        nxt.append(node.left)
                    if node.right:
                        nxt.append(node.right)
                self.res.append(cur[-1].val)
                cur = nxt
            return
        bfs(root)
        return self.res