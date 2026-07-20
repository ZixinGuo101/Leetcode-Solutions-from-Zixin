# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        end = False
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if cur is None:
                    end = True
                elif end:
                    return False
                else:
                    q.append(cur.left)
                    q.append(cur.right)
        return True
                    