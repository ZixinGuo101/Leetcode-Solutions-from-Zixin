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

        while p:
            while stk and p.val > res[stk[-1]]:
                res[stk.pop()] = p.val
            stk.append(len(res))
            res.append(p.val)
            p = p.next
        for i in stk:
            res[i] = 0
        
        return res
