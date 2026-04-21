class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = dict()
        ans = 0
        left = 0
        cnt = 0
        n = len(s)
        if n < k:
            return ans
        
        for right, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            
            while d[c] >= k:
                d[s[left]] -= 1
                left += 1
            
            ans += left
        
        return ans

