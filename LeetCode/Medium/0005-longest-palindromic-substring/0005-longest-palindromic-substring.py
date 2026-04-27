class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        
        ans = ''
        m = 0
        for i in range(1, len(s)):
            l = i-1
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                else:
                    break
            if (r - l - 1) > m:
                m = r - l - 1
                ans = s[l+1:r]

            if s[i-1] == s[i]:
                l = i-2
                r = i+1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        r += 1
                        l -= 1
                    else:
                        break
                if (r - l - 1) > m:
                    m = r - l - 1
                    ans = s[l+1:r]
        
        return ans