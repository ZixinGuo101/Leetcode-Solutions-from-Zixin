"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        depth = 0
        cur = [root]
        while cur:
            nxt = []
            depth += 1
            for node in cur:
                for child in node.children:
                    if child is not None:
                        nxt.append(child)
            cur = nxt
        return depth