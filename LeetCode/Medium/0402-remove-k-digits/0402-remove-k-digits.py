class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        count = 0
        stk = []
        # remain = len(num) - k
        for ch in num:
            while k and stk and int(ch) < int(stk[-1]):
                stk.pop()
                k -= 1
            stk.append(ch)
        final_stack = stk[:-k] if k else stk
        res = ''.join(final_stack).lstrip('0') 
        return res if res else '0'