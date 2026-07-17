# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        d = dict()
        q = deque()
        d[root] = 1
        q.append(root)
        while q:
            sz = len(q)
            mini = d[q[0]]
            l = 0
            for i in range(sz):
                cur = q.popleft()
                # print(d[cur])
                l = d[cur] - mini + 1
                if cur.left:
                    d[cur.left] = d[cur] << 1
                    q.append(cur.left)
                if cur.right:
                    d[cur.right] = (d[cur] << 1) + 1
                    q.append(cur.right)
            res = max(res, l)
        return res