class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        d = dict()
        left = 0
        v = 0

        for right, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            if d[c] == 1:
                v += 1
            
            while d[s[left]] > 1 and v == 3:
                d[s[left]] -= 1
                left += 1
            
            if v == 3:
                ans += left + 1
        
        return ans
        