class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_freq = 0
        maxfreq_c = ''
        left = 0
        ans = 0
        d = [0] * 26

        for right, c in enumerate(s):
            ri = ord(c) - ord('A')
            d[ri] += 1
            if d[ri] >= max_freq:
                maxfreq_c = c
                max_freq = d[ri]
            if right - left + 1 - max_freq > k:
                li = ord(s[left]) - ord('A')
                d[li] -= 1
                if d[li] == maxfreq_c:
                    max_freq -= 1
                left += 1
            
            ans = right - left + 1 if right - left + 1 > ans else ans
        
        return ans
            # A A A B C D

        