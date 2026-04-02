"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def n_postorder(self, root, res):
        for child in root.children:
            self.n_postorder(child, res)
        res.append(root.val)
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        self.n_postorder(root, res)
        return res
        