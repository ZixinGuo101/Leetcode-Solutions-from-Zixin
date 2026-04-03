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

        for i in range(n):
            p1 = p1.next
        
        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next
        
        temp = p2.next
        p2.next = temp.next

        if temp is not None:
            temp.next = None

        return dummy.next