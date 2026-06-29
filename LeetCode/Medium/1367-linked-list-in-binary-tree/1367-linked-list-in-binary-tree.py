# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        list_h = self.getHeight(head)

        def dfs(root) -> Tuple[int, bool]:
            if root is None:
                return 0, False
            lh, l_is_find = dfs(root.left)
            rh, r_is_find = dfs(root.right)
            if l_is_find or r_is_find:
                return 0, True
            h = max(lh, rh) + 1
            return h, h >= list_h and self.isSame(head, root)
        
        return dfs(root)[1]
            

    
    def isSame(self, head, root) -> bool:
        if head is None:
            return True
        if root is None:
            return False
        return root.val == head.val and (self.isSame(head.next, root.left) or self.isSame(head.next, root.right))
    
    def getHeight(self, head) -> int:
        count = 0
        p = head
        while p:
            p = p.next
            count += 1
        return count