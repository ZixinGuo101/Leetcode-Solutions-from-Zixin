# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p1 = head
        p2 = head

        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next
        
        return p2