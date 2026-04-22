class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = list(s)
        l = 0
        r = len(ls) - 1

        while l < r:
            if ls[l] != ls[r]:
                ls[l] = ls[r] = ls[l] if ls[l] < ls[r] else ls[r]
            l += 1
            r -= 1
        return ''.join(ls)
        