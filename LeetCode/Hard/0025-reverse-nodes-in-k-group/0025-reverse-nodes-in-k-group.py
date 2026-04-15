# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        s = True
        dummy = ListNode()
        dummy.next = head
        fro = dummy

        while s is True:
            tail = fro
            for _ in range(k):
                if tail is not None:
                    tail = tail.next
            
            if tail is None:
                return dummy.next
            
            res = self.reverseK(fro.next, k)

            temp = fro.next
            fro.next = res
            fro = temp
            # print(fro.val)
            
    def reverseK(self, head, k):
        if k == 1:
            return head
        pre = head
        cur = pre.next
        nxt = cur.next
        while k > 1:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt is not None:
                nxt = nxt.next
            k -= 1
        head.next = cur

        return pre

                