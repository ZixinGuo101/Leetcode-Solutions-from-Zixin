class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = [0] * 26
        ans = 0
        left = 0

        for right, c in enumerate(s):
            start = ord(c) - ord('A')
            d[start] += 1

            l = right - left + 1
            while l - max(d) > k:
                end = ord(s[left]) - ord('A')
                d[end] -= 1
                left += 1
                l = right - left + 1
            
            ans = l if l > ans else ans
        
        return ans

        