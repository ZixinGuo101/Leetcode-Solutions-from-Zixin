class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        left = 0
        res = 0

        for right, c in enumerate(s):
            while d.get(c, 0) != 0:
                d[s[left]] -= 1
                left += 1
            d[c] = d.get(c, 0) + 1
            l = right - left + 1
            res = l if l > res else res
        
        return res
        