class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)

        if m < n:
            return ''
        
        d = dict()
        for i in range(n):
            d[t[i]] = d.get(t[i], 0) + 1
        
        left = 0
        min_len = m + 1
        min_left = 0
        for right, c in enumerate(s):
            if c in d:
                if d[c] > 0:
                    n -= 1
                d[c] -= 1
            
            while n == 0:
                l = right - left + 1
                if l < min_len:
                    min_len = l
                    min_left = left
                if s[left] in d:
                    d[s[left]] += 1
                    if d[s[left]] > 0:
                        n += 1
                left += 1
        
        return s[min_left : min_left + min_len] if min_len < (m + 1) else ''