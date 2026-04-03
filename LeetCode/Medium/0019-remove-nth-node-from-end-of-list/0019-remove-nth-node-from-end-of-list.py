# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = dummy

        for _ in range(n+1):
            p1 = p1.next
        
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        
        temp = p2.next
        p2.next = temp.next
        temp.next = None

        return dummy.next
        