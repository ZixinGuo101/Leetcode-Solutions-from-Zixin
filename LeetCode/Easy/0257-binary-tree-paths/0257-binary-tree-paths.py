# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.path = []
        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            self.path.append(str(node.val))
            if node.left is None and node.right is None:
                self.res.append('->'.join(self.path))
            else:
                traverse(node.left)
                traverse(node.right)
            self.path.pop()
            return
        traverse(root)
        return self.res