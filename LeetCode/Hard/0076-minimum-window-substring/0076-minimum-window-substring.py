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
        m_len = m + 1
        start = 0
        k = n
        for right, c in enumerate(s):
            if c in d:
                if d[c] > 0:
                    k -= 1
                d[c] -= 1
            
            while k == 0:
                l = right - left + 1
                if l < m_len:
                    m_len = l
                    start = left
                
                if s[left] in d:
                    d[s[left]] += 1
                    if d[s[left]] > 0:
                        k += 1
                left += 1
        
        return s[start : start + m_len] if m_len < m + 1 else ''
        