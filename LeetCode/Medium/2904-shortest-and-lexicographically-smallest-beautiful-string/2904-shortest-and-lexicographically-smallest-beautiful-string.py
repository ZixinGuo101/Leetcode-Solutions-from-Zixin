class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s.count('1') < k:
            return ''

        cntk = 0
        ans = ''
        min_len = int
        left = 0
        for right, c in enumerate(s):
            cntk += int(c)

            while s[left] == '0' or cntk > k:
                cntk -= int(s[left])
                left += 1

            if cntk == k:
                l = right - left + 1
                res = s[left : right+1]
                if ans == '' or l < len(ans) or (l == len(ans) and res < ans):
                    ans = res
        
        return ans
                
        