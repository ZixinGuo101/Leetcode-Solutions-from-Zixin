"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def n_preorder(self, root, res):
        res.append(root.val)
        for child in root.children:
            self.n_preorder(child, res)

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        res = []
        if root is None:
            return res
        self.n_preorder(root, res)
        return res

        