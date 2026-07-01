# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        if root is None:
            return res
        s = set(to_delete)

        def forest(root, hasParent):
            if root is None:
                return None
            notDelete = False if root.val in s else True
            if not hasParent and notDelete:
                res.append(root)
            root.left = forest(root.left, notDelete)
            root.right = forest(root.right, notDelete)
            return root if notDelete else None
        
        forest(root, False)
        return res

        