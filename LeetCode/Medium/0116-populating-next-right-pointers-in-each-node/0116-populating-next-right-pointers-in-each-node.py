"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return
        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, l, r):
        if l is None:
            return
        l.next = r
        self.traverse(l.left, l.right)
        self.traverse(l.right, r.left)
        self.traverse(r.left, r.right)
        return

        