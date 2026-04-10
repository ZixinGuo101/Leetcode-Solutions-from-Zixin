# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        slow = head
        fast = head.next

        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None # 断开与后续链表的连接
        return head
                