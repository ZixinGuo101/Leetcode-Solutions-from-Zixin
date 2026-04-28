# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s = head
        f = head
        cnt = 0
        while f != None and f.next != None:
            s = s.next
            f = f.next
            f = f.next
            cnt += 1
        
        stack = []
        node = ListNode()
        s = s.next
        while s != None:
            node = s
            s = s.next
            stack.append(node)
        
        s = head
        while cnt > 0:
            if stack:
                node = stack.pop()
                temp = s.next
                s.next = node
                node.next = temp
                s = s.next
            cnt -= 1
            s = s.next
        s.next = None

        return head