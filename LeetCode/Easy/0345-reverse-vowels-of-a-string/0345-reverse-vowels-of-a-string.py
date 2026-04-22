class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        r = len(s) - 1
        s = list(s)

        while l < r:
            if s[l] in "aeiouAEIOU" and s[r] in "aeiouAEIOU":
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in "aeiouAEIOU":
                r -= 1
            elif s[r] in "aeiouAEIOU":
                l += 1
            else:
                l += 1
                r -= 1
        
        return ''.join(s)
        