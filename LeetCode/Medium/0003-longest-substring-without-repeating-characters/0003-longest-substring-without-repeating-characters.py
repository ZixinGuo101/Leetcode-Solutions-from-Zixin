class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set()
        left = 0
        ans = 0

        for right, c in enumerate(s):
            while c in d:
                d.discard(s[left])
                left += 1
            d.add(c)
            l = right - left + 1
            ans  = l if l > ans else ans

        return ans
        