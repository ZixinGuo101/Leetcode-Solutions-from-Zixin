class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        l = 0
        r = k-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return ''.join(s)
        