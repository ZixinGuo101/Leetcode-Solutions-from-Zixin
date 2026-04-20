class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        min_len = len(s) + 1
        left = 0
        cnt1 = 0
        ans = ''

        for right, c in enumerate(s):
            cnt1 += int(c) - int('0')

            while (s[left] == '0' and left < right) or cnt1 > k:
                cnt1 -= int(s[left]) - int('0')
                left += 1
            
            if cnt1 == k:
                l = right - left + 1
                if ans == '' or l < min_len or (l == min_len and s[left:right+1] < ans):
                    ans = s[left:right+1]
                    min_len = len(ans)
        
        return ans