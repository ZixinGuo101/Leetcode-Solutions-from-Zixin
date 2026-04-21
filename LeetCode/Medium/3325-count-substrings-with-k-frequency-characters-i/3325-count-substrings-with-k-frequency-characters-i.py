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
            if d[c] == k:
                cnt += 1
            
            while cnt >= 1:
                if d[s[left]] == k:
                    cnt -= 1
                d[s[left]] -= 1
                left += 1
            
            ans += left
        
        return ans

