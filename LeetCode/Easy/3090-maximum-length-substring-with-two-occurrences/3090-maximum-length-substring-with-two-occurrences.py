class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        d = dict()

        for right, c in enumerate(s):
            d[c] = d.get(c, 0) + 1

            while d[c] > 2:
                d[s[left]] -= 1
                left += 1
            
            l = right - left + 1
            ans  = l if l > ans else ans
        
        return ans
        