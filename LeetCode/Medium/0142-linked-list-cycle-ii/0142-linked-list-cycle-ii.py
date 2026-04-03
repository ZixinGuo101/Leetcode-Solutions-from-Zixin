# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        if fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        while slow != fast and  fast is not None:
            if fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            else:
                break
            
        
        if fast is None:
            return None
        if fast.next is None:
            return None
        
        print(fast.val)

        slow = head
        i = 0

        while slow != fast:
            i += 1
            
            slow = slow.next
            fast = fast.next
            # print(slow.val)

        return slow

        