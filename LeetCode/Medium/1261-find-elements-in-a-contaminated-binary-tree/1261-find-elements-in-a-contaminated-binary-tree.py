# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def build(root, v):
            if root is None:
                return
            root.val = v
            build(root.left, 2*v+1)
            build(root.right, 2*v+2)
            return
        build(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        path = format(target+1, 'b')
        self.idx = 0
        def ft(root):
            if root is None or self.idx > len(path) - 1:
                return False
            if self.idx == len(path) - 1:
                return True
            self.idx += 1
            if path[self.idx] == '1':
                return ft(root.right)
            else:
                return ft(root.left)
        return ft(self.root)



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)