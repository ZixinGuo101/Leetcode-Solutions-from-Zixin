class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        need = dict()
        window = dict()

        for i in range(n):
            need[t[i]] = need.get(t[i], 0) + 1
        
        valid = 0
        left = 0
        min_len = len(s) + 1
        min_left = 0
        for right, c in enumerate(s):
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                l = right - left + 1
                if l <= min_len:
                    min_len = l
                    min_left = left
                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        valid -= 1
                left += 1
            
        return s[min_left : min_left + min_len] if min_len < len(s) + 1 else ''

        