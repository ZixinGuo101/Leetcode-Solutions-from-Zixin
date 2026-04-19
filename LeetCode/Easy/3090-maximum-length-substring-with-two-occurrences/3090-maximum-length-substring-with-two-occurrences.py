class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        cnt = [0] * 26
        left = 0

        for right, c in enumerate(s):
            x = ord(c) -97
            cnt[x] += 1

            while cnt[x] > 2:
                y = ord(s[left]) - 97
                cnt[y] -= 1
                left += 1            

            l = right - left + 1
            ans = l if l > ans else ans
        
        return ans
        