# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        self.d = {}
        self.res = set()
        def traverse(node):
            if node is None:
                return '#'
            leftSerial = traverse(node.left)
            rightSerial = traverse(node.right)
            curSerial = ','.join([str(node.val), leftSerial, rightSerial])
            if curSerial in self.d:
                self.res.add(self.d[curSerial])
            else:
                self.d[curSerial] = node
            return curSerial
        
        traverse(root)
        return list(self.res)