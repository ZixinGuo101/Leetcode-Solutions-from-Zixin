# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return
        dummy = ListNode()
        p1 = head
        p2 = head.next
        p1.next = None
        while p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        dummy.next = p1
        
        return dummy.next
        