# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        val_to_idx = {val: idx for idx, val in enumerate(preorder)}
        self.post_pos = len(postorder) - 1

        def construct(left, right):
            if left > right:
                return None
            root = TreeNode(preorder[left])
            self.post_pos -= 1
            if left == right:
                return root
            idx = val_to_idx[postorder[self.post_pos]]
            root.right = construct(idx, right)
            root.left = construct(left+1, idx-1)
            return root

        return construct(0, len(preorder) - 1)

            
            