# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = -1
        while q:
            level += 1
            sz = len(q)
            prev = 0 if not level % 2 else inf
            for i in range(sz):
                cur = q.popleft()
                if (cur.val <= prev and not level % 2) or (cur.val >= prev and level % 2):
                    return False
                if not (cur.val + level) % 2:
                    return False
                prev = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return True