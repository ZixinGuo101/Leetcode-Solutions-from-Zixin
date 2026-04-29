class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        k = 0
        stack = []
        for c in s:
            if c.islower():
                res += c
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((res, k))
                res = ''
                k = 0
            else:
                prev, multi = stack.pop()
                res = prev + res * multi
            
        return res