# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        i = 1
        pre = dummy
        while i < left:
            pre = pre.next
            i += 1
        
        fro = pre
        pre = pre.next
        cur = pre.next
        if cur is not None:
            nxt = cur.next

        while i < right:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            i += 1
        
        fro.next.next = cur
        fro.next = pre

        return dummy.next
        