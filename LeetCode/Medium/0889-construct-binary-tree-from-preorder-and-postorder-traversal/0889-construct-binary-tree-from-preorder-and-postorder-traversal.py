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
        def build(pre,post):
            if not pre:
                return None
            root=TreeNode(pre[0])
            if len(pre)==1:
                return root
            leftroot=pre[1]
            idx=post.index(leftroot)
            leftsize=idx+1
            root.left=build(pre[1:leftsize+1],post[:leftsize])
            root.right=build(pre[leftsize+1:],post[leftsize:-1])

            return root
        return build(preorder,postorder)