# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        n = len(postorder)
        self.post_pos = n - 1
    
        def build(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_pos]
            self.post_pos -= 1
            root = TreeNode(root_val)
            if left == right:
                return root
            idx = val_to_idx[root_val]
            root.right = build(idx+1, right)
            root.left = build(left, idx-1)
            return root
        
        return build(0, n-1)