# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n = len(preorder)
        return self.build(preorder, 0, n-1, inorder, 0, n-1)
    
    def build(self, preorder, pl, pr, inorder, il, ir):
        if pl > pr:
            return None
        cur = TreeNode(preorder[pl])
        if pl == pr:
            return cur
        idx = self.findIndex(preorder[pl], inorder, il, ir)
        print(idx)
        print("preorder_left:", pl+1, pl+idx-il)
        print("preorder_right", pl+idx-il+1, pr)
        cur.left = self.build(preorder, pl+1, pl+idx-il, inorder, il, il+idx-1)
        cur.right = self.build(preorder, pl+idx-il+1, pr, inorder, idx+1, ir)
        return cur
    
    def findIndex(self, num, inorder, il, ir):
        for i in range(il, ir+1):
            if num == inorder[i]:
                return i