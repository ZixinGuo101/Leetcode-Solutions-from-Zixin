class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        min_len = len(s) + 1
        left = 0
        min_left = 0
        if m < n:
            return ''
        
        d = dict()
        for i, c in enumerate(t):
            d[c] = d.get(c, 0) + 1
        
        left  = 0
        for right, c in enumerate(s):
            if c in d:
                d[c] -= 1

            while left <= right and max(d.values()) <= 0:
                l = right - left + 1
                if l <= min_len:
                    min_len = l
                    min_left = left
                
                if s[left] in d:
                    d[s[left]] += 1
                left += 1
        
        return s[min_left : min_left + min_len] if min_len < len(s) + 1 else ''

            