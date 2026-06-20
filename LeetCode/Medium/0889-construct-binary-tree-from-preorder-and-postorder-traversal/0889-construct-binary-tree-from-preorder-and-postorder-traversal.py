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
        def construct(preorder, postorder, pre_l, pre_r, pst_l, pst_r):
            if pre_l > pre_r:
                return None
            root = TreeNode(preorder[pre_l])
            if pre_l == pre_r:
                return root
            leftVal = preorder[pre_l+1]
            idx = postorder.index(leftVal)
            left = TreeNode(leftVal)
            root.left = construct(preorder, postorder, pre_l+1, pre_l+idx-pst_l+1, pst_l, idx)
            root.right = construct(preorder, postorder, pre_l+idx-pst_l+2, pre_r, idx+1, pst_r)
            return root
        
        n = len(preorder)
        return construct(preorder, postorder, 0, n-1, 0, n-1)
        