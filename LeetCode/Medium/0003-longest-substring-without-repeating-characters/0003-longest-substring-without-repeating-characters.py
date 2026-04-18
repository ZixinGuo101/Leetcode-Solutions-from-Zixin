class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set()
        res = 0
        left = 0

        for right, c in enumerate(s):
            while c in d:
                d.discard(s[left])
                left += 1
            d.add(c)
            res = max(res, len(d))
        return res
