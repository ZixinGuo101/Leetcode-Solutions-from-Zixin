# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        res = []
        stk = []
        p = head
        idx = 0
        while p:
            while stk and p.val > res[stk[-1]]:
                res[stk.pop()] = p.val
            res.append(p.val)
            stk.append(idx)
            p = p.next
            idx += 1
        for i in stk:
            res[i] = 0
        
        return res
