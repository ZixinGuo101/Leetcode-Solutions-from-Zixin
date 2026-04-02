# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        d = 1

        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if (cur.left == None and cur.right == None):
                    return d
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            d += 1


        