# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        '''
        cur_inc and cur_dec represents 左右子树中能和当前节点接上的相同值
        recursion 的三部曲：
        signature : 以当前节点为起点，向子树延伸的相同值路径的最大边数。
        Sub_Problem : 左右孩子的最大值
        Recursion Step : 左右孩子的最大值 + 1
        '''
        def dfs(node):
            if not node:
                return 0

            left_length = dfs(node.left)
            right_length = dfs(node.right)

            arrow_left = 0
            arrow_right = 0

            if node.left and node.val == node.left.val:
                arrow_left = left_length + 1

            if node.right and node.val == node.right.val:
                arrow_right = right_length + 1
            
            self.max_len = max(arrow_left + arrow_right, self.max_len)
            return max(arrow_left,arrow_right)
        
        dfs(root)
        return self.max_len
        