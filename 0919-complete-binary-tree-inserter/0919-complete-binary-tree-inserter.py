# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([root])
        stop = False
        while self.q and not stop:
            sz = len(self.q)
            for i in range(sz):
                cur = self.q[0]
                if cur.left:
                    self.q.append(cur.left)
                if cur.right:
                    self.q.append(cur.right)
                if not cur.left or not cur.right:
                    stop = True
                    break
                else:
                    self.q.popleft()

    def insert(self, val: int) -> int:
        parent = self.q[0]
        cur = TreeNode(val)
        if not parent.left:
            parent.left = cur
        else:
            parent.right = cur
            self.q.popleft()
        self.q.append(cur)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()