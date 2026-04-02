"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        q = deque()
        q.append(root)
        while q:
            sz = len(q)
            level_res = []
            for i in range(sz):
                cur = q.popleft()
                level_res.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(level_res)
        return res

        