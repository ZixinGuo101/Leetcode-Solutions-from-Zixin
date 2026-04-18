class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        res = 0
        left = 0

        for right, c in enumerate(s):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            
            if (right - left + 1) == len(d):
                res = max(res, len(d))
                continue
            
            while left < right and (right - left + 1) != len(d):
                end = s[left]
                d[end] -= 1
                left += 1
                if d[end] == 0:
                    del d[end] 
        
        return res
            
            
        